# SNMP MIB module (NS-ROOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:14 2024
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
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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

netScaler = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5951)
)


# Types definitions



class EntityProtocolType(Integer32):
    """Custom type EntityProtocolType based on Integer32"""
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
              35,
              38,
              43,
              44,
              45,
              47,
              48,
              49,
              50,
              52)
        )
    )
    namedValues = NamedValues(
        *(("aaa", 21),
          ("adns", 16),
          ("adnstcp", 44),
          ("any", 13),
          ("dhcpClient", 49),
          ("dhcrpa", 35),
          ("dns", 15),
          ("dnsClient", 25),
          ("dnstcp", 43),
          ("ftp", 1),
          ("ha", 18),
          ("http", 0),
          ("httpclient", 9),
          ("httpserver", 8),
          ("monitor", 5),
          ("monitorPing", 19),
          ("monitorUdp", 6),
          ("nat", 12),
          ("nntp", 7),
          ("push", 47),
          ("radius", 50),
          ("rip", 24),
          ("rpcClient", 27),
          ("rpcServer", 26),
          ("rpcclient", 11),
          ("rpcserver", 10),
          ("rtsp", 45),
          ("secureMonitor", 22),
          ("serviceUnknown", 52),
          ("sipudp", 38),
          ("snmp", 17),
          ("ssl", 14),
          ("sslBridge", 4),
          ("sslOtherTcp", 20),
          ("sslPush", 48),
          ("sslvpnUdp", 23),
          ("tcp", 2),
          ("udp", 3))
    )





class EntityState(Integer32):
    """Custom type EntityState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("busy", 3),
          ("down", 1),
          ("outOfService", 4),
          ("transitionToOutOfService", 5),
          ("transitionToOutOfServiceDown", 8),
          ("unknown", 2),
          ("up", 7))
    )





class MepStatus(Integer32):
    """Custom type MepStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mepDown", 0),
          ("mepUp", 1))
    )





class SiteType(Integer32):
    """Custom type SiteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localSite", 1),
          ("remoteSite", 2))
    )





class MetricExchange(Integer32):
    """Custom type MetricExchange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 4))
    )





class AdminStatus(Integer32):
    """Custom type AdminStatus based on Integer32"""
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





class HAMode(Integer32):
    """Custom type HAMode based on Integer32"""
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
        *(("primary", 1),
          ("secondary", 2),
          ("standalone", 0),
          ("unknown", 3))
    )





class HAState(Integer32):
    """Custom type HAState based on Integer32"""
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
        *(("completeFail", 7),
          ("disabled", 9),
          ("down", 2),
          ("dumb", 8),
          ("init", 1),
          ("monitorFail", 5),
          ("monitorOk", 6),
          ("partialFail", 4),
          ("partialFailSsl", 10),
          ("routemonitorFail", 11),
          ("unknown", 0),
          ("up", 3))
    )





class HAON(Integer32):
    """Custom type HAON based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )





class FeatureStatus(Integer32):
    """Custom type FeatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("licensedAndEnabled", 2),
          ("licensedButDisabled", 1),
          ("notLicensed", 0))
    )





class FeaturePlatform(Integer32):
    """Custom type FeaturePlatform based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("agee", 1),
          ("ns", 0),
          ("nsva", 2))
    )





class ModeStatus(Integer32):
    """Custom type ModeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )





class LbPolicy(Integer32):
    """Custom type LbPolicy based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("asynchronousMAC", 4),
          ("callIDHashed", 18),
          ("customLoad", 11),
          ("destinationIPHashed", 7),
          ("domainHashed", 6),
          ("leastBandwidth", 9),
          ("leastConnections", 2),
          ("leastPackets", 10),
          ("leastResponse", 3),
          ("lrtm", 17),
          ("rtt", 14),
          ("sourceIPDestinationIPHashed", 15),
          ("sourceIPHashed", 8),
          ("sourceIPSourcePort", 16),
          ("staticProximity", 13),
          ("token", 12),
          ("urlHashed", 5),
          ("weightedRoundRobin", 1))
    )





class PersistanceType(Integer32):
    """Custom type PersistanceType based on Integer32"""
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
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("callerID", 17),
          ("cookieDelete", 3),
          ("cookieHash", 5),
          ("cookieInsert", 2),
          ("cookieRead", 4),
          ("customServerID", 10),
          ("destinationIP", 14),
          ("groupCookieInsert", 12),
          ("groupRule", 13),
          ("groupSourceID", 11),
          ("gslbBackup", 18),
          ("none", 0),
          ("rtspSessionID", 19),
          ("rule", 8),
          ("server", 7),
          ("sessionId", 6),
          ("sourceIPdestinationIP", 16),
          ("sourceIp", 1),
          ("spillOver", 15),
          ("urlPassive", 9))
    )





class ActionType(Integer32):
    """Custom type ActionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acs", 2),
          ("noAction", 3),
          ("ns", 1))
    )





class InputFormat(Integer32):
    """Custom type InputFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("der", 1),
          ("pem", 3))
    )





class IpAddressType(Integer32):
    """Custom type IpAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("mappedIp", 2),
          ("netScalerIp", 1),
          ("subnetIp", 4),
          ("vserverIp", 8))
    )





class IpAddressMode(Integer32):
    """Custom type IpAddressMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )





class AuthorizationStatus(Integer32):
    """Custom type AuthorizationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authorized", 1),
          ("notAuthorized", 2))
    )





class CommandExecutionStatus(Integer32):
    """Custom type CommandExecutionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("successful", 2))
    )





class MonitorType(Integer32):
    """Custom type MonitorType based on Integer32"""
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
              39)
        )
    )
    namedValues = NamedValues(
        *(("arp", 34),
          ("citrixAacLas", 37),
          ("citrixAacLoginPage", 36),
          ("citrixAg", 35),
          ("citrixStaService", 30),
          ("citrixStaServiceNhop", 31),
          ("citrixWebInterface", 29),
          ("citrixXdDdc", 38),
          ("citrixXmlService", 28),
          ("dbsResolver", 15),
          ("dns", 7),
          ("dnsTcp", 32),
          ("ftp", 8),
          ("ftpExtended", 20),
          ("http", 3),
          ("httpEcv", 5),
          ("httpInline", 17),
          ("https", 9),
          ("ldap", 25),
          ("ldnsDns", 13),
          ("ldnsPing", 11),
          ("ldnsTcp", 12),
          ("load", 27),
          ("mysql", 24),
          ("nd6", 39),
          ("nntp", 23),
          ("ping", 1),
          ("pop3", 26),
          ("radius", 14),
          ("rtsp", 33),
          ("sipTcp", 19),
          ("sipUdp", 18),
          ("smtp", 21),
          ("snmp", 22),
          ("tcp", 2),
          ("tcpEcv", 4),
          ("tcps", 10),
          ("udpEcv", 6),
          ("user", 16))
    )





class MonitorState(Integer32):
    """Custom type MonitorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              7)
        )
    )
    namedValues = NamedValues(
        *(("monitorStateDown", 1),
          ("monitorStateUnknown", 2),
          ("monitorStateUp", 7))
    )





class ServiceGroupState(Integer32):
    """Custom type ServiceGroupState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )





class VServerType(Integer32):
    """Custom type VServerType based on Integer32"""
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
        *(("cacheredirection", 5),
          ("contentswitching", 4),
          ("loadbalancing", 1),
          ("loadbalancinggroup", 2),
          ("sslvpn", 3),
          ("unknown", 0))
    )





class SvcEntityType(Integer32):
    """Custom type SvcEntityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("service", 0),
          ("serviceGroupMember", 1))
    )





class ActiveActiveState(Integer32):
    """Custom type ActiveActiveState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("backup", 2),
          ("notApplicable", 0))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsRoot_ObjectIdentity = ObjectIdentity
nsRoot = _NsRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1)
)
_NetScalerEvents_ObjectIdentity = ObjectIdentity
netScalerEvents = _NetScalerEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1)
)
_NetScalerEventsV2_ObjectIdentity = ObjectIdentity
netScalerEventsV2 = _NetScalerEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0)
)
if mibBuilder.loadTexts:
    netScalerEventsV2.setStatus("current")
_WsSystem_ObjectIdentity = ObjectIdentity
wsSystem = _WsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2)
)
_SysStatistics_ObjectIdentity = ObjectIdentity
sysStatistics = _SysStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1)
)
_TotalClientConnections_Type = Counter32
_TotalClientConnections_Object = MibScalar
totalClientConnections = _TotalClientConnections_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 1),
    _TotalClientConnections_Type()
)
totalClientConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalClientConnections.setStatus("obsolete")
_CurClientConnections_Type = Counter32
_CurClientConnections_Object = MibScalar
curClientConnections = _CurClientConnections_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 2),
    _CurClientConnections_Type()
)
curClientConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curClientConnections.setStatus("obsolete")
_TotalServerConnections_Type = Counter32
_TotalServerConnections_Object = MibScalar
totalServerConnections = _TotalServerConnections_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 3),
    _TotalServerConnections_Type()
)
totalServerConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalServerConnections.setStatus("obsolete")
_CurServerConnections_Type = Counter32
_CurServerConnections_Object = MibScalar
curServerConnections = _CurServerConnections_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 4),
    _CurServerConnections_Type()
)
curServerConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curServerConnections.setStatus("obsolete")
_ClientConnRefused_Type = Counter32
_ClientConnRefused_Object = MibScalar
clientConnRefused = _ClientConnRefused_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 5),
    _ClientConnRefused_Type()
)
clientConnRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientConnRefused.setStatus("obsolete")
_ReuseHit_Type = Counter32
_ReuseHit_Object = MibScalar
reuseHit = _ReuseHit_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 6),
    _ReuseHit_Type()
)
reuseHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reuseHit.setStatus("obsolete")
_ReuseMiss_Type = Counter32
_ReuseMiss_Object = MibScalar
reuseMiss = _ReuseMiss_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 7),
    _ReuseMiss_Type()
)
reuseMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reuseMiss.setStatus("obsolete")
_TotClientDontReuse_Type = Counter32
_TotClientDontReuse_Object = MibScalar
totClientDontReuse = _TotClientDontReuse_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 8),
    _TotClientDontReuse_Type()
)
totClientDontReuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totClientDontReuse.setStatus("obsolete")
_TotServerDontReuse_Type = Counter32
_TotServerDontReuse_Object = MibScalar
totServerDontReuse = _TotServerDontReuse_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 9),
    _TotServerDontReuse_Type()
)
totServerDontReuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totServerDontReuse.setStatus("obsolete")
_CurPhysicalServers_Type = Counter32
_CurPhysicalServers_Object = MibScalar
curPhysicalServers = _CurPhysicalServers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 10),
    _CurPhysicalServers_Type()
)
curPhysicalServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curPhysicalServers.setStatus("obsolete")
_TotPhysicalServers_Type = Counter32
_TotPhysicalServers_Object = MibScalar
totPhysicalServers = _TotPhysicalServers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 11),
    _TotPhysicalServers_Type()
)
totPhysicalServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totPhysicalServers.setStatus("obsolete")
_CookiePacketSeqReject_Type = Counter32
_CookiePacketSeqReject_Object = MibScalar
cookiePacketSeqReject = _CookiePacketSeqReject_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 12),
    _CookiePacketSeqReject_Type()
)
cookiePacketSeqReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cookiePacketSeqReject.setStatus("obsolete")
_CookieSignatureReject_Type = Counter32
_CookieSignatureReject_Object = MibScalar
cookieSignatureReject = _CookieSignatureReject_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 13),
    _CookieSignatureReject_Type()
)
cookieSignatureReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cookieSignatureReject.setStatus("obsolete")
_CpuUsage_Type = Counter32
_CpuUsage_Object = MibScalar
cpuUsage = _CpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 14),
    _CpuUsage_Type()
)
cpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUsage.setStatus("obsolete")
_UnackSyn_Type = Counter32
_UnackSyn_Object = MibScalar
unackSyn = _UnackSyn_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 15),
    _UnackSyn_Type()
)
unackSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unackSyn.setStatus("obsolete")
_CurClientEstablishedConn_Type = Counter32
_CurClientEstablishedConn_Object = MibScalar
curClientEstablishedConn = _CurClientEstablishedConn_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 16),
    _CurClientEstablishedConn_Type()
)
curClientEstablishedConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curClientEstablishedConn.setStatus("obsolete")
_CurServerEstablishedConn_Type = Counter32
_CurServerEstablishedConn_Object = MibScalar
curServerEstablishedConn = _CurServerEstablishedConn_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 17),
    _CurServerEstablishedConn_Type()
)
curServerEstablishedConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curServerEstablishedConn.setStatus("obsolete")
_WsHttpGroup_ObjectIdentity = ObjectIdentity
wsHttpGroup = _WsHttpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 18)
)
_TotalRequests_Type = Counter32
_TotalRequests_Object = MibScalar
totalRequests = _TotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 18, 1),
    _TotalRequests_Type()
)
totalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalRequests.setStatus("obsolete")
_TotalGets_Type = Counter32
_TotalGets_Object = MibScalar
totalGets = _TotalGets_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 18, 2),
    _TotalGets_Type()
)
totalGets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalGets.setStatus("obsolete")
_TotalRequests1_0_Type = Counter32
_TotalRequests1_0_Object = MibScalar
totalRequests1_0 = _TotalRequests1_0_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 18, 3),
    _TotalRequests1_0_Type()
)
totalRequests1_0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalRequests1_0.setStatus("obsolete")
_TotalPosts_Type = Counter32
_TotalPosts_Object = MibScalar
totalPosts = _TotalPosts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 18, 4),
    _TotalPosts_Type()
)
totalPosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalPosts.setStatus("obsolete")
_TotalResponses_Type = Counter32
_TotalResponses_Object = MibScalar
totalResponses = _TotalResponses_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 18, 5),
    _TotalResponses_Type()
)
totalResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalResponses.setStatus("obsolete")
_TotalResponses1_0_Type = Counter32
_TotalResponses1_0_Object = MibScalar
totalResponses1_0 = _TotalResponses1_0_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 18, 6),
    _TotalResponses1_0_Type()
)
totalResponses1_0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalResponses1_0.setStatus("obsolete")
_TotalContentLenResponses_Type = Counter32
_TotalContentLenResponses_Object = MibScalar
totalContentLenResponses = _TotalContentLenResponses_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 18, 7),
    _TotalContentLenResponses_Type()
)
totalContentLenResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalContentLenResponses.setStatus("obsolete")
_TotalChunkedResponses_Type = Counter32
_TotalChunkedResponses_Object = MibScalar
totalChunkedResponses = _TotalChunkedResponses_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 18, 8),
    _TotalChunkedResponses_Type()
)
totalChunkedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalChunkedResponses.setStatus("obsolete")
_TotalMultiPartResponses_Type = Counter32
_TotalMultiPartResponses_Object = MibScalar
totalMultiPartResponses = _TotalMultiPartResponses_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 18, 9),
    _TotalMultiPartResponses_Type()
)
totalMultiPartResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalMultiPartResponses.setStatus("obsolete")
_TotalIncompleteHeaders_Type = Counter32
_TotalIncompleteHeaders_Object = MibScalar
totalIncompleteHeaders = _TotalIncompleteHeaders_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 18, 10),
    _TotalIncompleteHeaders_Type()
)
totalIncompleteHeaders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalIncompleteHeaders.setStatus("obsolete")
_TotalIncompleteRequests_Type = Counter32
_TotalIncompleteRequests_Object = MibScalar
totalIncompleteRequests = _TotalIncompleteRequests_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 18, 11),
    _TotalIncompleteRequests_Type()
)
totalIncompleteRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalIncompleteRequests.setStatus("obsolete")
_TotalIncompleteResponses_Type = Counter32
_TotalIncompleteResponses_Object = MibScalar
totalIncompleteResponses = _TotalIncompleteResponses_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 18, 12),
    _TotalIncompleteResponses_Type()
)
totalIncompleteResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalIncompleteResponses.setStatus("obsolete")
_TotalPipeLinedRequests_Type = Counter32
_TotalPipeLinedRequests_Object = MibScalar
totalPipeLinedRequests = _TotalPipeLinedRequests_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 18, 13),
    _TotalPipeLinedRequests_Type()
)
totalPipeLinedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalPipeLinedRequests.setStatus("obsolete")
_ServerBusyErrs_Type = Counter32
_ServerBusyErrs_Object = MibScalar
serverBusyErrs = _ServerBusyErrs_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 18, 14),
    _ServerBusyErrs_Type()
)
serverBusyErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverBusyErrs.setStatus("obsolete")
_WsIfStatsTable_Object = MibTable
wsIfStatsTable = _WsIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 19)
)
if mibBuilder.loadTexts:
    wsIfStatsTable.setStatus("obsolete")
_WsIfStatsEntry_Object = MibTableRow
wsIfStatsEntry = _WsIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 19, 1)
)
wsIfStatsEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "index"),
)
if mibBuilder.loadTexts:
    wsIfStatsEntry.setStatus("obsolete")
_Index_Type = Integer32
_Index_Object = MibTableColumn
index = _Index_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 19, 1, 1),
    _Index_Type()
)
index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    index.setStatus("obsolete")
_WsIfName_Type = OctetString
_WsIfName_Object = MibTableColumn
wsIfName = _WsIfName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 19, 1, 2),
    _WsIfName_Type()
)
wsIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsIfName.setStatus("obsolete")
_WsIfMedia_Type = OctetString
_WsIfMedia_Object = MibTableColumn
wsIfMedia = _WsIfMedia_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 19, 1, 3),
    _WsIfMedia_Type()
)
wsIfMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsIfMedia.setStatus("obsolete")
_RxRawBandwidthUsage_Type = Counter32
_RxRawBandwidthUsage_Object = MibTableColumn
rxRawBandwidthUsage = _RxRawBandwidthUsage_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 19, 1, 4),
    _RxRawBandwidthUsage_Type()
)
rxRawBandwidthUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxRawBandwidthUsage.setStatus("obsolete")
_RxAveragePacketRate_Type = Counter32
_RxAveragePacketRate_Object = MibTableColumn
rxAveragePacketRate = _RxAveragePacketRate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 19, 1, 5),
    _RxAveragePacketRate_Type()
)
rxAveragePacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxAveragePacketRate.setStatus("obsolete")
_RxCurrentPacketRate_Type = Counter32
_RxCurrentPacketRate_Object = MibTableColumn
rxCurrentPacketRate = _RxCurrentPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 19, 1, 6),
    _RxCurrentPacketRate_Type()
)
rxCurrentPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxCurrentPacketRate.setStatus("obsolete")
_RxAveragePacketsSize_Type = Counter32
_RxAveragePacketsSize_Object = MibTableColumn
rxAveragePacketsSize = _RxAveragePacketsSize_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 19, 1, 7),
    _RxAveragePacketsSize_Type()
)
rxAveragePacketsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxAveragePacketsSize.setStatus("obsolete")
_RxFrameErrors_Type = Counter32
_RxFrameErrors_Object = MibTableColumn
rxFrameErrors = _RxFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 19, 1, 8),
    _RxFrameErrors_Type()
)
rxFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxFrameErrors.setStatus("obsolete")
_RxCrcErrors_Type = Counter32
_RxCrcErrors_Object = MibTableColumn
rxCrcErrors = _RxCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 19, 1, 9),
    _RxCrcErrors_Type()
)
rxCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxCrcErrors.setStatus("obsolete")
_RxAlignmentErrors_Type = Counter32
_RxAlignmentErrors_Object = MibTableColumn
rxAlignmentErrors = _RxAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 19, 1, 10),
    _RxAlignmentErrors_Type()
)
rxAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxAlignmentErrors.setStatus("obsolete")
_TxRawBandwidthUsage_Type = Counter32
_TxRawBandwidthUsage_Object = MibTableColumn
txRawBandwidthUsage = _TxRawBandwidthUsage_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 19, 1, 11),
    _TxRawBandwidthUsage_Type()
)
txRawBandwidthUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txRawBandwidthUsage.setStatus("obsolete")
_TxAveragePacketRate_Type = Counter32
_TxAveragePacketRate_Object = MibTableColumn
txAveragePacketRate = _TxAveragePacketRate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 19, 1, 12),
    _TxAveragePacketRate_Type()
)
txAveragePacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txAveragePacketRate.setStatus("obsolete")
_TxCurrentPacketRate_Type = Counter32
_TxCurrentPacketRate_Object = MibTableColumn
txCurrentPacketRate = _TxCurrentPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 19, 1, 13),
    _TxCurrentPacketRate_Type()
)
txCurrentPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txCurrentPacketRate.setStatus("obsolete")
_TxAveragePacketsSize_Type = Counter32
_TxAveragePacketsSize_Object = MibTableColumn
txAveragePacketsSize = _TxAveragePacketsSize_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 19, 1, 14),
    _TxAveragePacketsSize_Type()
)
txAveragePacketsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txAveragePacketsSize.setStatus("obsolete")
_TxExcessCollisions_Type = Counter32
_TxExcessCollisions_Object = MibTableColumn
txExcessCollisions = _TxExcessCollisions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 19, 1, 15),
    _TxExcessCollisions_Type()
)
txExcessCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txExcessCollisions.setStatus("obsolete")
_TxLateCollisions_Type = Counter32
_TxLateCollisions_Object = MibTableColumn
txLateCollisions = _TxLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 19, 1, 16),
    _TxLateCollisions_Type()
)
txLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txLateCollisions.setStatus("obsolete")
_TxCollisions_Type = Counter32
_TxCollisions_Object = MibTableColumn
txCollisions = _TxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 19, 1, 17),
    _TxCollisions_Type()
)
txCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txCollisions.setStatus("obsolete")
_TxMultiCollisionsErrors_Type = Counter32
_TxMultiCollisionsErrors_Object = MibTableColumn
txMultiCollisionsErrors = _TxMultiCollisionsErrors_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 19, 1, 18),
    _TxMultiCollisionsErrors_Type()
)
txMultiCollisionsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txMultiCollisionsErrors.setStatus("obsolete")
_TxCarrierErrors_Type = Counter32
_TxCarrierErrors_Object = MibTableColumn
txCarrierErrors = _TxCarrierErrors_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 19, 1, 19),
    _TxCarrierErrors_Type()
)
txCarrierErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txCarrierErrors.setStatus("obsolete")
_Wsudpgroup_ObjectIdentity = ObjectIdentity
wsudpgroup = _Wsudpgroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 20)
)
_Totudpsessions_Type = Counter32
_Totudpsessions_Object = MibScalar
totudpsessions = _Totudpsessions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 20, 1),
    _Totudpsessions_Type()
)
totudpsessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totudpsessions.setStatus("obsolete")
_Currudpsessions_Type = Counter32
_Currudpsessions_Object = MibScalar
currudpsessions = _Currudpsessions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 1, 20, 2),
    _Currudpsessions_Type()
)
currudpsessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currudpsessions.setStatus("obsolete")
_SysConfig_ObjectIdentity = ObjectIdentity
sysConfig = _SysConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 2)
)
_WsIpAddress_Type = IpAddress
_WsIpAddress_Object = MibScalar
wsIpAddress = _WsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 2, 1),
    _WsIpAddress_Type()
)
wsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsIpAddress.setStatus("obsolete")
_WsNetmask_Type = IpAddress
_WsNetmask_Object = MibScalar
wsNetmask = _WsNetmask_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 2, 2),
    _WsNetmask_Type()
)
wsNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetmask.setStatus("obsolete")
_WsMappedIpAddress_Type = IpAddress
_WsMappedIpAddress_Object = MibScalar
wsMappedIpAddress = _WsMappedIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 2, 3),
    _WsMappedIpAddress_Type()
)
wsMappedIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMappedIpAddress.setStatus("obsolete")
_WsLastMappedIpAddress_Type = IpAddress
_WsLastMappedIpAddress_Object = MibScalar
wsLastMappedIpAddress = _WsLastMappedIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 2, 4),
    _WsLastMappedIpAddress_Type()
)
wsLastMappedIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLastMappedIpAddress.setStatus("obsolete")
_WsMappedIpAddressRange_Type = Integer32
_WsMappedIpAddressRange_Object = MibScalar
wsMappedIpAddressRange = _WsMappedIpAddressRange_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 2, 5),
    _WsMappedIpAddressRange_Type()
)
wsMappedIpAddressRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMappedIpAddressRange.setStatus("obsolete")


class _WsFailOver_Type(Integer32):
    """Custom type wsFailOver based on Integer32"""
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


_WsFailOver_Type.__name__ = "Integer32"
_WsFailOver_Object = MibScalar
wsFailOver = _WsFailOver_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 2, 6),
    _WsFailOver_Type()
)
wsFailOver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsFailOver.setStatus("obsolete")
_WsPriority_Type = Integer32
_WsPriority_Object = MibScalar
wsPriority = _WsPriority_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 2, 7),
    _WsPriority_Type()
)
wsPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPriority.setStatus("obsolete")
_WsMaxClientList_Type = Integer32
_WsMaxClientList_Object = MibScalar
wsMaxClientList = _WsMaxClientList_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 2, 8),
    _WsMaxClientList_Type()
)
wsMaxClientList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMaxClientList.setStatus("obsolete")


class _WsClientIp_Type(Integer32):
    """Custom type wsClientIp based on Integer32"""
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


_WsClientIp_Type.__name__ = "Integer32"
_WsClientIp_Object = MibScalar
wsClientIp = _WsClientIp_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 2, 9),
    _WsClientIp_Type()
)
wsClientIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsClientIp.setStatus("obsolete")
_WsFailoverTime_Type = Integer32
_WsFailoverTime_Object = MibScalar
wsFailoverTime = _WsFailoverTime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 2, 10),
    _WsFailoverTime_Type()
)
wsFailoverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsFailoverTime.setStatus("obsolete")
_WsMaxRequestsPerConn_Type = Integer32
_WsMaxRequestsPerConn_Object = MibScalar
wsMaxRequestsPerConn = _WsMaxRequestsPerConn_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 2, 11),
    _WsMaxRequestsPerConn_Type()
)
wsMaxRequestsPerConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMaxRequestsPerConn.setStatus("obsolete")


class _WsSmoothConnection_Type(Integer32):
    """Custom type wsSmoothConnection based on Integer32"""
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


_WsSmoothConnection_Type.__name__ = "Integer32"
_WsSmoothConnection_Object = MibScalar
wsSmoothConnection = _WsSmoothConnection_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 2, 2, 12),
    _WsSmoothConnection_Type()
)
wsSmoothConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSmoothConnection.setStatus("obsolete")
_LoadBalancing_ObjectIdentity = ObjectIdentity
loadBalancing = _LoadBalancing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3)
)
_LbStatisticsTable_Object = MibTable
lbStatisticsTable = _LbStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lbStatisticsTable.setStatus("obsolete")
_LbStatisticsEntry_Object = MibTableRow
lbStatisticsEntry = _LbStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 1, 1)
)
lbStatisticsEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "vsId"),
    (0, "NS-ROOT-MIB", "psId"),
)
if mibBuilder.loadTexts:
    lbStatisticsEntry.setStatus("obsolete")
_VsId_Type = Integer32
_VsId_Object = MibTableColumn
vsId = _VsId_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 1, 1, 1),
    _VsId_Type()
)
vsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsId.setStatus("obsolete")
_PsId_Type = Integer32
_PsId_Object = MibTableColumn
psId = _PsId_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 1, 1, 2),
    _PsId_Type()
)
psId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psId.setStatus("obsolete")
_VsIpAddress_Type = IpAddress
_VsIpAddress_Object = MibTableColumn
vsIpAddress = _VsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 1, 1, 3),
    _VsIpAddress_Type()
)
vsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsIpAddress.setStatus("obsolete")
_VsPort_Type = Integer32
_VsPort_Object = MibTableColumn
vsPort = _VsPort_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 1, 1, 4),
    _VsPort_Type()
)
vsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsPort.setStatus("obsolete")
_PsIpAddress_Type = IpAddress
_PsIpAddress_Object = MibTableColumn
psIpAddress = _PsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 1, 1, 5),
    _PsIpAddress_Type()
)
psIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psIpAddress.setStatus("obsolete")
_PsPort_Type = Integer32
_PsPort_Object = MibTableColumn
psPort = _PsPort_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 1, 1, 6),
    _PsPort_Type()
)
psPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPort.setStatus("obsolete")


class _ProtocolType_Type(Integer32):
    """Custom type protocolType based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("adns", 17),
          ("any", 14),
          ("dns", 16),
          ("ftp", 1),
          ("ha", 19),
          ("http", 0),
          ("httpclient", 9),
          ("httpserver", 8),
          ("monitor", 5),
          ("monitorPing", 20),
          ("monitorUdp", 6),
          ("nat", 13),
          ("nntp", 7),
          ("rpcclient", 11),
          ("rpcserver", 10),
          ("serviceUnknown", 21),
          ("snmp", 18),
          ("ssf", 12),
          ("ssl", 15),
          ("sslBridge", 4),
          ("tcp", 2),
          ("udp", 3))
    )


_ProtocolType_Type.__name__ = "Integer32"
_ProtocolType_Object = MibTableColumn
protocolType = _ProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 1, 1, 7),
    _ProtocolType_Type()
)
protocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolType.setStatus("obsolete")


class _LbMethod_Type(Integer32):
    """Custom type lbMethod based on Integer32"""
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
        *(("asynchronousMAC", 4),
          ("destinationIPHashed", 7),
          ("domainHashed", 6),
          ("leastBandwidth", 9),
          ("leastConnections", 2),
          ("leastPackets", 10),
          ("leastResponse", 3),
          ("sourceIPHashed", 8),
          ("urlHashed", 5),
          ("weightedRoundRobin", 1))
    )


_LbMethod_Type.__name__ = "Integer32"
_LbMethod_Object = MibTableColumn
lbMethod = _LbMethod_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 1, 1, 8),
    _LbMethod_Type()
)
lbMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbMethod.setStatus("obsolete")
_ServiceHits_Type = Integer32
_ServiceHits_Object = MibTableColumn
serviceHits = _ServiceHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 1, 1, 9),
    _ServiceHits_Type()
)
serviceHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceHits.setStatus("obsolete")
_Latency_Type = Integer32
_Latency_Object = MibTableColumn
latency = _Latency_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 1, 1, 10),
    _Latency_Type()
)
latency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latency.setStatus("obsolete")
_Connections_Type = Integer32
_Connections_Object = MibTableColumn
connections = _Connections_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 1, 1, 11),
    _Connections_Type()
)
connections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connections.setStatus("obsolete")
_LbConfig_ObjectIdentity = ObjectIdentity
lbConfig = _LbConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 2)
)
_VirServiceTable_Object = MibTable
virServiceTable = _VirServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    virServiceTable.setStatus("obsolete")
_VirServiceEntry_Object = MibTableRow
virServiceEntry = _VirServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 2, 1, 1)
)
virServiceEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "vserId"),
)
if mibBuilder.loadTexts:
    virServiceEntry.setStatus("obsolete")
_VserId_Type = Integer32
_VserId_Object = MibTableColumn
vserId = _VserId_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 2, 1, 1, 1),
    _VserId_Type()
)
vserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vserId.setStatus("obsolete")
_IpAddress_Type = IpAddress
_IpAddress_Object = MibTableColumn
ipAddress = _IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 2, 1, 1, 2),
    _IpAddress_Type()
)
ipAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddress.setStatus("obsolete")
_Port_Type = Integer32
_Port_Object = MibTableColumn
port = _Port_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 2, 1, 1, 3),
    _Port_Type()
)
port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    port.setStatus("obsolete")


class _VsProtocolType_Type(Integer32):
    """Custom type vsProtocolType based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("adns", 17),
          ("any", 14),
          ("dns", 16),
          ("ftp", 1),
          ("ha", 19),
          ("http", 0),
          ("httpclient", 9),
          ("httpserver", 8),
          ("monitor", 5),
          ("monitorPing", 20),
          ("monitorUdp", 6),
          ("nat", 13),
          ("nntp", 7),
          ("rpcclient", 11),
          ("rpcserver", 10),
          ("serviceUnknown", 21),
          ("snmp", 18),
          ("ssf", 12),
          ("ssl", 15),
          ("sslBridge", 4),
          ("tcp", 2),
          ("udp", 3))
    )


_VsProtocolType_Type.__name__ = "Integer32"
_VsProtocolType_Object = MibTableColumn
vsProtocolType = _VsProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 2, 1, 1, 4),
    _VsProtocolType_Type()
)
vsProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsProtocolType.setStatus("obsolete")
_Name_Type = OctetString
_Name_Object = MibTableColumn
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 2, 1, 1, 5),
    _Name_Type()
)
name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    name.setStatus("obsolete")


class _VsLbMethod_Type(Integer32):
    """Custom type vsLbMethod based on Integer32"""
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
        *(("asynchronousMAC", 4),
          ("destinationIPHashed", 7),
          ("domainHashed", 6),
          ("leastBandwidth", 9),
          ("leastConnections", 2),
          ("leastPackets", 10),
          ("leastResponse", 3),
          ("sourceIPHashed", 8),
          ("urlHashed", 5),
          ("weightedRoundRobin", 1))
    )


_VsLbMethod_Type.__name__ = "Integer32"
_VsLbMethod_Object = MibTableColumn
vsLbMethod = _VsLbMethod_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 2, 1, 1, 6),
    _VsLbMethod_Type()
)
vsLbMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLbMethod.setStatus("obsolete")


class _PersistanceType_Type(Integer32):
    """Custom type persistanceType based on Integer32"""
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
        *(("cookieDelete", 3),
          ("cookieHash", 5),
          ("cookieInsert", 2),
          ("cookieRead", 4),
          ("server", 7),
          ("sessionId", 6),
          ("sourceIp", 1))
    )


_PersistanceType_Type.__name__ = "Integer32"
_PersistanceType_Object = MibTableColumn
persistanceType = _PersistanceType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 2, 1, 1, 7),
    _PersistanceType_Type()
)
persistanceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    persistanceType.setStatus("obsolete")
_PersistanceTimeout_Type = Integer32
_PersistanceTimeout_Object = MibTableColumn
persistanceTimeout = _PersistanceTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 2, 1, 1, 8),
    _PersistanceTimeout_Type()
)
persistanceTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    persistanceTimeout.setStatus("obsolete")


class _State_Type(Integer32):
    """Custom type state based on Integer32"""
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
        *(("busy", 3),
          ("down", 1),
          ("outOfService", 4),
          ("transitionToOutOfService", 5),
          ("unknown", 2),
          ("up", 0))
    )


_State_Type.__name__ = "Integer32"
_State_Object = MibTableColumn
state = _State_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 2, 1, 1, 9),
    _State_Type()
)
state.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    state.setStatus("obsolete")
_PhyServiceTable_Object = MibTable
phyServiceTable = _PhyServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    phyServiceTable.setStatus("obsolete")
_PhyServiceEntry_Object = MibTableRow
phyServiceEntry = _PhyServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 2, 2, 1)
)
phyServiceEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "pserId"),
)
if mibBuilder.loadTexts:
    phyServiceEntry.setStatus("obsolete")
_PserId_Type = Integer32
_PserId_Object = MibTableColumn
pserId = _PserId_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 2, 2, 1, 1),
    _PserId_Type()
)
pserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pserId.setStatus("obsolete")
_PserIpAddress_Type = IpAddress
_PserIpAddress_Object = MibTableColumn
pserIpAddress = _PserIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 2, 2, 1, 2),
    _PserIpAddress_Type()
)
pserIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pserIpAddress.setStatus("obsolete")
_PserPort_Type = Integer32
_PserPort_Object = MibTableColumn
pserPort = _PserPort_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 2, 2, 1, 3),
    _PserPort_Type()
)
pserPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pserPort.setStatus("obsolete")


class _PsProtocolType_Type(Integer32):
    """Custom type psProtocolType based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("adns", 17),
          ("any", 14),
          ("dns", 16),
          ("ftp", 1),
          ("ha", 19),
          ("http", 0),
          ("httpclient", 9),
          ("httpserver", 8),
          ("monitor", 5),
          ("monitorPing", 20),
          ("monitorUdp", 6),
          ("nat", 13),
          ("nntp", 7),
          ("rpcclient", 11),
          ("rpcserver", 10),
          ("serviceUnknown", 21),
          ("snmp", 18),
          ("ssf", 12),
          ("ssl", 15),
          ("sslBridge", 4),
          ("tcp", 2),
          ("udp", 3))
    )


_PsProtocolType_Type.__name__ = "Integer32"
_PsProtocolType_Object = MibTableColumn
psProtocolType = _PsProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 2, 2, 1, 4),
    _PsProtocolType_Type()
)
psProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psProtocolType.setStatus("obsolete")
_PsName_Type = OctetString
_PsName_Object = MibTableColumn
psName = _PsName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 2, 2, 1, 5),
    _PsName_Type()
)
psName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psName.setStatus("obsolete")


class _PsState_Type(Integer32):
    """Custom type psState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_PsState_Type.__name__ = "Integer32"
_PsState_Object = MibTableColumn
psState = _PsState_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 2, 2, 1, 6),
    _PsState_Type()
)
psState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psState.setStatus("obsolete")
_Weight_Type = Integer32
_Weight_Object = MibTableColumn
weight = _Weight_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 2, 2, 1, 7),
    _Weight_Type()
)
weight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    weight.setStatus("obsolete")
_PsVsIpAddress_Type = IpAddress
_PsVsIpAddress_Object = MibTableColumn
psVsIpAddress = _PsVsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 2, 2, 1, 8),
    _PsVsIpAddress_Type()
)
psVsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psVsIpAddress.setStatus("obsolete")
_PsVsPort_Type = Integer32
_PsVsPort_Object = MibTableColumn
psVsPort = _PsVsPort_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 3, 2, 2, 1, 9),
    _PsVsPort_Type()
)
psVsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psVsPort.setStatus("obsolete")
_SureConnect_ObjectIdentity = ObjectIdentity
sureConnect = _SureConnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4)
)
_ScStatistics_ObjectIdentity = ObjectIdentity
scStatistics = _ScStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 1)
)
_ScperServiceStatisticsTable_Object = MibTable
scperServiceStatisticsTable = _ScperServiceStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    scperServiceStatisticsTable.setStatus("obsolete")
_ScperServiceStatisticsEntry_Object = MibTableRow
scperServiceStatisticsEntry = _ScperServiceStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 1, 1, 1)
)
scperServiceStatisticsEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "devno"),
)
if mibBuilder.loadTexts:
    scperServiceStatisticsEntry.setStatus("obsolete")
_Devno_Type = Integer32
_Devno_Object = MibTableColumn
devno = _Devno_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 1, 1, 1, 1),
    _Devno_Type()
)
devno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devno.setStatus("obsolete")
_PhyIpAddress_Type = IpAddress
_PhyIpAddress_Object = MibTableColumn
phyIpAddress = _PhyIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 1, 1, 1, 2),
    _PhyIpAddress_Type()
)
phyIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyIpAddress.setStatus("obsolete")
_PhyPort_Type = Integer32
_PhyPort_Object = MibTableColumn
phyPort = _PhyPort_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 1, 1, 1, 3),
    _PhyPort_Type()
)
phyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyPort.setStatus("obsolete")


class _ScProtocolType_Type(Integer32):
    """Custom type scProtocolType based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("adns", 17),
          ("any", 14),
          ("dns", 16),
          ("ftp", 1),
          ("ha", 19),
          ("http", 0),
          ("httpclient", 9),
          ("httpserver", 8),
          ("monitor", 5),
          ("monitorPing", 20),
          ("monitorUdp", 6),
          ("nat", 13),
          ("nntp", 7),
          ("rpcclient", 11),
          ("rpcserver", 10),
          ("serviceUnknown", 21),
          ("snmp", 18),
          ("ssf", 12),
          ("ssl", 15),
          ("sslBridge", 4),
          ("tcp", 2),
          ("udp", 3))
    )


_ScProtocolType_Type.__name__ = "Integer32"
_ScProtocolType_Object = MibTableColumn
scProtocolType = _ScProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 1, 1, 1, 4),
    _ScProtocolType_Type()
)
scProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scProtocolType.setStatus("obsolete")
_CurrentDelay_Type = Integer32
_CurrentDelay_Object = MibTableColumn
currentDelay = _CurrentDelay_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 1, 1, 1, 5),
    _CurrentDelay_Type()
)
currentDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentDelay.setStatus("obsolete")
_AvgTxTime_Type = Integer32
_AvgTxTime_Object = MibTableColumn
avgTxTime = _AvgTxTime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 1, 1, 1, 6),
    _AvgTxTime_Type()
)
avgTxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgTxTime.setStatus("obsolete")
_SurgeCount_Type = Integer32
_SurgeCount_Object = MibTableColumn
surgeCount = _SurgeCount_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 1, 1, 1, 7),
    _SurgeCount_Type()
)
surgeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    surgeCount.setStatus("obsolete")
_IohCount_Type = Integer32
_IohCount_Object = MibTableColumn
iohCount = _IohCount_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 1, 1, 1, 8),
    _IohCount_Type()
)
iohCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iohCount.setStatus("obsolete")
_ScperPolicyStatisticsTable_Object = MibTable
scperPolicyStatisticsTable = _ScperPolicyStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    scperPolicyStatisticsTable.setStatus("obsolete")
_ScperPolicyStatisticsEntry_Object = MibTableRow
scperPolicyStatisticsEntry = _ScperPolicyStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 1, 2, 1)
)
scperPolicyStatisticsEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "policydevno"),
)
if mibBuilder.loadTexts:
    scperPolicyStatisticsEntry.setStatus("obsolete")
_Policydevno_Type = Integer32
_Policydevno_Object = MibTableColumn
policydevno = _Policydevno_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 1, 2, 1, 1),
    _Policydevno_Type()
)
policydevno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policydevno.setStatus("obsolete")
_PrimaryserviceIp_Type = IpAddress
_PrimaryserviceIp_Object = MibTableColumn
primaryserviceIp = _PrimaryserviceIp_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 1, 2, 1, 2),
    _PrimaryserviceIp_Type()
)
primaryserviceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    primaryserviceIp.setStatus("obsolete")
_Primaryserviceport_Type = Integer32
_Primaryserviceport_Object = MibTableColumn
primaryserviceport = _Primaryserviceport_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 1, 2, 1, 3),
    _Primaryserviceport_Type()
)
primaryserviceport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    primaryserviceport.setStatus("obsolete")
_DestserviceIp_Type = IpAddress
_DestserviceIp_Object = MibTableColumn
destserviceIp = _DestserviceIp_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 1, 2, 1, 4),
    _DestserviceIp_Type()
)
destserviceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destserviceIp.setStatus("obsolete")
_Destserviceport_Type = Integer32
_Destserviceport_Object = MibTableColumn
destserviceport = _Destserviceport_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 1, 2, 1, 5),
    _Destserviceport_Type()
)
destserviceport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destserviceport.setStatus("obsolete")
_Transactiontime_Type = Integer32
_Transactiontime_Object = MibTableColumn
transactiontime = _Transactiontime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 1, 2, 1, 6),
    _Transactiontime_Type()
)
transactiontime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transactiontime.setStatus("obsolete")
_Totaltransaction_Type = Integer32
_Totaltransaction_Object = MibTableColumn
totaltransaction = _Totaltransaction_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 1, 2, 1, 7),
    _Totaltransaction_Type()
)
totaltransaction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totaltransaction.setStatus("obsolete")
_Totalopenconnection_Type = Integer32
_Totalopenconnection_Object = MibTableColumn
totalopenconnection = _Totalopenconnection_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 1, 2, 1, 8),
    _Totalopenconnection_Type()
)
totalopenconnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalopenconnection.setStatus("obsolete")
_ScGlobalStats_ObjectIdentity = ObjectIdentity
scGlobalStats = _ScGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 1, 3)
)
_ScUrlHits_Type = Integer32
_ScUrlHits_Object = MibScalar
scUrlHits = _ScUrlHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 1, 3, 1),
    _ScUrlHits_Type()
)
scUrlHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scUrlHits.setStatus("obsolete")
_PopUps_Type = Integer32
_PopUps_Object = MibScalar
popUps = _PopUps_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 1, 3, 2),
    _PopUps_Type()
)
popUps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    popUps.setStatus("obsolete")
_AltContUrls_Type = Integer32
_AltContUrls_Object = MibScalar
altContUrls = _AltContUrls_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 1, 3, 3),
    _AltContUrls_Type()
)
altContUrls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altContUrls.setStatus("obsolete")
_SessReqs_Type = Integer32
_SessReqs_Object = MibScalar
sessReqs = _SessReqs_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 1, 3, 4),
    _SessReqs_Type()
)
sessReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessReqs.setStatus("obsolete")
_PostReqs_Type = Integer32
_PostReqs_Object = MibScalar
postReqs = _PostReqs_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 1, 3, 5),
    _PostReqs_Type()
)
postReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postReqs.setStatus("obsolete")
_ThresholdFail_Type = Integer32
_ThresholdFail_Object = MibScalar
thresholdFail = _ThresholdFail_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 1, 3, 6),
    _ThresholdFail_Type()
)
thresholdFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdFail.setStatus("obsolete")
_FaultyCookies_Type = Integer32
_FaultyCookies_Object = MibScalar
faultyCookies = _FaultyCookies_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 1, 3, 7),
    _FaultyCookies_Type()
)
faultyCookies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultyCookies.setStatus("obsolete")
_UnSupBrow_Type = Integer32
_UnSupBrow_Object = MibScalar
unSupBrow = _UnSupBrow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 1, 3, 8),
    _UnSupBrow_Type()
)
unSupBrow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unSupBrow.setStatus("obsolete")
_ResetStats_Type = Integer32
_ResetStats_Object = MibScalar
resetStats = _ResetStats_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 1, 3, 9),
    _ResetStats_Type()
)
resetStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resetStats.setStatus("obsolete")
_ScConfig_ObjectIdentity = ObjectIdentity
scConfig = _ScConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 2)
)
_ScPolicyconfigTable_Object = MibTable
scPolicyconfigTable = _ScPolicyconfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    scPolicyconfigTable.setStatus("obsolete")
_ScPolicyconfigEntry_Object = MibTableRow
scPolicyconfigEntry = _ScPolicyconfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 2, 1, 1)
)
scPolicyconfigEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "policyIndex"),
)
if mibBuilder.loadTexts:
    scPolicyconfigEntry.setStatus("obsolete")
_PolicyIndex_Type = Integer32
_PolicyIndex_Object = MibTableColumn
policyIndex = _PolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 2, 1, 1, 1),
    _PolicyIndex_Type()
)
policyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyIndex.setStatus("obsolete")
_PolicyName_Type = OctetString
_PolicyName_Object = MibTableColumn
policyName = _PolicyName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 2, 1, 1, 2),
    _PolicyName_Type()
)
policyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyName.setStatus("obsolete")
_ScPolicyUrl_Type = OctetString
_ScPolicyUrl_Object = MibTableColumn
scPolicyUrl = _ScPolicyUrl_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 2, 1, 1, 3),
    _ScPolicyUrl_Type()
)
scPolicyUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scPolicyUrl.setStatus("obsolete")


class _DelayThreshold_Type(Integer32):
    """Custom type delayThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("notconfigured", -1)
    )


_DelayThreshold_Type.__name__ = "Integer32"
_DelayThreshold_Object = MibTableColumn
delayThreshold = _DelayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 2, 1, 1, 4),
    _DelayThreshold_Type()
)
delayThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayThreshold.setStatus("obsolete")


class _MaxConnections_Type(Integer32):
    """Custom type maxConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("notconfigured", -1)
    )


_MaxConnections_Type.__name__ = "Integer32"
_MaxConnections_Object = MibTableColumn
maxConnections = _MaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 2, 1, 1, 5),
    _MaxConnections_Type()
)
maxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxConnections.setStatus("obsolete")


class _ActionType_Type(Integer32):
    """Custom type actionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("acs", 1),
          ("noAction", 4),
          ("ns", 0))
    )


_ActionType_Type.__name__ = "Integer32"
_ActionType_Object = MibTableColumn
actionType = _ActionType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 2, 1, 1, 6),
    _ActionType_Type()
)
actionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actionType.setStatus("obsolete")
_AlternatecontentServicename_Type = OctetString
_AlternatecontentServicename_Object = MibTableColumn
alternatecontentServicename = _AlternatecontentServicename_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 2, 1, 1, 7),
    _AlternatecontentServicename_Type()
)
alternatecontentServicename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alternatecontentServicename.setStatus("obsolete")
_RuleName_Type = OctetString
_RuleName_Object = MibTableColumn
ruleName = _RuleName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 2, 1, 1, 8),
    _RuleName_Type()
)
ruleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleName.setStatus("obsolete")
_AlternatecontentPath_Type = OctetString
_AlternatecontentPath_Object = MibTableColumn
alternatecontentPath = _AlternatecontentPath_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 4, 2, 1, 1, 9),
    _AlternatecontentPath_Type()
)
alternatecontentPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alternatecontentPath.setStatus("obsolete")
_ContentSwitching_ObjectIdentity = ObjectIdentity
contentSwitching = _ContentSwitching_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 5)
)
_CswStatisticsTable_Object = MibTable
cswStatisticsTable = _CswStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cswStatisticsTable.setStatus("obsolete")
_CswStatisticsEntry_Object = MibTableRow
cswStatisticsEntry = _CswStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 5, 1, 1)
)
cswStatisticsEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "cswIndex"),
)
if mibBuilder.loadTexts:
    cswStatisticsEntry.setStatus("obsolete")
_CswIndex_Type = Integer32
_CswIndex_Object = MibTableColumn
cswIndex = _CswIndex_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 5, 1, 1, 1),
    _CswIndex_Type()
)
cswIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswIndex.setStatus("obsolete")
_CswVsIpAddress_Type = IpAddress
_CswVsIpAddress_Object = MibTableColumn
cswVsIpAddress = _CswVsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 5, 1, 1, 2),
    _CswVsIpAddress_Type()
)
cswVsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswVsIpAddress.setStatus("obsolete")
_CswVsPort_Type = Integer32
_CswVsPort_Object = MibTableColumn
cswVsPort = _CswVsPort_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 5, 1, 1, 3),
    _CswVsPort_Type()
)
cswVsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswVsPort.setStatus("obsolete")


class _CswProtocolType_Type(Integer32):
    """Custom type cswProtocolType based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("adns", 17),
          ("any", 14),
          ("dns", 16),
          ("ftp", 1),
          ("ha", 19),
          ("http", 0),
          ("httpclient", 9),
          ("httpserver", 8),
          ("monitor", 5),
          ("monitorPing", 20),
          ("monitorUdp", 6),
          ("nat", 13),
          ("nntp", 7),
          ("rpcclient", 11),
          ("rpcserver", 10),
          ("serviceUnknown", 21),
          ("snmp", 18),
          ("ssf", 12),
          ("ssl", 15),
          ("sslBridge", 4),
          ("tcp", 2),
          ("udp", 3))
    )


_CswProtocolType_Type.__name__ = "Integer32"
_CswProtocolType_Object = MibTableColumn
cswProtocolType = _CswProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 5, 1, 1, 4),
    _CswProtocolType_Type()
)
cswProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswProtocolType.setStatus("obsolete")
_VirServiceName_Type = OctetString
_VirServiceName_Object = MibTableColumn
virServiceName = _VirServiceName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 5, 1, 1, 5),
    _VirServiceName_Type()
)
virServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virServiceName.setStatus("obsolete")
_VsHits_Type = Integer32
_VsHits_Object = MibTableColumn
vsHits = _VsHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 5, 1, 1, 6),
    _VsHits_Type()
)
vsHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsHits.setStatus("obsolete")
_VsMiss_Type = Integer32
_VsMiss_Object = MibTableColumn
vsMiss = _VsMiss_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 5, 1, 1, 7),
    _VsMiss_Type()
)
vsMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsMiss.setStatus("obsolete")
_CswConfigTable_Object = MibTable
cswConfigTable = _CswConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cswConfigTable.setStatus("obsolete")
_CswConfigEntry_Object = MibTableRow
cswConfigEntry = _CswConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 5, 2, 1)
)
cswConfigEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "cswVsId"),
    (0, "NS-ROOT-MIB", "policyId"),
)
if mibBuilder.loadTexts:
    cswConfigEntry.setStatus("obsolete")
_CswVsId_Type = Integer32
_CswVsId_Object = MibTableColumn
cswVsId = _CswVsId_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 5, 2, 1, 1),
    _CswVsId_Type()
)
cswVsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswVsId.setStatus("obsolete")
_PolicyId_Type = Integer32
_PolicyId_Object = MibTableColumn
policyId = _PolicyId_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 5, 2, 1, 2),
    _PolicyId_Type()
)
policyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyId.setStatus("obsolete")
_VServerName_Type = OctetString
_VServerName_Object = MibTableColumn
vServerName = _VServerName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 5, 2, 1, 3),
    _VServerName_Type()
)
vServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerName.setStatus("obsolete")
_Policyname_Type = OctetString
_Policyname_Object = MibTableColumn
policyname = _Policyname_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 5, 2, 1, 4),
    _Policyname_Type()
)
policyname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyname.setStatus("obsolete")
_Policyvalue_Type = OctetString
_Policyvalue_Object = MibTableColumn
policyvalue = _Policyvalue_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 5, 2, 1, 5),
    _Policyvalue_Type()
)
policyvalue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyvalue.setStatus("obsolete")
_PolicyHits_Type = Integer32
_PolicyHits_Object = MibTableColumn
policyHits = _PolicyHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 5, 2, 1, 6),
    _PolicyHits_Type()
)
policyHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyHits.setStatus("obsolete")
_Domain_Type = OctetString
_Domain_Object = MibTableColumn
domain = _Domain_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 5, 2, 1, 7),
    _Domain_Type()
)
domain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domain.setStatus("obsolete")
_CacheRedirection_ObjectIdentity = ObjectIdentity
cacheRedirection = _CacheRedirection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6)
)
_CrStatisticsTable_Object = MibTable
crStatisticsTable = _CrStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6, 1)
)
if mibBuilder.loadTexts:
    crStatisticsTable.setStatus("obsolete")
_CrStatisticsEntry_Object = MibTableRow
crStatisticsEntry = _CrStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6, 1, 1)
)
crStatisticsEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "crVsIndex"),
)
if mibBuilder.loadTexts:
    crStatisticsEntry.setStatus("obsolete")
_CrVsIndex_Type = Integer32
_CrVsIndex_Object = MibTableColumn
crVsIndex = _CrVsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6, 1, 1, 1),
    _CrVsIndex_Type()
)
crVsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crVsIndex.setStatus("obsolete")
_CrVsIpAddress_Type = IpAddress
_CrVsIpAddress_Object = MibTableColumn
crVsIpAddress = _CrVsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6, 1, 1, 2),
    _CrVsIpAddress_Type()
)
crVsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crVsIpAddress.setStatus("obsolete")
_CrVsPort_Type = Integer32
_CrVsPort_Object = MibTableColumn
crVsPort = _CrVsPort_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6, 1, 1, 3),
    _CrVsPort_Type()
)
crVsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crVsPort.setStatus("obsolete")


class _CrProtocolType_Type(Integer32):
    """Custom type crProtocolType based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("adns", 17),
          ("any", 14),
          ("dns", 16),
          ("ftp", 1),
          ("ha", 19),
          ("http", 0),
          ("httpclient", 9),
          ("httpserver", 8),
          ("monitor", 5),
          ("monitorPing", 20),
          ("monitorUdp", 6),
          ("nat", 13),
          ("nntp", 7),
          ("rpcclient", 11),
          ("rpcserver", 10),
          ("serviceUnknown", 21),
          ("snmp", 18),
          ("ssf", 12),
          ("ssl", 15),
          ("sslBridge", 4),
          ("tcp", 2),
          ("udp", 3))
    )


_CrProtocolType_Type.__name__ = "Integer32"
_CrProtocolType_Object = MibTableColumn
crProtocolType = _CrProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6, 1, 1, 4),
    _CrProtocolType_Type()
)
crProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crProtocolType.setStatus("obsolete")
_CrVirServiceName_Type = OctetString
_CrVirServiceName_Object = MibTableColumn
crVirServiceName = _CrVirServiceName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6, 1, 1, 5),
    _CrVirServiceName_Type()
)
crVirServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crVirServiceName.setStatus("obsolete")
_CrVsHits_Type = Integer32
_CrVsHits_Object = MibTableColumn
crVsHits = _CrVsHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6, 1, 1, 6),
    _CrVsHits_Type()
)
crVsHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crVsHits.setStatus("obsolete")
_CrVsMiss_Type = Integer32
_CrVsMiss_Object = MibTableColumn
crVsMiss = _CrVsMiss_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6, 1, 1, 7),
    _CrVsMiss_Type()
)
crVsMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crVsMiss.setStatus("obsolete")
_CrConfig_ObjectIdentity = ObjectIdentity
crConfig = _CrConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6, 2)
)
_CrPolBindConfigTable_Object = MibTable
crPolBindConfigTable = _CrPolBindConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    crPolBindConfigTable.setStatus("obsolete")
_CrPolBindConfigEntry_Object = MibTableRow
crPolBindConfigEntry = _CrPolBindConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6, 2, 1, 1)
)
crPolBindConfigEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "bindId"),
)
if mibBuilder.loadTexts:
    crPolBindConfigEntry.setStatus("obsolete")
_BindId_Type = Integer32
_BindId_Object = MibTableColumn
bindId = _BindId_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6, 2, 1, 1, 1),
    _BindId_Type()
)
bindId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bindId.setStatus("obsolete")
_CrbVServerName_Type = OctetString
_CrbVServerName_Object = MibTableColumn
crbVServerName = _CrbVServerName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6, 2, 1, 1, 2),
    _CrbVServerName_Type()
)
crbVServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crbVServerName.setStatus("obsolete")
_CrbPolicyname_Type = OctetString
_CrbPolicyname_Object = MibTableColumn
crbPolicyname = _CrbPolicyname_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6, 2, 1, 1, 3),
    _CrbPolicyname_Type()
)
crbPolicyname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crbPolicyname.setStatus("obsolete")
_CrbPolicyvalue_Type = OctetString
_CrbPolicyvalue_Object = MibTableColumn
crbPolicyvalue = _CrbPolicyvalue_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6, 2, 1, 1, 4),
    _CrbPolicyvalue_Type()
)
crbPolicyvalue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crbPolicyvalue.setStatus("obsolete")
_CrbPolicyHits_Type = Integer32
_CrbPolicyHits_Object = MibTableColumn
crbPolicyHits = _CrbPolicyHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6, 2, 1, 1, 5),
    _CrbPolicyHits_Type()
)
crbPolicyHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crbPolicyHits.setStatus("obsolete")
_CrMapBindConfigTable_Object = MibTable
crMapBindConfigTable = _CrMapBindConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6, 2, 2)
)
if mibBuilder.loadTexts:
    crMapBindConfigTable.setStatus("obsolete")
_CrMapBindConfigEntry_Object = MibTableRow
crMapBindConfigEntry = _CrMapBindConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6, 2, 2, 1)
)
crMapBindConfigEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "mapbindId"),
)
if mibBuilder.loadTexts:
    crMapBindConfigEntry.setStatus("obsolete")
_MapbindId_Type = Integer32
_MapbindId_Object = MibTableColumn
mapbindId = _MapbindId_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6, 2, 2, 1, 1),
    _MapbindId_Type()
)
mapbindId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapbindId.setStatus("obsolete")
_MapName_Type = OctetString
_MapName_Object = MibTableColumn
mapName = _MapName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6, 2, 2, 1, 2),
    _MapName_Type()
)
mapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapName.setStatus("obsolete")
_MapHits_Type = Integer32
_MapHits_Object = MibTableColumn
mapHits = _MapHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6, 2, 2, 1, 3),
    _MapHits_Type()
)
mapHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapHits.setStatus("obsolete")
_VserverName_Type = OctetString
_VserverName_Object = MibTableColumn
vserverName = _VserverName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6, 2, 2, 1, 4),
    _VserverName_Type()
)
vserverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vserverName.setStatus("obsolete")
_CrMapConfigTable_Object = MibTable
crMapConfigTable = _CrMapConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6, 2, 3)
)
if mibBuilder.loadTexts:
    crMapConfigTable.setStatus("obsolete")
_CrMapConfigEntry_Object = MibTableRow
crMapConfigEntry = _CrMapConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6, 2, 3, 1)
)
crMapConfigEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "crmIndex"),
)
if mibBuilder.loadTexts:
    crMapConfigEntry.setStatus("obsolete")
_CrmIndex_Type = Integer32
_CrmIndex_Object = MibTableColumn
crmIndex = _CrmIndex_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6, 2, 3, 1, 1),
    _CrmIndex_Type()
)
crmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmIndex.setStatus("obsolete")
_CrmMapName_Type = OctetString
_CrmMapName_Object = MibTableColumn
crmMapName = _CrmMapName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6, 2, 3, 1, 2),
    _CrmMapName_Type()
)
crmMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmMapName.setStatus("obsolete")
_SrcDomain_Type = OctetString
_SrcDomain_Object = MibTableColumn
srcDomain = _SrcDomain_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6, 2, 3, 1, 3),
    _SrcDomain_Type()
)
srcDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srcDomain.setStatus("obsolete")
_DstDomain_Type = OctetString
_DstDomain_Object = MibTableColumn
dstDomain = _DstDomain_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6, 2, 3, 1, 4),
    _DstDomain_Type()
)
dstDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstDomain.setStatus("obsolete")
_SrcUrl_Type = OctetString
_SrcUrl_Object = MibTableColumn
srcUrl = _SrcUrl_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6, 2, 3, 1, 5),
    _SrcUrl_Type()
)
srcUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srcUrl.setStatus("obsolete")
_DstUrl_Type = OctetString
_DstUrl_Object = MibTableColumn
dstUrl = _DstUrl_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 6, 2, 3, 1, 6),
    _DstUrl_Type()
)
dstUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstUrl.setStatus("obsolete")
_Compression_ObjectIdentity = ObjectIdentity
compression = _Compression_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 7)
)
_CompressionStats_ObjectIdentity = ObjectIdentity
compressionStats = _CompressionStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 7, 1)
)
_CmpTotRequests_Type = Counter32
_CmpTotRequests_Object = MibScalar
cmpTotRequests = _CmpTotRequests_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 7, 1, 1),
    _CmpTotRequests_Type()
)
cmpTotRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpTotRequests.setStatus("obsolete")
_CmpTotTxbytes_Type = Counter32
_CmpTotTxbytes_Object = MibScalar
cmpTotTxbytes = _CmpTotTxbytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 7, 1, 2),
    _CmpTotTxbytes_Type()
)
cmpTotTxbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpTotTxbytes.setStatus("obsolete")
_CmpTotRxbytes_Type = Counter32
_CmpTotRxbytes_Object = MibScalar
cmpTotRxbytes = _CmpTotRxbytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 7, 1, 3),
    _CmpTotRxbytes_Type()
)
cmpTotRxbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpTotRxbytes.setStatus("obsolete")
_CmpTotTxpkts_Type = Counter32
_CmpTotTxpkts_Object = MibScalar
cmpTotTxpkts = _CmpTotTxpkts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 7, 1, 4),
    _CmpTotTxpkts_Type()
)
cmpTotTxpkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpTotTxpkts.setStatus("obsolete")
_CmpTotRxpkts_Type = Counter32
_CmpTotRxpkts_Object = MibScalar
cmpTotRxpkts = _CmpTotRxpkts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 7, 1, 5),
    _CmpTotRxpkts_Type()
)
cmpTotRxpkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpTotRxpkts.setStatus("obsolete")
_CompressionRatio_Type = OctetString
_CompressionRatio_Object = MibScalar
compressionRatio = _CompressionRatio_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 7, 1, 6),
    _CompressionRatio_Type()
)
compressionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressionRatio.setStatus("obsolete")
_TotalDataCompressionRatio_Type = OctetString
_TotalDataCompressionRatio_Object = MibScalar
totalDataCompressionRatio = _TotalDataCompressionRatio_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 7, 1, 7),
    _TotalDataCompressionRatio_Type()
)
totalDataCompressionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalDataCompressionRatio.setStatus("obsolete")
_Vlan_ObjectIdentity = ObjectIdentity
vlan = _Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 8)
)
_VlanstatsTable_Object = MibTable
vlanstatsTable = _VlanstatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 8, 1)
)
if mibBuilder.loadTexts:
    vlanstatsTable.setStatus("obsolete")
_VlanstatsEntry_Object = MibTableRow
vlanstatsEntry = _VlanstatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 8, 1, 1)
)
vlanstatsEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "vlansDevno"),
)
if mibBuilder.loadTexts:
    vlanstatsEntry.setStatus("obsolete")
_VlansDevno_Type = Integer32
_VlansDevno_Object = MibTableColumn
vlansDevno = _VlansDevno_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 8, 1, 1, 1),
    _VlansDevno_Type()
)
vlansDevno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlansDevno.setStatus("obsolete")
_Totalrxpkts_Type = Counter32
_Totalrxpkts_Object = MibTableColumn
totalrxpkts = _Totalrxpkts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 8, 1, 1, 2),
    _Totalrxpkts_Type()
)
totalrxpkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalrxpkts.setStatus("obsolete")
_Totaltxpkts_Type = Counter32
_Totaltxpkts_Object = MibTableColumn
totaltxpkts = _Totaltxpkts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 8, 1, 1, 3),
    _Totaltxpkts_Type()
)
totaltxpkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totaltxpkts.setStatus("obsolete")
_Totalrxbytes_Type = Counter32
_Totalrxbytes_Object = MibTableColumn
totalrxbytes = _Totalrxbytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 8, 1, 1, 4),
    _Totalrxbytes_Type()
)
totalrxbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalrxbytes.setStatus("obsolete")
_Totaltxbytes_Type = Counter32
_Totaltxbytes_Object = MibTableColumn
totaltxbytes = _Totaltxbytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 8, 1, 1, 5),
    _Totaltxbytes_Type()
)
totaltxbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totaltxbytes.setStatus("obsolete")
_Totaldroppedpkts_Type = Counter32
_Totaldroppedpkts_Object = MibTableColumn
totaldroppedpkts = _Totaldroppedpkts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 8, 1, 1, 6),
    _Totaldroppedpkts_Type()
)
totaldroppedpkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totaldroppedpkts.setStatus("obsolete")
_Totalbroadcastpackets_Type = Counter32
_Totalbroadcastpackets_Object = MibTableColumn
totalbroadcastpackets = _Totalbroadcastpackets_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 8, 1, 1, 7),
    _Totalbroadcastpackets_Type()
)
totalbroadcastpackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalbroadcastpackets.setStatus("obsolete")
_VlanconfigTable_Object = MibTable
vlanconfigTable = _VlanconfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 8, 2)
)
if mibBuilder.loadTexts:
    vlanconfigTable.setStatus("obsolete")
_VlanconfigEntry_Object = MibTableRow
vlanconfigEntry = _VlanconfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 8, 2, 1)
)
vlanconfigEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "vlancDevno"),
)
if mibBuilder.loadTexts:
    vlanconfigEntry.setStatus("obsolete")
_VlancDevno_Type = Integer32
_VlancDevno_Object = MibTableColumn
vlancDevno = _VlancDevno_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 8, 2, 1, 1),
    _VlancDevno_Type()
)
vlancDevno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlancDevno.setStatus("obsolete")
_TagId_Type = Integer32
_TagId_Object = MibTableColumn
tagId = _TagId_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 8, 2, 1, 2),
    _TagId_Type()
)
tagId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tagId.setStatus("obsolete")
_VlancInterfaces_Type = OctetString
_VlancInterfaces_Object = MibTableColumn
vlancInterfaces = _VlancInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 8, 2, 1, 3),
    _VlancInterfaces_Type()
)
vlancInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlancInterfaces.setStatus("obsolete")
_Ipaddress_Type = IpAddress
_Ipaddress_Object = MibTableColumn
ipaddress = _Ipaddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 8, 2, 1, 4),
    _Ipaddress_Type()
)
ipaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddress.setStatus("obsolete")
_Netmask_Type = IpAddress
_Netmask_Object = MibTableColumn
netmask = _Netmask_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 8, 2, 1, 5),
    _Netmask_Type()
)
netmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netmask.setStatus("obsolete")
_Tagging_Type = OctetString
_Tagging_Object = MibTableColumn
tagging = _Tagging_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 8, 2, 1, 6),
    _Tagging_Type()
)
tagging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tagging.setStatus("obsolete")
_DomainNameService_ObjectIdentity = ObjectIdentity
domainNameService = _DomainNameService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 9)
)
_DnsServer_ObjectIdentity = ObjectIdentity
dnsServer = _DnsServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 9, 1)
)
_DnsServerStatistics_ObjectIdentity = ObjectIdentity
dnsServerStatistics = _DnsServerStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 9, 1, 1)
)
_TotQueries_Type = Counter32
_TotQueries_Object = MibScalar
totQueries = _TotQueries_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 9, 1, 1, 1),
    _TotQueries_Type()
)
totQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totQueries.setStatus("obsolete")
_TotAnswers_Type = Counter32
_TotAnswers_Object = MibScalar
totAnswers = _TotAnswers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 9, 1, 1, 2),
    _TotAnswers_Type()
)
totAnswers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totAnswers.setStatus("obsolete")
_TotAuthAns_Type = Counter32
_TotAuthAns_Object = MibScalar
totAuthAns = _TotAuthAns_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 9, 1, 1, 3),
    _TotAuthAns_Type()
)
totAuthAns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totAuthAns.setStatus("obsolete")
_TotAuthNoNames_Type = Counter32
_TotAuthNoNames_Object = MibScalar
totAuthNoNames = _TotAuthNoNames_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 9, 1, 1, 4),
    _TotAuthNoNames_Type()
)
totAuthNoNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totAuthNoNames.setStatus("obsolete")
_TotAuthNoDataResps_Type = Counter32
_TotAuthNoDataResps_Object = MibScalar
totAuthNoDataResps = _TotAuthNoDataResps_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 9, 1, 1, 5),
    _TotAuthNoDataResps_Type()
)
totAuthNoDataResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totAuthNoDataResps.setStatus("obsolete")
_TotNonAuthDatas_Type = Counter32
_TotNonAuthDatas_Object = MibScalar
totNonAuthDatas = _TotNonAuthDatas_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 9, 1, 1, 6),
    _TotNonAuthDatas_Type()
)
totNonAuthDatas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totNonAuthDatas.setStatus("obsolete")
_TotNonAuthNoDatas_Type = Counter32
_TotNonAuthNoDatas_Object = MibScalar
totNonAuthNoDatas = _TotNonAuthNoDatas_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 9, 1, 1, 7),
    _TotNonAuthNoDatas_Type()
)
totNonAuthNoDatas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totNonAuthNoDatas.setStatus("obsolete")
_TotReqRefusals_Type = Counter32
_TotReqRefusals_Object = MibScalar
totReqRefusals = _TotReqRefusals_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 9, 1, 1, 8),
    _TotReqRefusals_Type()
)
totReqRefusals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totReqRefusals.setStatus("obsolete")
_TotReqUnparses_Type = Counter32
_TotReqUnparses_Object = MibScalar
totReqUnparses = _TotReqUnparses_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 9, 1, 1, 9),
    _TotReqUnparses_Type()
)
totReqUnparses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totReqUnparses.setStatus("obsolete")
_TotOtherErrors_Type = Counter32
_TotOtherErrors_Object = MibScalar
totOtherErrors = _TotOtherErrors_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 9, 1, 1, 10),
    _TotOtherErrors_Type()
)
totOtherErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totOtherErrors.setStatus("obsolete")
_ARecQueries_Type = Counter32
_ARecQueries_Object = MibScalar
aRecQueries = _ARecQueries_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 9, 1, 1, 11),
    _ARecQueries_Type()
)
aRecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRecQueries.setStatus("obsolete")
_NsRecQueries_Type = Counter32
_NsRecQueries_Object = MibScalar
nsRecQueries = _NsRecQueries_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 9, 1, 1, 12),
    _NsRecQueries_Type()
)
nsRecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsRecQueries.setStatus("obsolete")
_MxRecQueries_Type = Counter32
_MxRecQueries_Object = MibScalar
mxRecQueries = _MxRecQueries_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 9, 1, 1, 13),
    _MxRecQueries_Type()
)
mxRecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mxRecQueries.setStatus("obsolete")
_SoaRecQueries_Type = Counter32
_SoaRecQueries_Object = MibScalar
soaRecQueries = _SoaRecQueries_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 9, 1, 1, 14),
    _SoaRecQueries_Type()
)
soaRecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soaRecQueries.setStatus("obsolete")
_CnameRecQueries_Type = Counter32
_CnameRecQueries_Object = MibScalar
cnameRecQueries = _CnameRecQueries_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 9, 1, 1, 15),
    _CnameRecQueries_Type()
)
cnameRecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnameRecQueries.setStatus("obsolete")
_TotUnsupportedQueries_Type = Counter32
_TotUnsupportedQueries_Object = MibScalar
totUnsupportedQueries = _TotUnsupportedQueries_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 9, 1, 1, 16),
    _TotUnsupportedQueries_Type()
)
totUnsupportedQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totUnsupportedQueries.setStatus("obsolete")
_DnsServerConfig_ObjectIdentity = ObjectIdentity
dnsServerConfig = _DnsServerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 9, 1, 2)
)


class _DnsServerRecursion_Type(Integer32):
    """Custom type dnsServerRecursion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("restricted", 2),
          ("unavailable", 3))
    )


_DnsServerRecursion_Type.__name__ = "Integer32"
_DnsServerRecursion_Object = MibScalar
dnsServerRecursion = _DnsServerRecursion_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 9, 1, 2, 1),
    _DnsServerRecursion_Type()
)
dnsServerRecursion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServerRecursion.setStatus("obsolete")
_DnsServerZoneTable_Object = MibTable
dnsServerZoneTable = _DnsServerZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 9, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dnsServerZoneTable.setStatus("obsolete")
_DnsServerZoneEntry_Object = MibTableRow
dnsServerZoneEntry = _DnsServerZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 9, 1, 2, 2, 1)
)
dnsServerZoneEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "zoneIndex"),
)
if mibBuilder.loadTexts:
    dnsServerZoneEntry.setStatus("obsolete")
_ZoneIndex_Type = Integer32
_ZoneIndex_Object = MibTableColumn
zoneIndex = _ZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 9, 1, 2, 2, 1, 1),
    _ZoneIndex_Type()
)
zoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneIndex.setStatus("obsolete")
_ZoneName_Type = OctetString
_ZoneName_Object = MibTableColumn
zoneName = _ZoneName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 9, 1, 2, 2, 1, 2),
    _ZoneName_Type()
)
zoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneName.setStatus("obsolete")
_GlobalServerLB_ObjectIdentity = ObjectIdentity
globalServerLB = _GlobalServerLB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 10)
)
_GslbStatistics_ObjectIdentity = ObjectIdentity
gslbStatistics = _GslbStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 10, 1)
)
_GslbDomainStatsTable_Object = MibTable
gslbDomainStatsTable = _GslbDomainStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 10, 1, 1)
)
if mibBuilder.loadTexts:
    gslbDomainStatsTable.setStatus("obsolete")
_GslbDomainStatsEntry_Object = MibTableRow
gslbDomainStatsEntry = _GslbDomainStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 10, 1, 1, 1)
)
gslbDomainStatsEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "gslbDomainIndex"),
)
if mibBuilder.loadTexts:
    gslbDomainStatsEntry.setStatus("obsolete")
_GslbDomainIndex_Type = Integer32
_GslbDomainIndex_Object = MibTableColumn
gslbDomainIndex = _GslbDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 10, 1, 1, 1, 1),
    _GslbDomainIndex_Type()
)
gslbDomainIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbDomainIndex.setStatus("obsolete")
_Domainname_Type = OctetString
_Domainname_Object = MibTableColumn
domainname = _Domainname_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 10, 1, 1, 1, 2),
    _Domainname_Type()
)
domainname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainname.setStatus("obsolete")
_GslbDomainQueries_Type = Counter32
_GslbDomainQueries_Object = MibTableColumn
gslbDomainQueries = _GslbDomainQueries_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 10, 1, 1, 1, 3),
    _GslbDomainQueries_Type()
)
gslbDomainQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbDomainQueries.setStatus("obsolete")
_GslbConfig_ObjectIdentity = ObjectIdentity
gslbConfig = _GslbConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 10, 2)
)
_GslbDomainConfigTable_Object = MibTable
gslbDomainConfigTable = _GslbDomainConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 10, 2, 1)
)
if mibBuilder.loadTexts:
    gslbDomainConfigTable.setStatus("obsolete")
_GslbDomainConfigEntry_Object = MibTableRow
gslbDomainConfigEntry = _GslbDomainConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 10, 2, 1, 1)
)
gslbDomainConfigEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "gslbcDomainIndex"),
)
if mibBuilder.loadTexts:
    gslbDomainConfigEntry.setStatus("obsolete")
_GslbcDomainIndex_Type = Integer32
_GslbcDomainIndex_Object = MibTableColumn
gslbcDomainIndex = _GslbcDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 10, 2, 1, 1, 1),
    _GslbcDomainIndex_Type()
)
gslbcDomainIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbcDomainIndex.setStatus("obsolete")
_GslbcDomainName_Type = OctetString
_GslbcDomainName_Object = MibTableColumn
gslbcDomainName = _GslbcDomainName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 10, 2, 1, 1, 2),
    _GslbcDomainName_Type()
)
gslbcDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbcDomainName.setStatus("obsolete")
_GslbVipName_Type = OctetString
_GslbVipName_Object = MibTableColumn
gslbVipName = _GslbVipName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 10, 2, 1, 1, 3),
    _GslbVipName_Type()
)
gslbVipName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbVipName.setStatus("obsolete")
_ReOrderInterval_Type = TimeTicks
_ReOrderInterval_Object = MibTableColumn
reOrderInterval = _ReOrderInterval_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 10, 2, 1, 1, 4),
    _ReOrderInterval_Type()
)
reOrderInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reOrderInterval.setStatus("obsolete")
_Pq_ObjectIdentity = ObjectIdentity
pq = _Pq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 11)
)
_Pqstatistics_ObjectIdentity = ObjectIdentity
pqstatistics = _Pqstatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 11, 1)
)
_PqStatsperLBVipTable_Object = MibTable
pqStatsperLBVipTable = _PqStatsperLBVipTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 11, 1, 1)
)
if mibBuilder.loadTexts:
    pqStatsperLBVipTable.setStatus("obsolete")
_PqStatsperLBVipEntry_Object = MibTableRow
pqStatsperLBVipEntry = _PqStatsperLBVipEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 11, 1, 1, 1)
)
pqStatsperLBVipEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "pqDevno"),
)
if mibBuilder.loadTexts:
    pqStatsperLBVipEntry.setStatus("obsolete")
_PqDevno_Type = Integer32
_PqDevno_Object = MibTableColumn
pqDevno = _PqDevno_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 11, 1, 1, 1, 1),
    _PqDevno_Type()
)
pqDevno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqDevno.setStatus("obsolete")
_Totclienttransactiontime_Type = Counter32
_Totclienttransactiontime_Object = MibTableColumn
totclienttransactiontime = _Totclienttransactiontime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 11, 1, 1, 1, 2),
    _Totclienttransactiontime_Type()
)
totclienttransactiontime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totclienttransactiontime.setStatus("obsolete")
_Totclienttransaction_Type = Counter32
_Totclienttransaction_Object = MibTableColumn
totclienttransaction = _Totclienttransaction_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 11, 1, 1, 1, 3),
    _Totclienttransaction_Type()
)
totclienttransaction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totclienttransaction.setStatus("obsolete")
_Dropped_Type = Counter32
_Dropped_Object = MibTableColumn
dropped = _Dropped_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 11, 1, 1, 1, 4),
    _Dropped_Type()
)
dropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dropped.setStatus("obsolete")
_Qdepth_Type = Counter32
_Qdepth_Object = MibTableColumn
qdepth = _Qdepth_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 11, 1, 1, 1, 5),
    _Qdepth_Type()
)
qdepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qdepth.setStatus("obsolete")
_PqStatsperpqpolicyandperLBVipTable_Object = MibTable
pqStatsperpqpolicyandperLBVipTable = _PqStatsperpqpolicyandperLBVipTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 11, 1, 2)
)
if mibBuilder.loadTexts:
    pqStatsperpqpolicyandperLBVipTable.setStatus("obsolete")
_PqStatsperpqpolicyandperLBVipEntry_Object = MibTableRow
pqStatsperpqpolicyandperLBVipEntry = _PqStatsperpqpolicyandperLBVipEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 11, 1, 2, 1)
)
pqStatsperpqpolicyandperLBVipEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "pqvsdevno"),
    (0, "NS-ROOT-MIB", "pqpoldevno"),
)
if mibBuilder.loadTexts:
    pqStatsperpqpolicyandperLBVipEntry.setStatus("obsolete")
_Pqvsdevno_Type = Integer32
_Pqvsdevno_Object = MibTableColumn
pqvsdevno = _Pqvsdevno_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 11, 1, 2, 1, 1),
    _Pqvsdevno_Type()
)
pqvsdevno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqvsdevno.setStatus("obsolete")
_Pqpoldevno_Type = Integer32
_Pqpoldevno_Object = MibTableColumn
pqpoldevno = _Pqpoldevno_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 11, 1, 2, 1, 2),
    _Pqpoldevno_Type()
)
pqpoldevno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqpoldevno.setStatus("obsolete")
_Pqtotclienttransactiontime_Type = Counter32
_Pqtotclienttransactiontime_Object = MibTableColumn
pqtotclienttransactiontime = _Pqtotclienttransactiontime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 11, 1, 2, 1, 3),
    _Pqtotclienttransactiontime_Type()
)
pqtotclienttransactiontime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqtotclienttransactiontime.setStatus("obsolete")
_Pqtotclienttransaction_Type = Counter32
_Pqtotclienttransaction_Object = MibTableColumn
pqtotclienttransaction = _Pqtotclienttransaction_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 11, 1, 2, 1, 4),
    _Pqtotclienttransaction_Type()
)
pqtotclienttransaction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqtotclienttransaction.setStatus("obsolete")
_PqDropped_Type = Counter32
_PqDropped_Object = MibTableColumn
pqDropped = _PqDropped_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 11, 1, 2, 1, 5),
    _PqDropped_Type()
)
pqDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqDropped.setStatus("obsolete")
_PqQdepth_Type = Counter32
_PqQdepth_Object = MibTableColumn
pqQdepth = _PqQdepth_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 11, 1, 2, 1, 6),
    _PqQdepth_Type()
)
pqQdepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqQdepth.setStatus("obsolete")
_Pqconfig_ObjectIdentity = ObjectIdentity
pqconfig = _Pqconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 11, 2)
)
_PqpolicyconfigTable_Object = MibTable
pqpolicyconfigTable = _PqpolicyconfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 11, 2, 1)
)
if mibBuilder.loadTexts:
    pqpolicyconfigTable.setStatus("obsolete")
_PqpolicyconfigEntry_Object = MibTableRow
pqpolicyconfigEntry = _PqpolicyconfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 11, 2, 1, 1)
)
pqpolicyconfigEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "pqPolDevno"),
)
if mibBuilder.loadTexts:
    pqpolicyconfigEntry.setStatus("obsolete")
_PqPolDevno_Type = Integer32
_PqPolDevno_Object = MibTableColumn
pqPolDevno = _PqPolDevno_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 11, 2, 1, 1, 1),
    _PqPolDevno_Type()
)
pqPolDevno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqPolDevno.setStatus("obsolete")
_Pqpolicyname_Type = OctetString
_Pqpolicyname_Object = MibTableColumn
pqpolicyname = _Pqpolicyname_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 11, 2, 1, 1, 2),
    _Pqpolicyname_Type()
)
pqpolicyname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqpolicyname.setStatus("obsolete")
_Rulename_Type = OctetString
_Rulename_Object = MibTableColumn
rulename = _Rulename_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 11, 2, 1, 1, 3),
    _Rulename_Type()
)
rulename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulename.setStatus("obsolete")
_QdepthThreshval_Type = Integer32
_QdepthThreshval_Object = MibTableColumn
qdepthThreshval = _QdepthThreshval_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 11, 2, 1, 1, 4),
    _QdepthThreshval_Type()
)
qdepthThreshval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qdepthThreshval.setStatus("obsolete")
_PolqdepthThreshval_Type = Integer32
_PolqdepthThreshval_Object = MibTableColumn
polqdepthThreshval = _PolqdepthThreshval_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 11, 2, 1, 1, 5),
    _PolqdepthThreshval_Type()
)
polqdepthThreshval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polqdepthThreshval.setStatus("obsolete")
_Priority_Type = Integer32
_Priority_Object = MibTableColumn
priority = _Priority_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 11, 2, 1, 1, 6),
    _Priority_Type()
)
priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    priority.setStatus("obsolete")
_PqPolWeight_Type = Integer32
_PqPolWeight_Object = MibTableColumn
pqPolWeight = _PqPolWeight_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 11, 2, 1, 1, 7),
    _PqPolWeight_Type()
)
pqPolWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqPolWeight.setStatus("obsolete")
_Dos_ObjectIdentity = ObjectIdentity
dos = _Dos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 12)
)
_Dosstatistics_ObjectIdentity = ObjectIdentity
dosstatistics = _Dosstatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 12, 1)
)
_DosservicestatsTable_Object = MibTable
dosservicestatsTable = _DosservicestatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 12, 1, 1)
)
if mibBuilder.loadTexts:
    dosservicestatsTable.setStatus("obsolete")
_DosservicestatsEntry_Object = MibTableRow
dosservicestatsEntry = _DosservicestatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 12, 1, 1, 1)
)
dosservicestatsEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "dosDevno"),
)
if mibBuilder.loadTexts:
    dosservicestatsEntry.setStatus("obsolete")
_DosDevno_Type = Integer32
_DosDevno_Object = MibTableColumn
dosDevno = _DosDevno_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 12, 1, 1, 1, 1),
    _DosDevno_Type()
)
dosDevno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosDevno.setStatus("obsolete")
_Surgecnt_Type = Counter32
_Surgecnt_Object = MibTableColumn
surgecnt = _Surgecnt_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 12, 1, 1, 1, 2),
    _Surgecnt_Type()
)
surgecnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    surgecnt.setStatus("obsolete")
_Dosqdepth_Type = Counter32
_Dosqdepth_Object = MibTableColumn
dosqdepth = _Dosqdepth_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 12, 1, 1, 1, 3),
    _Dosqdepth_Type()
)
dosqdepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosqdepth.setStatus("obsolete")
_Totaljstransaction_Type = Counter32
_Totaljstransaction_Object = MibTableColumn
totaljstransaction = _Totaljstransaction_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 12, 1, 1, 1, 4),
    _Totaljstransaction_Type()
)
totaljstransaction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totaljstransaction.setStatus("obsolete")
_Dosconfig_ObjectIdentity = ObjectIdentity
dosconfig = _Dosconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 12, 2)
)
_DospolicyconfigTable_Object = MibTable
dospolicyconfigTable = _DospolicyconfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 12, 2, 1)
)
if mibBuilder.loadTexts:
    dospolicyconfigTable.setStatus("obsolete")
_DospolicyconfigEntry_Object = MibTableRow
dospolicyconfigEntry = _DospolicyconfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 12, 2, 1, 1)
)
dospolicyconfigEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "dosPolDevno"),
)
if mibBuilder.loadTexts:
    dospolicyconfigEntry.setStatus("obsolete")
_DosPolDevno_Type = Integer32
_DosPolDevno_Object = MibTableColumn
dosPolDevno = _DosPolDevno_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 12, 2, 1, 1, 1),
    _DosPolDevno_Type()
)
dosPolDevno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosPolDevno.setStatus("obsolete")
_Dospolicyname_Type = OctetString
_Dospolicyname_Object = MibTableColumn
dospolicyname = _Dospolicyname_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 12, 2, 1, 1, 2),
    _Dospolicyname_Type()
)
dospolicyname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dospolicyname.setStatus("obsolete")
_Thresholdvalue_Type = Integer32
_Thresholdvalue_Object = MibTableColumn
thresholdvalue = _Thresholdvalue_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 12, 2, 1, 1, 3),
    _Thresholdvalue_Type()
)
thresholdvalue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdvalue.setStatus("obsolete")
_Ssloffloading_ObjectIdentity = ObjectIdentity
ssloffloading = _Ssloffloading_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13)
)
_Sslstatistics_ObjectIdentity = ObjectIdentity
sslstatistics = _Sslstatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 1)
)
_Sslglobalstats_ObjectIdentity = ObjectIdentity
sslglobalstats = _Sslglobalstats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 1, 1)
)
_CurrSPS_Type = Counter32
_CurrSPS_Object = MibScalar
currSPS = _CurrSPS_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 1, 1, 1),
    _CurrSPS_Type()
)
currSPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currSPS.setStatus("obsolete")
_SslV2TxCount_Type = Counter32
_SslV2TxCount_Object = MibScalar
sslV2TxCount = _SslV2TxCount_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 1, 1, 2),
    _SslV2TxCount_Type()
)
sslV2TxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslV2TxCount.setStatus("obsolete")
_SslV3TxCount_Type = Counter32
_SslV3TxCount_Object = MibScalar
sslV3TxCount = _SslV3TxCount_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 1, 1, 3),
    _SslV3TxCount_Type()
)
sslV3TxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslV3TxCount.setStatus("obsolete")
_TlsV1TxCount_Type = Counter32
_TlsV1TxCount_Object = MibScalar
tlsV1TxCount = _TlsV1TxCount_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 1, 1, 4),
    _TlsV1TxCount_Type()
)
tlsV1TxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsV1TxCount.setStatus("obsolete")
_KeyExRSA512_Type = Counter32
_KeyExRSA512_Object = MibScalar
keyExRSA512 = _KeyExRSA512_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 1, 1, 5),
    _KeyExRSA512_Type()
)
keyExRSA512.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyExRSA512.setStatus("obsolete")
_KeyExRSA1024_Type = Counter32
_KeyExRSA1024_Object = MibScalar
keyExRSA1024 = _KeyExRSA1024_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 1, 1, 6),
    _KeyExRSA1024_Type()
)
keyExRSA1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyExRSA1024.setStatus("obsolete")
_KeyExDH512_Type = Counter32
_KeyExDH512_Object = MibScalar
keyExDH512 = _KeyExDH512_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 1, 1, 7),
    _KeyExDH512_Type()
)
keyExDH512.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyExDH512.setStatus("obsolete")
_KeyExDH1024_Type = Counter32
_KeyExDH1024_Object = MibScalar
keyExDH1024 = _KeyExDH1024_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 1, 1, 8),
    _KeyExDH1024_Type()
)
keyExDH1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyExDH1024.setStatus("obsolete")
_AuthRSA_Type = Counter32
_AuthRSA_Object = MibScalar
authRSA = _AuthRSA_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 1, 1, 9),
    _AuthRSA_Type()
)
authRSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authRSA.setStatus("obsolete")
_AuthDH_Type = Counter32
_AuthDH_Object = MibScalar
authDH = _AuthDH_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 1, 1, 10),
    _AuthDH_Type()
)
authDH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authDH.setStatus("obsolete")
_AuthDS_Type = Counter32
_AuthDS_Object = MibScalar
authDS = _AuthDS_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 1, 1, 11),
    _AuthDS_Type()
)
authDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authDS.setStatus("obsolete")
_Cipher40BitRC4_Type = Counter32
_Cipher40BitRC4_Object = MibScalar
cipher40BitRC4 = _Cipher40BitRC4_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 1, 1, 12),
    _Cipher40BitRC4_Type()
)
cipher40BitRC4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipher40BitRC4.setStatus("obsolete")
_Cipher56BitRC4_Type = Counter32
_Cipher56BitRC4_Object = MibScalar
cipher56BitRC4 = _Cipher56BitRC4_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 1, 1, 13),
    _Cipher56BitRC4_Type()
)
cipher56BitRC4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipher56BitRC4.setStatus("obsolete")
_Cipher64BitRC4_Type = Counter32
_Cipher64BitRC4_Object = MibScalar
cipher64BitRC4 = _Cipher64BitRC4_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 1, 1, 14),
    _Cipher64BitRC4_Type()
)
cipher64BitRC4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipher64BitRC4.setStatus("obsolete")
_Cipher128BitRC4_Type = Counter32
_Cipher128BitRC4_Object = MibScalar
cipher128BitRC4 = _Cipher128BitRC4_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 1, 1, 15),
    _Cipher128BitRC4_Type()
)
cipher128BitRC4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipher128BitRC4.setStatus("obsolete")
_Cipher40BitDES_Type = Counter32
_Cipher40BitDES_Object = MibScalar
cipher40BitDES = _Cipher40BitDES_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 1, 1, 16),
    _Cipher40BitDES_Type()
)
cipher40BitDES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipher40BitDES.setStatus("obsolete")
_Cipher56BitDES_Type = Counter32
_Cipher56BitDES_Object = MibScalar
cipher56BitDES = _Cipher56BitDES_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 1, 1, 17),
    _Cipher56BitDES_Type()
)
cipher56BitDES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipher56BitDES.setStatus("obsolete")
_Cipher168Bit3DES_Type = Counter32
_Cipher168Bit3DES_Object = MibScalar
cipher168Bit3DES = _Cipher168Bit3DES_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 1, 1, 18),
    _Cipher168Bit3DES_Type()
)
cipher168Bit3DES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipher168Bit3DES.setStatus("obsolete")
_Cipher40BitRC2_Type = Counter32
_Cipher40BitRC2_Object = MibScalar
cipher40BitRC2 = _Cipher40BitRC2_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 1, 1, 19),
    _Cipher40BitRC2_Type()
)
cipher40BitRC2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipher40BitRC2.setStatus("obsolete")
_Cipher56BitRC2_Type = Counter32
_Cipher56BitRC2_Object = MibScalar
cipher56BitRC2 = _Cipher56BitRC2_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 1, 1, 20),
    _Cipher56BitRC2_Type()
)
cipher56BitRC2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipher56BitRC2.setStatus("obsolete")
_Cipher128BitRC2_Type = Counter32
_Cipher128BitRC2_Object = MibScalar
cipher128BitRC2 = _Cipher128BitRC2_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 1, 1, 21),
    _Cipher128BitRC2_Type()
)
cipher128BitRC2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipher128BitRC2.setStatus("obsolete")
_Cipher128BitIDEA_Type = Counter32
_Cipher128BitIDEA_Object = MibScalar
cipher128BitIDEA = _Cipher128BitIDEA_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 1, 1, 22),
    _Cipher128BitIDEA_Type()
)
cipher128BitIDEA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipher128BitIDEA.setStatus("obsolete")
_HashMD5_Type = Counter32
_HashMD5_Object = MibScalar
hashMD5 = _HashMD5_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 1, 1, 23),
    _HashMD5_Type()
)
hashMD5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hashMD5.setStatus("obsolete")
_HashSHA_Type = Counter32
_HashSHA_Object = MibScalar
hashSHA = _HashSHA_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 1, 1, 24),
    _HashSHA_Type()
)
hashSHA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hashSHA.setStatus("obsolete")
_SslConfig_ObjectIdentity = ObjectIdentity
sslConfig = _SslConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2)
)
_CertKeyTable_Object = MibTable
certKeyTable = _CertKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 1)
)
if mibBuilder.loadTexts:
    certKeyTable.setStatus("obsolete")
_CertKeyEntry_Object = MibTableRow
certKeyEntry = _CertKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 1, 1)
)
certKeyEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "certKeyId"),
)
if mibBuilder.loadTexts:
    certKeyEntry.setStatus("obsolete")
_CertKeyId_Type = Integer32
_CertKeyId_Object = MibTableColumn
certKeyId = _CertKeyId_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 1, 1, 1),
    _CertKeyId_Type()
)
certKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certKeyId.setStatus("obsolete")
_CertKeyName_Type = OctetString
_CertKeyName_Object = MibTableColumn
certKeyName = _CertKeyName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 1, 1, 2),
    _CertKeyName_Type()
)
certKeyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certKeyName.setStatus("obsolete")
_CertPath_Type = OctetString
_CertPath_Object = MibTableColumn
certPath = _CertPath_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 1, 1, 3),
    _CertPath_Type()
)
certPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certPath.setStatus("obsolete")
_KeyPath_Type = OctetString
_KeyPath_Object = MibTableColumn
keyPath = _KeyPath_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 1, 1, 4),
    _KeyPath_Type()
)
keyPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyPath.setStatus("obsolete")


class _InputFormat_Type(Integer32):
    """Custom type inputFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("der", 1),
          ("pem", 3))
    )


_InputFormat_Type.__name__ = "Integer32"
_InputFormat_Object = MibTableColumn
inputFormat = _InputFormat_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 1, 1, 5),
    _InputFormat_Type()
)
inputFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputFormat.setStatus("obsolete")
_CrlTable_Object = MibTable
crlTable = _CrlTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 2)
)
if mibBuilder.loadTexts:
    crlTable.setStatus("obsolete")
_CrlEntry_Object = MibTableRow
crlEntry = _CrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 2, 1)
)
crlEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "crlId"),
)
if mibBuilder.loadTexts:
    crlEntry.setStatus("obsolete")
_CrlId_Type = Integer32
_CrlId_Object = MibTableColumn
crlId = _CrlId_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 2, 1, 1),
    _CrlId_Type()
)
crlId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crlId.setStatus("obsolete")
_CrlName_Type = OctetString
_CrlName_Object = MibTableColumn
crlName = _CrlName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 2, 1, 2),
    _CrlName_Type()
)
crlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crlName.setStatus("obsolete")
_CrlPath_Type = OctetString
_CrlPath_Object = MibTableColumn
crlPath = _CrlPath_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 2, 1, 3),
    _CrlPath_Type()
)
crlPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crlPath.setStatus("obsolete")


class _CrlInputFormat_Type(Integer32):
    """Custom type crlInputFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("der", 1),
          ("pem", 3))
    )


_CrlInputFormat_Type.__name__ = "Integer32"
_CrlInputFormat_Object = MibTableColumn
crlInputFormat = _CrlInputFormat_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 2, 1, 4),
    _CrlInputFormat_Type()
)
crlInputFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crlInputFormat.setStatus("obsolete")
_CipherGroupTable_Object = MibTable
cipherGroupTable = _CipherGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 3)
)
if mibBuilder.loadTexts:
    cipherGroupTable.setStatus("obsolete")
_CipherGroupEntry_Object = MibTableRow
cipherGroupEntry = _CipherGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 3, 1)
)
cipherGroupEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "cipherGroupId"),
    (0, "NS-ROOT-MIB", "cipherId"),
)
if mibBuilder.loadTexts:
    cipherGroupEntry.setStatus("obsolete")
_CipherGroupId_Type = Integer32
_CipherGroupId_Object = MibTableColumn
cipherGroupId = _CipherGroupId_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 3, 1, 1),
    _CipherGroupId_Type()
)
cipherGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipherGroupId.setStatus("obsolete")
_CipherId_Type = Integer32
_CipherId_Object = MibTableColumn
cipherId = _CipherId_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 3, 1, 2),
    _CipherId_Type()
)
cipherId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipherId.setStatus("obsolete")
_CipherGroupName_Type = OctetString
_CipherGroupName_Object = MibTableColumn
cipherGroupName = _CipherGroupName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 3, 1, 3),
    _CipherGroupName_Type()
)
cipherGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipherGroupName.setStatus("obsolete")
_CipherName_Type = OctetString
_CipherName_Object = MibTableColumn
cipherName = _CipherName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 3, 1, 4),
    _CipherName_Type()
)
cipherName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipherName.setStatus("obsolete")
_CipherDesc_Type = OctetString
_CipherDesc_Object = MibTableColumn
cipherDesc = _CipherDesc_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 3, 1, 5),
    _CipherDesc_Type()
)
cipherDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipherDesc.setStatus("obsolete")
_AdvanceSSLConfigTable_Object = MibTable
advanceSSLConfigTable = _AdvanceSSLConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 4)
)
if mibBuilder.loadTexts:
    advanceSSLConfigTable.setStatus("obsolete")
_AdvanceSSLConfigEntry_Object = MibTableRow
advanceSSLConfigEntry = _AdvanceSSLConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 4, 1)
)
advanceSSLConfigEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "id"),
)
if mibBuilder.loadTexts:
    advanceSSLConfigEntry.setStatus("obsolete")
_Id_Type = Integer32
_Id_Object = MibTableColumn
id = _Id_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 4, 1, 1),
    _Id_Type()
)
id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    id.setStatus("obsolete")
_ServiceName_Type = OctetString
_ServiceName_Object = MibTableColumn
serviceName = _ServiceName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 4, 1, 2),
    _ServiceName_Type()
)
serviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceName.setStatus("obsolete")


class _Dh_Type(Integer32):
    """Custom type dh based on Integer32"""
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


_Dh_Type.__name__ = "Integer32"
_Dh_Object = MibTableColumn
dh = _Dh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 4, 1, 3),
    _Dh_Type()
)
dh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dh.setStatus("obsolete")
_DhCount_Type = Integer32
_DhCount_Object = MibTableColumn
dhCount = _DhCount_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 4, 1, 4),
    _DhCount_Type()
)
dhCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhCount.setStatus("obsolete")
_DhFile_Type = OctetString
_DhFile_Object = MibTableColumn
dhFile = _DhFile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 4, 1, 5),
    _DhFile_Type()
)
dhFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhFile.setStatus("obsolete")


class _ERSA_Type(Integer32):
    """Custom type eRSA based on Integer32"""
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


_ERSA_Type.__name__ = "Integer32"
_ERSA_Object = MibTableColumn
eRSA = _ERSA_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 4, 1, 6),
    _ERSA_Type()
)
eRSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eRSA.setStatus("obsolete")
_ERSACount_Type = Integer32
_ERSACount_Object = MibTableColumn
eRSACount = _ERSACount_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 4, 1, 7),
    _ERSACount_Type()
)
eRSACount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eRSACount.setStatus("obsolete")


class _CertHeader_Type(Integer32):
    """Custom type certHeader based on Integer32"""
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


_CertHeader_Type.__name__ = "Integer32"
_CertHeader_Object = MibTableColumn
certHeader = _CertHeader_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 4, 1, 8),
    _CertHeader_Type()
)
certHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certHeader.setStatus("obsolete")
_CertHeaderTag_Type = OctetString
_CertHeaderTag_Object = MibTableColumn
certHeaderTag = _CertHeaderTag_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 4, 1, 9),
    _CertHeaderTag_Type()
)
certHeaderTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certHeaderTag.setStatus("obsolete")


class _SessHeader_Type(Integer32):
    """Custom type sessHeader based on Integer32"""
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


_SessHeader_Type.__name__ = "Integer32"
_SessHeader_Object = MibTableColumn
sessHeader = _SessHeader_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 4, 1, 10),
    _SessHeader_Type()
)
sessHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessHeader.setStatus("obsolete")
_SessHeaderTag_Type = OctetString
_SessHeaderTag_Object = MibTableColumn
sessHeaderTag = _SessHeaderTag_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 4, 1, 11),
    _SessHeaderTag_Type()
)
sessHeaderTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessHeaderTag.setStatus("obsolete")


class _Sslv2_Type(Integer32):
    """Custom type sslv2 based on Integer32"""
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


_Sslv2_Type.__name__ = "Integer32"
_Sslv2_Object = MibTableColumn
sslv2 = _Sslv2_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 4, 1, 12),
    _Sslv2_Type()
)
sslv2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslv2.setStatus("obsolete")


class _Sslv3_Type(Integer32):
    """Custom type sslv3 based on Integer32"""
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


_Sslv3_Type.__name__ = "Integer32"
_Sslv3_Object = MibTableColumn
sslv3 = _Sslv3_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 4, 1, 13),
    _Sslv3_Type()
)
sslv3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslv3.setStatus("obsolete")


class _Tlsv1_Type(Integer32):
    """Custom type tlsv1 based on Integer32"""
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


_Tlsv1_Type.__name__ = "Integer32"
_Tlsv1_Object = MibTableColumn
tlsv1 = _Tlsv1_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 4, 1, 14),
    _Tlsv1_Type()
)
tlsv1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsv1.setStatus("obsolete")


class _OwaSupport_Type(Integer32):
    """Custom type owaSupport based on Integer32"""
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


_OwaSupport_Type.__name__ = "Integer32"
_OwaSupport_Object = MibTableColumn
owaSupport = _OwaSupport_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 4, 1, 15),
    _OwaSupport_Type()
)
owaSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owaSupport.setStatus("obsolete")


class _SslRedirect_Type(Integer32):
    """Custom type sslRedirect based on Integer32"""
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


_SslRedirect_Type.__name__ = "Integer32"
_SslRedirect_Object = MibTableColumn
sslRedirect = _SslRedirect_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 4, 1, 16),
    _SslRedirect_Type()
)
sslRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslRedirect.setStatus("obsolete")
_ClearTextPort_Type = Integer32
_ClearTextPort_Object = MibTableColumn
clearTextPort = _ClearTextPort_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 4, 1, 17),
    _ClearTextPort_Type()
)
clearTextPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clearTextPort.setStatus("obsolete")


class _ServiceType_Type(Integer32):
    """Custom type serviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("physicalservice", 1),
          ("virtualserver", 0))
    )


_ServiceType_Type.__name__ = "Integer32"
_ServiceType_Object = MibTableColumn
serviceType = _ServiceType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 4, 1, 18),
    _ServiceType_Type()
)
serviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceType.setStatus("obsolete")
_CertBindingConfigTable_Object = MibTable
certBindingConfigTable = _CertBindingConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 5)
)
if mibBuilder.loadTexts:
    certBindingConfigTable.setStatus("obsolete")
_CertBindingConfigEntry_Object = MibTableRow
certBindingConfigEntry = _CertBindingConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 5, 1)
)
certBindingConfigEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "certBindId"),
    (0, "NS-ROOT-MIB", "certKeyID"),
    (0, "NS-ROOT-MIB", "certType"),
)
if mibBuilder.loadTexts:
    certBindingConfigEntry.setStatus("obsolete")
_CertBindId_Type = Integer32
_CertBindId_Object = MibTableColumn
certBindId = _CertBindId_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 5, 1, 1),
    _CertBindId_Type()
)
certBindId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certBindId.setStatus("obsolete")
_CertKeyID_Type = Integer32
_CertKeyID_Object = MibTableColumn
certKeyID = _CertKeyID_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 5, 1, 2),
    _CertKeyID_Type()
)
certKeyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certKeyID.setStatus("obsolete")


class _CertType_Type(Integer32):
    """Custom type certType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("caCertificate", 2),
          ("serverCertificate", 1))
    )


_CertType_Type.__name__ = "Integer32"
_CertType_Object = MibTableColumn
certType = _CertType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 5, 1, 3),
    _CertType_Type()
)
certType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certType.setStatus("obsolete")
_CertBindServiceName_Type = OctetString
_CertBindServiceName_Object = MibTableColumn
certBindServiceName = _CertBindServiceName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 5, 1, 4),
    _CertBindServiceName_Type()
)
certBindServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certBindServiceName.setStatus("obsolete")
_CertBindKeyName_Type = OctetString
_CertBindKeyName_Object = MibTableColumn
certBindKeyName = _CertBindKeyName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 5, 1, 5),
    _CertBindKeyName_Type()
)
certBindKeyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certBindKeyName.setStatus("obsolete")


class _CertBindServiceType_Type(Integer32):
    """Custom type certBindServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("physicalservice", 1),
          ("virtualserver", 0))
    )


_CertBindServiceType_Type.__name__ = "Integer32"
_CertBindServiceType_Object = MibTableColumn
certBindServiceType = _CertBindServiceType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 5, 1, 6),
    _CertBindServiceType_Type()
)
certBindServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certBindServiceType.setStatus("obsolete")
_CipherBindingConfigTable_Object = MibTable
cipherBindingConfigTable = _CipherBindingConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 6)
)
if mibBuilder.loadTexts:
    cipherBindingConfigTable.setStatus("obsolete")
_CipherBindingConfigEntry_Object = MibTableRow
cipherBindingConfigEntry = _CipherBindingConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 6, 1)
)
cipherBindingConfigEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "cipherBindId"),
    (0, "NS-ROOT-MIB", "cipherID"),
)
if mibBuilder.loadTexts:
    cipherBindingConfigEntry.setStatus("obsolete")
_CipherBindId_Type = Integer32
_CipherBindId_Object = MibTableColumn
cipherBindId = _CipherBindId_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 6, 1, 1),
    _CipherBindId_Type()
)
cipherBindId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipherBindId.setStatus("obsolete")
_CipherID_Type = Integer32
_CipherID_Object = MibTableColumn
cipherID = _CipherID_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 6, 1, 2),
    _CipherID_Type()
)
cipherID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipherID.setStatus("obsolete")
_CipherBindServiceName_Type = OctetString
_CipherBindServiceName_Object = MibTableColumn
cipherBindServiceName = _CipherBindServiceName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 6, 1, 3),
    _CipherBindServiceName_Type()
)
cipherBindServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipherBindServiceName.setStatus("obsolete")
_CipherbName_Type = OctetString
_CipherbName_Object = MibTableColumn
cipherbName = _CipherbName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 6, 1, 4),
    _CipherbName_Type()
)
cipherbName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipherbName.setStatus("obsolete")
_CipherbDesc_Type = OctetString
_CipherbDesc_Object = MibTableColumn
cipherbDesc = _CipherbDesc_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 6, 1, 5),
    _CipherbDesc_Type()
)
cipherbDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipherbDesc.setStatus("obsolete")


class _CipherBindServiceType_Type(Integer32):
    """Custom type cipherBindServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("physicalservice", 1),
          ("virtualserver", 0))
    )


_CipherBindServiceType_Type.__name__ = "Integer32"
_CipherBindServiceType_Object = MibTableColumn
cipherBindServiceType = _CipherBindServiceType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 13, 2, 6, 1, 6),
    _CipherBindServiceType_Type()
)
cipherBindServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipherBindServiceType.setStatus("obsolete")
_Cpe_ObjectIdentity = ObjectIdentity
cpe = _Cpe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14)
)
_Cpestatistics_ObjectIdentity = ObjectIdentity
cpestatistics = _Cpestatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 1)
)
_CpestatspolicyTable_Object = MibTable
cpestatspolicyTable = _CpestatspolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 1, 1)
)
if mibBuilder.loadTexts:
    cpestatspolicyTable.setStatus("obsolete")
_CpestatspolicyEntry_Object = MibTableRow
cpestatspolicyEntry = _CpestatspolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 1, 1, 1)
)
cpestatspolicyEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "cpesDevno"),
)
if mibBuilder.loadTexts:
    cpestatspolicyEntry.setStatus("obsolete")
_CpesDevno_Type = Integer32
_CpesDevno_Object = MibTableColumn
cpesDevno = _CpesDevno_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 1, 1, 1, 1),
    _CpesDevno_Type()
)
cpesDevno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpesDevno.setStatus("obsolete")
_CpesPolicyname_Type = OctetString
_CpesPolicyname_Object = MibTableColumn
cpesPolicyname = _CpesPolicyname_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 1, 1, 1, 2),
    _CpesPolicyname_Type()
)
cpesPolicyname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpesPolicyname.setStatus("obsolete")
_CpesPolicyhits_Type = Counter32
_CpesPolicyhits_Object = MibTableColumn
cpesPolicyhits = _CpesPolicyhits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 1, 1, 1, 3),
    _CpesPolicyhits_Type()
)
cpesPolicyhits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpesPolicyhits.setStatus("obsolete")
_CpestatsactionTable_Object = MibTable
cpestatsactionTable = _CpestatsactionTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 1, 2)
)
if mibBuilder.loadTexts:
    cpestatsactionTable.setStatus("obsolete")
_CpestatsactionEntry_Object = MibTableRow
cpestatsactionEntry = _CpestatsactionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 1, 2, 1)
)
cpestatsactionEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "cpeaDevno"),
)
if mibBuilder.loadTexts:
    cpestatsactionEntry.setStatus("obsolete")
_CpeaDevno_Type = Integer32
_CpeaDevno_Object = MibTableColumn
cpeaDevno = _CpeaDevno_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 1, 2, 1, 1),
    _CpeaDevno_Type()
)
cpeaDevno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeaDevno.setStatus("obsolete")
_Actionname_Type = OctetString
_Actionname_Object = MibTableColumn
actionname = _Actionname_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 1, 2, 1, 2),
    _Actionname_Type()
)
actionname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actionname.setStatus("obsolete")
_Actionhits_Type = Counter32
_Actionhits_Object = MibTableColumn
actionhits = _Actionhits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 1, 2, 1, 3),
    _Actionhits_Type()
)
actionhits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actionhits.setStatus("obsolete")
_Cpeconfig_ObjectIdentity = ObjectIdentity
cpeconfig = _Cpeconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 2)
)
_CpeconfigpolicyTable_Object = MibTable
cpeconfigpolicyTable = _CpeconfigpolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 2, 1)
)
if mibBuilder.loadTexts:
    cpeconfigpolicyTable.setStatus("obsolete")
_CpeconfigpolicyEntry_Object = MibTableRow
cpeconfigpolicyEntry = _CpeconfigpolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 2, 1, 1)
)
cpeconfigpolicyEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "cpecDevno"),
)
if mibBuilder.loadTexts:
    cpeconfigpolicyEntry.setStatus("obsolete")
_CpecDevno_Type = Integer32
_CpecDevno_Object = MibTableColumn
cpecDevno = _CpecDevno_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 2, 1, 1, 1),
    _CpecDevno_Type()
)
cpecDevno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpecDevno.setStatus("obsolete")
_CpecPolicyname_Type = OctetString
_CpecPolicyname_Object = MibTableColumn
cpecPolicyname = _CpecPolicyname_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 2, 1, 1, 2),
    _CpecPolicyname_Type()
)
cpecPolicyname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpecPolicyname.setStatus("obsolete")
_Reqrule_Type = OctetString
_Reqrule_Object = MibTableColumn
reqrule = _Reqrule_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 2, 1, 1, 3),
    _Reqrule_Type()
)
reqrule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reqrule.setStatus("obsolete")
_Reqaction_Type = OctetString
_Reqaction_Object = MibTableColumn
reqaction = _Reqaction_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 2, 1, 1, 4),
    _Reqaction_Type()
)
reqaction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reqaction.setStatus("obsolete")
_CpeconfigactionTable_Object = MibTable
cpeconfigactionTable = _CpeconfigactionTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 2, 2)
)
if mibBuilder.loadTexts:
    cpeconfigactionTable.setStatus("obsolete")
_CpeconfigactionEntry_Object = MibTableRow
cpeconfigactionEntry = _CpeconfigactionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 2, 2, 1)
)
cpeconfigactionEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "cpecaDevno"),
)
if mibBuilder.loadTexts:
    cpeconfigactionEntry.setStatus("obsolete")
_CpecaDevno_Type = Integer32
_CpecaDevno_Object = MibTableColumn
cpecaDevno = _CpecaDevno_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 2, 2, 1, 1),
    _CpecaDevno_Type()
)
cpecaDevno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpecaDevno.setStatus("obsolete")
_CpecaActionname_Type = OctetString
_CpecaActionname_Object = MibTableColumn
cpecaActionname = _CpecaActionname_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 2, 2, 1, 2),
    _CpecaActionname_Type()
)
cpecaActionname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpecaActionname.setStatus("obsolete")


class _Directive_Type(Integer32):
    """Custom type directive based on Integer32"""
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
        *(("add", 5),
          ("cmp", 4),
          ("cor", 8),
          ("del", 7),
          ("drop", 2),
          ("forward", 9),
          ("httpec", 3),
          ("last", 11),
          ("mod", 6),
          ("noComparison", 10),
          ("reset", 1),
          ("unknown", 0))
    )


_Directive_Type.__name__ = "Integer32"
_Directive_Object = MibTableColumn
directive = _Directive_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 2, 2, 1, 3),
    _Directive_Type()
)
directive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    directive.setStatus("obsolete")


class _Qualifier_Type(Integer32):
    """Custom type qualifier based on Integer32"""
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
        *(("header", 2),
          ("http", 1),
          ("query", 3),
          ("unknown", 0))
    )


_Qualifier_Type.__name__ = "Integer32"
_Qualifier_Object = MibTableColumn
qualifier = _Qualifier_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 2, 2, 1, 4),
    _Qualifier_Type()
)
qualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qualifier.setStatus("obsolete")
_Value_Type = OctetString
_Value_Object = MibTableColumn
value = _Value_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 2, 2, 1, 5),
    _Value_Type()
)
value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    value.setStatus("obsolete")
_Page_Type = OctetString
_Page_Object = MibTableColumn
page = _Page_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 2, 2, 1, 6),
    _Page_Type()
)
page.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    page.setStatus("obsolete")
_Server_Type = OctetString
_Server_Object = MibTableColumn
server = _Server_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 2, 2, 1, 7),
    _Server_Type()
)
server.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    server.setStatus("obsolete")
_CpeExprConfigStatsTable_Object = MibTable
cpeExprConfigStatsTable = _CpeExprConfigStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 3)
)
if mibBuilder.loadTexts:
    cpeExprConfigStatsTable.setStatus("obsolete")
_CpeExprConfigStatsEntry_Object = MibTableRow
cpeExprConfigStatsEntry = _CpeExprConfigStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 3, 1)
)
cpeExprConfigStatsEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "cpeeIndex"),
)
if mibBuilder.loadTexts:
    cpeExprConfigStatsEntry.setStatus("obsolete")
_CpeeIndex_Type = Integer32
_CpeeIndex_Object = MibTableColumn
cpeeIndex = _CpeeIndex_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 3, 1, 1),
    _CpeeIndex_Type()
)
cpeeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeeIndex.setStatus("obsolete")
_ExprName_Type = OctetString
_ExprName_Object = MibTableColumn
exprName = _ExprName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 3, 1, 2),
    _ExprName_Type()
)
exprName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exprName.setStatus("obsolete")


class _CpeeQualifier_Type(Integer32):
    """Custom type cpeeQualifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
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
        *(("compoundExpression", 15),
          ("destinationIp", 13),
          ("destinationPort", 14),
          ("domain", 10),
          ("evaluatePredefined", 16),
          ("header", 5),
          ("method", 0),
          ("sourceIp", 11),
          ("sourcePort", 12),
          ("unknownQualifier", -1),
          ("url", 7),
          ("urlPrefix", 1),
          ("urlQuery", 6),
          ("urlSuffix", 2),
          ("urlTokens", 3),
          ("urllen", 8),
          ("urlquerylen", 9),
          ("version", 4))
    )


_CpeeQualifier_Type.__name__ = "Integer32"
_CpeeQualifier_Object = MibTableColumn
cpeeQualifier = _CpeeQualifier_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 3, 1, 3),
    _CpeeQualifier_Type()
)
cpeeQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeeQualifier.setStatus("obsolete")


class _Operator_Type(Integer32):
    """Custom type operator based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("and", 0),
          ("contains", 11),
          ("contents", 13),
          ("equal", 3),
          ("exists", 9),
          ("greaterThan", 5),
          ("greaterThanOrEqualTo", 7),
          ("lessThan", 6),
          ("lessThanOrEqualTo", 8),
          ("not", 2),
          ("notContains", 12),
          ("notEqual", 4),
          ("notExists", 10),
          ("or", 1))
    )


_Operator_Type.__name__ = "Integer32"
_Operator_Object = MibTableColumn
operator = _Operator_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 3, 1, 4),
    _Operator_Type()
)
operator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operator.setStatus("obsolete")
_HdrName_Type = OctetString
_HdrName_Object = MibTableColumn
hdrName = _HdrName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 3, 1, 5),
    _HdrName_Type()
)
hdrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdrName.setStatus("obsolete")
_CpeeValue_Type = OctetString
_CpeeValue_Object = MibTableColumn
cpeeValue = _CpeeValue_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 3, 1, 6),
    _CpeeValue_Type()
)
cpeeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeeValue.setStatus("obsolete")
_Length_Type = Integer32
_Length_Object = MibTableColumn
length = _Length_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 3, 1, 7),
    _Length_Type()
)
length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    length.setStatus("obsolete")
_Offset_Type = Integer32
_Offset_Object = MibTableColumn
offset = _Offset_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 3, 1, 8),
    _Offset_Type()
)
offset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    offset.setStatus("obsolete")
_CpeeNetmask_Type = Integer32
_CpeeNetmask_Object = MibTableColumn
cpeeNetmask = _CpeeNetmask_Object(
    (1, 3, 6, 1, 4, 1, 5951, 1, 14, 3, 1, 9),
    _CpeeNetmask_Type()
)
cpeeNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeeNetmask.setStatus("obsolete")
_NsProducts_ObjectIdentity = ObjectIdentity
nsProducts = _NsProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4)
)
_Rs9000_ObjectIdentity = ObjectIdentity
rs9000 = _Rs9000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1)
)
_NsSysGroup_ObjectIdentity = ObjectIdentity
nsSysGroup = _NsSysGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1)
)
_SysBuildVersion_Type = OctetString
_SysBuildVersion_Object = MibScalar
sysBuildVersion = _SysBuildVersion_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 1),
    _SysBuildVersion_Type()
)
sysBuildVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBuildVersion.setStatus("current")
_SysIpAddress_Type = IpAddress
_SysIpAddress_Object = MibScalar
sysIpAddress = _SysIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 2),
    _SysIpAddress_Type()
)
sysIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIpAddress.setStatus("current")
_SysNetmask_Type = IpAddress
_SysNetmask_Object = MibScalar
sysNetmask = _SysNetmask_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 3),
    _SysNetmask_Type()
)
sysNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysNetmask.setStatus("current")
_SysMappedIpAddress_Type = IpAddress
_SysMappedIpAddress_Object = MibScalar
sysMappedIpAddress = _SysMappedIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 4),
    _SysMappedIpAddress_Type()
)
sysMappedIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMappedIpAddress.setStatus("obsolete")
_SysMappedIpAddressRange_Type = Integer32
_SysMappedIpAddressRange_Object = MibScalar
sysMappedIpAddressRange = _SysMappedIpAddressRange_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 5),
    _SysMappedIpAddressRange_Type()
)
sysMappedIpAddressRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMappedIpAddressRange.setStatus("obsolete")
_SysHighAvailabilityMode_Type = HAMode
_SysHighAvailabilityMode_Object = MibScalar
sysHighAvailabilityMode = _SysHighAvailabilityMode_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 6),
    _SysHighAvailabilityMode_Type()
)
sysHighAvailabilityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHighAvailabilityMode.setStatus("current")
_SysGateway_Type = IpAddress
_SysGateway_Object = MibScalar
sysGateway = _SysGateway_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 7),
    _SysGateway_Type()
)
sysGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysGateway.setStatus("current")
_SysCurMappedIpCount_Type = Gauge32
_SysCurMappedIpCount_Object = MibScalar
sysCurMappedIpCount = _SysCurMappedIpCount_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 8),
    _SysCurMappedIpCount_Type()
)
sysCurMappedIpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCurMappedIpCount.setStatus("current")
_SysCustomID_Type = OctetString
_SysCustomID_Object = MibScalar
sysCustomID = _SysCustomID_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 9),
    _SysCustomID_Type()
)
sysCustomID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCustomID.setStatus("current")
_SysHardwareVersionId_Type = Integer32
_SysHardwareVersionId_Object = MibScalar
sysHardwareVersionId = _SysHardwareVersionId_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 10),
    _SysHardwareVersionId_Type()
)
sysHardwareVersionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHardwareVersionId.setStatus("current")
_SysHardwareVersionDesc_Type = OctetString
_SysHardwareVersionDesc_Object = MibScalar
sysHardwareVersionDesc = _SysHardwareVersionDesc_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 11),
    _SysHardwareVersionDesc_Type()
)
sysHardwareVersionDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHardwareVersionDesc.setStatus("current")
_SysTotConfigChanges_Type = Counter64
_SysTotConfigChanges_Object = MibScalar
sysTotConfigChanges = _SysTotConfigChanges_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 12),
    _SysTotConfigChanges_Type()
)
sysTotConfigChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTotConfigChanges.setStatus("current")
_SysTotSaveConfigs_Type = Counter64
_SysTotSaveConfigs_Object = MibScalar
sysTotSaveConfigs = _SysTotSaveConfigs_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 13),
    _SysTotSaveConfigs_Type()
)
sysTotSaveConfigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTotSaveConfigs.setStatus("current")
_SysHardwareSerialNumber_Type = OctetString
_SysHardwareSerialNumber_Object = MibScalar
sysHardwareSerialNumber = _SysHardwareSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 14),
    _SysHardwareSerialNumber_Type()
)
sysHardwareSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHardwareSerialNumber.setStatus("current")
_SysHardwareEncodedSerialNumber_Type = OctetString
_SysHardwareEncodedSerialNumber_Object = MibScalar
sysHardwareEncodedSerialNumber = _SysHardwareEncodedSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 15),
    _SysHardwareEncodedSerialNumber_Type()
)
sysHardwareEncodedSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHardwareEncodedSerialNumber.setStatus("current")
_NsFeatureInfo_ObjectIdentity = ObjectIdentity
nsFeatureInfo = _NsFeatureInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 20)
)
_FeatureWebLogging_Type = FeatureStatus
_FeatureWebLogging_Object = MibScalar
featureWebLogging = _FeatureWebLogging_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 20, 1),
    _FeatureWebLogging_Type()
)
featureWebLogging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureWebLogging.setStatus("current")
_FeatureSurgeProtection_Type = FeatureStatus
_FeatureSurgeProtection_Object = MibScalar
featureSurgeProtection = _FeatureSurgeProtection_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 20, 2),
    _FeatureSurgeProtection_Type()
)
featureSurgeProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureSurgeProtection.setStatus("current")
_FeatureLoadBalancing_Type = FeatureStatus
_FeatureLoadBalancing_Object = MibScalar
featureLoadBalancing = _FeatureLoadBalancing_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 20, 3),
    _FeatureLoadBalancing_Type()
)
featureLoadBalancing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureLoadBalancing.setStatus("current")
_FeatureContentSwitching_Type = FeatureStatus
_FeatureContentSwitching_Object = MibScalar
featureContentSwitching = _FeatureContentSwitching_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 20, 4),
    _FeatureContentSwitching_Type()
)
featureContentSwitching.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureContentSwitching.setStatus("current")
_FeatureCacheRedirection_Type = FeatureStatus
_FeatureCacheRedirection_Object = MibScalar
featureCacheRedirection = _FeatureCacheRedirection_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 20, 5),
    _FeatureCacheRedirection_Type()
)
featureCacheRedirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureCacheRedirection.setStatus("current")
_FeatureSureConnect_Type = FeatureStatus
_FeatureSureConnect_Object = MibScalar
featureSureConnect = _FeatureSureConnect_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 20, 6),
    _FeatureSureConnect_Type()
)
featureSureConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureSureConnect.setStatus("current")
_FeatureCompression_Type = FeatureStatus
_FeatureCompression_Object = MibScalar
featureCompression = _FeatureCompression_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 20, 7),
    _FeatureCompression_Type()
)
featureCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureCompression.setStatus("current")
_FeaturePriorityQueuing_Type = FeatureStatus
_FeaturePriorityQueuing_Object = MibScalar
featurePriorityQueuing = _FeaturePriorityQueuing_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 20, 8),
    _FeaturePriorityQueuing_Type()
)
featurePriorityQueuing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featurePriorityQueuing.setStatus("current")
_FeatureSslOffloading_Type = FeatureStatus
_FeatureSslOffloading_Object = MibScalar
featureSslOffloading = _FeatureSslOffloading_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 20, 9),
    _FeatureSslOffloading_Type()
)
featureSslOffloading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureSslOffloading.setStatus("current")
_FeatureGslb_Type = FeatureStatus
_FeatureGslb_Object = MibScalar
featureGslb = _FeatureGslb_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 20, 10),
    _FeatureGslb_Type()
)
featureGslb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureGslb.setStatus("current")
_FeatureHttpDosProtection_Type = FeatureStatus
_FeatureHttpDosProtection_Object = MibScalar
featureHttpDosProtection = _FeatureHttpDosProtection_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 20, 11),
    _FeatureHttpDosProtection_Type()
)
featureHttpDosProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureHttpDosProtection.setStatus("current")
_FeatureDynamicRouting_Type = FeatureStatus
_FeatureDynamicRouting_Object = MibScalar
featureDynamicRouting = _FeatureDynamicRouting_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 20, 12),
    _FeatureDynamicRouting_Type()
)
featureDynamicRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureDynamicRouting.setStatus("obsolete")
_FeatureContentFiltering_Type = FeatureStatus
_FeatureContentFiltering_Object = MibScalar
featureContentFiltering = _FeatureContentFiltering_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 20, 13),
    _FeatureContentFiltering_Type()
)
featureContentFiltering.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureContentFiltering.setStatus("current")
_FeatureInternalCaching_Type = FeatureStatus
_FeatureInternalCaching_Object = MibScalar
featureInternalCaching = _FeatureInternalCaching_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 20, 14),
    _FeatureInternalCaching_Type()
)
featureInternalCaching.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureInternalCaching.setStatus("current")
_FeatureSSLVPN_Type = FeatureStatus
_FeatureSSLVPN_Object = MibScalar
featureSSLVPN = _FeatureSSLVPN_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 20, 15),
    _FeatureSSLVPN_Type()
)
featureSSLVPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureSSLVPN.setStatus("current")
_FeatureOSPF_Type = FeatureStatus
_FeatureOSPF_Object = MibScalar
featureOSPF = _FeatureOSPF_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 20, 16),
    _FeatureOSPF_Type()
)
featureOSPF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureOSPF.setStatus("current")
_FeatureRIP_Type = FeatureStatus
_FeatureRIP_Object = MibScalar
featureRIP = _FeatureRIP_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 20, 17),
    _FeatureRIP_Type()
)
featureRIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureRIP.setStatus("current")
_FeatureBGP_Type = FeatureStatus
_FeatureBGP_Object = MibScalar
featureBGP = _FeatureBGP_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 20, 18),
    _FeatureBGP_Type()
)
featureBGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureBGP.setStatus("current")
_FeatureRewrite_Type = FeatureStatus
_FeatureRewrite_Object = MibScalar
featureRewrite = _FeatureRewrite_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 20, 19),
    _FeatureRewrite_Type()
)
featureRewrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureRewrite.setStatus("current")
_FeatureDeltaCompression_Type = FeatureStatus
_FeatureDeltaCompression_Object = MibScalar
featureDeltaCompression = _FeatureDeltaCompression_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 20, 20),
    _FeatureDeltaCompression_Type()
)
featureDeltaCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureDeltaCompression.setStatus("current")
_FeatureGSLBProximity_Type = FeatureStatus
_FeatureGSLBProximity_Object = MibScalar
featureGSLBProximity = _FeatureGSLBProximity_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 20, 21),
    _FeatureGSLBProximity_Type()
)
featureGSLBProximity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureGSLBProximity.setStatus("current")
_FeatureIPv6ProtocolTranslation_Type = FeatureStatus
_FeatureIPv6ProtocolTranslation_Object = MibScalar
featureIPv6ProtocolTranslation = _FeatureIPv6ProtocolTranslation_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 20, 22),
    _FeatureIPv6ProtocolTranslation_Type()
)
featureIPv6ProtocolTranslation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureIPv6ProtocolTranslation.setStatus("current")
_FeatureApplicationFirewall_Type = FeatureStatus
_FeatureApplicationFirewall_Object = MibScalar
featureApplicationFirewall = _FeatureApplicationFirewall_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 20, 23),
    _FeatureApplicationFirewall_Type()
)
featureApplicationFirewall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureApplicationFirewall.setStatus("current")
_FeatureResponder_Type = FeatureStatus
_FeatureResponder_Object = MibScalar
featureResponder = _FeatureResponder_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 20, 24),
    _FeatureResponder_Type()
)
featureResponder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureResponder.setStatus("current")
_FeatureHtmlInjection_Type = FeatureStatus
_FeatureHtmlInjection_Object = MibScalar
featureHtmlInjection = _FeatureHtmlInjection_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 20, 25),
    _FeatureHtmlInjection_Type()
)
featureHtmlInjection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureHtmlInjection.setStatus("current")
_FeatureAGEE_Type = FeatureStatus
_FeatureAGEE_Object = MibScalar
featureAGEE = _FeatureAGEE_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 20, 50),
    _FeatureAGEE_Type()
)
featureAGEE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureAGEE.setStatus("current")
_FeatureAAA_Type = FeatureStatus
_FeatureAAA_Object = MibScalar
featureAAA = _FeatureAAA_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 20, 51),
    _FeatureAAA_Type()
)
featureAAA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureAAA.setStatus("current")
_FeaturePLATFORM_Type = FeaturePlatform
_FeaturePLATFORM_Object = MibScalar
featurePLATFORM = _FeaturePLATFORM_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 20, 60),
    _FeaturePLATFORM_Type()
)
featurePLATFORM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featurePLATFORM.setStatus("current")
_NsModeInfo_ObjectIdentity = ObjectIdentity
nsModeInfo = _NsModeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 21)
)
_ModeFastRamp_Type = ModeStatus
_ModeFastRamp_Object = MibScalar
modeFastRamp = _ModeFastRamp_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 21, 1),
    _ModeFastRamp_Type()
)
modeFastRamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modeFastRamp.setStatus("current")
_L2Mode_Type = ModeStatus
_L2Mode_Object = MibScalar
l2Mode = _L2Mode_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 21, 2),
    _L2Mode_Type()
)
l2Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2Mode.setStatus("current")
_ModeUseSrcIp_Type = ModeStatus
_ModeUseSrcIp_Object = MibScalar
modeUseSrcIp = _ModeUseSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 21, 3),
    _ModeUseSrcIp_Type()
)
modeUseSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modeUseSrcIp.setStatus("current")
_ModeClientKeepAlive_Type = ModeStatus
_ModeClientKeepAlive_Object = MibScalar
modeClientKeepAlive = _ModeClientKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 21, 4),
    _ModeClientKeepAlive_Type()
)
modeClientKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modeClientKeepAlive.setStatus("current")
_ModeTcpBuffering_Type = ModeStatus
_ModeTcpBuffering_Object = MibScalar
modeTcpBuffering = _ModeTcpBuffering_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 21, 5),
    _ModeTcpBuffering_Type()
)
modeTcpBuffering.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modeTcpBuffering.setStatus("current")
_ModeMacBasedForwarding_Type = ModeStatus
_ModeMacBasedForwarding_Object = MibScalar
modeMacBasedForwarding = _ModeMacBasedForwarding_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 21, 6),
    _ModeMacBasedForwarding_Type()
)
modeMacBasedForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modeMacBasedForwarding.setStatus("current")
_ModeUseSubnetIp_Type = ModeStatus
_ModeUseSubnetIp_Object = MibScalar
modeUseSubnetIp = _ModeUseSubnetIp_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 21, 7),
    _ModeUseSubnetIp_Type()
)
modeUseSubnetIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modeUseSubnetIp.setStatus("current")
_ModeEdgeConfiguration_Type = ModeStatus
_ModeEdgeConfiguration_Object = MibScalar
modeEdgeConfiguration = _ModeEdgeConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 21, 8),
    _ModeEdgeConfiguration_Type()
)
modeEdgeConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modeEdgeConfiguration.setStatus("current")
_L3mode_Type = ModeStatus
_L3mode_Object = MibScalar
l3mode = _L3mode_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 21, 9),
    _L3mode_Type()
)
l3mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3mode.setStatus("current")
_ModePathMTUDiscovery_Type = ModeStatus
_ModePathMTUDiscovery_Object = MibScalar
modePathMTUDiscovery = _ModePathMTUDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 21, 10),
    _ModePathMTUDiscovery_Type()
)
modePathMTUDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modePathMTUDiscovery.setStatus("current")
_ModeStaticRouteAdv_Type = ModeStatus
_ModeStaticRouteAdv_Object = MibScalar
modeStaticRouteAdv = _ModeStaticRouteAdv_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 21, 11),
    _ModeStaticRouteAdv_Type()
)
modeStaticRouteAdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modeStaticRouteAdv.setStatus("current")
_ModeDirectRouteAdv_Type = ModeStatus
_ModeDirectRouteAdv_Object = MibScalar
modeDirectRouteAdv = _ModeDirectRouteAdv_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 21, 12),
    _ModeDirectRouteAdv_Type()
)
modeDirectRouteAdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modeDirectRouteAdv.setStatus("current")
_ModeIntranetRouteAdv_Type = ModeStatus
_ModeIntranetRouteAdv_Object = MibScalar
modeIntranetRouteAdv = _ModeIntranetRouteAdv_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 21, 13),
    _ModeIntranetRouteAdv_Type()
)
modeIntranetRouteAdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modeIntranetRouteAdv.setStatus("current")
_BrgBpdu_Type = ModeStatus
_BrgBpdu_Object = MibScalar
brgBpdu = _BrgBpdu_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 21, 14),
    _BrgBpdu_Type()
)
brgBpdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brgBpdu.setStatus("current")
_ModeIpv6StaticRouteAdv_Type = ModeStatus
_ModeIpv6StaticRouteAdv_Object = MibScalar
modeIpv6StaticRouteAdv = _ModeIpv6StaticRouteAdv_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 21, 15),
    _ModeIpv6StaticRouteAdv_Type()
)
modeIpv6StaticRouteAdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modeIpv6StaticRouteAdv.setStatus("current")
_ModeIpv6DirectRouteAdv_Type = ModeStatus
_ModeIpv6DirectRouteAdv_Object = MibScalar
modeIpv6DirectRouteAdv = _ModeIpv6DirectRouteAdv_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 21, 16),
    _ModeIpv6DirectRouteAdv_Type()
)
modeIpv6DirectRouteAdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modeIpv6DirectRouteAdv.setStatus("current")
_NsFiltersGroup_ObjectIdentity = ObjectIdentity
nsFiltersGroup = _NsFiltersGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22)
)
_AclStatsGroup_ObjectIdentity = ObjectIdentity
aclStatsGroup = _AclStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 1)
)
_AclTotPktsBridgedLow_Type = Counter32
_AclTotPktsBridgedLow_Object = MibScalar
aclTotPktsBridgedLow = _AclTotPktsBridgedLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 1, 1),
    _AclTotPktsBridgedLow_Type()
)
aclTotPktsBridgedLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclTotPktsBridgedLow.setStatus("obsolete")
_AclTotPktsBridgedHigh_Type = Counter32
_AclTotPktsBridgedHigh_Object = MibScalar
aclTotPktsBridgedHigh = _AclTotPktsBridgedHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 1, 2),
    _AclTotPktsBridgedHigh_Type()
)
aclTotPktsBridgedHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclTotPktsBridgedHigh.setStatus("obsolete")
_AclTotPktsDeniedLow_Type = Counter32
_AclTotPktsDeniedLow_Object = MibScalar
aclTotPktsDeniedLow = _AclTotPktsDeniedLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 1, 3),
    _AclTotPktsDeniedLow_Type()
)
aclTotPktsDeniedLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclTotPktsDeniedLow.setStatus("obsolete")
_AclTotPktsDeniedHigh_Type = Counter32
_AclTotPktsDeniedHigh_Object = MibScalar
aclTotPktsDeniedHigh = _AclTotPktsDeniedHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 1, 4),
    _AclTotPktsDeniedHigh_Type()
)
aclTotPktsDeniedHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclTotPktsDeniedHigh.setStatus("obsolete")
_AclTotPktsAllowedLow_Type = Counter32
_AclTotPktsAllowedLow_Object = MibScalar
aclTotPktsAllowedLow = _AclTotPktsAllowedLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 1, 5),
    _AclTotPktsAllowedLow_Type()
)
aclTotPktsAllowedLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclTotPktsAllowedLow.setStatus("obsolete")
_AclTotPktsAllowedHigh_Type = Counter32
_AclTotPktsAllowedHigh_Object = MibScalar
aclTotPktsAllowedHigh = _AclTotPktsAllowedHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 1, 6),
    _AclTotPktsAllowedHigh_Type()
)
aclTotPktsAllowedHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclTotPktsAllowedHigh.setStatus("obsolete")
_AclTotPktsReusedLow_Type = Counter32
_AclTotPktsReusedLow_Object = MibScalar
aclTotPktsReusedLow = _AclTotPktsReusedLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 1, 7),
    _AclTotPktsReusedLow_Type()
)
aclTotPktsReusedLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclTotPktsReusedLow.setStatus("obsolete")
_AclTotPktsReusedHigh_Type = Counter32
_AclTotPktsReusedHigh_Object = MibScalar
aclTotPktsReusedHigh = _AclTotPktsReusedHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 1, 8),
    _AclTotPktsReusedHigh_Type()
)
aclTotPktsReusedHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclTotPktsReusedHigh.setStatus("obsolete")
_AclTotPktsBridged_Type = Counter64
_AclTotPktsBridged_Object = MibScalar
aclTotPktsBridged = _AclTotPktsBridged_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 1, 9),
    _AclTotPktsBridged_Type()
)
aclTotPktsBridged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclTotPktsBridged.setStatus("current")
_AclTotPktsDenied_Type = Counter64
_AclTotPktsDenied_Object = MibScalar
aclTotPktsDenied = _AclTotPktsDenied_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 1, 10),
    _AclTotPktsDenied_Type()
)
aclTotPktsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclTotPktsDenied.setStatus("current")
_AclTotPktsAllowed_Type = Counter64
_AclTotPktsAllowed_Object = MibScalar
aclTotPktsAllowed = _AclTotPktsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 1, 11),
    _AclTotPktsAllowed_Type()
)
aclTotPktsAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclTotPktsAllowed.setStatus("current")
_AclTotHits_Type = Counter64
_AclTotHits_Object = MibScalar
aclTotHits = _AclTotHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 1, 12),
    _AclTotHits_Type()
)
aclTotHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclTotHits.setStatus("current")
_AclTotMisses_Type = Counter64
_AclTotMisses_Object = MibScalar
aclTotMisses = _AclTotMisses_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 1, 13),
    _AclTotMisses_Type()
)
aclTotMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclTotMisses.setStatus("current")
_AclTotPktsNAT_Type = Counter64
_AclTotPktsNAT_Object = MibScalar
aclTotPktsNAT = _AclTotPktsNAT_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 1, 14),
    _AclTotPktsNAT_Type()
)
aclTotPktsNAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclTotPktsNAT.setStatus("current")
_NsAclTable_Object = MibTable
nsAclTable = _NsAclTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 1, 20)
)
if mibBuilder.loadTexts:
    nsAclTable.setStatus("current")
_NsAclEntry_Object = MibTableRow
nsAclEntry = _NsAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 1, 20, 1)
)
nsAclEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "aclName"),
)
if mibBuilder.loadTexts:
    nsAclEntry.setStatus("current")
_AclName_Type = OctetString
_AclName_Object = MibTableColumn
aclName = _AclName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 1, 20, 1, 1),
    _AclName_Type()
)
aclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclName.setStatus("current")
_AclPriority_Type = Integer32
_AclPriority_Object = MibTableColumn
aclPriority = _AclPriority_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 1, 20, 1, 2),
    _AclPriority_Type()
)
aclPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclPriority.setStatus("current")
_AclHits_Type = Counter64
_AclHits_Object = MibTableColumn
aclHits = _AclHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 1, 20, 1, 3),
    _AclHits_Type()
)
aclHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclHits.setStatus("obsolete")
_AclperHits_Type = Counter64
_AclperHits_Object = MibTableColumn
aclperHits = _AclperHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 1, 20, 1, 4),
    _AclperHits_Type()
)
aclperHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclperHits.setStatus("current")
_AclFullName_Type = OctetString
_AclFullName_Object = MibTableColumn
aclFullName = _AclFullName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 1, 20, 1, 5),
    _AclFullName_Type()
)
aclFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclFullName.setStatus("current")
_ContentFiltersTable_Object = MibTable
contentFiltersTable = _ContentFiltersTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 2)
)
if mibBuilder.loadTexts:
    contentFiltersTable.setStatus("obsolete")
_ContentFiltersEntry_Object = MibTableRow
contentFiltersEntry = _ContentFiltersEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 2, 1)
)
contentFiltersEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "contentFilterName"),
)
if mibBuilder.loadTexts:
    contentFiltersEntry.setStatus("obsolete")
_ContentFilterName_Type = OctetString
_ContentFilterName_Object = MibTableColumn
contentFilterName = _ContentFilterName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 2, 1, 1),
    _ContentFilterName_Type()
)
contentFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contentFilterName.setStatus("obsolete")
_ContentFilterHitsLow_Type = Counter32
_ContentFilterHitsLow_Object = MibTableColumn
contentFilterHitsLow = _ContentFilterHitsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 2, 1, 2),
    _ContentFilterHitsLow_Type()
)
contentFilterHitsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contentFilterHitsLow.setStatus("obsolete")
_ContentFilterHitsHigh_Type = Counter32
_ContentFilterHitsHigh_Object = MibTableColumn
contentFilterHitsHigh = _ContentFilterHitsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 2, 1, 3),
    _ContentFilterHitsHigh_Type()
)
contentFilterHitsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contentFilterHitsHigh.setStatus("obsolete")
_ContentFilterHits_Type = Counter64
_ContentFilterHits_Object = MibTableColumn
contentFilterHits = _ContentFilterHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 2, 1, 4),
    _ContentFilterHits_Type()
)
contentFilterHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contentFilterHits.setStatus("obsolete")
_SaclStatsGroup_ObjectIdentity = ObjectIdentity
saclStatsGroup = _SaclStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 3)
)
_SaclTotPktsBridged_Type = Counter64
_SaclTotPktsBridged_Object = MibScalar
saclTotPktsBridged = _SaclTotPktsBridged_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 3, 1),
    _SaclTotPktsBridged_Type()
)
saclTotPktsBridged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saclTotPktsBridged.setStatus("current")
_SaclTotPktsDenied_Type = Counter64
_SaclTotPktsDenied_Object = MibScalar
saclTotPktsDenied = _SaclTotPktsDenied_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 3, 2),
    _SaclTotPktsDenied_Type()
)
saclTotPktsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saclTotPktsDenied.setStatus("current")
_SaclTotPktsAllowed_Type = Counter64
_SaclTotPktsAllowed_Object = MibScalar
saclTotPktsAllowed = _SaclTotPktsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 3, 3),
    _SaclTotPktsAllowed_Type()
)
saclTotPktsAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saclTotPktsAllowed.setStatus("current")
_SaclTotHits_Type = Counter64
_SaclTotHits_Object = MibScalar
saclTotHits = _SaclTotHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 3, 4),
    _SaclTotHits_Type()
)
saclTotHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saclTotHits.setStatus("current")
_SaclTotMisses_Type = Counter64
_SaclTotMisses_Object = MibScalar
saclTotMisses = _SaclTotMisses_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 3, 5),
    _SaclTotMisses_Type()
)
saclTotMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saclTotMisses.setStatus("current")
_SaclsCount_Type = Counter64
_SaclsCount_Object = MibScalar
saclsCount = _SaclsCount_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 3, 6),
    _SaclsCount_Type()
)
saclsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saclsCount.setStatus("current")
_Acl6StatsGroup_ObjectIdentity = ObjectIdentity
acl6StatsGroup = _Acl6StatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 4)
)
_NsAcl6Table_Object = MibTable
nsAcl6Table = _NsAcl6Table_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 4, 20)
)
if mibBuilder.loadTexts:
    nsAcl6Table.setStatus("current")
_NsAcl6Entry_Object = MibTableRow
nsAcl6Entry = _NsAcl6Entry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 4, 20, 1)
)
nsAcl6Entry.setIndexNames(
    (0, "NS-ROOT-MIB", "acAclName"),
)
if mibBuilder.loadTexts:
    nsAcl6Entry.setStatus("current")
_AcAclName_Type = OctetString
_AcAclName_Object = MibTableColumn
acAclName = _AcAclName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 4, 20, 1, 1),
    _AcAclName_Type()
)
acAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAclName.setStatus("current")
_Acl6Priority_Type = Integer32
_Acl6Priority_Object = MibTableColumn
acl6Priority = _Acl6Priority_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 4, 20, 1, 2),
    _Acl6Priority_Type()
)
acl6Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acl6Priority.setStatus("current")
_Acl6perHits_Type = Counter64
_Acl6perHits_Object = MibTableColumn
acl6perHits = _Acl6perHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 4, 20, 1, 3),
    _Acl6perHits_Type()
)
acl6perHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acl6perHits.setStatus("current")
_Acl6FullName_Type = OctetString
_Acl6FullName_Object = MibTableColumn
acl6FullName = _Acl6FullName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 4, 20, 1, 4),
    _Acl6FullName_Type()
)
acl6FullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acl6FullName.setStatus("current")
_Acl6TotPktsBridged_Type = Counter64
_Acl6TotPktsBridged_Object = MibScalar
acl6TotPktsBridged = _Acl6TotPktsBridged_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 4, 21),
    _Acl6TotPktsBridged_Type()
)
acl6TotPktsBridged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acl6TotPktsBridged.setStatus("current")
_Acl6TotPktsDenied_Type = Counter64
_Acl6TotPktsDenied_Object = MibScalar
acl6TotPktsDenied = _Acl6TotPktsDenied_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 4, 22),
    _Acl6TotPktsDenied_Type()
)
acl6TotPktsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acl6TotPktsDenied.setStatus("current")
_Acl6TotPktsAllowed_Type = Counter64
_Acl6TotPktsAllowed_Object = MibScalar
acl6TotPktsAllowed = _Acl6TotPktsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 4, 23),
    _Acl6TotPktsAllowed_Type()
)
acl6TotPktsAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acl6TotPktsAllowed.setStatus("current")
_Acl6TotPktsNAT_Type = Counter64
_Acl6TotPktsNAT_Object = MibScalar
acl6TotPktsNAT = _Acl6TotPktsNAT_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 4, 24),
    _Acl6TotPktsNAT_Type()
)
acl6TotPktsNAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acl6TotPktsNAT.setStatus("current")
_Acl6TotHits_Type = Counter64
_Acl6TotHits_Object = MibScalar
acl6TotHits = _Acl6TotHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 4, 25),
    _Acl6TotHits_Type()
)
acl6TotHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acl6TotHits.setStatus("current")
_Acl6TotMisses_Type = Counter64
_Acl6TotMisses_Object = MibScalar
acl6TotMisses = _Acl6TotMisses_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 4, 26),
    _Acl6TotMisses_Type()
)
acl6TotMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acl6TotMisses.setStatus("current")
_PbrStatsGroup_ObjectIdentity = ObjectIdentity
pbrStatsGroup = _PbrStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 5)
)
_NsPbrTable_Object = MibTable
nsPbrTable = _NsPbrTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 5, 20)
)
if mibBuilder.loadTexts:
    nsPbrTable.setStatus("current")
_NsPbrEntry_Object = MibTableRow
nsPbrEntry = _NsPbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 5, 20, 1)
)
nsPbrEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "pbrName"),
)
if mibBuilder.loadTexts:
    nsPbrEntry.setStatus("current")
_PbrName_Type = OctetString
_PbrName_Object = MibTableColumn
pbrName = _PbrName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 5, 20, 1, 1),
    _PbrName_Type()
)
pbrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbrName.setStatus("current")
_PbrFullName_Type = OctetString
_PbrFullName_Object = MibTableColumn
pbrFullName = _PbrFullName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 5, 20, 1, 2),
    _PbrFullName_Type()
)
pbrFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbrFullName.setStatus("current")
_PbrPriority_Type = Integer32
_PbrPriority_Object = MibTableColumn
pbrPriority = _PbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 5, 20, 1, 3),
    _PbrPriority_Type()
)
pbrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbrPriority.setStatus("current")
_PbrperHits_Type = Counter64
_PbrperHits_Object = MibTableColumn
pbrperHits = _PbrperHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 5, 20, 1, 4),
    _PbrperHits_Type()
)
pbrperHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbrperHits.setStatus("current")
_PbrTotPktsAllowed_Type = Counter64
_PbrTotPktsAllowed_Object = MibScalar
pbrTotPktsAllowed = _PbrTotPktsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 5, 21),
    _PbrTotPktsAllowed_Type()
)
pbrTotPktsAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbrTotPktsAllowed.setStatus("current")
_PbrTotPktsDenied_Type = Counter64
_PbrTotPktsDenied_Object = MibScalar
pbrTotPktsDenied = _PbrTotPktsDenied_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 5, 22),
    _PbrTotPktsDenied_Type()
)
pbrTotPktsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbrTotPktsDenied.setStatus("current")
_PbrTotHits_Type = Counter64
_PbrTotHits_Object = MibScalar
pbrTotHits = _PbrTotHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 5, 23),
    _PbrTotHits_Type()
)
pbrTotHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbrTotHits.setStatus("current")
_PbrTotMisses_Type = Counter64
_PbrTotMisses_Object = MibScalar
pbrTotMisses = _PbrTotMisses_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 22, 5, 24),
    _PbrTotMisses_Type()
)
pbrTotMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbrTotMisses.setStatus("current")
_NsHighAvailabilityGroup_ObjectIdentity = ObjectIdentity
nsHighAvailabilityGroup = _NsHighAvailabilityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 23)
)
_HaPeerId_Type = Integer32
_HaPeerId_Object = MibScalar
haPeerId = _HaPeerId_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 23, 1),
    _HaPeerId_Type()
)
haPeerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haPeerId.setStatus("current")
_HaPeerIpAddress_Type = IpAddress
_HaPeerIpAddress_Object = MibScalar
haPeerIpAddress = _HaPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 23, 2),
    _HaPeerIpAddress_Type()
)
haPeerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haPeerIpAddress.setStatus("current")
_HaPeerState_Type = HAMode
_HaPeerState_Object = MibScalar
haPeerState = _HaPeerState_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 23, 3),
    _HaPeerState_Type()
)
haPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haPeerState.setStatus("current")
_HaTotStateTransitions_Type = Counter64
_HaTotStateTransitions_Object = MibScalar
haTotStateTransitions = _HaTotStateTransitions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 23, 4),
    _HaTotStateTransitions_Type()
)
haTotStateTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haTotStateTransitions.setStatus("current")
_HaTimeofLastStateTransition_Type = TimeTicks
_HaTimeofLastStateTransition_Object = MibScalar
haTimeofLastStateTransition = _HaTimeofLastStateTransition_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 23, 5),
    _HaTimeofLastStateTransition_Type()
)
haTimeofLastStateTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haTimeofLastStateTransition.setStatus("current")
_HaTotStateFail_Type = Counter64
_HaTotStateFail_Object = MibScalar
haTotStateFail = _HaTotStateFail_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 23, 6),
    _HaTotStateFail_Type()
)
haTotStateFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haTotStateFail.setStatus("current")
_HaErrSyncFailure_Type = Counter64
_HaErrSyncFailure_Object = MibScalar
haErrSyncFailure = _HaErrSyncFailure_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 23, 7),
    _HaErrSyncFailure_Type()
)
haErrSyncFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haErrSyncFailure.setStatus("current")
_HaErrTotNodeDown_Type = Counter64
_HaErrTotNodeDown_Object = MibScalar
haErrTotNodeDown = _HaErrTotNodeDown_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 23, 8),
    _HaErrTotNodeDown_Type()
)
haErrTotNodeDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haErrTotNodeDown.setStatus("current")
_HaErrPropMemFail_Type = Counter64
_HaErrPropMemFail_Object = MibScalar
haErrPropMemFail = _HaErrPropMemFail_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 23, 9),
    _HaErrPropMemFail_Type()
)
haErrPropMemFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haErrPropMemFail.setStatus("current")
_HaErrNsbMemFail_Type = Counter64
_HaErrNsbMemFail_Object = MibScalar
haErrNsbMemFail = _HaErrNsbMemFail_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 23, 10),
    _HaErrNsbMemFail_Type()
)
haErrNsbMemFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haErrNsbMemFail.setStatus("current")
_HaErrPortSilent_Type = Counter64
_HaErrPortSilent_Object = MibScalar
haErrPortSilent = _HaErrPortSilent_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 23, 11),
    _HaErrPortSilent_Type()
)
haErrPortSilent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haErrPortSilent.setStatus("current")
_HaTotTimerRecoveries_Type = Counter64
_HaTotTimerRecoveries_Object = MibScalar
haTotTimerRecoveries = _HaTotTimerRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 23, 12),
    _HaTotTimerRecoveries_Type()
)
haTotTimerRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haTotTimerRecoveries.setStatus("current")
_HaErrSwMonitorFail_Type = Counter64
_HaErrSwMonitorFail_Object = MibScalar
haErrSwMonitorFail = _HaErrSwMonitorFail_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 23, 13),
    _HaErrSwMonitorFail_Type()
)
haErrSwMonitorFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haErrSwMonitorFail.setStatus("current")
_HaNicsMonitorFailed_Type = OctetString
_HaNicsMonitorFailed_Object = MibScalar
haNicsMonitorFailed = _HaNicsMonitorFailed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 23, 14),
    _HaNicsMonitorFailed_Type()
)
haNicsMonitorFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haNicsMonitorFailed.setStatus("current")
_HaLastMasterStateTransitionReason_Type = OctetString
_HaLastMasterStateTransitionReason_Object = MibScalar
haLastMasterStateTransitionReason = _HaLastMasterStateTransitionReason_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 23, 15),
    _HaLastMasterStateTransitionReason_Type()
)
haLastMasterStateTransitionReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haLastMasterStateTransitionReason.setStatus("current")
_HaPeerSystemState_Type = OctetString
_HaPeerSystemState_Object = MibScalar
haPeerSystemState = _HaPeerSystemState_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 23, 16),
    _HaPeerSystemState_Type()
)
haPeerSystemState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    haPeerSystemState.setStatus("current")
_HaErrPropTimeout_Type = Counter64
_HaErrPropTimeout_Object = MibScalar
haErrPropTimeout = _HaErrPropTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 23, 17),
    _HaErrPropTimeout_Type()
)
haErrPropTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haErrPropTimeout.setStatus("current")
_HaCurDerivedInc_Type = Counter32
_HaCurDerivedInc_Object = MibScalar
haCurDerivedInc = _HaCurDerivedInc_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 23, 18),
    _HaCurDerivedInc_Type()
)
haCurDerivedInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haCurDerivedInc.setStatus("current")
_HaCurPeerInc_Type = Counter32
_HaCurPeerInc_Object = MibScalar
haCurPeerInc = _HaCurPeerInc_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 23, 19),
    _HaCurPeerInc_Type()
)
haCurPeerInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haCurPeerInc.setStatus("current")
_HaErrMasterDispute_Type = Counter64
_HaErrMasterDispute_Object = MibScalar
haErrMasterDispute = _HaErrMasterDispute_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 23, 20),
    _HaErrMasterDispute_Type()
)
haErrMasterDispute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haErrMasterDispute.setStatus("current")
_HaTotPktTx_Type = Counter64
_HaTotPktTx_Object = MibScalar
haTotPktTx = _HaTotPktTx_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 23, 21),
    _HaTotPktTx_Type()
)
haTotPktTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haTotPktTx.setStatus("current")
_HaTotPktRx_Type = Counter64
_HaTotPktRx_Object = MibScalar
haTotPktRx = _HaTotPktRx_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 23, 22),
    _HaTotPktRx_Type()
)
haTotPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haTotPktRx.setStatus("current")
_HaCurStatus_Type = HAON
_HaCurStatus_Object = MibScalar
haCurStatus = _HaCurStatus_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 23, 23),
    _HaCurStatus_Type()
)
haCurStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haCurStatus.setStatus("current")
_HaCurState_Type = HAState
_HaCurState_Object = MibScalar
haCurState = _HaCurState_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 23, 24),
    _HaCurState_Type()
)
haCurState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haCurState.setStatus("current")
_HaPeerInetAddrType_Type = InetAddressType
_HaPeerInetAddrType_Object = MibScalar
haPeerInetAddrType = _HaPeerInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 23, 25),
    _HaPeerInetAddrType_Type()
)
haPeerInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haPeerInetAddrType.setStatus("current")
_HaPeerInetAddr_Type = InetAddress
_HaPeerInetAddr_Object = MibScalar
haPeerInetAddr = _HaPeerInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 23, 26),
    _HaPeerInetAddr_Type()
)
haPeerInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haPeerInetAddr.setStatus("current")
_VlanTable_Object = MibTable
vlanTable = _VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 24)
)
if mibBuilder.loadTexts:
    vlanTable.setStatus("current")
_VlanEntry_Object = MibTableRow
vlanEntry = _VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 24, 1)
)
vlanEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "vlanId"),
)
if mibBuilder.loadTexts:
    vlanEntry.setStatus("current")
_VlanId_Type = Integer32
_VlanId_Object = MibTableColumn
vlanId = _VlanId_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 24, 1, 1),
    _VlanId_Type()
)
vlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanId.setStatus("current")
_VlanMemberInterfaces_Type = OctetString
_VlanMemberInterfaces_Object = MibTableColumn
vlanMemberInterfaces = _VlanMemberInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 24, 1, 2),
    _VlanMemberInterfaces_Type()
)
vlanMemberInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanMemberInterfaces.setStatus("current")
_VlanTaggedInterfaces_Type = OctetString
_VlanTaggedInterfaces_Object = MibTableColumn
vlanTaggedInterfaces = _VlanTaggedInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 24, 1, 3),
    _VlanTaggedInterfaces_Type()
)
vlanTaggedInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTaggedInterfaces.setStatus("current")
_VlanTotRxPktsLow_Type = Counter32
_VlanTotRxPktsLow_Object = MibTableColumn
vlanTotRxPktsLow = _VlanTotRxPktsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 24, 1, 4),
    _VlanTotRxPktsLow_Type()
)
vlanTotRxPktsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTotRxPktsLow.setStatus("obsolete")
_VlanTotRxPktsHigh_Type = Counter32
_VlanTotRxPktsHigh_Object = MibTableColumn
vlanTotRxPktsHigh = _VlanTotRxPktsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 24, 1, 5),
    _VlanTotRxPktsHigh_Type()
)
vlanTotRxPktsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTotRxPktsHigh.setStatus("obsolete")
_VlanTotRxBytesLow_Type = Counter32
_VlanTotRxBytesLow_Object = MibTableColumn
vlanTotRxBytesLow = _VlanTotRxBytesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 24, 1, 6),
    _VlanTotRxBytesLow_Type()
)
vlanTotRxBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTotRxBytesLow.setStatus("obsolete")
_VlanTotRxBytesHigh_Type = Counter32
_VlanTotRxBytesHigh_Object = MibTableColumn
vlanTotRxBytesHigh = _VlanTotRxBytesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 24, 1, 7),
    _VlanTotRxBytesHigh_Type()
)
vlanTotRxBytesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTotRxBytesHigh.setStatus("obsolete")
_VlanTotTxPktsLow_Type = Counter32
_VlanTotTxPktsLow_Object = MibTableColumn
vlanTotTxPktsLow = _VlanTotTxPktsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 24, 1, 8),
    _VlanTotTxPktsLow_Type()
)
vlanTotTxPktsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTotTxPktsLow.setStatus("obsolete")
_VlanTotTxPktsHigh_Type = Counter32
_VlanTotTxPktsHigh_Object = MibTableColumn
vlanTotTxPktsHigh = _VlanTotTxPktsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 24, 1, 9),
    _VlanTotTxPktsHigh_Type()
)
vlanTotTxPktsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTotTxPktsHigh.setStatus("obsolete")
_VlanTotTxBytesLow_Type = Counter32
_VlanTotTxBytesLow_Object = MibTableColumn
vlanTotTxBytesLow = _VlanTotTxBytesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 24, 1, 10),
    _VlanTotTxBytesLow_Type()
)
vlanTotTxBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTotTxBytesLow.setStatus("obsolete")
_VlanTotTxBytesHigh_Type = Counter32
_VlanTotTxBytesHigh_Object = MibTableColumn
vlanTotTxBytesHigh = _VlanTotTxBytesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 24, 1, 11),
    _VlanTotTxBytesHigh_Type()
)
vlanTotTxBytesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTotTxBytesHigh.setStatus("obsolete")
_VlanTotDroppedPktsLow_Type = Counter32
_VlanTotDroppedPktsLow_Object = MibTableColumn
vlanTotDroppedPktsLow = _VlanTotDroppedPktsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 24, 1, 12),
    _VlanTotDroppedPktsLow_Type()
)
vlanTotDroppedPktsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTotDroppedPktsLow.setStatus("obsolete")
_VlanTotDroppedPktsHigh_Type = Counter32
_VlanTotDroppedPktsHigh_Object = MibTableColumn
vlanTotDroppedPktsHigh = _VlanTotDroppedPktsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 24, 1, 13),
    _VlanTotDroppedPktsHigh_Type()
)
vlanTotDroppedPktsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTotDroppedPktsHigh.setStatus("obsolete")
_VlanTotBroadcastPktsLow_Type = Counter32
_VlanTotBroadcastPktsLow_Object = MibTableColumn
vlanTotBroadcastPktsLow = _VlanTotBroadcastPktsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 24, 1, 14),
    _VlanTotBroadcastPktsLow_Type()
)
vlanTotBroadcastPktsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTotBroadcastPktsLow.setStatus("obsolete")
_VlanTotBroadcastPktsHigh_Type = Counter32
_VlanTotBroadcastPktsHigh_Object = MibTableColumn
vlanTotBroadcastPktsHigh = _VlanTotBroadcastPktsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 24, 1, 15),
    _VlanTotBroadcastPktsHigh_Type()
)
vlanTotBroadcastPktsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTotBroadcastPktsHigh.setStatus("obsolete")
_VlanTotRxPkts_Type = Counter64
_VlanTotRxPkts_Object = MibTableColumn
vlanTotRxPkts = _VlanTotRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 24, 1, 16),
    _VlanTotRxPkts_Type()
)
vlanTotRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTotRxPkts.setStatus("current")
_VlanTotRxBytes_Type = Counter64
_VlanTotRxBytes_Object = MibTableColumn
vlanTotRxBytes = _VlanTotRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 24, 1, 17),
    _VlanTotRxBytes_Type()
)
vlanTotRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTotRxBytes.setStatus("current")
_VlanTotTxPkts_Type = Counter64
_VlanTotTxPkts_Object = MibTableColumn
vlanTotTxPkts = _VlanTotTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 24, 1, 18),
    _VlanTotTxPkts_Type()
)
vlanTotTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTotTxPkts.setStatus("current")
_VlanTotTxBytes_Type = Counter64
_VlanTotTxBytes_Object = MibTableColumn
vlanTotTxBytes = _VlanTotTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 24, 1, 19),
    _VlanTotTxBytes_Type()
)
vlanTotTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTotTxBytes.setStatus("current")
_VlanTotDroppedPkts_Type = Counter64
_VlanTotDroppedPkts_Object = MibTableColumn
vlanTotDroppedPkts = _VlanTotDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 24, 1, 20),
    _VlanTotDroppedPkts_Type()
)
vlanTotDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTotDroppedPkts.setStatus("current")
_VlanTotBroadcastPkts_Type = Counter64
_VlanTotBroadcastPkts_Object = MibTableColumn
vlanTotBroadcastPkts = _VlanTotBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 24, 1, 21),
    _VlanTotBroadcastPkts_Type()
)
vlanTotBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTotBroadcastPkts.setStatus("current")
_VlanBindIpAddress_Type = IpAddress
_VlanBindIpAddress_Object = MibTableColumn
vlanBindIpAddress = _VlanBindIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 24, 1, 22),
    _VlanBindIpAddress_Type()
)
vlanBindIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanBindIpAddress.setStatus("obsolete")
_VlanBindIpNetmask_Type = IpAddress
_VlanBindIpNetmask_Object = MibTableColumn
vlanBindIpNetmask = _VlanBindIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 24, 1, 23),
    _VlanBindIpNetmask_Type()
)
vlanBindIpNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanBindIpNetmask.setStatus("obsolete")
_VlanBridgeGroup_Type = Integer32
_VlanBridgeGroup_Object = MibTableColumn
vlanBridgeGroup = _VlanBridgeGroup_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 24, 1, 24),
    _VlanBridgeGroup_Type()
)
vlanBridgeGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanBridgeGroup.setStatus("current")
_NsIpAddrTable_Object = MibTable
nsIpAddrTable = _NsIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 26)
)
if mibBuilder.loadTexts:
    nsIpAddrTable.setStatus("current")
_NsIpAddrEntry_Object = MibTableRow
nsIpAddrEntry = _NsIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 26, 1)
)
nsIpAddrEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "ipAddr"),
)
if mibBuilder.loadTexts:
    nsIpAddrEntry.setStatus("current")
_IpAddr_Type = IpAddress
_IpAddr_Object = MibTableColumn
ipAddr = _IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 26, 1, 1),
    _IpAddr_Type()
)
ipAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddr.setStatus("current")
_IpNetmask_Type = IpAddress
_IpNetmask_Object = MibTableColumn
ipNetmask = _IpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 26, 1, 2),
    _IpNetmask_Type()
)
ipNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNetmask.setStatus("current")
_IpType_Type = IpAddressType
_IpType_Object = MibTableColumn
ipType = _IpType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 26, 1, 3),
    _IpType_Type()
)
ipType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipType.setStatus("current")
_IpMode_Type = IpAddressMode
_IpMode_Object = MibTableColumn
ipMode = _IpMode_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 26, 1, 4),
    _IpMode_Type()
)
ipMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMode.setStatus("current")
_IpFreePorts_Type = Gauge32
_IpFreePorts_Object = MibTableColumn
ipFreePorts = _IpFreePorts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 26, 1, 5),
    _IpFreePorts_Type()
)
ipFreePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFreePorts.setStatus("current")
_IpVlan_Type = OctetString
_IpVlan_Object = MibTableColumn
ipVlan = _IpVlan_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 26, 1, 6),
    _IpVlan_Type()
)
ipVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipVlan.setStatus("current")
_IpBridgeGroup_Type = OctetString
_IpBridgeGroup_Object = MibTableColumn
ipBridgeGroup = _IpBridgeGroup_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 26, 1, 7),
    _IpBridgeGroup_Type()
)
ipBridgeGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBridgeGroup.setStatus("current")
_NsResourceGroup_ObjectIdentity = ObjectIdentity
nsResourceGroup = _NsResourceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 41)
)
_ResCpuUsage_Type = Gauge32
_ResCpuUsage_Object = MibScalar
resCpuUsage = _ResCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 41, 1),
    _ResCpuUsage_Type()
)
resCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resCpuUsage.setStatus("current")
_ResMemUsage_Type = Gauge32
_ResMemUsage_Object = MibScalar
resMemUsage = _ResMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 41, 2),
    _ResMemUsage_Type()
)
resMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resMemUsage.setStatus("current")
_NumCPUs_Type = Integer32
_NumCPUs_Object = MibScalar
numCPUs = _NumCPUs_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 41, 3),
    _NumCPUs_Type()
)
numCPUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numCPUs.setStatus("current")
_MemSizeMB_Type = Integer32
_MemSizeMB_Object = MibScalar
memSizeMB = _MemSizeMB_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 41, 4),
    _MemSizeMB_Type()
)
memSizeMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memSizeMB.setStatus("current")
_NumSSLCards_Type = Integer32
_NumSSLCards_Object = MibScalar
numSSLCards = _NumSSLCards_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 41, 5),
    _NumSSLCards_Type()
)
numSSLCards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numSSLCards.setStatus("current")
_NsCPUTable_Object = MibTable
nsCPUTable = _NsCPUTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 41, 6)
)
if mibBuilder.loadTexts:
    nsCPUTable.setStatus("current")
_NsCPUEntry_Object = MibTableRow
nsCPUEntry = _NsCPUEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 41, 6, 1)
)
nsCPUEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "nsCPUname"),
)
if mibBuilder.loadTexts:
    nsCPUEntry.setStatus("current")
_NsCPUname_Type = OctetString
_NsCPUname_Object = MibTableColumn
nsCPUname = _NsCPUname_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 41, 6, 1, 1),
    _NsCPUname_Type()
)
nsCPUname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCPUname.setStatus("current")
_NsCPUusage_Type = Gauge32
_NsCPUusage_Object = MibTableColumn
nsCPUusage = _NsCPUusage_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 41, 6, 1, 2),
    _NsCPUusage_Type()
)
nsCPUusage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCPUusage.setStatus("current")
_NsSysHealthTable_Object = MibTable
nsSysHealthTable = _NsSysHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 41, 7)
)
if mibBuilder.loadTexts:
    nsSysHealthTable.setStatus("current")
_NsSysHealthEntry_Object = MibTableRow
nsSysHealthEntry = _NsSysHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 41, 7, 1)
)
nsSysHealthEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "sysHealthCounterName"),
)
if mibBuilder.loadTexts:
    nsSysHealthEntry.setStatus("current")
_SysHealthCounterName_Type = OctetString
_SysHealthCounterName_Object = MibTableColumn
sysHealthCounterName = _SysHealthCounterName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 41, 7, 1, 1),
    _SysHealthCounterName_Type()
)
sysHealthCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHealthCounterName.setStatus("current")
_SysHealthCounterValue_Type = Integer32
_SysHealthCounterValue_Object = MibTableColumn
sysHealthCounterValue = _SysHealthCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 41, 7, 1, 2),
    _SysHealthCounterValue_Type()
)
sysHealthCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHealthCounterValue.setStatus("current")
_NsSysHealthDiskTable_Object = MibTable
nsSysHealthDiskTable = _NsSysHealthDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 41, 8)
)
if mibBuilder.loadTexts:
    nsSysHealthDiskTable.setStatus("current")
_NsSysHealthDiskEntry_Object = MibTableRow
nsSysHealthDiskEntry = _NsSysHealthDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 41, 8, 1)
)
nsSysHealthDiskEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "sysHealthDiskName"),
)
if mibBuilder.loadTexts:
    nsSysHealthDiskEntry.setStatus("current")
_SysHealthDiskName_Type = OctetString
_SysHealthDiskName_Object = MibTableColumn
sysHealthDiskName = _SysHealthDiskName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 41, 8, 1, 1),
    _SysHealthDiskName_Type()
)
sysHealthDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHealthDiskName.setStatus("current")
_SysHealthDiskSize_Type = Gauge32
_SysHealthDiskSize_Object = MibTableColumn
sysHealthDiskSize = _SysHealthDiskSize_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 41, 8, 1, 2),
    _SysHealthDiskSize_Type()
)
sysHealthDiskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHealthDiskSize.setStatus("current")
_SysHealthDiskAvail_Type = Gauge32
_SysHealthDiskAvail_Object = MibTableColumn
sysHealthDiskAvail = _SysHealthDiskAvail_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 41, 8, 1, 3),
    _SysHealthDiskAvail_Type()
)
sysHealthDiskAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHealthDiskAvail.setStatus("current")
_SysHealthDiskUsed_Type = Gauge32
_SysHealthDiskUsed_Object = MibTableColumn
sysHealthDiskUsed = _SysHealthDiskUsed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 41, 8, 1, 4),
    _SysHealthDiskUsed_Type()
)
sysHealthDiskUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHealthDiskUsed.setStatus("current")
_SysHealthDiskPerusage_Type = Gauge32
_SysHealthDiskPerusage_Object = MibTableColumn
sysHealthDiskPerusage = _SysHealthDiskPerusage_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 41, 8, 1, 5),
    _SysHealthDiskPerusage_Type()
)
sysHealthDiskPerusage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHealthDiskPerusage.setStatus("current")
_CpuSpeedMHz_Type = Integer32
_CpuSpeedMHz_Object = MibScalar
cpuSpeedMHz = _CpuSpeedMHz_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 41, 15),
    _CpuSpeedMHz_Type()
)
cpuSpeedMHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuSpeedMHz.setStatus("current")
_NumPEs_Type = Integer32
_NumPEs_Object = MibScalar
numPEs = _NumPEs_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 41, 16),
    _NumPEs_Type()
)
numPEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numPEs.setStatus("current")
_NsIpStatsGroup_ObjectIdentity = ObjectIdentity
nsIpStatsGroup = _NsIpStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43)
)
_IpTotRxPktsLow_Type = Counter32
_IpTotRxPktsLow_Object = MibScalar
ipTotRxPktsLow = _IpTotRxPktsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 1),
    _IpTotRxPktsLow_Type()
)
ipTotRxPktsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotRxPktsLow.setStatus("obsolete")
_IpTotRxPktsHigh_Type = Counter32
_IpTotRxPktsHigh_Object = MibScalar
ipTotRxPktsHigh = _IpTotRxPktsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 2),
    _IpTotRxPktsHigh_Type()
)
ipTotRxPktsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotRxPktsHigh.setStatus("obsolete")
_IpTotRxBytesLow_Type = Counter32
_IpTotRxBytesLow_Object = MibScalar
ipTotRxBytesLow = _IpTotRxBytesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 3),
    _IpTotRxBytesLow_Type()
)
ipTotRxBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotRxBytesLow.setStatus("obsolete")
_IpTotRxBytesHigh_Type = Counter32
_IpTotRxBytesHigh_Object = MibScalar
ipTotRxBytesHigh = _IpTotRxBytesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 4),
    _IpTotRxBytesHigh_Type()
)
ipTotRxBytesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotRxBytesHigh.setStatus("obsolete")
_IpTotRxMbitsLow_Type = Counter32
_IpTotRxMbitsLow_Object = MibScalar
ipTotRxMbitsLow = _IpTotRxMbitsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 5),
    _IpTotRxMbitsLow_Type()
)
ipTotRxMbitsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotRxMbitsLow.setStatus("obsolete")
_IpTotRxMbitsHigh_Type = Counter32
_IpTotRxMbitsHigh_Object = MibScalar
ipTotRxMbitsHigh = _IpTotRxMbitsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 6),
    _IpTotRxMbitsHigh_Type()
)
ipTotRxMbitsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotRxMbitsHigh.setStatus("obsolete")
_IpTotTxPktsLow_Type = Counter32
_IpTotTxPktsLow_Object = MibScalar
ipTotTxPktsLow = _IpTotTxPktsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 7),
    _IpTotTxPktsLow_Type()
)
ipTotTxPktsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotTxPktsLow.setStatus("obsolete")
_IpTotTxPktsHigh_Type = Counter32
_IpTotTxPktsHigh_Object = MibScalar
ipTotTxPktsHigh = _IpTotTxPktsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 8),
    _IpTotTxPktsHigh_Type()
)
ipTotTxPktsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotTxPktsHigh.setStatus("obsolete")
_IpTotTxBytesLow_Type = Counter32
_IpTotTxBytesLow_Object = MibScalar
ipTotTxBytesLow = _IpTotTxBytesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 9),
    _IpTotTxBytesLow_Type()
)
ipTotTxBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotTxBytesLow.setStatus("obsolete")
_IpTotTxBytesHigh_Type = Counter32
_IpTotTxBytesHigh_Object = MibScalar
ipTotTxBytesHigh = _IpTotTxBytesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 10),
    _IpTotTxBytesHigh_Type()
)
ipTotTxBytesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotTxBytesHigh.setStatus("obsolete")
_IpTotTxMbitsLow_Type = Counter32
_IpTotTxMbitsLow_Object = MibScalar
ipTotTxMbitsLow = _IpTotTxMbitsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 11),
    _IpTotTxMbitsLow_Type()
)
ipTotTxMbitsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotTxMbitsLow.setStatus("obsolete")
_IpTotTxMbitsHigh_Type = Counter32
_IpTotTxMbitsHigh_Object = MibScalar
ipTotTxMbitsHigh = _IpTotTxMbitsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 12),
    _IpTotTxMbitsHigh_Type()
)
ipTotTxMbitsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotTxMbitsHigh.setStatus("obsolete")
_IpTotFragmentsLow_Type = Counter32
_IpTotFragmentsLow_Object = MibScalar
ipTotFragmentsLow = _IpTotFragmentsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 13),
    _IpTotFragmentsLow_Type()
)
ipTotFragmentsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotFragmentsLow.setStatus("obsolete")
_IpTotFragmentsHigh_Type = Counter32
_IpTotFragmentsHigh_Object = MibScalar
ipTotFragmentsHigh = _IpTotFragmentsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 14),
    _IpTotFragmentsHigh_Type()
)
ipTotFragmentsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotFragmentsHigh.setStatus("obsolete")
_IpTotBadlensLow_Type = Counter32
_IpTotBadlensLow_Object = MibScalar
ipTotBadlensLow = _IpTotBadlensLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 15),
    _IpTotBadlensLow_Type()
)
ipTotBadlensLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotBadlensLow.setStatus("obsolete")
_IpTotBadlensHigh_Type = Counter32
_IpTotBadlensHigh_Object = MibScalar
ipTotBadlensHigh = _IpTotBadlensHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 16),
    _IpTotBadlensHigh_Type()
)
ipTotBadlensHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotBadlensHigh.setStatus("obsolete")
_IpTotBadMacAddrsLow_Type = Counter32
_IpTotBadMacAddrsLow_Object = MibScalar
ipTotBadMacAddrsLow = _IpTotBadMacAddrsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 17),
    _IpTotBadMacAddrsLow_Type()
)
ipTotBadMacAddrsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotBadMacAddrsLow.setStatus("obsolete")
_IpTotBadMacAddrsHigh_Type = Counter32
_IpTotBadMacAddrsHigh_Object = MibScalar
ipTotBadMacAddrsHigh = _IpTotBadMacAddrsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 18),
    _IpTotBadMacAddrsHigh_Type()
)
ipTotBadMacAddrsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotBadMacAddrsHigh.setStatus("obsolete")
_IpTotMaxClientsLow_Type = Counter32
_IpTotMaxClientsLow_Object = MibScalar
ipTotMaxClientsLow = _IpTotMaxClientsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 19),
    _IpTotMaxClientsLow_Type()
)
ipTotMaxClientsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotMaxClientsLow.setStatus("obsolete")
_IpTotMaxClientsHigh_Type = Counter32
_IpTotMaxClientsHigh_Object = MibScalar
ipTotMaxClientsHigh = _IpTotMaxClientsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 20),
    _IpTotMaxClientsHigh_Type()
)
ipTotMaxClientsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotMaxClientsHigh.setStatus("obsolete")
_IpTotUnknownSvcsLow_Type = Counter32
_IpTotUnknownSvcsLow_Object = MibScalar
ipTotUnknownSvcsLow = _IpTotUnknownSvcsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 21),
    _IpTotUnknownSvcsLow_Type()
)
ipTotUnknownSvcsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotUnknownSvcsLow.setStatus("obsolete")
_IpTotUnknownSvcsHigh_Type = Counter32
_IpTotUnknownSvcsHigh_Object = MibScalar
ipTotUnknownSvcsHigh = _IpTotUnknownSvcsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 22),
    _IpTotUnknownSvcsHigh_Type()
)
ipTotUnknownSvcsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotUnknownSvcsHigh.setStatus("obsolete")
_IpTotLandattacksLow_Type = Counter32
_IpTotLandattacksLow_Object = MibScalar
ipTotLandattacksLow = _IpTotLandattacksLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 23),
    _IpTotLandattacksLow_Type()
)
ipTotLandattacksLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotLandattacksLow.setStatus("obsolete")
_IpTotLandattacksHigh_Type = Counter32
_IpTotLandattacksHigh_Object = MibScalar
ipTotLandattacksHigh = _IpTotLandattacksHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 24),
    _IpTotLandattacksHigh_Type()
)
ipTotLandattacksHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotLandattacksHigh.setStatus("obsolete")
_IpTotRxPkts_Type = Counter64
_IpTotRxPkts_Object = MibScalar
ipTotRxPkts = _IpTotRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 25),
    _IpTotRxPkts_Type()
)
ipTotRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotRxPkts.setStatus("current")
_IpTotRxBytes_Type = Counter64
_IpTotRxBytes_Object = MibScalar
ipTotRxBytes = _IpTotRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 26),
    _IpTotRxBytes_Type()
)
ipTotRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotRxBytes.setStatus("current")
_IpTotRxMbits_Type = Counter64
_IpTotRxMbits_Object = MibScalar
ipTotRxMbits = _IpTotRxMbits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 27),
    _IpTotRxMbits_Type()
)
ipTotRxMbits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotRxMbits.setStatus("current")
_IpTotTxPkts_Type = Counter64
_IpTotTxPkts_Object = MibScalar
ipTotTxPkts = _IpTotTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 28),
    _IpTotTxPkts_Type()
)
ipTotTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotTxPkts.setStatus("current")
_IpTotTxBytes_Type = Counter64
_IpTotTxBytes_Object = MibScalar
ipTotTxBytes = _IpTotTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 29),
    _IpTotTxBytes_Type()
)
ipTotTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotTxBytes.setStatus("current")
_IpTotTxMbits_Type = Counter64
_IpTotTxMbits_Object = MibScalar
ipTotTxMbits = _IpTotTxMbits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 30),
    _IpTotTxMbits_Type()
)
ipTotTxMbits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotTxMbits.setStatus("current")
_IpTotFragments_Type = Counter64
_IpTotFragments_Object = MibScalar
ipTotFragments = _IpTotFragments_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 31),
    _IpTotFragments_Type()
)
ipTotFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotFragments.setStatus("current")
_IpTotBadlens_Type = Counter64
_IpTotBadlens_Object = MibScalar
ipTotBadlens = _IpTotBadlens_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 32),
    _IpTotBadlens_Type()
)
ipTotBadlens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotBadlens.setStatus("current")
_IpTotBadMacAddrs_Type = Counter64
_IpTotBadMacAddrs_Object = MibScalar
ipTotBadMacAddrs = _IpTotBadMacAddrs_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 33),
    _IpTotBadMacAddrs_Type()
)
ipTotBadMacAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotBadMacAddrs.setStatus("current")
_IpTotMaxClients_Type = Counter64
_IpTotMaxClients_Object = MibScalar
ipTotMaxClients = _IpTotMaxClients_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 34),
    _IpTotMaxClients_Type()
)
ipTotMaxClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotMaxClients.setStatus("current")
_IpTotUnknownSvcs_Type = Counter64
_IpTotUnknownSvcs_Object = MibScalar
ipTotUnknownSvcs = _IpTotUnknownSvcs_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 35),
    _IpTotUnknownSvcs_Type()
)
ipTotUnknownSvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotUnknownSvcs.setStatus("current")
_IpTotLandattacks_Type = Counter64
_IpTotLandattacks_Object = MibScalar
ipTotLandattacks = _IpTotLandattacks_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 36),
    _IpTotLandattacks_Type()
)
ipTotLandattacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotLandattacks.setStatus("current")
_IpTotBadChecksums_Type = Counter64
_IpTotBadChecksums_Object = MibScalar
ipTotBadChecksums = _IpTotBadChecksums_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 37),
    _IpTotBadChecksums_Type()
)
ipTotBadChecksums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotBadChecksums.setStatus("current")
_IpTotReassemblyAttempt_Type = Counter64
_IpTotReassemblyAttempt_Object = MibScalar
ipTotReassemblyAttempt = _IpTotReassemblyAttempt_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 38),
    _IpTotReassemblyAttempt_Type()
)
ipTotReassemblyAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotReassemblyAttempt.setStatus("current")
_IpTotSuccReassembly_Type = Counter64
_IpTotSuccReassembly_Object = MibScalar
ipTotSuccReassembly = _IpTotSuccReassembly_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 39),
    _IpTotSuccReassembly_Type()
)
ipTotSuccReassembly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotSuccReassembly.setStatus("current")
_IpTotUnsuccReassembly_Type = Counter64
_IpTotUnsuccReassembly_Object = MibScalar
ipTotUnsuccReassembly = _IpTotUnsuccReassembly_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 40),
    _IpTotUnsuccReassembly_Type()
)
ipTotUnsuccReassembly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotUnsuccReassembly.setStatus("current")
_IpTotTooBig_Type = Counter64
_IpTotTooBig_Object = MibScalar
ipTotTooBig = _IpTotTooBig_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 41),
    _IpTotTooBig_Type()
)
ipTotTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotTooBig.setStatus("current")
_IpTotZeroFragmentLen_Type = Counter64
_IpTotZeroFragmentLen_Object = MibScalar
ipTotZeroFragmentLen = _IpTotZeroFragmentLen_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 42),
    _IpTotZeroFragmentLen_Type()
)
ipTotZeroFragmentLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotZeroFragmentLen.setStatus("current")
_IpTotDupFragments_Type = Counter64
_IpTotDupFragments_Object = MibScalar
ipTotDupFragments = _IpTotDupFragments_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 43),
    _IpTotDupFragments_Type()
)
ipTotDupFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotDupFragments.setStatus("current")
_IpTotOutOfOrderFrag_Type = Counter64
_IpTotOutOfOrderFrag_Object = MibScalar
ipTotOutOfOrderFrag = _IpTotOutOfOrderFrag_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 44),
    _IpTotOutOfOrderFrag_Type()
)
ipTotOutOfOrderFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotOutOfOrderFrag.setStatus("current")
_IpTotUnknownDstRcvd_Type = Counter64
_IpTotUnknownDstRcvd_Object = MibScalar
ipTotUnknownDstRcvd = _IpTotUnknownDstRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 45),
    _IpTotUnknownDstRcvd_Type()
)
ipTotUnknownDstRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotUnknownDstRcvd.setStatus("current")
_IpTotBadTransport_Type = Counter64
_IpTotBadTransport_Object = MibScalar
ipTotBadTransport = _IpTotBadTransport_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 46),
    _IpTotBadTransport_Type()
)
ipTotBadTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotBadTransport.setStatus("current")
_IpTotVIPDown_Type = Counter64
_IpTotVIPDown_Object = MibScalar
ipTotVIPDown = _IpTotVIPDown_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 47),
    _IpTotVIPDown_Type()
)
ipTotVIPDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotVIPDown.setStatus("current")
_IpTotFixHeaderFail_Type = Counter64
_IpTotFixHeaderFail_Object = MibScalar
ipTotFixHeaderFail = _IpTotFixHeaderFail_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 48),
    _IpTotFixHeaderFail_Type()
)
ipTotFixHeaderFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotFixHeaderFail.setStatus("current")
_IpTotAddrLookup_Type = Counter64
_IpTotAddrLookup_Object = MibScalar
ipTotAddrLookup = _IpTotAddrLookup_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 49),
    _IpTotAddrLookup_Type()
)
ipTotAddrLookup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotAddrLookup.setStatus("current")
_IpTotAddrLookupFail_Type = Counter64
_IpTotAddrLookupFail_Object = MibScalar
ipTotAddrLookupFail = _IpTotAddrLookupFail_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 50),
    _IpTotAddrLookupFail_Type()
)
ipTotAddrLookupFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotAddrLookupFail.setStatus("current")
_IpTotUDPfragmentsFwd_Type = Counter64
_IpTotUDPfragmentsFwd_Object = MibScalar
ipTotUDPfragmentsFwd = _IpTotUDPfragmentsFwd_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 51),
    _IpTotUDPfragmentsFwd_Type()
)
ipTotUDPfragmentsFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotUDPfragmentsFwd.setStatus("current")
_IpTotTCPfragmentsFwd_Type = Counter64
_IpTotTCPfragmentsFwd_Object = MibScalar
ipTotTCPfragmentsFwd = _IpTotTCPfragmentsFwd_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 52),
    _IpTotTCPfragmentsFwd_Type()
)
ipTotTCPfragmentsFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotTCPfragmentsFwd.setStatus("current")
_IpTotFragPktsGen_Type = Counter64
_IpTotFragPktsGen_Object = MibScalar
ipTotFragPktsGen = _IpTotFragPktsGen_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 53),
    _IpTotFragPktsGen_Type()
)
ipTotFragPktsGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotFragPktsGen.setStatus("current")
_IpTotInvalidHeaderSz_Type = Counter64
_IpTotInvalidHeaderSz_Object = MibScalar
ipTotInvalidHeaderSz = _IpTotInvalidHeaderSz_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 54),
    _IpTotInvalidHeaderSz_Type()
)
ipTotInvalidHeaderSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotInvalidHeaderSz.setStatus("current")
_IpTotInvalidPacketSize_Type = Counter64
_IpTotInvalidPacketSize_Object = MibScalar
ipTotInvalidPacketSize = _IpTotInvalidPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 55),
    _IpTotInvalidPacketSize_Type()
)
ipTotInvalidPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotInvalidPacketSize.setStatus("current")
_IpTotTruncatedPackets_Type = Counter64
_IpTotTruncatedPackets_Object = MibScalar
ipTotTruncatedPackets = _IpTotTruncatedPackets_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 56),
    _IpTotTruncatedPackets_Type()
)
ipTotTruncatedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotTruncatedPackets.setStatus("current")
_IpTotZeroNextHop_Type = Counter64
_IpTotZeroNextHop_Object = MibScalar
ipTotZeroNextHop = _IpTotZeroNextHop_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 57),
    _IpTotZeroNextHop_Type()
)
ipTotZeroNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotZeroNextHop.setStatus("current")
_IpTotTtlExpired_Type = Counter64
_IpTotTtlExpired_Object = MibScalar
ipTotTtlExpired = _IpTotTtlExpired_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 58),
    _IpTotTtlExpired_Type()
)
ipTotTtlExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTotTtlExpired.setStatus("current")
_NonIpTotTruncatedPackets_Type = Counter64
_NonIpTotTruncatedPackets_Object = MibScalar
nonIpTotTruncatedPackets = _NonIpTotTruncatedPackets_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 43, 59),
    _NonIpTotTruncatedPackets_Type()
)
nonIpTotTruncatedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nonIpTotTruncatedPackets.setStatus("current")
_NsIcmpStatsGroup_ObjectIdentity = ObjectIdentity
nsIcmpStatsGroup = _NsIcmpStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44)
)
_IcmpTotRxPktsLow_Type = Counter32
_IcmpTotRxPktsLow_Object = MibScalar
icmpTotRxPktsLow = _IcmpTotRxPktsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 1),
    _IcmpTotRxPktsLow_Type()
)
icmpTotRxPktsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotRxPktsLow.setStatus("obsolete")
_IcmpTotRxPktsHigh_Type = Counter32
_IcmpTotRxPktsHigh_Object = MibScalar
icmpTotRxPktsHigh = _IcmpTotRxPktsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 2),
    _IcmpTotRxPktsHigh_Type()
)
icmpTotRxPktsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotRxPktsHigh.setStatus("obsolete")
_IcmpTotRxBytesLow_Type = Counter32
_IcmpTotRxBytesLow_Object = MibScalar
icmpTotRxBytesLow = _IcmpTotRxBytesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 3),
    _IcmpTotRxBytesLow_Type()
)
icmpTotRxBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotRxBytesLow.setStatus("obsolete")
_IcmpTotRxBytesHigh_Type = Counter32
_IcmpTotRxBytesHigh_Object = MibScalar
icmpTotRxBytesHigh = _IcmpTotRxBytesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 4),
    _IcmpTotRxBytesHigh_Type()
)
icmpTotRxBytesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotRxBytesHigh.setStatus("obsolete")
_IcmpTotTxPktsLow_Type = Counter32
_IcmpTotTxPktsLow_Object = MibScalar
icmpTotTxPktsLow = _IcmpTotTxPktsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 5),
    _IcmpTotTxPktsLow_Type()
)
icmpTotTxPktsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotTxPktsLow.setStatus("obsolete")
_IcmpTotTxPktsHigh_Type = Counter32
_IcmpTotTxPktsHigh_Object = MibScalar
icmpTotTxPktsHigh = _IcmpTotTxPktsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 6),
    _IcmpTotTxPktsHigh_Type()
)
icmpTotTxPktsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotTxPktsHigh.setStatus("obsolete")
_IcmpTotTxBytesLow_Type = Counter32
_IcmpTotTxBytesLow_Object = MibScalar
icmpTotTxBytesLow = _IcmpTotTxBytesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 7),
    _IcmpTotTxBytesLow_Type()
)
icmpTotTxBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotTxBytesLow.setStatus("obsolete")
_IcmpTotTxBytesHigh_Type = Counter32
_IcmpTotTxBytesHigh_Object = MibScalar
icmpTotTxBytesHigh = _IcmpTotTxBytesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 8),
    _IcmpTotTxBytesHigh_Type()
)
icmpTotTxBytesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotTxBytesHigh.setStatus("obsolete")
_IcmpTotRxEchoReplyLow_Type = Counter32
_IcmpTotRxEchoReplyLow_Object = MibScalar
icmpTotRxEchoReplyLow = _IcmpTotRxEchoReplyLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 9),
    _IcmpTotRxEchoReplyLow_Type()
)
icmpTotRxEchoReplyLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotRxEchoReplyLow.setStatus("obsolete")
_IcmpTotRxEchoReplyHigh_Type = Counter32
_IcmpTotRxEchoReplyHigh_Object = MibScalar
icmpTotRxEchoReplyHigh = _IcmpTotRxEchoReplyHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 10),
    _IcmpTotRxEchoReplyHigh_Type()
)
icmpTotRxEchoReplyHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotRxEchoReplyHigh.setStatus("obsolete")
_IcmpTotTxEchoReplyLow_Type = Counter32
_IcmpTotTxEchoReplyLow_Object = MibScalar
icmpTotTxEchoReplyLow = _IcmpTotTxEchoReplyLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 11),
    _IcmpTotTxEchoReplyLow_Type()
)
icmpTotTxEchoReplyLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotTxEchoReplyLow.setStatus("obsolete")
_IcmpTotTxEchoReplyHigh_Type = Counter32
_IcmpTotTxEchoReplyHigh_Object = MibScalar
icmpTotTxEchoReplyHigh = _IcmpTotTxEchoReplyHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 12),
    _IcmpTotTxEchoReplyHigh_Type()
)
icmpTotTxEchoReplyHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotTxEchoReplyHigh.setStatus("obsolete")
_IcmpTotRxEchoLow_Type = Counter32
_IcmpTotRxEchoLow_Object = MibScalar
icmpTotRxEchoLow = _IcmpTotRxEchoLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 13),
    _IcmpTotRxEchoLow_Type()
)
icmpTotRxEchoLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotRxEchoLow.setStatus("obsolete")
_IcmpTotRxEchoHigh_Type = Counter32
_IcmpTotRxEchoHigh_Object = MibScalar
icmpTotRxEchoHigh = _IcmpTotRxEchoHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 14),
    _IcmpTotRxEchoHigh_Type()
)
icmpTotRxEchoHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotRxEchoHigh.setStatus("obsolete")
_IcmpTotPktsDroppedLow_Type = Counter32
_IcmpTotPktsDroppedLow_Object = MibScalar
icmpTotPktsDroppedLow = _IcmpTotPktsDroppedLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 15),
    _IcmpTotPktsDroppedLow_Type()
)
icmpTotPktsDroppedLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotPktsDroppedLow.setStatus("obsolete")
_IcmpTotPktsDroppedHigh_Type = Counter32
_IcmpTotPktsDroppedHigh_Object = MibScalar
icmpTotPktsDroppedHigh = _IcmpTotPktsDroppedHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 16),
    _IcmpTotPktsDroppedHigh_Type()
)
icmpTotPktsDroppedHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotPktsDroppedHigh.setStatus("obsolete")
_IcmpCurRateThreshold_Type = Integer32
_IcmpCurRateThreshold_Object = MibScalar
icmpCurRateThreshold = _IcmpCurRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 17),
    _IcmpCurRateThreshold_Type()
)
icmpCurRateThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpCurRateThreshold.setStatus("current")
_IcmpCurRateThresholdInterval_Type = Integer32
_IcmpCurRateThresholdInterval_Object = MibScalar
icmpCurRateThresholdInterval = _IcmpCurRateThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 18),
    _IcmpCurRateThresholdInterval_Type()
)
icmpCurRateThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpCurRateThresholdInterval.setStatus("obsolete")
_IcmpCurRateCounter_Type = Counter32
_IcmpCurRateCounter_Object = MibScalar
icmpCurRateCounter = _IcmpCurRateCounter_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 19),
    _IcmpCurRateCounter_Type()
)
icmpCurRateCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpCurRateCounter.setStatus("obsolete")
_IcmpTotThresholdExceedsLow_Type = Counter32
_IcmpTotThresholdExceedsLow_Object = MibScalar
icmpTotThresholdExceedsLow = _IcmpTotThresholdExceedsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 20),
    _IcmpTotThresholdExceedsLow_Type()
)
icmpTotThresholdExceedsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotThresholdExceedsLow.setStatus("obsolete")
_IcmpTotThresholdExceedsHigh_Type = Counter32
_IcmpTotThresholdExceedsHigh_Object = MibScalar
icmpTotThresholdExceedsHigh = _IcmpTotThresholdExceedsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 21),
    _IcmpTotThresholdExceedsHigh_Type()
)
icmpTotThresholdExceedsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotThresholdExceedsHigh.setStatus("obsolete")
_IcmpTotRxPkts_Type = Counter64
_IcmpTotRxPkts_Object = MibScalar
icmpTotRxPkts = _IcmpTotRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 22),
    _IcmpTotRxPkts_Type()
)
icmpTotRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotRxPkts.setStatus("current")
_IcmpTotRxBytes_Type = Counter64
_IcmpTotRxBytes_Object = MibScalar
icmpTotRxBytes = _IcmpTotRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 23),
    _IcmpTotRxBytes_Type()
)
icmpTotRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotRxBytes.setStatus("current")
_IcmpTotTxPkts_Type = Counter64
_IcmpTotTxPkts_Object = MibScalar
icmpTotTxPkts = _IcmpTotTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 24),
    _IcmpTotTxPkts_Type()
)
icmpTotTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotTxPkts.setStatus("current")
_IcmpTotTxBytes_Type = Counter64
_IcmpTotTxBytes_Object = MibScalar
icmpTotTxBytes = _IcmpTotTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 25),
    _IcmpTotTxBytes_Type()
)
icmpTotTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotTxBytes.setStatus("current")
_IcmpTotRxEchoReply_Type = Counter64
_IcmpTotRxEchoReply_Object = MibScalar
icmpTotRxEchoReply = _IcmpTotRxEchoReply_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 26),
    _IcmpTotRxEchoReply_Type()
)
icmpTotRxEchoReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotRxEchoReply.setStatus("current")
_IcmpTotTxEchoReply_Type = Counter64
_IcmpTotTxEchoReply_Object = MibScalar
icmpTotTxEchoReply = _IcmpTotTxEchoReply_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 27),
    _IcmpTotTxEchoReply_Type()
)
icmpTotTxEchoReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotTxEchoReply.setStatus("current")
_IcmpTotRxEcho_Type = Counter64
_IcmpTotRxEcho_Object = MibScalar
icmpTotRxEcho = _IcmpTotRxEcho_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 28),
    _IcmpTotRxEcho_Type()
)
icmpTotRxEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotRxEcho.setStatus("current")
_IcmpTotPktsDropped_Type = Counter64
_IcmpTotPktsDropped_Object = MibScalar
icmpTotPktsDropped = _IcmpTotPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 29),
    _IcmpTotPktsDropped_Type()
)
icmpTotPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotPktsDropped.setStatus("current")
_IcmpTotThresholdExceeds_Type = Counter64
_IcmpTotThresholdExceeds_Object = MibScalar
icmpTotThresholdExceeds = _IcmpTotThresholdExceeds_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 30),
    _IcmpTotThresholdExceeds_Type()
)
icmpTotThresholdExceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotThresholdExceeds.setStatus("current")
_IcmpTotPortUnreachableRx_Type = Counter64
_IcmpTotPortUnreachableRx_Object = MibScalar
icmpTotPortUnreachableRx = _IcmpTotPortUnreachableRx_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 31),
    _IcmpTotPortUnreachableRx_Type()
)
icmpTotPortUnreachableRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotPortUnreachableRx.setStatus("current")
_IcmpTotPortUnreachableTx_Type = Counter64
_IcmpTotPortUnreachableTx_Object = MibScalar
icmpTotPortUnreachableTx = _IcmpTotPortUnreachableTx_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 32),
    _IcmpTotPortUnreachableTx_Type()
)
icmpTotPortUnreachableTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotPortUnreachableTx.setStatus("current")
_IcmpTotBadChecksum_Type = Counter64
_IcmpTotBadChecksum_Object = MibScalar
icmpTotBadChecksum = _IcmpTotBadChecksum_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 33),
    _IcmpTotBadChecksum_Type()
)
icmpTotBadChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotBadChecksum.setStatus("current")
_IcmpTotNeedFragRx_Type = Counter64
_IcmpTotNeedFragRx_Object = MibScalar
icmpTotNeedFragRx = _IcmpTotNeedFragRx_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 34),
    _IcmpTotNeedFragRx_Type()
)
icmpTotNeedFragRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotNeedFragRx.setStatus("current")
_IcmpTotNonFirstIpFrag_Type = Counter64
_IcmpTotNonFirstIpFrag_Object = MibScalar
icmpTotNonFirstIpFrag = _IcmpTotNonFirstIpFrag_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 35),
    _IcmpTotNonFirstIpFrag_Type()
)
icmpTotNonFirstIpFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotNonFirstIpFrag.setStatus("current")
_IcmpTotInvalidBodyLen_Type = Counter64
_IcmpTotInvalidBodyLen_Object = MibScalar
icmpTotInvalidBodyLen = _IcmpTotInvalidBodyLen_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 36),
    _IcmpTotInvalidBodyLen_Type()
)
icmpTotInvalidBodyLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotInvalidBodyLen.setStatus("current")
_IcmpTotNoTcpConn_Type = Counter64
_IcmpTotNoTcpConn_Object = MibScalar
icmpTotNoTcpConn = _IcmpTotNoTcpConn_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 37),
    _IcmpTotNoTcpConn_Type()
)
icmpTotNoTcpConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotNoTcpConn.setStatus("current")
_IcmpTotNoUdpConn_Type = Counter64
_IcmpTotNoUdpConn_Object = MibScalar
icmpTotNoUdpConn = _IcmpTotNoUdpConn_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 38),
    _IcmpTotNoUdpConn_Type()
)
icmpTotNoUdpConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotNoUdpConn.setStatus("current")
_IcmpTotInvalidTcpSeqno_Type = Counter64
_IcmpTotInvalidTcpSeqno_Object = MibScalar
icmpTotInvalidTcpSeqno = _IcmpTotInvalidTcpSeqno_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 39),
    _IcmpTotInvalidTcpSeqno_Type()
)
icmpTotInvalidTcpSeqno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotInvalidTcpSeqno.setStatus("current")
_IcmpTotInvalidNextMTUval_Type = Counter64
_IcmpTotInvalidNextMTUval_Object = MibScalar
icmpTotInvalidNextMTUval = _IcmpTotInvalidNextMTUval_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 40),
    _IcmpTotInvalidNextMTUval_Type()
)
icmpTotInvalidNextMTUval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotInvalidNextMTUval.setStatus("current")
_IcmpTotDstIpLookup_Type = Counter64
_IcmpTotDstIpLookup_Object = MibScalar
icmpTotDstIpLookup = _IcmpTotDstIpLookup_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 41),
    _IcmpTotDstIpLookup_Type()
)
icmpTotDstIpLookup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotDstIpLookup.setStatus("current")
_IcmpTotBigNextMTU_Type = Counter64
_IcmpTotBigNextMTU_Object = MibScalar
icmpTotBigNextMTU = _IcmpTotBigNextMTU_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 42),
    _IcmpTotBigNextMTU_Type()
)
icmpTotBigNextMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotBigNextMTU.setStatus("current")
_IcmpTotInvalidProtocol_Type = Counter64
_IcmpTotInvalidProtocol_Object = MibScalar
icmpTotInvalidProtocol = _IcmpTotInvalidProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 43),
    _IcmpTotInvalidProtocol_Type()
)
icmpTotInvalidProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotInvalidProtocol.setStatus("current")
_IcmpTotBadPMTUIpChecksum_Type = Counter64
_IcmpTotBadPMTUIpChecksum_Object = MibScalar
icmpTotBadPMTUIpChecksum = _IcmpTotBadPMTUIpChecksum_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 44),
    _IcmpTotBadPMTUIpChecksum_Type()
)
icmpTotBadPMTUIpChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotBadPMTUIpChecksum.setStatus("current")
_IcmpTotPMTUnoLink_Type = Counter64
_IcmpTotPMTUnoLink_Object = MibScalar
icmpTotPMTUnoLink = _IcmpTotPMTUnoLink_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 45),
    _IcmpTotPMTUnoLink_Type()
)
icmpTotPMTUnoLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotPMTUnoLink.setStatus("current")
_IcmpTotPMTUDiscoveryDisabled_Type = Counter64
_IcmpTotPMTUDiscoveryDisabled_Object = MibScalar
icmpTotPMTUDiscoveryDisabled = _IcmpTotPMTUDiscoveryDisabled_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 44, 46),
    _IcmpTotPMTUDiscoveryDisabled_Type()
)
icmpTotPMTUDiscoveryDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpTotPMTUDiscoveryDisabled.setStatus("current")
_NsUdpStatsGroup_ObjectIdentity = ObjectIdentity
nsUdpStatsGroup = _NsUdpStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 45)
)
_UdpTotUnknownSvcPktsLow_Type = Counter32
_UdpTotUnknownSvcPktsLow_Object = MibScalar
udpTotUnknownSvcPktsLow = _UdpTotUnknownSvcPktsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 45, 1),
    _UdpTotUnknownSvcPktsLow_Type()
)
udpTotUnknownSvcPktsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpTotUnknownSvcPktsLow.setStatus("obsolete")
_UdpTotUnknownSvcPktsHigh_Type = Counter32
_UdpTotUnknownSvcPktsHigh_Object = MibScalar
udpTotUnknownSvcPktsHigh = _UdpTotUnknownSvcPktsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 45, 2),
    _UdpTotUnknownSvcPktsHigh_Type()
)
udpTotUnknownSvcPktsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpTotUnknownSvcPktsHigh.setStatus("obsolete")
_UdpTotRxPktsLow_Type = Counter32
_UdpTotRxPktsLow_Object = MibScalar
udpTotRxPktsLow = _UdpTotRxPktsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 45, 3),
    _UdpTotRxPktsLow_Type()
)
udpTotRxPktsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpTotRxPktsLow.setStatus("obsolete")
_UdpTotRxPktsHigh_Type = Counter32
_UdpTotRxPktsHigh_Object = MibScalar
udpTotRxPktsHigh = _UdpTotRxPktsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 45, 4),
    _UdpTotRxPktsHigh_Type()
)
udpTotRxPktsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpTotRxPktsHigh.setStatus("obsolete")
_UdpTotRxBytesLow_Type = Counter32
_UdpTotRxBytesLow_Object = MibScalar
udpTotRxBytesLow = _UdpTotRxBytesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 45, 5),
    _UdpTotRxBytesLow_Type()
)
udpTotRxBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpTotRxBytesLow.setStatus("obsolete")
_UdpTotRxBytesHigh_Type = Counter32
_UdpTotRxBytesHigh_Object = MibScalar
udpTotRxBytesHigh = _UdpTotRxBytesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 45, 6),
    _UdpTotRxBytesHigh_Type()
)
udpTotRxBytesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpTotRxBytesHigh.setStatus("obsolete")
_UdpTotTxPktsLow_Type = Counter32
_UdpTotTxPktsLow_Object = MibScalar
udpTotTxPktsLow = _UdpTotTxPktsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 45, 7),
    _UdpTotTxPktsLow_Type()
)
udpTotTxPktsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpTotTxPktsLow.setStatus("obsolete")
_UdpTotTxPktsHigh_Type = Counter32
_UdpTotTxPktsHigh_Object = MibScalar
udpTotTxPktsHigh = _UdpTotTxPktsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 45, 8),
    _UdpTotTxPktsHigh_Type()
)
udpTotTxPktsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpTotTxPktsHigh.setStatus("obsolete")
_UdpTotTxBytesLow_Type = Counter32
_UdpTotTxBytesLow_Object = MibScalar
udpTotTxBytesLow = _UdpTotTxBytesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 45, 9),
    _UdpTotTxBytesLow_Type()
)
udpTotTxBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpTotTxBytesLow.setStatus("obsolete")
_UdpTotTxBytesHigh_Type = Counter32
_UdpTotTxBytesHigh_Object = MibScalar
udpTotTxBytesHigh = _UdpTotTxBytesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 45, 10),
    _UdpTotTxBytesHigh_Type()
)
udpTotTxBytesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpTotTxBytesHigh.setStatus("obsolete")
_UdpCurRateThreshold_Type = Counter32
_UdpCurRateThreshold_Object = MibScalar
udpCurRateThreshold = _UdpCurRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 45, 11),
    _UdpCurRateThreshold_Type()
)
udpCurRateThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpCurRateThreshold.setStatus("current")
_UdpRateInterval_Type = Counter32
_UdpRateInterval_Object = MibScalar
udpRateInterval = _UdpRateInterval_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 45, 12),
    _UdpRateInterval_Type()
)
udpRateInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpRateInterval.setStatus("obsolete")
_UdpCurRateCounter_Type = Counter32
_UdpCurRateCounter_Object = MibScalar
udpCurRateCounter = _UdpCurRateCounter_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 45, 13),
    _UdpCurRateCounter_Type()
)
udpCurRateCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpCurRateCounter.setStatus("obsolete")
_UdpCurRateThresholdExceedsLow_Type = Counter32
_UdpCurRateThresholdExceedsLow_Object = MibScalar
udpCurRateThresholdExceedsLow = _UdpCurRateThresholdExceedsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 45, 14),
    _UdpCurRateThresholdExceedsLow_Type()
)
udpCurRateThresholdExceedsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpCurRateThresholdExceedsLow.setStatus("obsolete")
_UdpCurRateThresholdExceedsHigh_Type = Counter32
_UdpCurRateThresholdExceedsHigh_Object = MibScalar
udpCurRateThresholdExceedsHigh = _UdpCurRateThresholdExceedsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 45, 15),
    _UdpCurRateThresholdExceedsHigh_Type()
)
udpCurRateThresholdExceedsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpCurRateThresholdExceedsHigh.setStatus("obsolete")
_UdpTotUnknownSvcPkts_Type = Counter64
_UdpTotUnknownSvcPkts_Object = MibScalar
udpTotUnknownSvcPkts = _UdpTotUnknownSvcPkts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 45, 16),
    _UdpTotUnknownSvcPkts_Type()
)
udpTotUnknownSvcPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpTotUnknownSvcPkts.setStatus("current")
_UdpTotRxPkts_Type = Counter64
_UdpTotRxPkts_Object = MibScalar
udpTotRxPkts = _UdpTotRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 45, 17),
    _UdpTotRxPkts_Type()
)
udpTotRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpTotRxPkts.setStatus("current")
_UdpTotRxBytes_Type = Counter64
_UdpTotRxBytes_Object = MibScalar
udpTotRxBytes = _UdpTotRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 45, 18),
    _UdpTotRxBytes_Type()
)
udpTotRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpTotRxBytes.setStatus("current")
_UdpTotTxPkts_Type = Counter64
_UdpTotTxPkts_Object = MibScalar
udpTotTxPkts = _UdpTotTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 45, 19),
    _UdpTotTxPkts_Type()
)
udpTotTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpTotTxPkts.setStatus("current")
_UdpTotTxBytes_Type = Counter64
_UdpTotTxBytes_Object = MibScalar
udpTotTxBytes = _UdpTotTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 45, 20),
    _UdpTotTxBytes_Type()
)
udpTotTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpTotTxBytes.setStatus("current")
_UdpCurRateThresholdExceeds_Type = Counter64
_UdpCurRateThresholdExceeds_Object = MibScalar
udpCurRateThresholdExceeds = _UdpCurRateThresholdExceeds_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 45, 21),
    _UdpCurRateThresholdExceeds_Type()
)
udpCurRateThresholdExceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpCurRateThresholdExceeds.setStatus("current")
_UdpBadChecksum_Type = Counter64
_UdpBadChecksum_Object = MibScalar
udpBadChecksum = _UdpBadChecksum_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 45, 22),
    _UdpBadChecksum_Type()
)
udpBadChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpBadChecksum.setStatus("current")
_NsTcpStatsGroup_ObjectIdentity = ObjectIdentity
nsTcpStatsGroup = _NsTcpStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46)
)
_TcpCurServerConn_Type = Gauge32
_TcpCurServerConn_Object = MibScalar
tcpCurServerConn = _TcpCurServerConn_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 1),
    _TcpCurServerConn_Type()
)
tcpCurServerConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpCurServerConn.setStatus("current")
_TcpCurClientConn_Type = Gauge32
_TcpCurClientConn_Object = MibScalar
tcpCurClientConn = _TcpCurClientConn_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 2),
    _TcpCurClientConn_Type()
)
tcpCurClientConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpCurClientConn.setStatus("current")
_TcpCurPendingConn_Type = Gauge32
_TcpCurPendingConn_Object = MibScalar
tcpCurPendingConn = _TcpCurPendingConn_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 3),
    _TcpCurPendingConn_Type()
)
tcpCurPendingConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpCurPendingConn.setStatus("obsolete")
_TcpCurResetCount_Type = Counter32
_TcpCurResetCount_Object = MibScalar
tcpCurResetCount = _TcpCurResetCount_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 4),
    _TcpCurResetCount_Type()
)
tcpCurResetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpCurResetCount.setStatus("obsolete")
_TcpMaxServerConnections_Type = Integer32
_TcpMaxServerConnections_Object = MibScalar
tcpMaxServerConnections = _TcpMaxServerConnections_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 5),
    _TcpMaxServerConnections_Type()
)
tcpMaxServerConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpMaxServerConnections.setStatus("obsolete")
_TcpMaxReqsperConn_Type = Integer32
_TcpMaxReqsperConn_Object = MibScalar
tcpMaxReqsperConn = _TcpMaxReqsperConn_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 6),
    _TcpMaxReqsperConn_Type()
)
tcpMaxReqsperConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpMaxReqsperConn.setStatus("obsolete")
_TcpMaxPerSrvrReusePool_Type = Integer32
_TcpMaxPerSrvrReusePool_Object = MibScalar
tcpMaxPerSrvrReusePool = _TcpMaxPerSrvrReusePool_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 7),
    _TcpMaxPerSrvrReusePool_Type()
)
tcpMaxPerSrvrReusePool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpMaxPerSrvrReusePool.setStatus("obsolete")
_TcpActiveServerConn_Type = Gauge32
_TcpActiveServerConn_Object = MibScalar
tcpActiveServerConn = _TcpActiveServerConn_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 8),
    _TcpActiveServerConn_Type()
)
tcpActiveServerConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpActiveServerConn.setStatus("current")
_TcpCurClientConnClosing_Type = Gauge32
_TcpCurClientConnClosing_Object = MibScalar
tcpCurClientConnClosing = _TcpCurClientConnClosing_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 9),
    _TcpCurClientConnClosing_Type()
)
tcpCurClientConnClosing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpCurClientConnClosing.setStatus("current")
_TcpCurServerConnEstablished_Type = Gauge32
_TcpCurServerConnEstablished_Object = MibScalar
tcpCurServerConnEstablished = _TcpCurServerConnEstablished_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 10),
    _TcpCurServerConnEstablished_Type()
)
tcpCurServerConnEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpCurServerConnEstablished.setStatus("current")
_TcpCurClientConnOpening_Type = Gauge32
_TcpCurClientConnOpening_Object = MibScalar
tcpCurClientConnOpening = _TcpCurClientConnOpening_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 11),
    _TcpCurClientConnOpening_Type()
)
tcpCurClientConnOpening.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpCurClientConnOpening.setStatus("current")
_TcpCurClientConnEstablished_Type = Gauge32
_TcpCurClientConnEstablished_Object = MibScalar
tcpCurClientConnEstablished = _TcpCurClientConnEstablished_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 12),
    _TcpCurClientConnEstablished_Type()
)
tcpCurClientConnEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpCurClientConnEstablished.setStatus("current")
_TcpCurServerConnClosing_Type = Gauge32
_TcpCurServerConnClosing_Object = MibScalar
tcpCurServerConnClosing = _TcpCurServerConnClosing_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 13),
    _TcpCurServerConnClosing_Type()
)
tcpCurServerConnClosing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpCurServerConnClosing.setStatus("current")
_TcpSpareConn_Type = Gauge32
_TcpSpareConn_Object = MibScalar
tcpSpareConn = _TcpSpareConn_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 14),
    _TcpSpareConn_Type()
)
tcpSpareConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpSpareConn.setStatus("current")
_TcpSurgeQueueLen_Type = Gauge32
_TcpSurgeQueueLen_Object = MibScalar
tcpSurgeQueueLen = _TcpSurgeQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 15),
    _TcpSurgeQueueLen_Type()
)
tcpSurgeQueueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpSurgeQueueLen.setStatus("current")
_TcpCurServerConnOpening_Type = Gauge32
_TcpCurServerConnOpening_Object = MibScalar
tcpCurServerConnOpening = _TcpCurServerConnOpening_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 16),
    _TcpCurServerConnOpening_Type()
)
tcpCurServerConnOpening.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpCurServerConnOpening.setStatus("current")
_TcpTotServerConnOpened_Type = Counter64
_TcpTotServerConnOpened_Object = MibScalar
tcpTotServerConnOpened = _TcpTotServerConnOpened_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 17),
    _TcpTotServerConnOpened_Type()
)
tcpTotServerConnOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpTotServerConnOpened.setStatus("current")
_TcpTotServerConnClosed_Type = Counter64
_TcpTotServerConnClosed_Object = MibScalar
tcpTotServerConnClosed = _TcpTotServerConnClosed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 18),
    _TcpTotServerConnClosed_Type()
)
tcpTotServerConnClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpTotServerConnClosed.setStatus("current")
_TcpTotClientConnOpened_Type = Counter64
_TcpTotClientConnOpened_Object = MibScalar
tcpTotClientConnOpened = _TcpTotClientConnOpened_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 19),
    _TcpTotClientConnOpened_Type()
)
tcpTotClientConnOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpTotClientConnOpened.setStatus("current")
_TcpTotClientConnClosed_Type = Counter64
_TcpTotClientConnClosed_Object = MibScalar
tcpTotClientConnClosed = _TcpTotClientConnClosed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 20),
    _TcpTotClientConnClosed_Type()
)
tcpTotClientConnClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpTotClientConnClosed.setStatus("current")
_TcpTotSyn_Type = Counter64
_TcpTotSyn_Object = MibScalar
tcpTotSyn = _TcpTotSyn_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 21),
    _TcpTotSyn_Type()
)
tcpTotSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpTotSyn.setStatus("current")
_TcpTotSynProbe_Type = Counter64
_TcpTotSynProbe_Object = MibScalar
tcpTotSynProbe = _TcpTotSynProbe_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 22),
    _TcpTotSynProbe_Type()
)
tcpTotSynProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpTotSynProbe.setStatus("current")
_TcpTotSvrFin_Type = Counter64
_TcpTotSvrFin_Object = MibScalar
tcpTotSvrFin = _TcpTotSvrFin_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 23),
    _TcpTotSvrFin_Type()
)
tcpTotSvrFin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpTotSvrFin.setStatus("current")
_TcpTotCltFin_Type = Counter64
_TcpTotCltFin_Object = MibScalar
tcpTotCltFin = _TcpTotCltFin_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 24),
    _TcpTotCltFin_Type()
)
tcpTotCltFin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpTotCltFin.setStatus("current")
_TcpWaitToSyn_Type = Counter64
_TcpWaitToSyn_Object = MibScalar
tcpWaitToSyn = _TcpWaitToSyn_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 25),
    _TcpWaitToSyn_Type()
)
tcpWaitToSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpWaitToSyn.setStatus("current")
_TcpTotZombieCltConnFlushed_Type = Counter64
_TcpTotZombieCltConnFlushed_Object = MibScalar
tcpTotZombieCltConnFlushed = _TcpTotZombieCltConnFlushed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 26),
    _TcpTotZombieCltConnFlushed_Type()
)
tcpTotZombieCltConnFlushed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpTotZombieCltConnFlushed.setStatus("current")
_TcpTotZombieSvrConnFlushed_Type = Counter64
_TcpTotZombieSvrConnFlushed_Object = MibScalar
tcpTotZombieSvrConnFlushed = _TcpTotZombieSvrConnFlushed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 27),
    _TcpTotZombieSvrConnFlushed_Type()
)
tcpTotZombieSvrConnFlushed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpTotZombieSvrConnFlushed.setStatus("current")
_TcpTotZombieHalfOpenCltConnFlushed_Type = Counter64
_TcpTotZombieHalfOpenCltConnFlushed_Object = MibScalar
tcpTotZombieHalfOpenCltConnFlushed = _TcpTotZombieHalfOpenCltConnFlushed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 28),
    _TcpTotZombieHalfOpenCltConnFlushed_Type()
)
tcpTotZombieHalfOpenCltConnFlushed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpTotZombieHalfOpenCltConnFlushed.setStatus("current")
_TcpTotZombieHalfOpenSvrConnFlushed_Type = Counter64
_TcpTotZombieHalfOpenSvrConnFlushed_Object = MibScalar
tcpTotZombieHalfOpenSvrConnFlushed = _TcpTotZombieHalfOpenSvrConnFlushed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 29),
    _TcpTotZombieHalfOpenSvrConnFlushed_Type()
)
tcpTotZombieHalfOpenSvrConnFlushed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpTotZombieHalfOpenSvrConnFlushed.setStatus("current")
_TcpTotZombieActiveHalfCloseCltConnFlushed_Type = Counter64
_TcpTotZombieActiveHalfCloseCltConnFlushed_Object = MibScalar
tcpTotZombieActiveHalfCloseCltConnFlushed = _TcpTotZombieActiveHalfCloseCltConnFlushed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 30),
    _TcpTotZombieActiveHalfCloseCltConnFlushed_Type()
)
tcpTotZombieActiveHalfCloseCltConnFlushed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpTotZombieActiveHalfCloseCltConnFlushed.setStatus("current")
_TcpTotZombieActiveHalfCloseSvrConnFlushed_Type = Counter64
_TcpTotZombieActiveHalfCloseSvrConnFlushed_Object = MibScalar
tcpTotZombieActiveHalfCloseSvrConnFlushed = _TcpTotZombieActiveHalfCloseSvrConnFlushed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 31),
    _TcpTotZombieActiveHalfCloseSvrConnFlushed_Type()
)
tcpTotZombieActiveHalfCloseSvrConnFlushed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpTotZombieActiveHalfCloseSvrConnFlushed.setStatus("current")
_TcpTotZombiePassiveHalfCloseCltConnFlushed_Type = Counter64
_TcpTotZombiePassiveHalfCloseCltConnFlushed_Object = MibScalar
tcpTotZombiePassiveHalfCloseCltConnFlushed = _TcpTotZombiePassiveHalfCloseCltConnFlushed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 32),
    _TcpTotZombiePassiveHalfCloseCltConnFlushed_Type()
)
tcpTotZombiePassiveHalfCloseCltConnFlushed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpTotZombiePassiveHalfCloseCltConnFlushed.setStatus("current")
_TcpTotZombiePassiveHalfCloseSrvConnFlushed_Type = Counter64
_TcpTotZombiePassiveHalfCloseSrvConnFlushed_Object = MibScalar
tcpTotZombiePassiveHalfCloseSrvConnFlushed = _TcpTotZombiePassiveHalfCloseSrvConnFlushed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 33),
    _TcpTotZombiePassiveHalfCloseSrvConnFlushed_Type()
)
tcpTotZombiePassiveHalfCloseSrvConnFlushed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpTotZombiePassiveHalfCloseSrvConnFlushed.setStatus("current")
_TcpErrBadCheckSum_Type = Counter64
_TcpErrBadCheckSum_Object = MibScalar
tcpErrBadCheckSum = _TcpErrBadCheckSum_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 34),
    _TcpErrBadCheckSum_Type()
)
tcpErrBadCheckSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrBadCheckSum.setStatus("current")
_TcpErrSynInSynRcvd_Type = Counter64
_TcpErrSynInSynRcvd_Object = MibScalar
tcpErrSynInSynRcvd = _TcpErrSynInSynRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 35),
    _TcpErrSynInSynRcvd_Type()
)
tcpErrSynInSynRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrSynInSynRcvd.setStatus("current")
_TcpErrSynInEst_Type = Counter64
_TcpErrSynInEst_Object = MibScalar
tcpErrSynInEst = _TcpErrSynInEst_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 36),
    _TcpErrSynInEst_Type()
)
tcpErrSynInEst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrSynInEst.setStatus("current")
_TcpErrSynGiveUp_Type = Counter64
_TcpErrSynGiveUp_Object = MibScalar
tcpErrSynGiveUp = _TcpErrSynGiveUp_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 37),
    _TcpErrSynGiveUp_Type()
)
tcpErrSynGiveUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrSynGiveUp.setStatus("current")
_TcpErrSynSentBadAck_Type = Counter64
_TcpErrSynSentBadAck_Object = MibScalar
tcpErrSynSentBadAck = _TcpErrSynSentBadAck_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 38),
    _TcpErrSynSentBadAck_Type()
)
tcpErrSynSentBadAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrSynSentBadAck.setStatus("current")
_TcpErrSynRetry_Type = Counter64
_TcpErrSynRetry_Object = MibScalar
tcpErrSynRetry = _TcpErrSynRetry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 39),
    _TcpErrSynRetry_Type()
)
tcpErrSynRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrSynRetry.setStatus("current")
_TcpErrFinRetry_Type = Counter64
_TcpErrFinRetry_Object = MibScalar
tcpErrFinRetry = _TcpErrFinRetry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 40),
    _TcpErrFinRetry_Type()
)
tcpErrFinRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrFinRetry.setStatus("current")
_TcpErrFinGiveUp_Type = Counter64
_TcpErrFinGiveUp_Object = MibScalar
tcpErrFinGiveUp = _TcpErrFinGiveUp_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 41),
    _TcpErrFinGiveUp_Type()
)
tcpErrFinGiveUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrFinGiveUp.setStatus("current")
_TcpErrFinDup_Type = Counter64
_TcpErrFinDup_Object = MibScalar
tcpErrFinDup = _TcpErrFinDup_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 42),
    _TcpErrFinDup_Type()
)
tcpErrFinDup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrFinDup.setStatus("current")
_TcpErrRst_Type = Counter64
_TcpErrRst_Object = MibScalar
tcpErrRst = _TcpErrRst_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 43),
    _TcpErrRst_Type()
)
tcpErrRst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrRst.setStatus("current")
_TcpErrRstNonEst_Type = Counter64
_TcpErrRstNonEst_Object = MibScalar
tcpErrRstNonEst = _TcpErrRstNonEst_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 44),
    _TcpErrRstNonEst_Type()
)
tcpErrRstNonEst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrRstNonEst.setStatus("current")
_TcpErrRstOutOfWindow_Type = Counter64
_TcpErrRstOutOfWindow_Object = MibScalar
tcpErrRstOutOfWindow = _TcpErrRstOutOfWindow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 45),
    _TcpErrRstOutOfWindow_Type()
)
tcpErrRstOutOfWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrRstOutOfWindow.setStatus("current")
_TcpErrRstInTimewait_Type = Counter64
_TcpErrRstInTimewait_Object = MibScalar
tcpErrRstInTimewait = _TcpErrRstInTimewait_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 46),
    _TcpErrRstInTimewait_Type()
)
tcpErrRstInTimewait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrRstInTimewait.setStatus("current")
_TcpErrSvrRetrasmit_Type = Counter64
_TcpErrSvrRetrasmit_Object = MibScalar
tcpErrSvrRetrasmit = _TcpErrSvrRetrasmit_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 47),
    _TcpErrSvrRetrasmit_Type()
)
tcpErrSvrRetrasmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrSvrRetrasmit.setStatus("current")
_TcpErrCltRetrasmit_Type = Counter64
_TcpErrCltRetrasmit_Object = MibScalar
tcpErrCltRetrasmit = _TcpErrCltRetrasmit_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 48),
    _TcpErrCltRetrasmit_Type()
)
tcpErrCltRetrasmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrCltRetrasmit.setStatus("current")
_TcpErrFullRetrasmit_Type = Counter64
_TcpErrFullRetrasmit_Object = MibScalar
tcpErrFullRetrasmit = _TcpErrFullRetrasmit_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 49),
    _TcpErrFullRetrasmit_Type()
)
tcpErrFullRetrasmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrFullRetrasmit.setStatus("current")
_TcpErrPartialRetrasmit_Type = Counter64
_TcpErrPartialRetrasmit_Object = MibScalar
tcpErrPartialRetrasmit = _TcpErrPartialRetrasmit_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 50),
    _TcpErrPartialRetrasmit_Type()
)
tcpErrPartialRetrasmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrPartialRetrasmit.setStatus("current")
_TcpErrSvrOutOfOrder_Type = Counter64
_TcpErrSvrOutOfOrder_Object = MibScalar
tcpErrSvrOutOfOrder = _TcpErrSvrOutOfOrder_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 51),
    _TcpErrSvrOutOfOrder_Type()
)
tcpErrSvrOutOfOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrSvrOutOfOrder.setStatus("current")
_TcpErrCltOutOfOrder_Type = Counter64
_TcpErrCltOutOfOrder_Object = MibScalar
tcpErrCltOutOfOrder = _TcpErrCltOutOfOrder_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 52),
    _TcpErrCltOutOfOrder_Type()
)
tcpErrCltOutOfOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrCltOutOfOrder.setStatus("current")
_TcpErrCltHole_Type = Counter64
_TcpErrCltHole_Object = MibScalar
tcpErrCltHole = _TcpErrCltHole_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 53),
    _TcpErrCltHole_Type()
)
tcpErrCltHole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrCltHole.setStatus("current")
_TcpErrSvrHole_Type = Counter64
_TcpErrSvrHole_Object = MibScalar
tcpErrSvrHole = _TcpErrSvrHole_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 54),
    _TcpErrSvrHole_Type()
)
tcpErrSvrHole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrSvrHole.setStatus("current")
_TcpErrCookiePktSeqReject_Type = Counter64
_TcpErrCookiePktSeqReject_Object = MibScalar
tcpErrCookiePktSeqReject = _TcpErrCookiePktSeqReject_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 55),
    _TcpErrCookiePktSeqReject_Type()
)
tcpErrCookiePktSeqReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrCookiePktSeqReject.setStatus("current")
_TcpErrCookiePktSigReject_Type = Counter64
_TcpErrCookiePktSigReject_Object = MibScalar
tcpErrCookiePktSigReject = _TcpErrCookiePktSigReject_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 56),
    _TcpErrCookiePktSigReject_Type()
)
tcpErrCookiePktSigReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrCookiePktSigReject.setStatus("current")
_TcpErrCookiePktSeqDrop_Type = Counter64
_TcpErrCookiePktSeqDrop_Object = MibScalar
tcpErrCookiePktSeqDrop = _TcpErrCookiePktSeqDrop_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 57),
    _TcpErrCookiePktSeqDrop_Type()
)
tcpErrCookiePktSeqDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrCookiePktSeqDrop.setStatus("current")
_TcpErrCookiePktMssReject_Type = Counter64
_TcpErrCookiePktMssReject_Object = MibScalar
tcpErrCookiePktMssReject = _TcpErrCookiePktMssReject_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 58),
    _TcpErrCookiePktMssReject_Type()
)
tcpErrCookiePktMssReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrCookiePktMssReject.setStatus("current")
_TcpErrRetransmit_Type = Counter64
_TcpErrRetransmit_Object = MibScalar
tcpErrRetransmit = _TcpErrRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 59),
    _TcpErrRetransmit_Type()
)
tcpErrRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrRetransmit.setStatus("current")
_TcpErrRetransmitGiveUp_Type = Counter64
_TcpErrRetransmitGiveUp_Object = MibScalar
tcpErrRetransmitGiveUp = _TcpErrRetransmitGiveUp_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 60),
    _TcpErrRetransmitGiveUp_Type()
)
tcpErrRetransmitGiveUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrRetransmitGiveUp.setStatus("current")
_TcpTotRxPkts_Type = Counter64
_TcpTotRxPkts_Object = MibScalar
tcpTotRxPkts = _TcpTotRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 61),
    _TcpTotRxPkts_Type()
)
tcpTotRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpTotRxPkts.setStatus("current")
_TcpTotRxBytes_Type = Counter64
_TcpTotRxBytes_Object = MibScalar
tcpTotRxBytes = _TcpTotRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 62),
    _TcpTotRxBytes_Type()
)
tcpTotRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpTotRxBytes.setStatus("current")
_TcpTotTxPkts_Type = Counter64
_TcpTotTxPkts_Object = MibScalar
tcpTotTxPkts = _TcpTotTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 63),
    _TcpTotTxPkts_Type()
)
tcpTotTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpTotTxPkts.setStatus("current")
_TcpTotTxBytes_Type = Counter64
_TcpTotTxBytes_Object = MibScalar
tcpTotTxBytes = _TcpTotTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 64),
    _TcpTotTxBytes_Type()
)
tcpTotTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpTotTxBytes.setStatus("current")
_PcbTotZombieCall_Type = Counter64
_PcbTotZombieCall_Object = MibScalar
pcbTotZombieCall = _PcbTotZombieCall_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 65),
    _PcbTotZombieCall_Type()
)
pcbTotZombieCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcbTotZombieCall.setStatus("current")
_TcpTotSynHeld_Type = Counter64
_TcpTotSynHeld_Object = MibScalar
tcpTotSynHeld = _TcpTotSynHeld_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 66),
    _TcpTotSynHeld_Type()
)
tcpTotSynHeld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpTotSynHeld.setStatus("current")
_TcpTotSynFlush_Type = Counter64
_TcpTotSynFlush_Object = MibScalar
tcpTotSynFlush = _TcpTotSynFlush_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 67),
    _TcpTotSynFlush_Type()
)
tcpTotSynFlush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpTotSynFlush.setStatus("current")
_TcpTotFinWaitClosed_Type = Counter64
_TcpTotFinWaitClosed_Object = MibScalar
tcpTotFinWaitClosed = _TcpTotFinWaitClosed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 68),
    _TcpTotFinWaitClosed_Type()
)
tcpTotFinWaitClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpTotFinWaitClosed.setStatus("current")
_TcpErrAnyPortFail_Type = Counter64
_TcpErrAnyPortFail_Object = MibScalar
tcpErrAnyPortFail = _TcpErrAnyPortFail_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 69),
    _TcpErrAnyPortFail_Type()
)
tcpErrAnyPortFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrAnyPortFail.setStatus("current")
_TcpErrIpPortFail_Type = Counter64
_TcpErrIpPortFail_Object = MibScalar
tcpErrIpPortFail = _TcpErrIpPortFail_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 70),
    _TcpErrIpPortFail_Type()
)
tcpErrIpPortFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrIpPortFail.setStatus("current")
_TcpErrSentRst_Type = Counter64
_TcpErrSentRst_Object = MibScalar
tcpErrSentRst = _TcpErrSentRst_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 71),
    _TcpErrSentRst_Type()
)
tcpErrSentRst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrSentRst.setStatus("current")
_TcpErrBadStateConn_Type = Counter64
_TcpErrBadStateConn_Object = MibScalar
tcpErrBadStateConn = _TcpErrBadStateConn_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 72),
    _TcpErrBadStateConn_Type()
)
tcpErrBadStateConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrBadStateConn.setStatus("current")
_TcpErrFastRetransmissions_Type = Counter64
_TcpErrFastRetransmissions_Object = MibScalar
tcpErrFastRetransmissions = _TcpErrFastRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 73),
    _TcpErrFastRetransmissions_Type()
)
tcpErrFastRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrFastRetransmissions.setStatus("current")
_TcpErrFirstRetransmissions_Type = Counter64
_TcpErrFirstRetransmissions_Object = MibScalar
tcpErrFirstRetransmissions = _TcpErrFirstRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 74),
    _TcpErrFirstRetransmissions_Type()
)
tcpErrFirstRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrFirstRetransmissions.setStatus("current")
_TcpErrSecondRetransmissions_Type = Counter64
_TcpErrSecondRetransmissions_Object = MibScalar
tcpErrSecondRetransmissions = _TcpErrSecondRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 75),
    _TcpErrSecondRetransmissions_Type()
)
tcpErrSecondRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrSecondRetransmissions.setStatus("current")
_TcpErrThirdRetransmissions_Type = Counter64
_TcpErrThirdRetransmissions_Object = MibScalar
tcpErrThirdRetransmissions = _TcpErrThirdRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 76),
    _TcpErrThirdRetransmissions_Type()
)
tcpErrThirdRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrThirdRetransmissions.setStatus("current")
_TcpErrForthRetransmissions_Type = Counter64
_TcpErrForthRetransmissions_Object = MibScalar
tcpErrForthRetransmissions = _TcpErrForthRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 77),
    _TcpErrForthRetransmissions_Type()
)
tcpErrForthRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrForthRetransmissions.setStatus("current")
_TcpErrFifthRetransmissions_Type = Counter64
_TcpErrFifthRetransmissions_Object = MibScalar
tcpErrFifthRetransmissions = _TcpErrFifthRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 78),
    _TcpErrFifthRetransmissions_Type()
)
tcpErrFifthRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrFifthRetransmissions.setStatus("current")
_TcpErrSixthRetransmissions_Type = Counter64
_TcpErrSixthRetransmissions_Object = MibScalar
tcpErrSixthRetransmissions = _TcpErrSixthRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 79),
    _TcpErrSixthRetransmissions_Type()
)
tcpErrSixthRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrSixthRetransmissions.setStatus("current")
_TcpErrSeventhRetransmissions_Type = Counter64
_TcpErrSeventhRetransmissions_Object = MibScalar
tcpErrSeventhRetransmissions = _TcpErrSeventhRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 80),
    _TcpErrSeventhRetransmissions_Type()
)
tcpErrSeventhRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrSeventhRetransmissions.setStatus("current")
_TcpErrDataAfterFin_Type = Counter64
_TcpErrDataAfterFin_Object = MibScalar
tcpErrDataAfterFin = _TcpErrDataAfterFin_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 81),
    _TcpErrDataAfterFin_Type()
)
tcpErrDataAfterFin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrDataAfterFin.setStatus("current")
_TcpErrRstThreshold_Type = Counter64
_TcpErrRstThreshold_Object = MibScalar
tcpErrRstThreshold = _TcpErrRstThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 82),
    _TcpErrRstThreshold_Type()
)
tcpErrRstThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrRstThreshold.setStatus("current")
_TcpErrOutOfWindowPkts_Type = Counter64
_TcpErrOutOfWindowPkts_Object = MibScalar
tcpErrOutOfWindowPkts = _TcpErrOutOfWindowPkts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 83),
    _TcpErrOutOfWindowPkts_Type()
)
tcpErrOutOfWindowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrOutOfWindowPkts.setStatus("current")
_TcpErrSynDroppedCongestion_Type = Counter64
_TcpErrSynDroppedCongestion_Object = MibScalar
tcpErrSynDroppedCongestion = _TcpErrSynDroppedCongestion_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 84),
    _TcpErrSynDroppedCongestion_Type()
)
tcpErrSynDroppedCongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrSynDroppedCongestion.setStatus("current")
_TcpCurPhysicalServers_Type = Gauge32
_TcpCurPhysicalServers_Object = MibScalar
tcpCurPhysicalServers = _TcpCurPhysicalServers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 85),
    _TcpCurPhysicalServers_Type()
)
tcpCurPhysicalServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpCurPhysicalServers.setStatus("current")
_TcpReuseHit_Type = Gauge32
_TcpReuseHit_Object = MibScalar
tcpReuseHit = _TcpReuseHit_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 86),
    _TcpReuseHit_Type()
)
tcpReuseHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpReuseHit.setStatus("current")
_TcpWaitToData_Type = Counter64
_TcpWaitToData_Object = MibScalar
tcpWaitToData = _TcpWaitToData_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 87),
    _TcpWaitToData_Type()
)
tcpWaitToData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpWaitToData.setStatus("current")
_TcpErrStrayPkt_Type = Counter64
_TcpErrStrayPkt_Object = MibScalar
tcpErrStrayPkt = _TcpErrStrayPkt_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 88),
    _TcpErrStrayPkt_Type()
)
tcpErrStrayPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpErrStrayPkt.setStatus("current")
_TcpTotClientConnOpenRate_Type = OctetString
_TcpTotClientConnOpenRate_Object = MibScalar
tcpTotClientConnOpenRate = _TcpTotClientConnOpenRate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 46, 89),
    _TcpTotClientConnOpenRate_Type()
)
tcpTotClientConnOpenRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpTotClientConnOpenRate.setStatus("current")
_NsSslStatsGroup_ObjectIdentity = ObjectIdentity
nsSslStatsGroup = _NsSslStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47)
)
_SslCardStatus_Type = Integer32
_SslCardStatus_Object = MibScalar
sslCardStatus = _SslCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 1),
    _SslCardStatus_Type()
)
sslCardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCardStatus.setStatus("current")
_SslEngineStatus_Type = Integer32
_SslEngineStatus_Object = MibScalar
sslEngineStatus = _SslEngineStatus_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 2),
    _SslEngineStatus_Type()
)
sslEngineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslEngineStatus.setStatus("current")
_SslSessionsPerSec_Type = Gauge32
_SslSessionsPerSec_Object = MibScalar
sslSessionsPerSec = _SslSessionsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 3),
    _SslSessionsPerSec_Type()
)
sslSessionsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSessionsPerSec.setStatus("current")
_SslTotTransactionsLow_Type = Counter32
_SslTotTransactionsLow_Object = MibScalar
sslTotTransactionsLow = _SslTotTransactionsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 11),
    _SslTotTransactionsLow_Type()
)
sslTotTransactionsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotTransactionsLow.setStatus("obsolete")
_SslTotTransactionsHigh_Type = Counter32
_SslTotTransactionsHigh_Object = MibScalar
sslTotTransactionsHigh = _SslTotTransactionsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 12),
    _SslTotTransactionsHigh_Type()
)
sslTotTransactionsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotTransactionsHigh.setStatus("obsolete")
_SslTotSSLv2TransactionsLow_Type = Counter32
_SslTotSSLv2TransactionsLow_Object = MibScalar
sslTotSSLv2TransactionsLow = _SslTotSSLv2TransactionsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 13),
    _SslTotSSLv2TransactionsLow_Type()
)
sslTotSSLv2TransactionsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSSLv2TransactionsLow.setStatus("obsolete")
_SslTotSSLv2TransactionsHigh_Type = Counter32
_SslTotSSLv2TransactionsHigh_Object = MibScalar
sslTotSSLv2TransactionsHigh = _SslTotSSLv2TransactionsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 14),
    _SslTotSSLv2TransactionsHigh_Type()
)
sslTotSSLv2TransactionsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSSLv2TransactionsHigh.setStatus("obsolete")
_SslTotSSLv3TransactionsLow_Type = Counter32
_SslTotSSLv3TransactionsLow_Object = MibScalar
sslTotSSLv3TransactionsLow = _SslTotSSLv3TransactionsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 15),
    _SslTotSSLv3TransactionsLow_Type()
)
sslTotSSLv3TransactionsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSSLv3TransactionsLow.setStatus("obsolete")
_SslTotSSLv3TransactionsHigh_Type = Counter32
_SslTotSSLv3TransactionsHigh_Object = MibScalar
sslTotSSLv3TransactionsHigh = _SslTotSSLv3TransactionsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 16),
    _SslTotSSLv3TransactionsHigh_Type()
)
sslTotSSLv3TransactionsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSSLv3TransactionsHigh.setStatus("obsolete")
_SslTotTLSv1TransactionsLow_Type = Counter32
_SslTotTLSv1TransactionsLow_Object = MibScalar
sslTotTLSv1TransactionsLow = _SslTotTLSv1TransactionsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 17),
    _SslTotTLSv1TransactionsLow_Type()
)
sslTotTLSv1TransactionsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotTLSv1TransactionsLow.setStatus("obsolete")
_SslTotTLSv1TransactionsHigh_Type = Counter32
_SslTotTLSv1TransactionsHigh_Object = MibScalar
sslTotTLSv1TransactionsHigh = _SslTotTLSv1TransactionsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 18),
    _SslTotTLSv1TransactionsHigh_Type()
)
sslTotTLSv1TransactionsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotTLSv1TransactionsHigh.setStatus("obsolete")
_SslTotSessionsLow_Type = Counter32
_SslTotSessionsLow_Object = MibScalar
sslTotSessionsLow = _SslTotSessionsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 19),
    _SslTotSessionsLow_Type()
)
sslTotSessionsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSessionsLow.setStatus("obsolete")
_SslTotSessionsHigh_Type = Counter32
_SslTotSessionsHigh_Object = MibScalar
sslTotSessionsHigh = _SslTotSessionsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 20),
    _SslTotSessionsHigh_Type()
)
sslTotSessionsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSessionsHigh.setStatus("obsolete")
_SslTotSSLv2SessionsLow_Type = Counter32
_SslTotSSLv2SessionsLow_Object = MibScalar
sslTotSSLv2SessionsLow = _SslTotSSLv2SessionsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 21),
    _SslTotSSLv2SessionsLow_Type()
)
sslTotSSLv2SessionsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSSLv2SessionsLow.setStatus("obsolete")
_SslTotSSLv2SessionsHigh_Type = Counter32
_SslTotSSLv2SessionsHigh_Object = MibScalar
sslTotSSLv2SessionsHigh = _SslTotSSLv2SessionsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 22),
    _SslTotSSLv2SessionsHigh_Type()
)
sslTotSSLv2SessionsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSSLv2SessionsHigh.setStatus("obsolete")
_SslTotSSLv3SessionsLow_Type = Counter32
_SslTotSSLv3SessionsLow_Object = MibScalar
sslTotSSLv3SessionsLow = _SslTotSSLv3SessionsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 23),
    _SslTotSSLv3SessionsLow_Type()
)
sslTotSSLv3SessionsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSSLv3SessionsLow.setStatus("obsolete")
_SslTotSSLv3SessionsHigh_Type = Counter32
_SslTotSSLv3SessionsHigh_Object = MibScalar
sslTotSSLv3SessionsHigh = _SslTotSSLv3SessionsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 24),
    _SslTotSSLv3SessionsHigh_Type()
)
sslTotSSLv3SessionsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSSLv3SessionsHigh.setStatus("obsolete")
_SslTotTLSv1SessionsLow_Type = Counter32
_SslTotTLSv1SessionsLow_Object = MibScalar
sslTotTLSv1SessionsLow = _SslTotTLSv1SessionsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 25),
    _SslTotTLSv1SessionsLow_Type()
)
sslTotTLSv1SessionsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotTLSv1SessionsLow.setStatus("obsolete")
_SslTotTLSv1SessionsHigh_Type = Counter32
_SslTotTLSv1SessionsHigh_Object = MibScalar
sslTotTLSv1SessionsHigh = _SslTotTLSv1SessionsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 26),
    _SslTotTLSv1SessionsHigh_Type()
)
sslTotTLSv1SessionsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotTLSv1SessionsHigh.setStatus("obsolete")
_SslTotExpiredSessionsLow_Type = Counter32
_SslTotExpiredSessionsLow_Object = MibScalar
sslTotExpiredSessionsLow = _SslTotExpiredSessionsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 27),
    _SslTotExpiredSessionsLow_Type()
)
sslTotExpiredSessionsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotExpiredSessionsLow.setStatus("obsolete")
_SslTotExpiredSessionsHigh_Type = Counter32
_SslTotExpiredSessionsHigh_Object = MibScalar
sslTotExpiredSessionsHigh = _SslTotExpiredSessionsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 28),
    _SslTotExpiredSessionsHigh_Type()
)
sslTotExpiredSessionsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotExpiredSessionsHigh.setStatus("obsolete")
_SslTotNewSessionsLow_Type = Counter32
_SslTotNewSessionsLow_Object = MibScalar
sslTotNewSessionsLow = _SslTotNewSessionsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 29),
    _SslTotNewSessionsLow_Type()
)
sslTotNewSessionsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotNewSessionsLow.setStatus("obsolete")
_SslTotNewSessionsHigh_Type = Counter32
_SslTotNewSessionsHigh_Object = MibScalar
sslTotNewSessionsHigh = _SslTotNewSessionsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 30),
    _SslTotNewSessionsHigh_Type()
)
sslTotNewSessionsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotNewSessionsHigh.setStatus("obsolete")
_SslTotSessionHitsLow_Type = Counter32
_SslTotSessionHitsLow_Object = MibScalar
sslTotSessionHitsLow = _SslTotSessionHitsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 31),
    _SslTotSessionHitsLow_Type()
)
sslTotSessionHitsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSessionHitsLow.setStatus("obsolete")
_SslTotSessionHitsHigh_Type = Counter32
_SslTotSessionHitsHigh_Object = MibScalar
sslTotSessionHitsHigh = _SslTotSessionHitsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 32),
    _SslTotSessionHitsHigh_Type()
)
sslTotSessionHitsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSessionHitsHigh.setStatus("obsolete")
_SslTotSessionMissLow_Type = Counter32
_SslTotSessionMissLow_Object = MibScalar
sslTotSessionMissLow = _SslTotSessionMissLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 33),
    _SslTotSessionMissLow_Type()
)
sslTotSessionMissLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSessionMissLow.setStatus("obsolete")
_SslTotSessionMissHigh_Type = Counter32
_SslTotSessionMissHigh_Object = MibScalar
sslTotSessionMissHigh = _SslTotSessionMissHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 34),
    _SslTotSessionMissHigh_Type()
)
sslTotSessionMissHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSessionMissHigh.setStatus("obsolete")
_SslTotRenegSessionsLow_Type = Counter32
_SslTotRenegSessionsLow_Object = MibScalar
sslTotRenegSessionsLow = _SslTotRenegSessionsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 35),
    _SslTotRenegSessionsLow_Type()
)
sslTotRenegSessionsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotRenegSessionsLow.setStatus("obsolete")
_SslTotRenegSessionsHigh_Type = Counter32
_SslTotRenegSessionsHigh_Object = MibScalar
sslTotRenegSessionsHigh = _SslTotRenegSessionsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 36),
    _SslTotRenegSessionsHigh_Type()
)
sslTotRenegSessionsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotRenegSessionsHigh.setStatus("obsolete")
_SslTotSSLv3RenegSessionsLow_Type = Counter32
_SslTotSSLv3RenegSessionsLow_Object = MibScalar
sslTotSSLv3RenegSessionsLow = _SslTotSSLv3RenegSessionsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 37),
    _SslTotSSLv3RenegSessionsLow_Type()
)
sslTotSSLv3RenegSessionsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSSLv3RenegSessionsLow.setStatus("obsolete")
_SslTotSSLv3RenegSessionsHigh_Type = Counter32
_SslTotSSLv3RenegSessionsHigh_Object = MibScalar
sslTotSSLv3RenegSessionsHigh = _SslTotSSLv3RenegSessionsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 38),
    _SslTotSSLv3RenegSessionsHigh_Type()
)
sslTotSSLv3RenegSessionsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSSLv3RenegSessionsHigh.setStatus("obsolete")
_SslTotTLSv1RenegSessionsLow_Type = Counter32
_SslTotTLSv1RenegSessionsLow_Object = MibScalar
sslTotTLSv1RenegSessionsLow = _SslTotTLSv1RenegSessionsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 39),
    _SslTotTLSv1RenegSessionsLow_Type()
)
sslTotTLSv1RenegSessionsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotTLSv1RenegSessionsLow.setStatus("obsolete")
_SslTotTLSv1RenegSessionsHigh_Type = Counter32
_SslTotTLSv1RenegSessionsHigh_Object = MibScalar
sslTotTLSv1RenegSessionsHigh = _SslTotTLSv1RenegSessionsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 40),
    _SslTotTLSv1RenegSessionsHigh_Type()
)
sslTotTLSv1RenegSessionsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotTLSv1RenegSessionsHigh.setStatus("obsolete")
_SslTotSSLv2HandshakesLow_Type = Counter32
_SslTotSSLv2HandshakesLow_Object = MibScalar
sslTotSSLv2HandshakesLow = _SslTotSSLv2HandshakesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 41),
    _SslTotSSLv2HandshakesLow_Type()
)
sslTotSSLv2HandshakesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSSLv2HandshakesLow.setStatus("obsolete")
_SslTotSSLv2HandshakesHigh_Type = Counter32
_SslTotSSLv2HandshakesHigh_Object = MibScalar
sslTotSSLv2HandshakesHigh = _SslTotSSLv2HandshakesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 42),
    _SslTotSSLv2HandshakesHigh_Type()
)
sslTotSSLv2HandshakesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSSLv2HandshakesHigh.setStatus("obsolete")
_SslTotSSLv3HandshakesLow_Type = Counter32
_SslTotSSLv3HandshakesLow_Object = MibScalar
sslTotSSLv3HandshakesLow = _SslTotSSLv3HandshakesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 43),
    _SslTotSSLv3HandshakesLow_Type()
)
sslTotSSLv3HandshakesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSSLv3HandshakesLow.setStatus("obsolete")
_SslTotSSLv3HandshakesHigh_Type = Counter32
_SslTotSSLv3HandshakesHigh_Object = MibScalar
sslTotSSLv3HandshakesHigh = _SslTotSSLv3HandshakesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 44),
    _SslTotSSLv3HandshakesHigh_Type()
)
sslTotSSLv3HandshakesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSSLv3HandshakesHigh.setStatus("obsolete")
_SslTotTLSv1HandshakesLow_Type = Counter32
_SslTotTLSv1HandshakesLow_Object = MibScalar
sslTotTLSv1HandshakesLow = _SslTotTLSv1HandshakesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 45),
    _SslTotTLSv1HandshakesLow_Type()
)
sslTotTLSv1HandshakesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotTLSv1HandshakesLow.setStatus("obsolete")
_SslTotTLSv1HandshakesHigh_Type = Counter32
_SslTotTLSv1HandshakesHigh_Object = MibScalar
sslTotTLSv1HandshakesHigh = _SslTotTLSv1HandshakesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 46),
    _SslTotTLSv1HandshakesHigh_Type()
)
sslTotTLSv1HandshakesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotTLSv1HandshakesHigh.setStatus("obsolete")
_SslTotSSLv2ClientAuthenticationsLow_Type = Counter32
_SslTotSSLv2ClientAuthenticationsLow_Object = MibScalar
sslTotSSLv2ClientAuthenticationsLow = _SslTotSSLv2ClientAuthenticationsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 47),
    _SslTotSSLv2ClientAuthenticationsLow_Type()
)
sslTotSSLv2ClientAuthenticationsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSSLv2ClientAuthenticationsLow.setStatus("obsolete")
_SslTotSSLv2ClientAuthenticationsHigh_Type = Counter32
_SslTotSSLv2ClientAuthenticationsHigh_Object = MibScalar
sslTotSSLv2ClientAuthenticationsHigh = _SslTotSSLv2ClientAuthenticationsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 48),
    _SslTotSSLv2ClientAuthenticationsHigh_Type()
)
sslTotSSLv2ClientAuthenticationsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSSLv2ClientAuthenticationsHigh.setStatus("obsolete")
_SslTotSSLv3ClientAuthenticationsLow_Type = Counter32
_SslTotSSLv3ClientAuthenticationsLow_Object = MibScalar
sslTotSSLv3ClientAuthenticationsLow = _SslTotSSLv3ClientAuthenticationsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 49),
    _SslTotSSLv3ClientAuthenticationsLow_Type()
)
sslTotSSLv3ClientAuthenticationsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSSLv3ClientAuthenticationsLow.setStatus("obsolete")
_SslTotSSLv3ClientAuthenticationsHigh_Type = Counter32
_SslTotSSLv3ClientAuthenticationsHigh_Object = MibScalar
sslTotSSLv3ClientAuthenticationsHigh = _SslTotSSLv3ClientAuthenticationsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 50),
    _SslTotSSLv3ClientAuthenticationsHigh_Type()
)
sslTotSSLv3ClientAuthenticationsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSSLv3ClientAuthenticationsHigh.setStatus("obsolete")
_SslTotTLSv1ClientAuthenticationsLow_Type = Counter32
_SslTotTLSv1ClientAuthenticationsLow_Object = MibScalar
sslTotTLSv1ClientAuthenticationsLow = _SslTotTLSv1ClientAuthenticationsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 51),
    _SslTotTLSv1ClientAuthenticationsLow_Type()
)
sslTotTLSv1ClientAuthenticationsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotTLSv1ClientAuthenticationsLow.setStatus("obsolete")
_SslTotTLSv1ClientAuthenticationsHigh_Type = Counter32
_SslTotTLSv1ClientAuthenticationsHigh_Object = MibScalar
sslTotTLSv1ClientAuthenticationsHigh = _SslTotTLSv1ClientAuthenticationsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 52),
    _SslTotTLSv1ClientAuthenticationsHigh_Type()
)
sslTotTLSv1ClientAuthenticationsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotTLSv1ClientAuthenticationsHigh.setStatus("obsolete")
_SslTotRSA512keyExchangesLow_Type = Counter32
_SslTotRSA512keyExchangesLow_Object = MibScalar
sslTotRSA512keyExchangesLow = _SslTotRSA512keyExchangesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 53),
    _SslTotRSA512keyExchangesLow_Type()
)
sslTotRSA512keyExchangesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotRSA512keyExchangesLow.setStatus("obsolete")
_SslTotRSA512keyExchangesHigh_Type = Counter32
_SslTotRSA512keyExchangesHigh_Object = MibScalar
sslTotRSA512keyExchangesHigh = _SslTotRSA512keyExchangesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 54),
    _SslTotRSA512keyExchangesHigh_Type()
)
sslTotRSA512keyExchangesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotRSA512keyExchangesHigh.setStatus("obsolete")
_SslTotRSA1024keyExchangesLow_Type = Counter32
_SslTotRSA1024keyExchangesLow_Object = MibScalar
sslTotRSA1024keyExchangesLow = _SslTotRSA1024keyExchangesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 55),
    _SslTotRSA1024keyExchangesLow_Type()
)
sslTotRSA1024keyExchangesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotRSA1024keyExchangesLow.setStatus("obsolete")
_SslTotRSA1024keyExchangesHigh_Type = Counter32
_SslTotRSA1024keyExchangesHigh_Object = MibScalar
sslTotRSA1024keyExchangesHigh = _SslTotRSA1024keyExchangesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 56),
    _SslTotRSA1024keyExchangesHigh_Type()
)
sslTotRSA1024keyExchangesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotRSA1024keyExchangesHigh.setStatus("obsolete")
_SslTotRSA2048keyExchangesLow_Type = Counter32
_SslTotRSA2048keyExchangesLow_Object = MibScalar
sslTotRSA2048keyExchangesLow = _SslTotRSA2048keyExchangesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 57),
    _SslTotRSA2048keyExchangesLow_Type()
)
sslTotRSA2048keyExchangesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotRSA2048keyExchangesLow.setStatus("obsolete")
_SslTotRSA2048keyExchangesHigh_Type = Counter32
_SslTotRSA2048keyExchangesHigh_Object = MibScalar
sslTotRSA2048keyExchangesHigh = _SslTotRSA2048keyExchangesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 58),
    _SslTotRSA2048keyExchangesHigh_Type()
)
sslTotRSA2048keyExchangesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotRSA2048keyExchangesHigh.setStatus("obsolete")
_SslTotDH512keyExchangesLow_Type = Counter32
_SslTotDH512keyExchangesLow_Object = MibScalar
sslTotDH512keyExchangesLow = _SslTotDH512keyExchangesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 59),
    _SslTotDH512keyExchangesLow_Type()
)
sslTotDH512keyExchangesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotDH512keyExchangesLow.setStatus("obsolete")
_SslTotDH512keyExchangesHigh_Type = Counter32
_SslTotDH512keyExchangesHigh_Object = MibScalar
sslTotDH512keyExchangesHigh = _SslTotDH512keyExchangesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 60),
    _SslTotDH512keyExchangesHigh_Type()
)
sslTotDH512keyExchangesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotDH512keyExchangesHigh.setStatus("obsolete")
_SslTotDH1024keyExchangesLow_Type = Counter32
_SslTotDH1024keyExchangesLow_Object = MibScalar
sslTotDH1024keyExchangesLow = _SslTotDH1024keyExchangesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 61),
    _SslTotDH1024keyExchangesLow_Type()
)
sslTotDH1024keyExchangesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotDH1024keyExchangesLow.setStatus("obsolete")
_SslTotDH1024keyExchangesHigh_Type = Counter32
_SslTotDH1024keyExchangesHigh_Object = MibScalar
sslTotDH1024keyExchangesHigh = _SslTotDH1024keyExchangesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 62),
    _SslTotDH1024keyExchangesHigh_Type()
)
sslTotDH1024keyExchangesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotDH1024keyExchangesHigh.setStatus("obsolete")
_SslTotDH2048keyExchangesLow_Type = Counter32
_SslTotDH2048keyExchangesLow_Object = MibScalar
sslTotDH2048keyExchangesLow = _SslTotDH2048keyExchangesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 63),
    _SslTotDH2048keyExchangesLow_Type()
)
sslTotDH2048keyExchangesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotDH2048keyExchangesLow.setStatus("obsolete")
_SslTotDH2048keyExchangesHigh_Type = Counter32
_SslTotDH2048keyExchangesHigh_Object = MibScalar
sslTotDH2048keyExchangesHigh = _SslTotDH2048keyExchangesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 64),
    _SslTotDH2048keyExchangesHigh_Type()
)
sslTotDH2048keyExchangesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotDH2048keyExchangesHigh.setStatus("obsolete")
_SslTotRSAAuthorizationsLow_Type = Counter32
_SslTotRSAAuthorizationsLow_Object = MibScalar
sslTotRSAAuthorizationsLow = _SslTotRSAAuthorizationsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 65),
    _SslTotRSAAuthorizationsLow_Type()
)
sslTotRSAAuthorizationsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotRSAAuthorizationsLow.setStatus("obsolete")
_SslTotRSAAuthorizationsHigh_Type = Counter32
_SslTotRSAAuthorizationsHigh_Object = MibScalar
sslTotRSAAuthorizationsHigh = _SslTotRSAAuthorizationsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 66),
    _SslTotRSAAuthorizationsHigh_Type()
)
sslTotRSAAuthorizationsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotRSAAuthorizationsHigh.setStatus("obsolete")
_SslTotDHAuthorizationsLow_Type = Counter32
_SslTotDHAuthorizationsLow_Object = MibScalar
sslTotDHAuthorizationsLow = _SslTotDHAuthorizationsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 67),
    _SslTotDHAuthorizationsLow_Type()
)
sslTotDHAuthorizationsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotDHAuthorizationsLow.setStatus("obsolete")
_SslTotDHAuthorizationsHigh_Type = Counter32
_SslTotDHAuthorizationsHigh_Object = MibScalar
sslTotDHAuthorizationsHigh = _SslTotDHAuthorizationsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 68),
    _SslTotDHAuthorizationsHigh_Type()
)
sslTotDHAuthorizationsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotDHAuthorizationsHigh.setStatus("obsolete")
_SslTotDSSAuthorizationsLow_Type = Counter32
_SslTotDSSAuthorizationsLow_Object = MibScalar
sslTotDSSAuthorizationsLow = _SslTotDSSAuthorizationsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 69),
    _SslTotDSSAuthorizationsLow_Type()
)
sslTotDSSAuthorizationsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotDSSAuthorizationsLow.setStatus("obsolete")
_SslTotDSSAuthorizationsHigh_Type = Counter32
_SslTotDSSAuthorizationsHigh_Object = MibScalar
sslTotDSSAuthorizationsHigh = _SslTotDSSAuthorizationsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 70),
    _SslTotDSSAuthorizationsHigh_Type()
)
sslTotDSSAuthorizationsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotDSSAuthorizationsHigh.setStatus("obsolete")
_SslTotNULLAuthorizationsLow_Type = Counter32
_SslTotNULLAuthorizationsLow_Object = MibScalar
sslTotNULLAuthorizationsLow = _SslTotNULLAuthorizationsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 71),
    _SslTotNULLAuthorizationsLow_Type()
)
sslTotNULLAuthorizationsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotNULLAuthorizationsLow.setStatus("obsolete")
_SslTotNULLAuthorizationsHigh_Type = Counter32
_SslTotNULLAuthorizationsHigh_Object = MibScalar
sslTotNULLAuthorizationsHigh = _SslTotNULLAuthorizationsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 72),
    _SslTotNULLAuthorizationsHigh_Type()
)
sslTotNULLAuthorizationsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotNULLAuthorizationsHigh.setStatus("obsolete")
_SslTot40BitRC4CiphersLow_Type = Counter32
_SslTot40BitRC4CiphersLow_Object = MibScalar
sslTot40BitRC4CiphersLow = _SslTot40BitRC4CiphersLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 73),
    _SslTot40BitRC4CiphersLow_Type()
)
sslTot40BitRC4CiphersLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot40BitRC4CiphersLow.setStatus("obsolete")
_SslTot40BitRC4CiphersHigh_Type = Counter32
_SslTot40BitRC4CiphersHigh_Object = MibScalar
sslTot40BitRC4CiphersHigh = _SslTot40BitRC4CiphersHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 74),
    _SslTot40BitRC4CiphersHigh_Type()
)
sslTot40BitRC4CiphersHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot40BitRC4CiphersHigh.setStatus("obsolete")
_SslTot56BitRC4CiphersLow_Type = Counter32
_SslTot56BitRC4CiphersLow_Object = MibScalar
sslTot56BitRC4CiphersLow = _SslTot56BitRC4CiphersLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 75),
    _SslTot56BitRC4CiphersLow_Type()
)
sslTot56BitRC4CiphersLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot56BitRC4CiphersLow.setStatus("obsolete")
_SslTot56BitRC4CiphersHigh_Type = Counter32
_SslTot56BitRC4CiphersHigh_Object = MibScalar
sslTot56BitRC4CiphersHigh = _SslTot56BitRC4CiphersHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 76),
    _SslTot56BitRC4CiphersHigh_Type()
)
sslTot56BitRC4CiphersHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot56BitRC4CiphersHigh.setStatus("obsolete")
_SslTot64BitRC4CiphersLow_Type = Counter32
_SslTot64BitRC4CiphersLow_Object = MibScalar
sslTot64BitRC4CiphersLow = _SslTot64BitRC4CiphersLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 77),
    _SslTot64BitRC4CiphersLow_Type()
)
sslTot64BitRC4CiphersLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot64BitRC4CiphersLow.setStatus("obsolete")
_SslTot64BitRC4CiphersHigh_Type = Counter32
_SslTot64BitRC4CiphersHigh_Object = MibScalar
sslTot64BitRC4CiphersHigh = _SslTot64BitRC4CiphersHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 78),
    _SslTot64BitRC4CiphersHigh_Type()
)
sslTot64BitRC4CiphersHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot64BitRC4CiphersHigh.setStatus("obsolete")
_SslTot128BitRC4CiphersLow_Type = Counter32
_SslTot128BitRC4CiphersLow_Object = MibScalar
sslTot128BitRC4CiphersLow = _SslTot128BitRC4CiphersLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 79),
    _SslTot128BitRC4CiphersLow_Type()
)
sslTot128BitRC4CiphersLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot128BitRC4CiphersLow.setStatus("obsolete")
_SslTot128BitRC4CiphersHigh_Type = Counter32
_SslTot128BitRC4CiphersHigh_Object = MibScalar
sslTot128BitRC4CiphersHigh = _SslTot128BitRC4CiphersHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 80),
    _SslTot128BitRC4CiphersHigh_Type()
)
sslTot128BitRC4CiphersHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot128BitRC4CiphersHigh.setStatus("obsolete")
_SslTot40BitDESCiphersLow_Type = Counter32
_SslTot40BitDESCiphersLow_Object = MibScalar
sslTot40BitDESCiphersLow = _SslTot40BitDESCiphersLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 81),
    _SslTot40BitDESCiphersLow_Type()
)
sslTot40BitDESCiphersLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot40BitDESCiphersLow.setStatus("obsolete")
_SslTot40BitDESCiphersHigh_Type = Counter32
_SslTot40BitDESCiphersHigh_Object = MibScalar
sslTot40BitDESCiphersHigh = _SslTot40BitDESCiphersHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 82),
    _SslTot40BitDESCiphersHigh_Type()
)
sslTot40BitDESCiphersHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot40BitDESCiphersHigh.setStatus("obsolete")
_SslTot56BitDESCiphersLow_Type = Counter32
_SslTot56BitDESCiphersLow_Object = MibScalar
sslTot56BitDESCiphersLow = _SslTot56BitDESCiphersLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 83),
    _SslTot56BitDESCiphersLow_Type()
)
sslTot56BitDESCiphersLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot56BitDESCiphersLow.setStatus("obsolete")
_SslTot56BitDESCiphersHigh_Type = Counter32
_SslTot56BitDESCiphersHigh_Object = MibScalar
sslTot56BitDESCiphersHigh = _SslTot56BitDESCiphersHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 84),
    _SslTot56BitDESCiphersHigh_Type()
)
sslTot56BitDESCiphersHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot56BitDESCiphersHigh.setStatus("obsolete")
_SslTot168Bit3DESCiphersLow_Type = Counter32
_SslTot168Bit3DESCiphersLow_Object = MibScalar
sslTot168Bit3DESCiphersLow = _SslTot168Bit3DESCiphersLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 85),
    _SslTot168Bit3DESCiphersLow_Type()
)
sslTot168Bit3DESCiphersLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot168Bit3DESCiphersLow.setStatus("obsolete")
_SslTot168Bit3DESCiphersHigh_Type = Counter32
_SslTot168Bit3DESCiphersHigh_Object = MibScalar
sslTot168Bit3DESCiphersHigh = _SslTot168Bit3DESCiphersHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 86),
    _SslTot168Bit3DESCiphersHigh_Type()
)
sslTot168Bit3DESCiphersHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot168Bit3DESCiphersHigh.setStatus("obsolete")
_SslTot40BitRC2CiphersLow_Type = Counter32
_SslTot40BitRC2CiphersLow_Object = MibScalar
sslTot40BitRC2CiphersLow = _SslTot40BitRC2CiphersLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 87),
    _SslTot40BitRC2CiphersLow_Type()
)
sslTot40BitRC2CiphersLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot40BitRC2CiphersLow.setStatus("obsolete")
_SslTot40BitRC2CiphersHigh_Type = Counter32
_SslTot40BitRC2CiphersHigh_Object = MibScalar
sslTot40BitRC2CiphersHigh = _SslTot40BitRC2CiphersHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 88),
    _SslTot40BitRC2CiphersHigh_Type()
)
sslTot40BitRC2CiphersHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot40BitRC2CiphersHigh.setStatus("obsolete")
_SslTot56BitRC2CiphersLow_Type = Counter32
_SslTot56BitRC2CiphersLow_Object = MibScalar
sslTot56BitRC2CiphersLow = _SslTot56BitRC2CiphersLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 89),
    _SslTot56BitRC2CiphersLow_Type()
)
sslTot56BitRC2CiphersLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot56BitRC2CiphersLow.setStatus("obsolete")
_SslTot56BitRC2CiphersHigh_Type = Counter32
_SslTot56BitRC2CiphersHigh_Object = MibScalar
sslTot56BitRC2CiphersHigh = _SslTot56BitRC2CiphersHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 90),
    _SslTot56BitRC2CiphersHigh_Type()
)
sslTot56BitRC2CiphersHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot56BitRC2CiphersHigh.setStatus("obsolete")
_SslTot128BitRC2CiphersLow_Type = Counter32
_SslTot128BitRC2CiphersLow_Object = MibScalar
sslTot128BitRC2CiphersLow = _SslTot128BitRC2CiphersLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 91),
    _SslTot128BitRC2CiphersLow_Type()
)
sslTot128BitRC2CiphersLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot128BitRC2CiphersLow.setStatus("obsolete")
_SslTot128BitRC2CiphersHigh_Type = Counter32
_SslTot128BitRC2CiphersHigh_Object = MibScalar
sslTot128BitRC2CiphersHigh = _SslTot128BitRC2CiphersHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 92),
    _SslTot128BitRC2CiphersHigh_Type()
)
sslTot128BitRC2CiphersHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot128BitRC2CiphersHigh.setStatus("obsolete")
_SslTot128BitIDEACiphersLow_Type = Counter32
_SslTot128BitIDEACiphersLow_Object = MibScalar
sslTot128BitIDEACiphersLow = _SslTot128BitIDEACiphersLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 93),
    _SslTot128BitIDEACiphersLow_Type()
)
sslTot128BitIDEACiphersLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot128BitIDEACiphersLow.setStatus("obsolete")
_SslTot128BitIDEACiphersHigh_Type = Counter32
_SslTot128BitIDEACiphersHigh_Object = MibScalar
sslTot128BitIDEACiphersHigh = _SslTot128BitIDEACiphersHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 94),
    _SslTot128BitIDEACiphersHigh_Type()
)
sslTot128BitIDEACiphersHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot128BitIDEACiphersHigh.setStatus("obsolete")
_SslTotNULLCiphersLow_Type = Counter32
_SslTotNULLCiphersLow_Object = MibScalar
sslTotNULLCiphersLow = _SslTotNULLCiphersLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 95),
    _SslTotNULLCiphersLow_Type()
)
sslTotNULLCiphersLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotNULLCiphersLow.setStatus("obsolete")
_SslTotNULLCiphersHigh_Type = Counter32
_SslTotNULLCiphersHigh_Object = MibScalar
sslTotNULLCiphersHigh = _SslTotNULLCiphersHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 96),
    _SslTotNULLCiphersHigh_Type()
)
sslTotNULLCiphersHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotNULLCiphersHigh.setStatus("obsolete")
_SslTotMD5MacLow_Type = Counter32
_SslTotMD5MacLow_Object = MibScalar
sslTotMD5MacLow = _SslTotMD5MacLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 97),
    _SslTotMD5MacLow_Type()
)
sslTotMD5MacLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotMD5MacLow.setStatus("obsolete")
_SslTotMD5MacHigh_Type = Counter32
_SslTotMD5MacHigh_Object = MibScalar
sslTotMD5MacHigh = _SslTotMD5MacHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 98),
    _SslTotMD5MacHigh_Type()
)
sslTotMD5MacHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotMD5MacHigh.setStatus("obsolete")
_SslTotSHAMacLow_Type = Counter32
_SslTotSHAMacLow_Object = MibScalar
sslTotSHAMacLow = _SslTotSHAMacLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 99),
    _SslTotSHAMacLow_Type()
)
sslTotSHAMacLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSHAMacLow.setStatus("obsolete")
_SslTotSHAMacHigh_Type = Counter32
_SslTotSHAMacHigh_Object = MibScalar
sslTotSHAMacHigh = _SslTotSHAMacHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 100),
    _SslTotSHAMacHigh_Type()
)
sslTotSHAMacHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSHAMacHigh.setStatus("obsolete")
_SslTotOffloadBulkDESLow_Type = Counter32
_SslTotOffloadBulkDESLow_Object = MibScalar
sslTotOffloadBulkDESLow = _SslTotOffloadBulkDESLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 101),
    _SslTotOffloadBulkDESLow_Type()
)
sslTotOffloadBulkDESLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotOffloadBulkDESLow.setStatus("obsolete")
_SslTotOffloadBulkDESHigh_Type = Counter32
_SslTotOffloadBulkDESHigh_Object = MibScalar
sslTotOffloadBulkDESHigh = _SslTotOffloadBulkDESHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 102),
    _SslTotOffloadBulkDESHigh_Type()
)
sslTotOffloadBulkDESHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotOffloadBulkDESHigh.setStatus("obsolete")
_SslTotOffloadRSAKeyExchangesLow_Type = Counter32
_SslTotOffloadRSAKeyExchangesLow_Object = MibScalar
sslTotOffloadRSAKeyExchangesLow = _SslTotOffloadRSAKeyExchangesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 103),
    _SslTotOffloadRSAKeyExchangesLow_Type()
)
sslTotOffloadRSAKeyExchangesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotOffloadRSAKeyExchangesLow.setStatus("obsolete")
_SslTotOffloadRSAKeyExchangesHigh_Type = Counter32
_SslTotOffloadRSAKeyExchangesHigh_Object = MibScalar
sslTotOffloadRSAKeyExchangesHigh = _SslTotOffloadRSAKeyExchangesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 104),
    _SslTotOffloadRSAKeyExchangesHigh_Type()
)
sslTotOffloadRSAKeyExchangesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotOffloadRSAKeyExchangesHigh.setStatus("obsolete")
_SslTotOffloadDHKeyExchangesLow_Type = Counter32
_SslTotOffloadDHKeyExchangesLow_Object = MibScalar
sslTotOffloadDHKeyExchangesLow = _SslTotOffloadDHKeyExchangesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 105),
    _SslTotOffloadDHKeyExchangesLow_Type()
)
sslTotOffloadDHKeyExchangesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotOffloadDHKeyExchangesLow.setStatus("obsolete")
_SslTotOffloadDHKeyExchangesHigh_Type = Counter32
_SslTotOffloadDHKeyExchangesHigh_Object = MibScalar
sslTotOffloadDHKeyExchangesHigh = _SslTotOffloadDHKeyExchangesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 106),
    _SslTotOffloadDHKeyExchangesHigh_Type()
)
sslTotOffloadDHKeyExchangesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotOffloadDHKeyExchangesHigh.setStatus("obsolete")
_SslTotOffloadSignRSALow_Type = Counter32
_SslTotOffloadSignRSALow_Object = MibScalar
sslTotOffloadSignRSALow = _SslTotOffloadSignRSALow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 107),
    _SslTotOffloadSignRSALow_Type()
)
sslTotOffloadSignRSALow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotOffloadSignRSALow.setStatus("obsolete")
_SslTotOffloadSignRSAHigh_Type = Counter32
_SslTotOffloadSignRSAHigh_Object = MibScalar
sslTotOffloadSignRSAHigh = _SslTotOffloadSignRSAHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 108),
    _SslTotOffloadSignRSAHigh_Type()
)
sslTotOffloadSignRSAHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotOffloadSignRSAHigh.setStatus("obsolete")
_SslBeTotSessionsLow_Type = Counter32
_SslBeTotSessionsLow_Object = MibScalar
sslBeTotSessionsLow = _SslBeTotSessionsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 120),
    _SslBeTotSessionsLow_Type()
)
sslBeTotSessionsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotSessionsLow.setStatus("obsolete")
_SslBeTotSessionsHigh_Type = Counter32
_SslBeTotSessionsHigh_Object = MibScalar
sslBeTotSessionsHigh = _SslBeTotSessionsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 121),
    _SslBeTotSessionsHigh_Type()
)
sslBeTotSessionsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotSessionsHigh.setStatus("obsolete")
_SslBeTotSSLv3SessionsLow_Type = Counter32
_SslBeTotSSLv3SessionsLow_Object = MibScalar
sslBeTotSSLv3SessionsLow = _SslBeTotSSLv3SessionsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 122),
    _SslBeTotSSLv3SessionsLow_Type()
)
sslBeTotSSLv3SessionsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotSSLv3SessionsLow.setStatus("obsolete")
_SslBeTotSSLv3SessionsHigh_Type = Counter32
_SslBeTotSSLv3SessionsHigh_Object = MibScalar
sslBeTotSSLv3SessionsHigh = _SslBeTotSSLv3SessionsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 123),
    _SslBeTotSSLv3SessionsHigh_Type()
)
sslBeTotSSLv3SessionsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotSSLv3SessionsHigh.setStatus("obsolete")
_SslBeTotTLSv1SessionsLow_Type = Counter32
_SslBeTotTLSv1SessionsLow_Object = MibScalar
sslBeTotTLSv1SessionsLow = _SslBeTotTLSv1SessionsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 124),
    _SslBeTotTLSv1SessionsLow_Type()
)
sslBeTotTLSv1SessionsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotTLSv1SessionsLow.setStatus("obsolete")
_SslBeTotTLSv1SessionsHigh_Type = Counter32
_SslBeTotTLSv1SessionsHigh_Object = MibScalar
sslBeTotTLSv1SessionsHigh = _SslBeTotTLSv1SessionsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 125),
    _SslBeTotTLSv1SessionsHigh_Type()
)
sslBeTotTLSv1SessionsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotTLSv1SessionsHigh.setStatus("obsolete")
_SslBeExpiredSessionsLow_Type = Counter32
_SslBeExpiredSessionsLow_Object = MibScalar
sslBeExpiredSessionsLow = _SslBeExpiredSessionsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 126),
    _SslBeExpiredSessionsLow_Type()
)
sslBeExpiredSessionsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeExpiredSessionsLow.setStatus("obsolete")
_SslBeTotExpiredSessionsHigh_Type = Counter32
_SslBeTotExpiredSessionsHigh_Object = MibScalar
sslBeTotExpiredSessionsHigh = _SslBeTotExpiredSessionsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 127),
    _SslBeTotExpiredSessionsHigh_Type()
)
sslBeTotExpiredSessionsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotExpiredSessionsHigh.setStatus("obsolete")
_SslBeTotSessionMultiplexAttemptsLow_Type = Counter32
_SslBeTotSessionMultiplexAttemptsLow_Object = MibScalar
sslBeTotSessionMultiplexAttemptsLow = _SslBeTotSessionMultiplexAttemptsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 128),
    _SslBeTotSessionMultiplexAttemptsLow_Type()
)
sslBeTotSessionMultiplexAttemptsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotSessionMultiplexAttemptsLow.setStatus("obsolete")
_SslBeTotSessionMultiplexAttemptsHigh_Type = Counter32
_SslBeTotSessionMultiplexAttemptsHigh_Object = MibScalar
sslBeTotSessionMultiplexAttemptsHigh = _SslBeTotSessionMultiplexAttemptsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 129),
    _SslBeTotSessionMultiplexAttemptsHigh_Type()
)
sslBeTotSessionMultiplexAttemptsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotSessionMultiplexAttemptsHigh.setStatus("obsolete")
_SslBeTotSessionMultiplexAttemptSuccessLow_Type = Counter32
_SslBeTotSessionMultiplexAttemptSuccessLow_Object = MibScalar
sslBeTotSessionMultiplexAttemptSuccessLow = _SslBeTotSessionMultiplexAttemptSuccessLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 130),
    _SslBeTotSessionMultiplexAttemptSuccessLow_Type()
)
sslBeTotSessionMultiplexAttemptSuccessLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotSessionMultiplexAttemptSuccessLow.setStatus("obsolete")
_SslBeTotSessionMultiplexAttemptSuccessHigh_Type = Counter32
_SslBeTotSessionMultiplexAttemptSuccessHigh_Object = MibScalar
sslBeTotSessionMultiplexAttemptSuccessHigh = _SslBeTotSessionMultiplexAttemptSuccessHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 131),
    _SslBeTotSessionMultiplexAttemptSuccessHigh_Type()
)
sslBeTotSessionMultiplexAttemptSuccessHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotSessionMultiplexAttemptSuccessHigh.setStatus("obsolete")
_SslBeTotSessionMultiplexAttemptFailsLow_Type = Counter32
_SslBeTotSessionMultiplexAttemptFailsLow_Object = MibScalar
sslBeTotSessionMultiplexAttemptFailsLow = _SslBeTotSessionMultiplexAttemptFailsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 132),
    _SslBeTotSessionMultiplexAttemptFailsLow_Type()
)
sslBeTotSessionMultiplexAttemptFailsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotSessionMultiplexAttemptFailsLow.setStatus("obsolete")
_SslBeTotSessionMultiplexAttemptFailsHigh_Type = Counter32
_SslBeTotSessionMultiplexAttemptFailsHigh_Object = MibScalar
sslBeTotSessionMultiplexAttemptFailsHigh = _SslBeTotSessionMultiplexAttemptFailsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 133),
    _SslBeTotSessionMultiplexAttemptFailsHigh_Type()
)
sslBeTotSessionMultiplexAttemptFailsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotSessionMultiplexAttemptFailsHigh.setStatus("obsolete")
_SslBeMaxMultiplexedSessionsLow_Type = Counter32
_SslBeMaxMultiplexedSessionsLow_Object = MibScalar
sslBeMaxMultiplexedSessionsLow = _SslBeMaxMultiplexedSessionsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 134),
    _SslBeMaxMultiplexedSessionsLow_Type()
)
sslBeMaxMultiplexedSessionsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeMaxMultiplexedSessionsLow.setStatus("obsolete")
_SslBeMaxMultiplexedSessionsHigh_Type = Counter32
_SslBeMaxMultiplexedSessionsHigh_Object = MibScalar
sslBeMaxMultiplexedSessionsHigh = _SslBeMaxMultiplexedSessionsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 135),
    _SslBeMaxMultiplexedSessionsHigh_Type()
)
sslBeMaxMultiplexedSessionsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeMaxMultiplexedSessionsHigh.setStatus("obsolete")
_SslBeSessionsReplacedLow_Type = Counter32
_SslBeSessionsReplacedLow_Object = MibScalar
sslBeSessionsReplacedLow = _SslBeSessionsReplacedLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 136),
    _SslBeSessionsReplacedLow_Type()
)
sslBeSessionsReplacedLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeSessionsReplacedLow.setStatus("obsolete")
_SslBeSessionsReplacedHigh_Type = Counter32
_SslBeSessionsReplacedHigh_Object = MibScalar
sslBeSessionsReplacedHigh = _SslBeSessionsReplacedHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 137),
    _SslBeSessionsReplacedHigh_Type()
)
sslBeSessionsReplacedHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeSessionsReplacedHigh.setStatus("obsolete")
_SslBeTotSSLv3HandshakesLow_Type = Counter32
_SslBeTotSSLv3HandshakesLow_Object = MibScalar
sslBeTotSSLv3HandshakesLow = _SslBeTotSSLv3HandshakesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 138),
    _SslBeTotSSLv3HandshakesLow_Type()
)
sslBeTotSSLv3HandshakesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotSSLv3HandshakesLow.setStatus("obsolete")
_SslBeTotSSLv3HandshakesHigh_Type = Counter32
_SslBeTotSSLv3HandshakesHigh_Object = MibScalar
sslBeTotSSLv3HandshakesHigh = _SslBeTotSSLv3HandshakesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 139),
    _SslBeTotSSLv3HandshakesHigh_Type()
)
sslBeTotSSLv3HandshakesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotSSLv3HandshakesHigh.setStatus("obsolete")
_SslBeTotTLSv1HandshakesLow_Type = Counter32
_SslBeTotTLSv1HandshakesLow_Object = MibScalar
sslBeTotTLSv1HandshakesLow = _SslBeTotTLSv1HandshakesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 140),
    _SslBeTotTLSv1HandshakesLow_Type()
)
sslBeTotTLSv1HandshakesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotTLSv1HandshakesLow.setStatus("obsolete")
_SslBeTotTLSv1HandshakesHigh_Type = Counter32
_SslBeTotTLSv1HandshakesHigh_Object = MibScalar
sslBeTotTLSv1HandshakesHigh = _SslBeTotTLSv1HandshakesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 141),
    _SslBeTotTLSv1HandshakesHigh_Type()
)
sslBeTotTLSv1HandshakesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotTLSv1HandshakesHigh.setStatus("obsolete")
_SslBeTotSSLv3ClientAuthenticationsLow_Type = Counter32
_SslBeTotSSLv3ClientAuthenticationsLow_Object = MibScalar
sslBeTotSSLv3ClientAuthenticationsLow = _SslBeTotSSLv3ClientAuthenticationsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 142),
    _SslBeTotSSLv3ClientAuthenticationsLow_Type()
)
sslBeTotSSLv3ClientAuthenticationsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotSSLv3ClientAuthenticationsLow.setStatus("obsolete")
_SslBeTotSSLv3ClientAuthenticationsHigh_Type = Counter32
_SslBeTotSSLv3ClientAuthenticationsHigh_Object = MibScalar
sslBeTotSSLv3ClientAuthenticationsHigh = _SslBeTotSSLv3ClientAuthenticationsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 143),
    _SslBeTotSSLv3ClientAuthenticationsHigh_Type()
)
sslBeTotSSLv3ClientAuthenticationsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotSSLv3ClientAuthenticationsHigh.setStatus("obsolete")
_SslBeTotTLSv1ClientAuthenticationsLow_Type = Counter32
_SslBeTotTLSv1ClientAuthenticationsLow_Object = MibScalar
sslBeTotTLSv1ClientAuthenticationsLow = _SslBeTotTLSv1ClientAuthenticationsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 144),
    _SslBeTotTLSv1ClientAuthenticationsLow_Type()
)
sslBeTotTLSv1ClientAuthenticationsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotTLSv1ClientAuthenticationsLow.setStatus("obsolete")
_SslBeTotTLSv1ClientAuthenticationsHigh_Type = Counter32
_SslBeTotTLSv1ClientAuthenticationsHigh_Object = MibScalar
sslBeTotTLSv1ClientAuthenticationsHigh = _SslBeTotTLSv1ClientAuthenticationsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 145),
    _SslBeTotTLSv1ClientAuthenticationsHigh_Type()
)
sslBeTotTLSv1ClientAuthenticationsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotTLSv1ClientAuthenticationsHigh.setStatus("obsolete")
_SslBeTotRSA512keyExchangesLow_Type = Counter32
_SslBeTotRSA512keyExchangesLow_Object = MibScalar
sslBeTotRSA512keyExchangesLow = _SslBeTotRSA512keyExchangesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 146),
    _SslBeTotRSA512keyExchangesLow_Type()
)
sslBeTotRSA512keyExchangesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotRSA512keyExchangesLow.setStatus("obsolete")
_SslBeTotRSA512keyExchangesHigh_Type = Counter32
_SslBeTotRSA512keyExchangesHigh_Object = MibScalar
sslBeTotRSA512keyExchangesHigh = _SslBeTotRSA512keyExchangesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 147),
    _SslBeTotRSA512keyExchangesHigh_Type()
)
sslBeTotRSA512keyExchangesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotRSA512keyExchangesHigh.setStatus("obsolete")
_SslBeTotRSA1024keyExchangesLow_Type = Counter32
_SslBeTotRSA1024keyExchangesLow_Object = MibScalar
sslBeTotRSA1024keyExchangesLow = _SslBeTotRSA1024keyExchangesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 148),
    _SslBeTotRSA1024keyExchangesLow_Type()
)
sslBeTotRSA1024keyExchangesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotRSA1024keyExchangesLow.setStatus("obsolete")
_SslBeTotRSA1024keyExchangesHigh_Type = Counter32
_SslBeTotRSA1024keyExchangesHigh_Object = MibScalar
sslBeTotRSA1024keyExchangesHigh = _SslBeTotRSA1024keyExchangesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 149),
    _SslBeTotRSA1024keyExchangesHigh_Type()
)
sslBeTotRSA1024keyExchangesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotRSA1024keyExchangesHigh.setStatus("obsolete")
_SslBeTotRSA2048keyExchangesLow_Type = Counter32
_SslBeTotRSA2048keyExchangesLow_Object = MibScalar
sslBeTotRSA2048keyExchangesLow = _SslBeTotRSA2048keyExchangesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 150),
    _SslBeTotRSA2048keyExchangesLow_Type()
)
sslBeTotRSA2048keyExchangesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotRSA2048keyExchangesLow.setStatus("obsolete")
_SslBeTotRSA2048keyExchangesHigh_Type = Counter32
_SslBeTotRSA2048keyExchangesHigh_Object = MibScalar
sslBeTotRSA2048keyExchangesHigh = _SslBeTotRSA2048keyExchangesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 151),
    _SslBeTotRSA2048keyExchangesHigh_Type()
)
sslBeTotRSA2048keyExchangesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotRSA2048keyExchangesHigh.setStatus("obsolete")
_SslBeTotDH512keyExchangesLow_Type = Counter32
_SslBeTotDH512keyExchangesLow_Object = MibScalar
sslBeTotDH512keyExchangesLow = _SslBeTotDH512keyExchangesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 152),
    _SslBeTotDH512keyExchangesLow_Type()
)
sslBeTotDH512keyExchangesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotDH512keyExchangesLow.setStatus("obsolete")
_SslBeTotDH512keyExchangesHigh_Type = Counter32
_SslBeTotDH512keyExchangesHigh_Object = MibScalar
sslBeTotDH512keyExchangesHigh = _SslBeTotDH512keyExchangesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 153),
    _SslBeTotDH512keyExchangesHigh_Type()
)
sslBeTotDH512keyExchangesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotDH512keyExchangesHigh.setStatus("obsolete")
_SslBeTotDH1024keyExchangesLow_Type = Counter32
_SslBeTotDH1024keyExchangesLow_Object = MibScalar
sslBeTotDH1024keyExchangesLow = _SslBeTotDH1024keyExchangesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 154),
    _SslBeTotDH1024keyExchangesLow_Type()
)
sslBeTotDH1024keyExchangesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotDH1024keyExchangesLow.setStatus("obsolete")
_SslBeTotDH1024keyExchangesHigh_Type = Counter32
_SslBeTotDH1024keyExchangesHigh_Object = MibScalar
sslBeTotDH1024keyExchangesHigh = _SslBeTotDH1024keyExchangesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 155),
    _SslBeTotDH1024keyExchangesHigh_Type()
)
sslBeTotDH1024keyExchangesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotDH1024keyExchangesHigh.setStatus("obsolete")
_SslBeTotDH2048keyExchangesLow_Type = Counter32
_SslBeTotDH2048keyExchangesLow_Object = MibScalar
sslBeTotDH2048keyExchangesLow = _SslBeTotDH2048keyExchangesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 156),
    _SslBeTotDH2048keyExchangesLow_Type()
)
sslBeTotDH2048keyExchangesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotDH2048keyExchangesLow.setStatus("obsolete")
_SslBeTotDH2048keyExchangesHigh_Type = Counter32
_SslBeTotDH2048keyExchangesHigh_Object = MibScalar
sslBeTotDH2048keyExchangesHigh = _SslBeTotDH2048keyExchangesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 157),
    _SslBeTotDH2048keyExchangesHigh_Type()
)
sslBeTotDH2048keyExchangesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotDH2048keyExchangesHigh.setStatus("obsolete")
_SslBeTotRSAAuthorizationsLow_Type = Counter32
_SslBeTotRSAAuthorizationsLow_Object = MibScalar
sslBeTotRSAAuthorizationsLow = _SslBeTotRSAAuthorizationsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 158),
    _SslBeTotRSAAuthorizationsLow_Type()
)
sslBeTotRSAAuthorizationsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotRSAAuthorizationsLow.setStatus("obsolete")
_SslBeTotRSAAuthorizationsHigh_Type = Counter32
_SslBeTotRSAAuthorizationsHigh_Object = MibScalar
sslBeTotRSAAuthorizationsHigh = _SslBeTotRSAAuthorizationsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 159),
    _SslBeTotRSAAuthorizationsHigh_Type()
)
sslBeTotRSAAuthorizationsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotRSAAuthorizationsHigh.setStatus("obsolete")
_SslBeTotDHAuthorizationsLow_Type = Counter32
_SslBeTotDHAuthorizationsLow_Object = MibScalar
sslBeTotDHAuthorizationsLow = _SslBeTotDHAuthorizationsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 160),
    _SslBeTotDHAuthorizationsLow_Type()
)
sslBeTotDHAuthorizationsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotDHAuthorizationsLow.setStatus("obsolete")
_SslBeTotDHAuthorizationsHigh_Type = Counter32
_SslBeTotDHAuthorizationsHigh_Object = MibScalar
sslBeTotDHAuthorizationsHigh = _SslBeTotDHAuthorizationsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 161),
    _SslBeTotDHAuthorizationsHigh_Type()
)
sslBeTotDHAuthorizationsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotDHAuthorizationsHigh.setStatus("obsolete")
_SslBeTotDSSAuthorizationsLow_Type = Counter32
_SslBeTotDSSAuthorizationsLow_Object = MibScalar
sslBeTotDSSAuthorizationsLow = _SslBeTotDSSAuthorizationsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 162),
    _SslBeTotDSSAuthorizationsLow_Type()
)
sslBeTotDSSAuthorizationsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotDSSAuthorizationsLow.setStatus("obsolete")
_SslBeTotDSSAuthorizationsHigh_Type = Counter32
_SslBeTotDSSAuthorizationsHigh_Object = MibScalar
sslBeTotDSSAuthorizationsHigh = _SslBeTotDSSAuthorizationsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 163),
    _SslBeTotDSSAuthorizationsHigh_Type()
)
sslBeTotDSSAuthorizationsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotDSSAuthorizationsHigh.setStatus("obsolete")
_SslBeTotNULLAuthorizationsLow_Type = Counter32
_SslBeTotNULLAuthorizationsLow_Object = MibScalar
sslBeTotNULLAuthorizationsLow = _SslBeTotNULLAuthorizationsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 164),
    _SslBeTotNULLAuthorizationsLow_Type()
)
sslBeTotNULLAuthorizationsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotNULLAuthorizationsLow.setStatus("obsolete")
_SslBeTotNULLAuthorizationsHigh_Type = Counter32
_SslBeTotNULLAuthorizationsHigh_Object = MibScalar
sslBeTotNULLAuthorizationsHigh = _SslBeTotNULLAuthorizationsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 165),
    _SslBeTotNULLAuthorizationsHigh_Type()
)
sslBeTotNULLAuthorizationsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotNULLAuthorizationsHigh.setStatus("obsolete")
_SslBeTot40BitRC4CiphersLow_Type = Counter32
_SslBeTot40BitRC4CiphersLow_Object = MibScalar
sslBeTot40BitRC4CiphersLow = _SslBeTot40BitRC4CiphersLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 166),
    _SslBeTot40BitRC4CiphersLow_Type()
)
sslBeTot40BitRC4CiphersLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot40BitRC4CiphersLow.setStatus("obsolete")
_SslBeTot40BitRC4CiphersHigh_Type = Counter32
_SslBeTot40BitRC4CiphersHigh_Object = MibScalar
sslBeTot40BitRC4CiphersHigh = _SslBeTot40BitRC4CiphersHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 167),
    _SslBeTot40BitRC4CiphersHigh_Type()
)
sslBeTot40BitRC4CiphersHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot40BitRC4CiphersHigh.setStatus("obsolete")
_SslBeTot56BitRC4CiphersLow_Type = Counter32
_SslBeTot56BitRC4CiphersLow_Object = MibScalar
sslBeTot56BitRC4CiphersLow = _SslBeTot56BitRC4CiphersLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 168),
    _SslBeTot56BitRC4CiphersLow_Type()
)
sslBeTot56BitRC4CiphersLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot56BitRC4CiphersLow.setStatus("obsolete")
_SslBeTot56BitRC4CiphersHigh_Type = Counter32
_SslBeTot56BitRC4CiphersHigh_Object = MibScalar
sslBeTot56BitRC4CiphersHigh = _SslBeTot56BitRC4CiphersHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 169),
    _SslBeTot56BitRC4CiphersHigh_Type()
)
sslBeTot56BitRC4CiphersHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot56BitRC4CiphersHigh.setStatus("obsolete")
_SslBeTot64BitRC4CiphersLow_Type = Counter32
_SslBeTot64BitRC4CiphersLow_Object = MibScalar
sslBeTot64BitRC4CiphersLow = _SslBeTot64BitRC4CiphersLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 170),
    _SslBeTot64BitRC4CiphersLow_Type()
)
sslBeTot64BitRC4CiphersLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot64BitRC4CiphersLow.setStatus("obsolete")
_SslBeTot64BitRC4CiphersHigh_Type = Counter32
_SslBeTot64BitRC4CiphersHigh_Object = MibScalar
sslBeTot64BitRC4CiphersHigh = _SslBeTot64BitRC4CiphersHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 171),
    _SslBeTot64BitRC4CiphersHigh_Type()
)
sslBeTot64BitRC4CiphersHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot64BitRC4CiphersHigh.setStatus("obsolete")
_SslBeTot128BitRC4CiphersLow_Type = Counter32
_SslBeTot128BitRC4CiphersLow_Object = MibScalar
sslBeTot128BitRC4CiphersLow = _SslBeTot128BitRC4CiphersLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 172),
    _SslBeTot128BitRC4CiphersLow_Type()
)
sslBeTot128BitRC4CiphersLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot128BitRC4CiphersLow.setStatus("obsolete")
_SslBeTot128BitRC4CiphersHigh_Type = Counter32
_SslBeTot128BitRC4CiphersHigh_Object = MibScalar
sslBeTot128BitRC4CiphersHigh = _SslBeTot128BitRC4CiphersHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 173),
    _SslBeTot128BitRC4CiphersHigh_Type()
)
sslBeTot128BitRC4CiphersHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot128BitRC4CiphersHigh.setStatus("obsolete")
_SslBeTot40BitDESCiphersLow_Type = Counter32
_SslBeTot40BitDESCiphersLow_Object = MibScalar
sslBeTot40BitDESCiphersLow = _SslBeTot40BitDESCiphersLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 174),
    _SslBeTot40BitDESCiphersLow_Type()
)
sslBeTot40BitDESCiphersLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot40BitDESCiphersLow.setStatus("obsolete")
_SslBeTot40BitDESCiphersHigh_Type = Counter32
_SslBeTot40BitDESCiphersHigh_Object = MibScalar
sslBeTot40BitDESCiphersHigh = _SslBeTot40BitDESCiphersHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 175),
    _SslBeTot40BitDESCiphersHigh_Type()
)
sslBeTot40BitDESCiphersHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot40BitDESCiphersHigh.setStatus("obsolete")
_SslBeTot56BitDESCiphersLow_Type = Counter32
_SslBeTot56BitDESCiphersLow_Object = MibScalar
sslBeTot56BitDESCiphersLow = _SslBeTot56BitDESCiphersLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 176),
    _SslBeTot56BitDESCiphersLow_Type()
)
sslBeTot56BitDESCiphersLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot56BitDESCiphersLow.setStatus("obsolete")
_SslBeTot56BitDESCiphersHigh_Type = Counter32
_SslBeTot56BitDESCiphersHigh_Object = MibScalar
sslBeTot56BitDESCiphersHigh = _SslBeTot56BitDESCiphersHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 177),
    _SslBeTot56BitDESCiphersHigh_Type()
)
sslBeTot56BitDESCiphersHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot56BitDESCiphersHigh.setStatus("obsolete")
_SslBeTot168Bit3DESCiphersLow_Type = Counter32
_SslBeTot168Bit3DESCiphersLow_Object = MibScalar
sslBeTot168Bit3DESCiphersLow = _SslBeTot168Bit3DESCiphersLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 178),
    _SslBeTot168Bit3DESCiphersLow_Type()
)
sslBeTot168Bit3DESCiphersLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot168Bit3DESCiphersLow.setStatus("obsolete")
_SslBeTot168Bit3DESCiphersHigh_Type = Counter32
_SslBeTot168Bit3DESCiphersHigh_Object = MibScalar
sslBeTot168Bit3DESCiphersHigh = _SslBeTot168Bit3DESCiphersHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 179),
    _SslBeTot168Bit3DESCiphersHigh_Type()
)
sslBeTot168Bit3DESCiphersHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot168Bit3DESCiphersHigh.setStatus("obsolete")
_SslBeTot40BitRC2CiphersLow_Type = Counter32
_SslBeTot40BitRC2CiphersLow_Object = MibScalar
sslBeTot40BitRC2CiphersLow = _SslBeTot40BitRC2CiphersLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 180),
    _SslBeTot40BitRC2CiphersLow_Type()
)
sslBeTot40BitRC2CiphersLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot40BitRC2CiphersLow.setStatus("obsolete")
_SslBeTot40BitRC2CiphersHigh_Type = Counter32
_SslBeTot40BitRC2CiphersHigh_Object = MibScalar
sslBeTot40BitRC2CiphersHigh = _SslBeTot40BitRC2CiphersHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 181),
    _SslBeTot40BitRC2CiphersHigh_Type()
)
sslBeTot40BitRC2CiphersHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot40BitRC2CiphersHigh.setStatus("obsolete")
_SslBeTot56BitRC2CiphersLow_Type = Counter32
_SslBeTot56BitRC2CiphersLow_Object = MibScalar
sslBeTot56BitRC2CiphersLow = _SslBeTot56BitRC2CiphersLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 182),
    _SslBeTot56BitRC2CiphersLow_Type()
)
sslBeTot56BitRC2CiphersLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot56BitRC2CiphersLow.setStatus("obsolete")
_SslBeTot56BitRC2CiphersHigh_Type = Counter32
_SslBeTot56BitRC2CiphersHigh_Object = MibScalar
sslBeTot56BitRC2CiphersHigh = _SslBeTot56BitRC2CiphersHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 183),
    _SslBeTot56BitRC2CiphersHigh_Type()
)
sslBeTot56BitRC2CiphersHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot56BitRC2CiphersHigh.setStatus("obsolete")
_SslBeTot128BitRC2CiphersLow_Type = Counter32
_SslBeTot128BitRC2CiphersLow_Object = MibScalar
sslBeTot128BitRC2CiphersLow = _SslBeTot128BitRC2CiphersLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 184),
    _SslBeTot128BitRC2CiphersLow_Type()
)
sslBeTot128BitRC2CiphersLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot128BitRC2CiphersLow.setStatus("obsolete")
_SslBeTot128BitRC2CiphersHigh_Type = Counter32
_SslBeTot128BitRC2CiphersHigh_Object = MibScalar
sslBeTot128BitRC2CiphersHigh = _SslBeTot128BitRC2CiphersHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 185),
    _SslBeTot128BitRC2CiphersHigh_Type()
)
sslBeTot128BitRC2CiphersHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot128BitRC2CiphersHigh.setStatus("obsolete")
_SslBeTot128BitIDEACiphersLow_Type = Counter32
_SslBeTot128BitIDEACiphersLow_Object = MibScalar
sslBeTot128BitIDEACiphersLow = _SslBeTot128BitIDEACiphersLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 186),
    _SslBeTot128BitIDEACiphersLow_Type()
)
sslBeTot128BitIDEACiphersLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot128BitIDEACiphersLow.setStatus("obsolete")
_SslBeTot128BitIDEACiphersHigh_Type = Counter32
_SslBeTot128BitIDEACiphersHigh_Object = MibScalar
sslBeTot128BitIDEACiphersHigh = _SslBeTot128BitIDEACiphersHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 187),
    _SslBeTot128BitIDEACiphersHigh_Type()
)
sslBeTot128BitIDEACiphersHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot128BitIDEACiphersHigh.setStatus("obsolete")
_SslBeTotNULLCiphersLow_Type = Counter32
_SslBeTotNULLCiphersLow_Object = MibScalar
sslBeTotNULLCiphersLow = _SslBeTotNULLCiphersLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 188),
    _SslBeTotNULLCiphersLow_Type()
)
sslBeTotNULLCiphersLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotNULLCiphersLow.setStatus("obsolete")
_SslBeTotNULLCiphersHigh_Type = Counter32
_SslBeTotNULLCiphersHigh_Object = MibScalar
sslBeTotNULLCiphersHigh = _SslBeTotNULLCiphersHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 189),
    _SslBeTotNULLCiphersHigh_Type()
)
sslBeTotNULLCiphersHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotNULLCiphersHigh.setStatus("obsolete")
_SslBeTotMD5MacLow_Type = Counter32
_SslBeTotMD5MacLow_Object = MibScalar
sslBeTotMD5MacLow = _SslBeTotMD5MacLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 190),
    _SslBeTotMD5MacLow_Type()
)
sslBeTotMD5MacLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotMD5MacLow.setStatus("obsolete")
_SslBeTotMD5MacHigh_Type = Counter32
_SslBeTotMD5MacHigh_Object = MibScalar
sslBeTotMD5MacHigh = _SslBeTotMD5MacHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 191),
    _SslBeTotMD5MacHigh_Type()
)
sslBeTotMD5MacHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotMD5MacHigh.setStatus("obsolete")
_SslBeTotSHAMacLow_Type = Counter32
_SslBeTotSHAMacLow_Object = MibScalar
sslBeTotSHAMacLow = _SslBeTotSHAMacLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 192),
    _SslBeTotSHAMacLow_Type()
)
sslBeTotSHAMacLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotSHAMacLow.setStatus("obsolete")
_SslBeTotSHAMacHigh_Type = Counter32
_SslBeTotSHAMacHigh_Object = MibScalar
sslBeTotSHAMacHigh = _SslBeTotSHAMacHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 193),
    _SslBeTotSHAMacHigh_Type()
)
sslBeTotSHAMacHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotSHAMacHigh.setStatus("obsolete")
_SslTotTransactions_Type = Counter64
_SslTotTransactions_Object = MibScalar
sslTotTransactions = _SslTotTransactions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 200),
    _SslTotTransactions_Type()
)
sslTotTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotTransactions.setStatus("current")
_SslTotSSLv2Transactions_Type = Counter64
_SslTotSSLv2Transactions_Object = MibScalar
sslTotSSLv2Transactions = _SslTotSSLv2Transactions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 201),
    _SslTotSSLv2Transactions_Type()
)
sslTotSSLv2Transactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSSLv2Transactions.setStatus("current")
_SslTotSSLv3Transactions_Type = Counter64
_SslTotSSLv3Transactions_Object = MibScalar
sslTotSSLv3Transactions = _SslTotSSLv3Transactions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 202),
    _SslTotSSLv3Transactions_Type()
)
sslTotSSLv3Transactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSSLv3Transactions.setStatus("current")
_SslTotTLSv1Transactions_Type = Counter64
_SslTotTLSv1Transactions_Object = MibScalar
sslTotTLSv1Transactions = _SslTotTLSv1Transactions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 203),
    _SslTotTLSv1Transactions_Type()
)
sslTotTLSv1Transactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotTLSv1Transactions.setStatus("current")
_SslTotSessions_Type = Counter64
_SslTotSessions_Object = MibScalar
sslTotSessions = _SslTotSessions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 204),
    _SslTotSessions_Type()
)
sslTotSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSessions.setStatus("current")
_SslTotSSLv2Sessions_Type = Counter64
_SslTotSSLv2Sessions_Object = MibScalar
sslTotSSLv2Sessions = _SslTotSSLv2Sessions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 205),
    _SslTotSSLv2Sessions_Type()
)
sslTotSSLv2Sessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSSLv2Sessions.setStatus("current")
_SslTotSSLv3Sessions_Type = Counter64
_SslTotSSLv3Sessions_Object = MibScalar
sslTotSSLv3Sessions = _SslTotSSLv3Sessions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 206),
    _SslTotSSLv3Sessions_Type()
)
sslTotSSLv3Sessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSSLv3Sessions.setStatus("current")
_SslTotTLSv1Sessions_Type = Counter64
_SslTotTLSv1Sessions_Object = MibScalar
sslTotTLSv1Sessions = _SslTotTLSv1Sessions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 207),
    _SslTotTLSv1Sessions_Type()
)
sslTotTLSv1Sessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotTLSv1Sessions.setStatus("current")
_SslTotExpiredSessions_Type = Counter64
_SslTotExpiredSessions_Object = MibScalar
sslTotExpiredSessions = _SslTotExpiredSessions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 208),
    _SslTotExpiredSessions_Type()
)
sslTotExpiredSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotExpiredSessions.setStatus("current")
_SslTotNewSessions_Type = Counter64
_SslTotNewSessions_Object = MibScalar
sslTotNewSessions = _SslTotNewSessions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 209),
    _SslTotNewSessions_Type()
)
sslTotNewSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotNewSessions.setStatus("current")
_SslTotSessionHits_Type = Counter64
_SslTotSessionHits_Object = MibScalar
sslTotSessionHits = _SslTotSessionHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 210),
    _SslTotSessionHits_Type()
)
sslTotSessionHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSessionHits.setStatus("current")
_SslTotSessionMiss_Type = Counter64
_SslTotSessionMiss_Object = MibScalar
sslTotSessionMiss = _SslTotSessionMiss_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 211),
    _SslTotSessionMiss_Type()
)
sslTotSessionMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSessionMiss.setStatus("current")
_SslTotRenegSessions_Type = Counter64
_SslTotRenegSessions_Object = MibScalar
sslTotRenegSessions = _SslTotRenegSessions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 212),
    _SslTotRenegSessions_Type()
)
sslTotRenegSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotRenegSessions.setStatus("current")
_SslTotSSLv3RenegSessions_Type = Counter64
_SslTotSSLv3RenegSessions_Object = MibScalar
sslTotSSLv3RenegSessions = _SslTotSSLv3RenegSessions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 213),
    _SslTotSSLv3RenegSessions_Type()
)
sslTotSSLv3RenegSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSSLv3RenegSessions.setStatus("current")
_SslTotTLSv1RenegSessions_Type = Counter64
_SslTotTLSv1RenegSessions_Object = MibScalar
sslTotTLSv1RenegSessions = _SslTotTLSv1RenegSessions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 214),
    _SslTotTLSv1RenegSessions_Type()
)
sslTotTLSv1RenegSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotTLSv1RenegSessions.setStatus("current")
_SslTotSSLv2Handshakes_Type = Counter64
_SslTotSSLv2Handshakes_Object = MibScalar
sslTotSSLv2Handshakes = _SslTotSSLv2Handshakes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 215),
    _SslTotSSLv2Handshakes_Type()
)
sslTotSSLv2Handshakes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSSLv2Handshakes.setStatus("current")
_SslTotSSLv3Handshakes_Type = Counter64
_SslTotSSLv3Handshakes_Object = MibScalar
sslTotSSLv3Handshakes = _SslTotSSLv3Handshakes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 216),
    _SslTotSSLv3Handshakes_Type()
)
sslTotSSLv3Handshakes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSSLv3Handshakes.setStatus("current")
_SslTotTLSv1Handshakes_Type = Counter64
_SslTotTLSv1Handshakes_Object = MibScalar
sslTotTLSv1Handshakes = _SslTotTLSv1Handshakes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 217),
    _SslTotTLSv1Handshakes_Type()
)
sslTotTLSv1Handshakes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotTLSv1Handshakes.setStatus("current")
_SslTotSSLv2ClientAuthentications_Type = Counter64
_SslTotSSLv2ClientAuthentications_Object = MibScalar
sslTotSSLv2ClientAuthentications = _SslTotSSLv2ClientAuthentications_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 218),
    _SslTotSSLv2ClientAuthentications_Type()
)
sslTotSSLv2ClientAuthentications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSSLv2ClientAuthentications.setStatus("current")
_SslTotSSLv3ClientAuthentications_Type = Counter64
_SslTotSSLv3ClientAuthentications_Object = MibScalar
sslTotSSLv3ClientAuthentications = _SslTotSSLv3ClientAuthentications_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 219),
    _SslTotSSLv3ClientAuthentications_Type()
)
sslTotSSLv3ClientAuthentications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSSLv3ClientAuthentications.setStatus("current")
_SslTotTLSv1ClientAuthentications_Type = Counter64
_SslTotTLSv1ClientAuthentications_Object = MibScalar
sslTotTLSv1ClientAuthentications = _SslTotTLSv1ClientAuthentications_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 220),
    _SslTotTLSv1ClientAuthentications_Type()
)
sslTotTLSv1ClientAuthentications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotTLSv1ClientAuthentications.setStatus("current")
_SslTotRSA512keyExchanges_Type = Counter64
_SslTotRSA512keyExchanges_Object = MibScalar
sslTotRSA512keyExchanges = _SslTotRSA512keyExchanges_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 221),
    _SslTotRSA512keyExchanges_Type()
)
sslTotRSA512keyExchanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotRSA512keyExchanges.setStatus("current")
_SslTotRSA1024keyExchanges_Type = Counter64
_SslTotRSA1024keyExchanges_Object = MibScalar
sslTotRSA1024keyExchanges = _SslTotRSA1024keyExchanges_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 222),
    _SslTotRSA1024keyExchanges_Type()
)
sslTotRSA1024keyExchanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotRSA1024keyExchanges.setStatus("current")
_SslTotRSA2048keyExchanges_Type = Counter64
_SslTotRSA2048keyExchanges_Object = MibScalar
sslTotRSA2048keyExchanges = _SslTotRSA2048keyExchanges_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 223),
    _SslTotRSA2048keyExchanges_Type()
)
sslTotRSA2048keyExchanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotRSA2048keyExchanges.setStatus("current")
_SslTotDH512keyExchanges_Type = Counter64
_SslTotDH512keyExchanges_Object = MibScalar
sslTotDH512keyExchanges = _SslTotDH512keyExchanges_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 224),
    _SslTotDH512keyExchanges_Type()
)
sslTotDH512keyExchanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotDH512keyExchanges.setStatus("current")
_SslTotDH1024keyExchanges_Type = Counter64
_SslTotDH1024keyExchanges_Object = MibScalar
sslTotDH1024keyExchanges = _SslTotDH1024keyExchanges_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 225),
    _SslTotDH1024keyExchanges_Type()
)
sslTotDH1024keyExchanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotDH1024keyExchanges.setStatus("current")
_SslTotDH2048keyExchanges_Type = Counter64
_SslTotDH2048keyExchanges_Object = MibScalar
sslTotDH2048keyExchanges = _SslTotDH2048keyExchanges_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 226),
    _SslTotDH2048keyExchanges_Type()
)
sslTotDH2048keyExchanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotDH2048keyExchanges.setStatus("current")
_SslTotRSAAuthorizations_Type = Counter64
_SslTotRSAAuthorizations_Object = MibScalar
sslTotRSAAuthorizations = _SslTotRSAAuthorizations_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 227),
    _SslTotRSAAuthorizations_Type()
)
sslTotRSAAuthorizations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotRSAAuthorizations.setStatus("current")
_SslTotDHAuthorizations_Type = Counter64
_SslTotDHAuthorizations_Object = MibScalar
sslTotDHAuthorizations = _SslTotDHAuthorizations_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 228),
    _SslTotDHAuthorizations_Type()
)
sslTotDHAuthorizations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotDHAuthorizations.setStatus("current")
_SslTotDSSAuthorizations_Type = Counter64
_SslTotDSSAuthorizations_Object = MibScalar
sslTotDSSAuthorizations = _SslTotDSSAuthorizations_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 229),
    _SslTotDSSAuthorizations_Type()
)
sslTotDSSAuthorizations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotDSSAuthorizations.setStatus("current")
_SslTotNULLAuthorizations_Type = Counter64
_SslTotNULLAuthorizations_Object = MibScalar
sslTotNULLAuthorizations = _SslTotNULLAuthorizations_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 230),
    _SslTotNULLAuthorizations_Type()
)
sslTotNULLAuthorizations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotNULLAuthorizations.setStatus("current")
_SslTot40BitRC4Ciphers_Type = Counter64
_SslTot40BitRC4Ciphers_Object = MibScalar
sslTot40BitRC4Ciphers = _SslTot40BitRC4Ciphers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 231),
    _SslTot40BitRC4Ciphers_Type()
)
sslTot40BitRC4Ciphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot40BitRC4Ciphers.setStatus("current")
_SslTot56BitRC4Ciphers_Type = Counter64
_SslTot56BitRC4Ciphers_Object = MibScalar
sslTot56BitRC4Ciphers = _SslTot56BitRC4Ciphers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 232),
    _SslTot56BitRC4Ciphers_Type()
)
sslTot56BitRC4Ciphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot56BitRC4Ciphers.setStatus("current")
_SslTot64BitRC4Ciphers_Type = Counter64
_SslTot64BitRC4Ciphers_Object = MibScalar
sslTot64BitRC4Ciphers = _SslTot64BitRC4Ciphers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 233),
    _SslTot64BitRC4Ciphers_Type()
)
sslTot64BitRC4Ciphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot64BitRC4Ciphers.setStatus("current")
_SslTot128BitRC4Ciphers_Type = Counter64
_SslTot128BitRC4Ciphers_Object = MibScalar
sslTot128BitRC4Ciphers = _SslTot128BitRC4Ciphers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 234),
    _SslTot128BitRC4Ciphers_Type()
)
sslTot128BitRC4Ciphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot128BitRC4Ciphers.setStatus("current")
_SslTot40BitDESCiphers_Type = Counter64
_SslTot40BitDESCiphers_Object = MibScalar
sslTot40BitDESCiphers = _SslTot40BitDESCiphers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 235),
    _SslTot40BitDESCiphers_Type()
)
sslTot40BitDESCiphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot40BitDESCiphers.setStatus("current")
_SslTot56BitDESCiphers_Type = Counter64
_SslTot56BitDESCiphers_Object = MibScalar
sslTot56BitDESCiphers = _SslTot56BitDESCiphers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 236),
    _SslTot56BitDESCiphers_Type()
)
sslTot56BitDESCiphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot56BitDESCiphers.setStatus("current")
_SslTot168Bit3DESCiphers_Type = Counter64
_SslTot168Bit3DESCiphers_Object = MibScalar
sslTot168Bit3DESCiphers = _SslTot168Bit3DESCiphers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 237),
    _SslTot168Bit3DESCiphers_Type()
)
sslTot168Bit3DESCiphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot168Bit3DESCiphers.setStatus("current")
_SslTot40BitRC2Ciphers_Type = Counter64
_SslTot40BitRC2Ciphers_Object = MibScalar
sslTot40BitRC2Ciphers = _SslTot40BitRC2Ciphers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 238),
    _SslTot40BitRC2Ciphers_Type()
)
sslTot40BitRC2Ciphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot40BitRC2Ciphers.setStatus("current")
_SslTot56BitRC2Ciphers_Type = Counter64
_SslTot56BitRC2Ciphers_Object = MibScalar
sslTot56BitRC2Ciphers = _SslTot56BitRC2Ciphers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 239),
    _SslTot56BitRC2Ciphers_Type()
)
sslTot56BitRC2Ciphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot56BitRC2Ciphers.setStatus("current")
_SslTot128BitRC2Ciphers_Type = Counter64
_SslTot128BitRC2Ciphers_Object = MibScalar
sslTot128BitRC2Ciphers = _SslTot128BitRC2Ciphers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 240),
    _SslTot128BitRC2Ciphers_Type()
)
sslTot128BitRC2Ciphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot128BitRC2Ciphers.setStatus("current")
_SslTot128BitIDEACiphers_Type = Counter64
_SslTot128BitIDEACiphers_Object = MibScalar
sslTot128BitIDEACiphers = _SslTot128BitIDEACiphers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 241),
    _SslTot128BitIDEACiphers_Type()
)
sslTot128BitIDEACiphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTot128BitIDEACiphers.setStatus("current")
_SslTotNULLCiphers_Type = Counter64
_SslTotNULLCiphers_Object = MibScalar
sslTotNULLCiphers = _SslTotNULLCiphers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 242),
    _SslTotNULLCiphers_Type()
)
sslTotNULLCiphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotNULLCiphers.setStatus("current")
_SslTotMD5Mac_Type = Counter64
_SslTotMD5Mac_Object = MibScalar
sslTotMD5Mac = _SslTotMD5Mac_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 243),
    _SslTotMD5Mac_Type()
)
sslTotMD5Mac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotMD5Mac.setStatus("current")
_SslTotSHAMac_Type = Counter64
_SslTotSHAMac_Object = MibScalar
sslTotSHAMac = _SslTotSHAMac_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 244),
    _SslTotSHAMac_Type()
)
sslTotSHAMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSHAMac.setStatus("current")
_SslTotOffloadBulkDES_Type = Counter64
_SslTotOffloadBulkDES_Object = MibScalar
sslTotOffloadBulkDES = _SslTotOffloadBulkDES_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 245),
    _SslTotOffloadBulkDES_Type()
)
sslTotOffloadBulkDES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotOffloadBulkDES.setStatus("current")
_SslTotOffloadRSAKeyExchanges_Type = Counter64
_SslTotOffloadRSAKeyExchanges_Object = MibScalar
sslTotOffloadRSAKeyExchanges = _SslTotOffloadRSAKeyExchanges_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 246),
    _SslTotOffloadRSAKeyExchanges_Type()
)
sslTotOffloadRSAKeyExchanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotOffloadRSAKeyExchanges.setStatus("current")
_SslTotOffloadDHKeyExchanges_Type = Counter64
_SslTotOffloadDHKeyExchanges_Object = MibScalar
sslTotOffloadDHKeyExchanges = _SslTotOffloadDHKeyExchanges_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 247),
    _SslTotOffloadDHKeyExchanges_Type()
)
sslTotOffloadDHKeyExchanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotOffloadDHKeyExchanges.setStatus("current")
_SslTotOffloadSignRSA_Type = Counter64
_SslTotOffloadSignRSA_Object = MibScalar
sslTotOffloadSignRSA = _SslTotOffloadSignRSA_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 248),
    _SslTotOffloadSignRSA_Type()
)
sslTotOffloadSignRSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotOffloadSignRSA.setStatus("current")
_SslBeTotSessions_Type = Counter64
_SslBeTotSessions_Object = MibScalar
sslBeTotSessions = _SslBeTotSessions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 260),
    _SslBeTotSessions_Type()
)
sslBeTotSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotSessions.setStatus("current")
_SslBeTotSSLv3Sessions_Type = Counter64
_SslBeTotSSLv3Sessions_Object = MibScalar
sslBeTotSSLv3Sessions = _SslBeTotSSLv3Sessions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 261),
    _SslBeTotSSLv3Sessions_Type()
)
sslBeTotSSLv3Sessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotSSLv3Sessions.setStatus("current")
_SslBeTotTLSv1Sessions_Type = Counter64
_SslBeTotTLSv1Sessions_Object = MibScalar
sslBeTotTLSv1Sessions = _SslBeTotTLSv1Sessions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 262),
    _SslBeTotTLSv1Sessions_Type()
)
sslBeTotTLSv1Sessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotTLSv1Sessions.setStatus("current")
_SslBeExpiredSessions_Type = Counter64
_SslBeExpiredSessions_Object = MibScalar
sslBeExpiredSessions = _SslBeExpiredSessions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 263),
    _SslBeExpiredSessions_Type()
)
sslBeExpiredSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeExpiredSessions.setStatus("current")
_SslBeTotSessionMultiplexAttempts_Type = Counter64
_SslBeTotSessionMultiplexAttempts_Object = MibScalar
sslBeTotSessionMultiplexAttempts = _SslBeTotSessionMultiplexAttempts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 264),
    _SslBeTotSessionMultiplexAttempts_Type()
)
sslBeTotSessionMultiplexAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotSessionMultiplexAttempts.setStatus("current")
_SslBeTotSessionMultiplexAttemptSuccess_Type = Counter64
_SslBeTotSessionMultiplexAttemptSuccess_Object = MibScalar
sslBeTotSessionMultiplexAttemptSuccess = _SslBeTotSessionMultiplexAttemptSuccess_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 265),
    _SslBeTotSessionMultiplexAttemptSuccess_Type()
)
sslBeTotSessionMultiplexAttemptSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotSessionMultiplexAttemptSuccess.setStatus("current")
_SslBeTotSessionMultiplexAttemptFails_Type = Counter64
_SslBeTotSessionMultiplexAttemptFails_Object = MibScalar
sslBeTotSessionMultiplexAttemptFails = _SslBeTotSessionMultiplexAttemptFails_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 266),
    _SslBeTotSessionMultiplexAttemptFails_Type()
)
sslBeTotSessionMultiplexAttemptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotSessionMultiplexAttemptFails.setStatus("current")
_SslBeMaxMultiplexedSessions_Type = Counter64
_SslBeMaxMultiplexedSessions_Object = MibScalar
sslBeMaxMultiplexedSessions = _SslBeMaxMultiplexedSessions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 267),
    _SslBeMaxMultiplexedSessions_Type()
)
sslBeMaxMultiplexedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeMaxMultiplexedSessions.setStatus("current")
_SslBeTotSSLv3Handshakes_Type = Counter64
_SslBeTotSSLv3Handshakes_Object = MibScalar
sslBeTotSSLv3Handshakes = _SslBeTotSSLv3Handshakes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 268),
    _SslBeTotSSLv3Handshakes_Type()
)
sslBeTotSSLv3Handshakes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotSSLv3Handshakes.setStatus("current")
_SslBeTotTLSv1Handshakes_Type = Counter64
_SslBeTotTLSv1Handshakes_Object = MibScalar
sslBeTotTLSv1Handshakes = _SslBeTotTLSv1Handshakes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 269),
    _SslBeTotTLSv1Handshakes_Type()
)
sslBeTotTLSv1Handshakes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotTLSv1Handshakes.setStatus("current")
_SslBeTotSSLv3ClientAuthentications_Type = Counter64
_SslBeTotSSLv3ClientAuthentications_Object = MibScalar
sslBeTotSSLv3ClientAuthentications = _SslBeTotSSLv3ClientAuthentications_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 270),
    _SslBeTotSSLv3ClientAuthentications_Type()
)
sslBeTotSSLv3ClientAuthentications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotSSLv3ClientAuthentications.setStatus("current")
_SslBeTotTLSv1ClientAuthentications_Type = Counter64
_SslBeTotTLSv1ClientAuthentications_Object = MibScalar
sslBeTotTLSv1ClientAuthentications = _SslBeTotTLSv1ClientAuthentications_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 271),
    _SslBeTotTLSv1ClientAuthentications_Type()
)
sslBeTotTLSv1ClientAuthentications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotTLSv1ClientAuthentications.setStatus("current")
_SslBeTotRSA512keyExchanges_Type = Counter64
_SslBeTotRSA512keyExchanges_Object = MibScalar
sslBeTotRSA512keyExchanges = _SslBeTotRSA512keyExchanges_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 272),
    _SslBeTotRSA512keyExchanges_Type()
)
sslBeTotRSA512keyExchanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotRSA512keyExchanges.setStatus("current")
_SslBeTotRSA1024keyExchanges_Type = Counter64
_SslBeTotRSA1024keyExchanges_Object = MibScalar
sslBeTotRSA1024keyExchanges = _SslBeTotRSA1024keyExchanges_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 273),
    _SslBeTotRSA1024keyExchanges_Type()
)
sslBeTotRSA1024keyExchanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotRSA1024keyExchanges.setStatus("current")
_SslBeTotRSA2048keyExchanges_Type = Counter64
_SslBeTotRSA2048keyExchanges_Object = MibScalar
sslBeTotRSA2048keyExchanges = _SslBeTotRSA2048keyExchanges_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 274),
    _SslBeTotRSA2048keyExchanges_Type()
)
sslBeTotRSA2048keyExchanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotRSA2048keyExchanges.setStatus("current")
_SslBeTotDH512keyExchanges_Type = Counter64
_SslBeTotDH512keyExchanges_Object = MibScalar
sslBeTotDH512keyExchanges = _SslBeTotDH512keyExchanges_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 275),
    _SslBeTotDH512keyExchanges_Type()
)
sslBeTotDH512keyExchanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotDH512keyExchanges.setStatus("current")
_SslBeTotDH1024keyExchanges_Type = Counter64
_SslBeTotDH1024keyExchanges_Object = MibScalar
sslBeTotDH1024keyExchanges = _SslBeTotDH1024keyExchanges_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 276),
    _SslBeTotDH1024keyExchanges_Type()
)
sslBeTotDH1024keyExchanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotDH1024keyExchanges.setStatus("current")
_SslBeTotDH2048keyExchanges_Type = Counter64
_SslBeTotDH2048keyExchanges_Object = MibScalar
sslBeTotDH2048keyExchanges = _SslBeTotDH2048keyExchanges_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 277),
    _SslBeTotDH2048keyExchanges_Type()
)
sslBeTotDH2048keyExchanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotDH2048keyExchanges.setStatus("current")
_SslBeTotRSAAuthorizations_Type = Counter64
_SslBeTotRSAAuthorizations_Object = MibScalar
sslBeTotRSAAuthorizations = _SslBeTotRSAAuthorizations_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 278),
    _SslBeTotRSAAuthorizations_Type()
)
sslBeTotRSAAuthorizations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotRSAAuthorizations.setStatus("current")
_SslBeTotDHAuthorizations_Type = Counter64
_SslBeTotDHAuthorizations_Object = MibScalar
sslBeTotDHAuthorizations = _SslBeTotDHAuthorizations_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 279),
    _SslBeTotDHAuthorizations_Type()
)
sslBeTotDHAuthorizations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotDHAuthorizations.setStatus("current")
_SslBeTotDSSAuthorizations_Type = Counter64
_SslBeTotDSSAuthorizations_Object = MibScalar
sslBeTotDSSAuthorizations = _SslBeTotDSSAuthorizations_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 280),
    _SslBeTotDSSAuthorizations_Type()
)
sslBeTotDSSAuthorizations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotDSSAuthorizations.setStatus("current")
_SslBeTotNULLAuthorizations_Type = Counter64
_SslBeTotNULLAuthorizations_Object = MibScalar
sslBeTotNULLAuthorizations = _SslBeTotNULLAuthorizations_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 281),
    _SslBeTotNULLAuthorizations_Type()
)
sslBeTotNULLAuthorizations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotNULLAuthorizations.setStatus("current")
_SslBeTot40BitRC4Ciphers_Type = Counter64
_SslBeTot40BitRC4Ciphers_Object = MibScalar
sslBeTot40BitRC4Ciphers = _SslBeTot40BitRC4Ciphers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 282),
    _SslBeTot40BitRC4Ciphers_Type()
)
sslBeTot40BitRC4Ciphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot40BitRC4Ciphers.setStatus("current")
_SslBeTot56BitRC4Ciphers_Type = Counter64
_SslBeTot56BitRC4Ciphers_Object = MibScalar
sslBeTot56BitRC4Ciphers = _SslBeTot56BitRC4Ciphers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 283),
    _SslBeTot56BitRC4Ciphers_Type()
)
sslBeTot56BitRC4Ciphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot56BitRC4Ciphers.setStatus("current")
_SslBeTot64BitRC4Ciphers_Type = Counter64
_SslBeTot64BitRC4Ciphers_Object = MibScalar
sslBeTot64BitRC4Ciphers = _SslBeTot64BitRC4Ciphers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 284),
    _SslBeTot64BitRC4Ciphers_Type()
)
sslBeTot64BitRC4Ciphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot64BitRC4Ciphers.setStatus("current")
_SslBeTot128BitRC4Ciphers_Type = Counter64
_SslBeTot128BitRC4Ciphers_Object = MibScalar
sslBeTot128BitRC4Ciphers = _SslBeTot128BitRC4Ciphers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 285),
    _SslBeTot128BitRC4Ciphers_Type()
)
sslBeTot128BitRC4Ciphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot128BitRC4Ciphers.setStatus("current")
_SslBeTot40BitDESCiphers_Type = Counter64
_SslBeTot40BitDESCiphers_Object = MibScalar
sslBeTot40BitDESCiphers = _SslBeTot40BitDESCiphers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 286),
    _SslBeTot40BitDESCiphers_Type()
)
sslBeTot40BitDESCiphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot40BitDESCiphers.setStatus("current")
_SslBeTot56BitDESCiphers_Type = Counter64
_SslBeTot56BitDESCiphers_Object = MibScalar
sslBeTot56BitDESCiphers = _SslBeTot56BitDESCiphers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 287),
    _SslBeTot56BitDESCiphers_Type()
)
sslBeTot56BitDESCiphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot56BitDESCiphers.setStatus("current")
_SslBeTot168Bit3DESCiphers_Type = Counter64
_SslBeTot168Bit3DESCiphers_Object = MibScalar
sslBeTot168Bit3DESCiphers = _SslBeTot168Bit3DESCiphers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 288),
    _SslBeTot168Bit3DESCiphers_Type()
)
sslBeTot168Bit3DESCiphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot168Bit3DESCiphers.setStatus("current")
_SslBeTot40BitRC2Ciphers_Type = Counter64
_SslBeTot40BitRC2Ciphers_Object = MibScalar
sslBeTot40BitRC2Ciphers = _SslBeTot40BitRC2Ciphers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 289),
    _SslBeTot40BitRC2Ciphers_Type()
)
sslBeTot40BitRC2Ciphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot40BitRC2Ciphers.setStatus("current")
_SslBeTot56BitRC2Ciphers_Type = Counter64
_SslBeTot56BitRC2Ciphers_Object = MibScalar
sslBeTot56BitRC2Ciphers = _SslBeTot56BitRC2Ciphers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 290),
    _SslBeTot56BitRC2Ciphers_Type()
)
sslBeTot56BitRC2Ciphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot56BitRC2Ciphers.setStatus("current")
_SslBeTot128BitRC2Ciphers_Type = Counter64
_SslBeTot128BitRC2Ciphers_Object = MibScalar
sslBeTot128BitRC2Ciphers = _SslBeTot128BitRC2Ciphers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 291),
    _SslBeTot128BitRC2Ciphers_Type()
)
sslBeTot128BitRC2Ciphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot128BitRC2Ciphers.setStatus("current")
_SslBeTot128BitIDEACiphers_Type = Counter64
_SslBeTot128BitIDEACiphers_Object = MibScalar
sslBeTot128BitIDEACiphers = _SslBeTot128BitIDEACiphers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 292),
    _SslBeTot128BitIDEACiphers_Type()
)
sslBeTot128BitIDEACiphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTot128BitIDEACiphers.setStatus("current")
_SslBeTotNULLCiphers_Type = Counter64
_SslBeTotNULLCiphers_Object = MibScalar
sslBeTotNULLCiphers = _SslBeTotNULLCiphers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 293),
    _SslBeTotNULLCiphers_Type()
)
sslBeTotNULLCiphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotNULLCiphers.setStatus("current")
_SslBeTotMD5Mac_Type = Counter64
_SslBeTotMD5Mac_Object = MibScalar
sslBeTotMD5Mac = _SslBeTotMD5Mac_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 294),
    _SslBeTotMD5Mac_Type()
)
sslBeTotMD5Mac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotMD5Mac.setStatus("current")
_SslBeTotSHAMac_Type = Counter64
_SslBeTotSHAMac_Object = MibScalar
sslBeTotSHAMac = _SslBeTotSHAMac_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 295),
    _SslBeTotSHAMac_Type()
)
sslBeTotSHAMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslBeTotSHAMac.setStatus("current")
_SslCurSessions_Type = Counter32
_SslCurSessions_Object = MibScalar
sslCurSessions = _SslCurSessions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 296),
    _SslCurSessions_Type()
)
sslCurSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCurSessions.setStatus("current")
_SslTotOffloadBulkAES_Type = Counter64
_SslTotOffloadBulkAES_Object = MibScalar
sslTotOffloadBulkAES = _SslTotOffloadBulkAES_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 297),
    _SslTotOffloadBulkAES_Type()
)
sslTotOffloadBulkAES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotOffloadBulkAES.setStatus("current")
_SslTotOffloadBulkRC4_Type = Counter64
_SslTotOffloadBulkRC4_Object = MibScalar
sslTotOffloadBulkRC4 = _SslTotOffloadBulkRC4_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 298),
    _SslTotOffloadBulkRC4_Type()
)
sslTotOffloadBulkRC4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotOffloadBulkRC4.setStatus("current")
_SslNumCardsUP_Type = Gauge32
_SslNumCardsUP_Object = MibScalar
sslNumCardsUP = _SslNumCardsUP_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 299),
    _SslNumCardsUP_Type()
)
sslNumCardsUP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslNumCardsUP.setStatus("current")
_SslCards_Type = Integer32
_SslCards_Object = MibScalar
sslCards = _SslCards_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 300),
    _SslCards_Type()
)
sslCards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCards.setStatus("current")
_SslTotBkendSessionReNegotiate_Type = Counter64
_SslTotBkendSessionReNegotiate_Object = MibScalar
sslTotBkendSessionReNegotiate = _SslTotBkendSessionReNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 301),
    _SslTotBkendSessionReNegotiate_Type()
)
sslTotBkendSessionReNegotiate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotBkendSessionReNegotiate.setStatus("current")
_SslTotCipherAES128_Type = Counter64
_SslTotCipherAES128_Object = MibScalar
sslTotCipherAES128 = _SslTotCipherAES128_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 302),
    _SslTotCipherAES128_Type()
)
sslTotCipherAES128.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotCipherAES128.setStatus("current")
_SslTotBkendSslV3Renego_Type = Counter64
_SslTotBkendSslV3Renego_Object = MibScalar
sslTotBkendSslV3Renego = _SslTotBkendSslV3Renego_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 303),
    _SslTotBkendSslV3Renego_Type()
)
sslTotBkendSslV3Renego.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotBkendSslV3Renego.setStatus("current")
_SslTotBkendTlSvlRenego_Type = Counter64
_SslTotBkendTlSvlRenego_Object = MibScalar
sslTotBkendTlSvlRenego = _SslTotBkendTlSvlRenego_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 304),
    _SslTotBkendTlSvlRenego_Type()
)
sslTotBkendTlSvlRenego.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotBkendTlSvlRenego.setStatus("current")
_SslTotCipherAES256_Type = Counter64
_SslTotCipherAES256_Object = MibScalar
sslTotCipherAES256 = _SslTotCipherAES256_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 305),
    _SslTotCipherAES256_Type()
)
sslTotCipherAES256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotCipherAES256.setStatus("current")
_SslTotBkendCipherAES128_Type = Counter64
_SslTotBkendCipherAES128_Object = MibScalar
sslTotBkendCipherAES128 = _SslTotBkendCipherAES128_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 306),
    _SslTotBkendCipherAES128_Type()
)
sslTotBkendCipherAES128.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotBkendCipherAES128.setStatus("current")
_SslTotBkendCipherAES256_Type = Counter64
_SslTotBkendCipherAES256_Object = MibScalar
sslTotBkendCipherAES256 = _SslTotBkendCipherAES256_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 307),
    _SslTotBkendCipherAES256_Type()
)
sslTotBkendCipherAES256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotBkendCipherAES256.setStatus("current")
_SslTotHwEncBE_Type = Counter64
_SslTotHwEncBE_Object = MibScalar
sslTotHwEncBE = _SslTotHwEncBE_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 308),
    _SslTotHwEncBE_Type()
)
sslTotHwEncBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotHwEncBE.setStatus("current")
_SslTotDec_Type = Counter64
_SslTotDec_Object = MibScalar
sslTotDec = _SslTotDec_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 309),
    _SslTotDec_Type()
)
sslTotDec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotDec.setStatus("current")
_SslTotSwEncFE_Type = Counter64
_SslTotSwEncFE_Object = MibScalar
sslTotSwEncFE = _SslTotSwEncFE_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 310),
    _SslTotSwEncFE_Type()
)
sslTotSwEncFE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSwEncFE.setStatus("current")
_SslTotEncFE_Type = Counter64
_SslTotEncFE_Object = MibScalar
sslTotEncFE = _SslTotEncFE_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 311),
    _SslTotEncFE_Type()
)
sslTotEncFE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotEncFE.setStatus("current")
_SslTotEnc_Type = Counter64
_SslTotEnc_Object = MibScalar
sslTotEnc = _SslTotEnc_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 312),
    _SslTotEnc_Type()
)
sslTotEnc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotEnc.setStatus("current")
_SslTotDecHw_Type = Counter64
_SslTotDecHw_Object = MibScalar
sslTotDecHw = _SslTotDecHw_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 313),
    _SslTotDecHw_Type()
)
sslTotDecHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotDecHw.setStatus("current")
_SslTotSwDecBE_Type = Counter64
_SslTotSwDecBE_Object = MibScalar
sslTotSwDecBE = _SslTotSwDecBE_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 314),
    _SslTotSwDecBE_Type()
)
sslTotSwDecBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSwDecBE.setStatus("current")
_SslTotHwDecFE_Type = Counter64
_SslTotHwDecFE_Object = MibScalar
sslTotHwDecFE = _SslTotHwDecFE_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 315),
    _SslTotHwDecFE_Type()
)
sslTotHwDecFE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotHwDecFE.setStatus("current")
_SslTotEncHw_Type = Counter64
_SslTotEncHw_Object = MibScalar
sslTotEncHw = _SslTotEncHw_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 316),
    _SslTotEncHw_Type()
)
sslTotEncHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotEncHw.setStatus("current")
_SslTotDecSw_Type = Counter64
_SslTotDecSw_Object = MibScalar
sslTotDecSw = _SslTotDecSw_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 317),
    _SslTotDecSw_Type()
)
sslTotDecSw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotDecSw.setStatus("current")
_SslTotSwEncBE_Type = Counter64
_SslTotSwEncBE_Object = MibScalar
sslTotSwEncBE = _SslTotSwEncBE_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 318),
    _SslTotSwEncBE_Type()
)
sslTotSwEncBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSwEncBE.setStatus("current")
_SslTotEncSw_Type = Counter64
_SslTotEncSw_Object = MibScalar
sslTotEncSw = _SslTotEncSw_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 319),
    _SslTotEncSw_Type()
)
sslTotEncSw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotEncSw.setStatus("current")
_SslTotSwDecFE_Type = Counter64
_SslTotSwDecFE_Object = MibScalar
sslTotSwDecFE = _SslTotSwDecFE_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 320),
    _SslTotSwDecFE_Type()
)
sslTotSwDecFE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotSwDecFE.setStatus("current")
_SslTotEncBE_Type = Counter64
_SslTotEncBE_Object = MibScalar
sslTotEncBE = _SslTotEncBE_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 321),
    _SslTotEncBE_Type()
)
sslTotEncBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotEncBE.setStatus("current")
_SslTotDecBE_Type = Counter64
_SslTotDecBE_Object = MibScalar
sslTotDecBE = _SslTotDecBE_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 322),
    _SslTotDecBE_Type()
)
sslTotDecBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotDecBE.setStatus("current")
_SslTotHwDecBE_Type = Counter64
_SslTotHwDecBE_Object = MibScalar
sslTotHwDecBE = _SslTotHwDecBE_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 323),
    _SslTotHwDecBE_Type()
)
sslTotHwDecBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotHwDecBE.setStatus("current")
_SslTotDecFE_Type = Counter64
_SslTotDecFE_Object = MibScalar
sslTotDecFE = _SslTotDecFE_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 324),
    _SslTotDecFE_Type()
)
sslTotDecFE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotDecFE.setStatus("current")
_SslTotHwEncFE_Type = Counter64
_SslTotHwEncFE_Object = MibScalar
sslTotHwEncFE = _SslTotHwEncFE_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 325),
    _SslTotHwEncFE_Type()
)
sslTotHwEncFE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotHwEncFE.setStatus("current")
_SslTotRSA4096keyExchanges_Type = Counter64
_SslTotRSA4096keyExchanges_Object = MibScalar
sslTotRSA4096keyExchanges = _SslTotRSA4096keyExchanges_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 47, 326),
    _SslTotRSA4096keyExchanges_Type()
)
sslTotRSA4096keyExchanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTotRSA4096keyExchanges.setStatus("current")
_NsHttpStatsGroup_ObjectIdentity = ObjectIdentity
nsHttpStatsGroup = _NsHttpStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48)
)
_HttpTotGetsLow_Type = Counter32
_HttpTotGetsLow_Object = MibScalar
httpTotGetsLow = _HttpTotGetsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 1),
    _HttpTotGetsLow_Type()
)
httpTotGetsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotGetsLow.setStatus("obsolete")
_HttpTotGetsHigh_Type = Counter32
_HttpTotGetsHigh_Object = MibScalar
httpTotGetsHigh = _HttpTotGetsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 2),
    _HttpTotGetsHigh_Type()
)
httpTotGetsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotGetsHigh.setStatus("obsolete")
_HttpTotPostsLow_Type = Counter32
_HttpTotPostsLow_Object = MibScalar
httpTotPostsLow = _HttpTotPostsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 3),
    _HttpTotPostsLow_Type()
)
httpTotPostsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotPostsLow.setStatus("obsolete")
_HttpTotPostsHigh_Type = Counter32
_HttpTotPostsHigh_Object = MibScalar
httpTotPostsHigh = _HttpTotPostsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 4),
    _HttpTotPostsHigh_Type()
)
httpTotPostsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotPostsHigh.setStatus("obsolete")
_HttpTotOthersLow_Type = Counter32
_HttpTotOthersLow_Object = MibScalar
httpTotOthersLow = _HttpTotOthersLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 5),
    _HttpTotOthersLow_Type()
)
httpTotOthersLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotOthersLow.setStatus("obsolete")
_HttpTotOthersHigh_Type = Counter32
_HttpTotOthersHigh_Object = MibScalar
httpTotOthersHigh = _HttpTotOthersHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 6),
    _HttpTotOthersHigh_Type()
)
httpTotOthersHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotOthersHigh.setStatus("obsolete")
_HttpTotRxRequestBytesLow_Type = Counter32
_HttpTotRxRequestBytesLow_Object = MibScalar
httpTotRxRequestBytesLow = _HttpTotRxRequestBytesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 7),
    _HttpTotRxRequestBytesLow_Type()
)
httpTotRxRequestBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotRxRequestBytesLow.setStatus("obsolete")
_HttpTotRxRequestBytesHigh_Type = Counter32
_HttpTotRxRequestBytesHigh_Object = MibScalar
httpTotRxRequestBytesHigh = _HttpTotRxRequestBytesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 8),
    _HttpTotRxRequestBytesHigh_Type()
)
httpTotRxRequestBytesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotRxRequestBytesHigh.setStatus("obsolete")
_HttpTotRxResponseBytesLow_Type = Counter32
_HttpTotRxResponseBytesLow_Object = MibScalar
httpTotRxResponseBytesLow = _HttpTotRxResponseBytesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 9),
    _HttpTotRxResponseBytesLow_Type()
)
httpTotRxResponseBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotRxResponseBytesLow.setStatus("obsolete")
_HttpTotRxResponseBytesHigh_Type = Counter32
_HttpTotRxResponseBytesHigh_Object = MibScalar
httpTotRxResponseBytesHigh = _HttpTotRxResponseBytesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 10),
    _HttpTotRxResponseBytesHigh_Type()
)
httpTotRxResponseBytesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotRxResponseBytesHigh.setStatus("obsolete")
_HttpTotTxRequestBytesLow_Type = Counter32
_HttpTotTxRequestBytesLow_Object = MibScalar
httpTotTxRequestBytesLow = _HttpTotTxRequestBytesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 11),
    _HttpTotTxRequestBytesLow_Type()
)
httpTotTxRequestBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotTxRequestBytesLow.setStatus("obsolete")
_HttpTotTxRequestBytesHigh_Type = Counter32
_HttpTotTxRequestBytesHigh_Object = MibScalar
httpTotTxRequestBytesHigh = _HttpTotTxRequestBytesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 12),
    _HttpTotTxRequestBytesHigh_Type()
)
httpTotTxRequestBytesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotTxRequestBytesHigh.setStatus("obsolete")
_HttpTotTxResponseBytesLow_Type = Counter32
_HttpTotTxResponseBytesLow_Object = MibScalar
httpTotTxResponseBytesLow = _HttpTotTxResponseBytesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 13),
    _HttpTotTxResponseBytesLow_Type()
)
httpTotTxResponseBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotTxResponseBytesLow.setStatus("obsolete")
_HttpTotTxResponseBytesHigh_Type = Counter32
_HttpTotTxResponseBytesHigh_Object = MibScalar
httpTotTxResponseBytesHigh = _HttpTotTxResponseBytesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 14),
    _HttpTotTxResponseBytesHigh_Type()
)
httpTotTxResponseBytesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotTxResponseBytesHigh.setStatus("obsolete")
_HttpTotHTTP10reqLow_Type = Counter32
_HttpTotHTTP10reqLow_Object = MibScalar
httpTotHTTP10reqLow = _HttpTotHTTP10reqLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 15),
    _HttpTotHTTP10reqLow_Type()
)
httpTotHTTP10reqLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotHTTP10reqLow.setStatus("obsolete")
_HttpTotHTTP10reqHigh_Type = Counter32
_HttpTotHTTP10reqHigh_Object = MibScalar
httpTotHTTP10reqHigh = _HttpTotHTTP10reqHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 16),
    _HttpTotHTTP10reqHigh_Type()
)
httpTotHTTP10reqHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotHTTP10reqHigh.setStatus("obsolete")
_HttpTotResponsesLow_Type = Counter32
_HttpTotResponsesLow_Object = MibScalar
httpTotResponsesLow = _HttpTotResponsesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 17),
    _HttpTotResponsesLow_Type()
)
httpTotResponsesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotResponsesLow.setStatus("obsolete")
_HttpTotResponsesHigh_Type = Counter32
_HttpTotResponsesHigh_Object = MibScalar
httpTotResponsesHigh = _HttpTotResponsesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 18),
    _HttpTotResponsesHigh_Type()
)
httpTotResponsesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotResponsesHigh.setStatus("obsolete")
_HttpTot10ResponsesLow_Type = Counter32
_HttpTot10ResponsesLow_Object = MibScalar
httpTot10ResponsesLow = _HttpTot10ResponsesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 19),
    _HttpTot10ResponsesLow_Type()
)
httpTot10ResponsesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTot10ResponsesLow.setStatus("obsolete")
_HttpTot10ResponsesHigh_Type = Counter32
_HttpTot10ResponsesHigh_Object = MibScalar
httpTot10ResponsesHigh = _HttpTot10ResponsesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 20),
    _HttpTot10ResponsesHigh_Type()
)
httpTot10ResponsesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTot10ResponsesHigh.setStatus("obsolete")
_HttpTotClenResponsesLow_Type = Counter32
_HttpTotClenResponsesLow_Object = MibScalar
httpTotClenResponsesLow = _HttpTotClenResponsesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 21),
    _HttpTotClenResponsesLow_Type()
)
httpTotClenResponsesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotClenResponsesLow.setStatus("obsolete")
_HttpTotClenResponsesHigh_Type = Counter32
_HttpTotClenResponsesHigh_Object = MibScalar
httpTotClenResponsesHigh = _HttpTotClenResponsesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 22),
    _HttpTotClenResponsesHigh_Type()
)
httpTotClenResponsesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotClenResponsesHigh.setStatus("obsolete")
_HttpTotChunkedResponsesLow_Type = Counter32
_HttpTotChunkedResponsesLow_Object = MibScalar
httpTotChunkedResponsesLow = _HttpTotChunkedResponsesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 23),
    _HttpTotChunkedResponsesLow_Type()
)
httpTotChunkedResponsesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotChunkedResponsesLow.setStatus("obsolete")
_HttpTotChunkedResponsesHigh_Type = Counter32
_HttpTotChunkedResponsesHigh_Object = MibScalar
httpTotChunkedResponsesHigh = _HttpTotChunkedResponsesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 24),
    _HttpTotChunkedResponsesHigh_Type()
)
httpTotChunkedResponsesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotChunkedResponsesHigh.setStatus("obsolete")
_HttpErrIncompleteRequestsLow_Type = Counter32
_HttpErrIncompleteRequestsLow_Object = MibScalar
httpErrIncompleteRequestsLow = _HttpErrIncompleteRequestsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 25),
    _HttpErrIncompleteRequestsLow_Type()
)
httpErrIncompleteRequestsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpErrIncompleteRequestsLow.setStatus("obsolete")
_HttpErrIncompleteRequestsHigh_Type = Counter32
_HttpErrIncompleteRequestsHigh_Object = MibScalar
httpErrIncompleteRequestsHigh = _HttpErrIncompleteRequestsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 26),
    _HttpErrIncompleteRequestsHigh_Type()
)
httpErrIncompleteRequestsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpErrIncompleteRequestsHigh.setStatus("obsolete")
_HttpErrIncompleteResponsesLow_Type = Counter32
_HttpErrIncompleteResponsesLow_Object = MibScalar
httpErrIncompleteResponsesLow = _HttpErrIncompleteResponsesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 27),
    _HttpErrIncompleteResponsesLow_Type()
)
httpErrIncompleteResponsesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpErrIncompleteResponsesLow.setStatus("obsolete")
_HttpErrIncompleteResponsesHigh_Type = Counter32
_HttpErrIncompleteResponsesHigh_Object = MibScalar
httpErrIncompleteResponsesHigh = _HttpErrIncompleteResponsesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 28),
    _HttpErrIncompleteResponsesHigh_Type()
)
httpErrIncompleteResponsesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpErrIncompleteResponsesHigh.setStatus("obsolete")
_HttpErrPipelinedRequestsLow_Type = Counter32
_HttpErrPipelinedRequestsLow_Object = MibScalar
httpErrPipelinedRequestsLow = _HttpErrPipelinedRequestsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 29),
    _HttpErrPipelinedRequestsLow_Type()
)
httpErrPipelinedRequestsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpErrPipelinedRequestsLow.setStatus("obsolete")
_HttpErrPipelinedRequestsHigh_Type = Counter32
_HttpErrPipelinedRequestsHigh_Object = MibScalar
httpErrPipelinedRequestsHigh = _HttpErrPipelinedRequestsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 30),
    _HttpErrPipelinedRequestsHigh_Type()
)
httpErrPipelinedRequestsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpErrPipelinedRequestsHigh.setStatus("obsolete")
_HttpErrIncompleteHeadersLow_Type = Counter32
_HttpErrIncompleteHeadersLow_Object = MibScalar
httpErrIncompleteHeadersLow = _HttpErrIncompleteHeadersLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 31),
    _HttpErrIncompleteHeadersLow_Type()
)
httpErrIncompleteHeadersLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpErrIncompleteHeadersLow.setStatus("obsolete")
_HttpErrIncompleteHeadersHigh_Type = Counter32
_HttpErrIncompleteHeadersHigh_Object = MibScalar
httpErrIncompleteHeadersHigh = _HttpErrIncompleteHeadersHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 32),
    _HttpErrIncompleteHeadersHigh_Type()
)
httpErrIncompleteHeadersHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpErrIncompleteHeadersHigh.setStatus("obsolete")
_HttpErrServerBusyLow_Type = Counter32
_HttpErrServerBusyLow_Object = MibScalar
httpErrServerBusyLow = _HttpErrServerBusyLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 33),
    _HttpErrServerBusyLow_Type()
)
httpErrServerBusyLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpErrServerBusyLow.setStatus("obsolete")
_HttpErrServerBusyHigh_Type = Counter32
_HttpErrServerBusyHigh_Object = MibScalar
httpErrServerBusyHigh = _HttpErrServerBusyHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 34),
    _HttpErrServerBusyHigh_Type()
)
httpErrServerBusyHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpErrServerBusyHigh.setStatus("obsolete")
_HttpTotChunkedReqLow_Type = Counter32
_HttpTotChunkedReqLow_Object = MibScalar
httpTotChunkedReqLow = _HttpTotChunkedReqLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 35),
    _HttpTotChunkedReqLow_Type()
)
httpTotChunkedReqLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotChunkedReqLow.setStatus("obsolete")
_HttpTotChunkedReqHigh_Type = Counter32
_HttpTotChunkedReqHigh_Object = MibScalar
httpTotChunkedReqHigh = _HttpTotChunkedReqHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 36),
    _HttpTotChunkedReqHigh_Type()
)
httpTotChunkedReqHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotChunkedReqHigh.setStatus("obsolete")
_HttpTotClenReqLow_Type = Counter32
_HttpTotClenReqLow_Object = MibScalar
httpTotClenReqLow = _HttpTotClenReqLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 37),
    _HttpTotClenReqLow_Type()
)
httpTotClenReqLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotClenReqLow.setStatus("obsolete")
_HttpTotClenReqHigh_Type = Counter32
_HttpTotClenReqHigh_Object = MibScalar
httpTotClenReqHigh = _HttpTotClenReqHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 38),
    _HttpTotClenReqHigh_Type()
)
httpTotClenReqHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotClenReqHigh.setStatus("obsolete")
_HttpErrLargeContentLow_Type = Counter32
_HttpErrLargeContentLow_Object = MibScalar
httpErrLargeContentLow = _HttpErrLargeContentLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 39),
    _HttpErrLargeContentLow_Type()
)
httpErrLargeContentLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpErrLargeContentLow.setStatus("obsolete")
_HttpErrLargeContentHigh_Type = Counter32
_HttpErrLargeContentHigh_Object = MibScalar
httpErrLargeContentHigh = _HttpErrLargeContentHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 40),
    _HttpErrLargeContentHigh_Type()
)
httpErrLargeContentHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpErrLargeContentHigh.setStatus("obsolete")
_HttpErrLargeCtlenLow_Type = Counter32
_HttpErrLargeCtlenLow_Object = MibScalar
httpErrLargeCtlenLow = _HttpErrLargeCtlenLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 41),
    _HttpErrLargeCtlenLow_Type()
)
httpErrLargeCtlenLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpErrLargeCtlenLow.setStatus("obsolete")
_HttpErrLargeCtlenHigh_Type = Counter32
_HttpErrLargeCtlenHigh_Object = MibScalar
httpErrLargeCtlenHigh = _HttpErrLargeCtlenHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 42),
    _HttpErrLargeCtlenHigh_Type()
)
httpErrLargeCtlenHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpErrLargeCtlenHigh.setStatus("obsolete")
_HttpErrLargeChunkLow_Type = Counter32
_HttpErrLargeChunkLow_Object = MibScalar
httpErrLargeChunkLow = _HttpErrLargeChunkLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 43),
    _HttpErrLargeChunkLow_Type()
)
httpErrLargeChunkLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpErrLargeChunkLow.setStatus("obsolete")
_HttpErrLargeChunkHigh_Type = Counter32
_HttpErrLargeChunkHigh_Object = MibScalar
httpErrLargeChunkHigh = _HttpErrLargeChunkHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 44),
    _HttpErrLargeChunkHigh_Type()
)
httpErrLargeChunkHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpErrLargeChunkHigh.setStatus("obsolete")
_HttpTotGets_Type = Counter64
_HttpTotGets_Object = MibScalar
httpTotGets = _HttpTotGets_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 45),
    _HttpTotGets_Type()
)
httpTotGets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotGets.setStatus("current")
_HttpTotPosts_Type = Counter64
_HttpTotPosts_Object = MibScalar
httpTotPosts = _HttpTotPosts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 46),
    _HttpTotPosts_Type()
)
httpTotPosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotPosts.setStatus("current")
_HttpTotOthers_Type = Counter64
_HttpTotOthers_Object = MibScalar
httpTotOthers = _HttpTotOthers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 47),
    _HttpTotOthers_Type()
)
httpTotOthers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotOthers.setStatus("current")
_HttpTotRxRequestBytes_Type = Counter64
_HttpTotRxRequestBytes_Object = MibScalar
httpTotRxRequestBytes = _HttpTotRxRequestBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 48),
    _HttpTotRxRequestBytes_Type()
)
httpTotRxRequestBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotRxRequestBytes.setStatus("current")
_HttpTotRxResponseBytes_Type = Counter64
_HttpTotRxResponseBytes_Object = MibScalar
httpTotRxResponseBytes = _HttpTotRxResponseBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 49),
    _HttpTotRxResponseBytes_Type()
)
httpTotRxResponseBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotRxResponseBytes.setStatus("current")
_HttpTotTxRequestBytes_Type = Counter64
_HttpTotTxRequestBytes_Object = MibScalar
httpTotTxRequestBytes = _HttpTotTxRequestBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 50),
    _HttpTotTxRequestBytes_Type()
)
httpTotTxRequestBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotTxRequestBytes.setStatus("current")
_HttpTotTxResponseBytes_Type = Counter64
_HttpTotTxResponseBytes_Object = MibScalar
httpTotTxResponseBytes = _HttpTotTxResponseBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 51),
    _HttpTotTxResponseBytes_Type()
)
httpTotTxResponseBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotTxResponseBytes.setStatus("current")
_HttpTot10Requests_Type = Counter64
_HttpTot10Requests_Object = MibScalar
httpTot10Requests = _HttpTot10Requests_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 52),
    _HttpTot10Requests_Type()
)
httpTot10Requests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTot10Requests.setStatus("current")
_HttpTotResponses_Type = Counter64
_HttpTotResponses_Object = MibScalar
httpTotResponses = _HttpTotResponses_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 53),
    _HttpTotResponses_Type()
)
httpTotResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotResponses.setStatus("current")
_HttpTot10Responses_Type = Counter64
_HttpTot10Responses_Object = MibScalar
httpTot10Responses = _HttpTot10Responses_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 54),
    _HttpTot10Responses_Type()
)
httpTot10Responses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTot10Responses.setStatus("current")
_HttpTotClenResponses_Type = Counter64
_HttpTotClenResponses_Object = MibScalar
httpTotClenResponses = _HttpTotClenResponses_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 55),
    _HttpTotClenResponses_Type()
)
httpTotClenResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotClenResponses.setStatus("current")
_HttpTotChunkedResponses_Type = Counter64
_HttpTotChunkedResponses_Object = MibScalar
httpTotChunkedResponses = _HttpTotChunkedResponses_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 56),
    _HttpTotChunkedResponses_Type()
)
httpTotChunkedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotChunkedResponses.setStatus("current")
_HttpErrIncompleteRequests_Type = Counter64
_HttpErrIncompleteRequests_Object = MibScalar
httpErrIncompleteRequests = _HttpErrIncompleteRequests_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 57),
    _HttpErrIncompleteRequests_Type()
)
httpErrIncompleteRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpErrIncompleteRequests.setStatus("current")
_HttpErrIncompleteResponses_Type = Counter64
_HttpErrIncompleteResponses_Object = MibScalar
httpErrIncompleteResponses = _HttpErrIncompleteResponses_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 58),
    _HttpErrIncompleteResponses_Type()
)
httpErrIncompleteResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpErrIncompleteResponses.setStatus("current")
_HttpErrPipelinedRequests_Type = Counter64
_HttpErrPipelinedRequests_Object = MibScalar
httpErrPipelinedRequests = _HttpErrPipelinedRequests_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 59),
    _HttpErrPipelinedRequests_Type()
)
httpErrPipelinedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpErrPipelinedRequests.setStatus("obsolete")
_HttpErrIncompleteHeaders_Type = Counter64
_HttpErrIncompleteHeaders_Object = MibScalar
httpErrIncompleteHeaders = _HttpErrIncompleteHeaders_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 60),
    _HttpErrIncompleteHeaders_Type()
)
httpErrIncompleteHeaders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpErrIncompleteHeaders.setStatus("current")
_HttpErrServerBusy_Type = Counter64
_HttpErrServerBusy_Object = MibScalar
httpErrServerBusy = _HttpErrServerBusy_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 61),
    _HttpErrServerBusy_Type()
)
httpErrServerBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpErrServerBusy.setStatus("current")
_HttpTotChunkedRequests_Type = Counter64
_HttpTotChunkedRequests_Object = MibScalar
httpTotChunkedRequests = _HttpTotChunkedRequests_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 62),
    _HttpTotChunkedRequests_Type()
)
httpTotChunkedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotChunkedRequests.setStatus("current")
_HttpTotClenRequests_Type = Counter64
_HttpTotClenRequests_Object = MibScalar
httpTotClenRequests = _HttpTotClenRequests_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 63),
    _HttpTotClenRequests_Type()
)
httpTotClenRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotClenRequests.setStatus("current")
_HttpErrLargeContent_Type = Counter64
_HttpErrLargeContent_Object = MibScalar
httpErrLargeContent = _HttpErrLargeContent_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 64),
    _HttpErrLargeContent_Type()
)
httpErrLargeContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpErrLargeContent.setStatus("current")
_HttpErrLargeCtlen_Type = Counter64
_HttpErrLargeCtlen_Object = MibScalar
httpErrLargeCtlen = _HttpErrLargeCtlen_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 65),
    _HttpErrLargeCtlen_Type()
)
httpErrLargeCtlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpErrLargeCtlen.setStatus("current")
_HttpErrLargeChunk_Type = Counter64
_HttpErrLargeChunk_Object = MibScalar
httpErrLargeChunk = _HttpErrLargeChunk_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 66),
    _HttpErrLargeChunk_Type()
)
httpErrLargeChunk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpErrLargeChunk.setStatus("current")
_HttpTotRequests_Type = Counter64
_HttpTotRequests_Object = MibScalar
httpTotRequests = _HttpTotRequests_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 67),
    _HttpTotRequests_Type()
)
httpTotRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotRequests.setStatus("current")
_HttpTot11Requests_Type = Counter64
_HttpTot11Requests_Object = MibScalar
httpTot11Requests = _HttpTot11Requests_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 68),
    _HttpTot11Requests_Type()
)
httpTot11Requests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTot11Requests.setStatus("current")
_HttpTot11Responses_Type = Counter64
_HttpTot11Responses_Object = MibScalar
httpTot11Responses = _HttpTot11Responses_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 69),
    _HttpTot11Responses_Type()
)
httpTot11Responses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTot11Responses.setStatus("current")
_HttpTotNoClenChunkResponses_Type = Counter64
_HttpTotNoClenChunkResponses_Object = MibScalar
httpTotNoClenChunkResponses = _HttpTotNoClenChunkResponses_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 70),
    _HttpTotNoClenChunkResponses_Type()
)
httpTotNoClenChunkResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTotNoClenChunkResponses.setStatus("current")
_HttpErrNoreuseMultipart_Type = Counter64
_HttpErrNoreuseMultipart_Object = MibScalar
httpErrNoreuseMultipart = _HttpErrNoreuseMultipart_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 48, 71),
    _HttpErrNoreuseMultipart_Type()
)
httpErrNoreuseMultipart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpErrNoreuseMultipart.setStatus("current")
_NsCacheStatsGroup_ObjectIdentity = ObjectIdentity
nsCacheStatsGroup = _NsCacheStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49)
)
_CacheMaxMemoryKB_Type = Counter64
_CacheMaxMemoryKB_Object = MibScalar
cacheMaxMemoryKB = _CacheMaxMemoryKB_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 1),
    _CacheMaxMemoryKB_Type()
)
cacheMaxMemoryKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMaxMemoryKB.setStatus("current")
_CacheUtilizedMemoryKB_Type = Counter32
_CacheUtilizedMemoryKB_Object = MibScalar
cacheUtilizedMemoryKB = _CacheUtilizedMemoryKB_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 2),
    _CacheUtilizedMemoryKB_Type()
)
cacheUtilizedMemoryKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheUtilizedMemoryKB.setStatus("current")
_CacheNumCached_Type = Counter32
_CacheNumCached_Object = MibScalar
cacheNumCached = _CacheNumCached_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 3),
    _CacheNumCached_Type()
)
cacheNumCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheNumCached.setStatus("current")
_CacheErrMemAllocLow_Type = Counter32
_CacheErrMemAllocLow_Object = MibScalar
cacheErrMemAllocLow = _CacheErrMemAllocLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 4),
    _CacheErrMemAllocLow_Type()
)
cacheErrMemAllocLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheErrMemAllocLow.setStatus("obsolete")
_CacheErrMemAllocHigh_Type = Counter32
_CacheErrMemAllocHigh_Object = MibScalar
cacheErrMemAllocHigh = _CacheErrMemAllocHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 5),
    _CacheErrMemAllocHigh_Type()
)
cacheErrMemAllocHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheErrMemAllocHigh.setStatus("obsolete")
_CacheTotRequestsLow_Type = Counter32
_CacheTotRequestsLow_Object = MibScalar
cacheTotRequestsLow = _CacheTotRequestsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 6),
    _CacheTotRequestsLow_Type()
)
cacheTotRequestsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotRequestsLow.setStatus("obsolete")
_CacheTotRequestsHigh_Type = Counter32
_CacheTotRequestsHigh_Object = MibScalar
cacheTotRequestsHigh = _CacheTotRequestsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 7),
    _CacheTotRequestsHigh_Type()
)
cacheTotRequestsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotRequestsHigh.setStatus("obsolete")
_CacheTotHitsLow_Type = Counter32
_CacheTotHitsLow_Object = MibScalar
cacheTotHitsLow = _CacheTotHitsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 8),
    _CacheTotHitsLow_Type()
)
cacheTotHitsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotHitsLow.setStatus("obsolete")
_CacheTotHitsHigh_Type = Counter32
_CacheTotHitsHigh_Object = MibScalar
cacheTotHitsHigh = _CacheTotHitsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 9),
    _CacheTotHitsHigh_Type()
)
cacheTotHitsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotHitsHigh.setStatus("obsolete")
_CacheTotMissesLow_Type = Counter32
_CacheTotMissesLow_Object = MibScalar
cacheTotMissesLow = _CacheTotMissesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 10),
    _CacheTotMissesLow_Type()
)
cacheTotMissesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotMissesLow.setStatus("obsolete")
_CacheTotMissesHigh_Type = Counter32
_CacheTotMissesHigh_Object = MibScalar
cacheTotMissesHigh = _CacheTotMissesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 11),
    _CacheTotMissesHigh_Type()
)
cacheTotMissesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotMissesHigh.setStatus("obsolete")
_CachePercentHit_Type = Counter32
_CachePercentHit_Object = MibScalar
cachePercentHit = _CachePercentHit_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 12),
    _CachePercentHit_Type()
)
cachePercentHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cachePercentHit.setStatus("current")
_CacheRecentPercentHit_Type = Counter32
_CacheRecentPercentHit_Object = MibScalar
cacheRecentPercentHit = _CacheRecentPercentHit_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 13),
    _CacheRecentPercentHit_Type()
)
cacheRecentPercentHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheRecentPercentHit.setStatus("current")
_CacheCurHits_Type = Gauge32
_CacheCurHits_Object = MibScalar
cacheCurHits = _CacheCurHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 14),
    _CacheCurHits_Type()
)
cacheCurHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheCurHits.setStatus("current")
_CacheCurMisses_Type = Gauge32
_CacheCurMisses_Object = MibScalar
cacheCurMisses = _CacheCurMisses_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 15),
    _CacheCurMisses_Type()
)
cacheCurMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheCurMisses.setStatus("current")
_CacheTot304HitsLow_Type = Counter32
_CacheTot304HitsLow_Object = MibScalar
cacheTot304HitsLow = _CacheTot304HitsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 16),
    _CacheTot304HitsLow_Type()
)
cacheTot304HitsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTot304HitsLow.setStatus("obsolete")
_CacheTot304HitsHigh_Type = Counter32
_CacheTot304HitsHigh_Object = MibScalar
cacheTot304HitsHigh = _CacheTot304HitsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 17),
    _CacheTot304HitsHigh_Type()
)
cacheTot304HitsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTot304HitsHigh.setStatus("obsolete")
_CacheTotNon304HitsLow_Type = Counter32
_CacheTotNon304HitsLow_Object = MibScalar
cacheTotNon304HitsLow = _CacheTotNon304HitsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 18),
    _CacheTotNon304HitsLow_Type()
)
cacheTotNon304HitsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotNon304HitsLow.setStatus("obsolete")
_CacheTotNon304HitsHigh_Type = Counter32
_CacheTotNon304HitsHigh_Object = MibScalar
cacheTotNon304HitsHigh = _CacheTotNon304HitsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 19),
    _CacheTotNon304HitsHigh_Type()
)
cacheTotNon304HitsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotNon304HitsHigh.setStatus("obsolete")
_CachePercent304Hits_Type = Counter32
_CachePercent304Hits_Object = MibScalar
cachePercent304Hits = _CachePercent304Hits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 20),
    _CachePercent304Hits_Type()
)
cachePercent304Hits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cachePercent304Hits.setStatus("current")
_CacheRecentPercent304Hits_Type = Counter32
_CacheRecentPercent304Hits_Object = MibScalar
cacheRecentPercent304Hits = _CacheRecentPercent304Hits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 21),
    _CacheRecentPercent304Hits_Type()
)
cacheRecentPercent304Hits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheRecentPercent304Hits.setStatus("current")
_CacheTotStoreAbleMissesLow_Type = Counter32
_CacheTotStoreAbleMissesLow_Object = MibScalar
cacheTotStoreAbleMissesLow = _CacheTotStoreAbleMissesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 22),
    _CacheTotStoreAbleMissesLow_Type()
)
cacheTotStoreAbleMissesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotStoreAbleMissesLow.setStatus("obsolete")
_CacheTotStoreAbleMissesHigh_Type = Counter32
_CacheTotStoreAbleMissesHigh_Object = MibScalar
cacheTotStoreAbleMissesHigh = _CacheTotStoreAbleMissesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 23),
    _CacheTotStoreAbleMissesHigh_Type()
)
cacheTotStoreAbleMissesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotStoreAbleMissesHigh.setStatus("obsolete")
_CacheTotNonStoreAbleMissesLow_Type = Counter32
_CacheTotNonStoreAbleMissesLow_Object = MibScalar
cacheTotNonStoreAbleMissesLow = _CacheTotNonStoreAbleMissesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 24),
    _CacheTotNonStoreAbleMissesLow_Type()
)
cacheTotNonStoreAbleMissesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotNonStoreAbleMissesLow.setStatus("obsolete")
_CacheTotNonStoreAbleMissesHigh_Type = Counter32
_CacheTotNonStoreAbleMissesHigh_Object = MibScalar
cacheTotNonStoreAbleMissesHigh = _CacheTotNonStoreAbleMissesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 25),
    _CacheTotNonStoreAbleMissesHigh_Type()
)
cacheTotNonStoreAbleMissesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotNonStoreAbleMissesHigh.setStatus("obsolete")
_CachePercentStoreAbleMiss_Type = Counter32
_CachePercentStoreAbleMiss_Object = MibScalar
cachePercentStoreAbleMiss = _CachePercentStoreAbleMiss_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 26),
    _CachePercentStoreAbleMiss_Type()
)
cachePercentStoreAbleMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cachePercentStoreAbleMiss.setStatus("current")
_CacheRecentPercentStoreAbleMiss_Type = Counter32
_CacheRecentPercentStoreAbleMiss_Object = MibScalar
cacheRecentPercentStoreAbleMiss = _CacheRecentPercentStoreAbleMiss_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 27),
    _CacheRecentPercentStoreAbleMiss_Type()
)
cacheRecentPercentStoreAbleMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheRecentPercentStoreAbleMiss.setStatus("current")
_CacheTotRevalidationMissLow_Type = Counter32
_CacheTotRevalidationMissLow_Object = MibScalar
cacheTotRevalidationMissLow = _CacheTotRevalidationMissLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 28),
    _CacheTotRevalidationMissLow_Type()
)
cacheTotRevalidationMissLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotRevalidationMissLow.setStatus("obsolete")
_CacheTotRevalidationMissHigh_Type = Counter32
_CacheTotRevalidationMissHigh_Object = MibScalar
cacheTotRevalidationMissHigh = _CacheTotRevalidationMissHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 29),
    _CacheTotRevalidationMissHigh_Type()
)
cacheTotRevalidationMissHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotRevalidationMissHigh.setStatus("obsolete")
_CacheTotFullToConditionalRequestLow_Type = Counter32
_CacheTotFullToConditionalRequestLow_Object = MibScalar
cacheTotFullToConditionalRequestLow = _CacheTotFullToConditionalRequestLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 30),
    _CacheTotFullToConditionalRequestLow_Type()
)
cacheTotFullToConditionalRequestLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotFullToConditionalRequestLow.setStatus("obsolete")
_CacheTotFullToConditionalRequestHigh_Type = Counter32
_CacheTotFullToConditionalRequestHigh_Object = MibScalar
cacheTotFullToConditionalRequestHigh = _CacheTotFullToConditionalRequestHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 31),
    _CacheTotFullToConditionalRequestHigh_Type()
)
cacheTotFullToConditionalRequestHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotFullToConditionalRequestHigh.setStatus("obsolete")
_CacheTotSuccessfulRevalidationLow_Type = Counter32
_CacheTotSuccessfulRevalidationLow_Object = MibScalar
cacheTotSuccessfulRevalidationLow = _CacheTotSuccessfulRevalidationLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 32),
    _CacheTotSuccessfulRevalidationLow_Type()
)
cacheTotSuccessfulRevalidationLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotSuccessfulRevalidationLow.setStatus("obsolete")
_CacheTotSuccessfulRevalidationHigh_Type = Counter32
_CacheTotSuccessfulRevalidationHigh_Object = MibScalar
cacheTotSuccessfulRevalidationHigh = _CacheTotSuccessfulRevalidationHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 33),
    _CacheTotSuccessfulRevalidationHigh_Type()
)
cacheTotSuccessfulRevalidationHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotSuccessfulRevalidationHigh.setStatus("obsolete")
_CachePercentSuccessfulRevalidation_Type = Counter32
_CachePercentSuccessfulRevalidation_Object = MibScalar
cachePercentSuccessfulRevalidation = _CachePercentSuccessfulRevalidation_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 34),
    _CachePercentSuccessfulRevalidation_Type()
)
cachePercentSuccessfulRevalidation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cachePercentSuccessfulRevalidation.setStatus("current")
_CacheRecentPercentSuccessfulRevalidation_Type = Counter32
_CacheRecentPercentSuccessfulRevalidation_Object = MibScalar
cacheRecentPercentSuccessfulRevalidation = _CacheRecentPercentSuccessfulRevalidation_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 35),
    _CacheRecentPercentSuccessfulRevalidation_Type()
)
cacheRecentPercentSuccessfulRevalidation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheRecentPercentSuccessfulRevalidation.setStatus("current")
_CacheBytesServedLow_Type = Counter32
_CacheBytesServedLow_Object = MibScalar
cacheBytesServedLow = _CacheBytesServedLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 36),
    _CacheBytesServedLow_Type()
)
cacheBytesServedLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBytesServedLow.setStatus("obsolete")
_CacheBytesServedHigh_Type = Counter32
_CacheBytesServedHigh_Object = MibScalar
cacheBytesServedHigh = _CacheBytesServedHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 37),
    _CacheBytesServedHigh_Type()
)
cacheBytesServedHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBytesServedHigh.setStatus("obsolete")
_CacheCompressedBytesServedLow_Type = Counter32
_CacheCompressedBytesServedLow_Object = MibScalar
cacheCompressedBytesServedLow = _CacheCompressedBytesServedLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 38),
    _CacheCompressedBytesServedLow_Type()
)
cacheCompressedBytesServedLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheCompressedBytesServedLow.setStatus("obsolete")
_CacheCompressedBytesServedHigh_Type = Counter32
_CacheCompressedBytesServedHigh_Object = MibScalar
cacheCompressedBytesServedHigh = _CacheCompressedBytesServedHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 39),
    _CacheCompressedBytesServedHigh_Type()
)
cacheCompressedBytesServedHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheCompressedBytesServedHigh.setStatus("obsolete")
_CachePercentByteHit_Type = Counter32
_CachePercentByteHit_Object = MibScalar
cachePercentByteHit = _CachePercentByteHit_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 40),
    _CachePercentByteHit_Type()
)
cachePercentByteHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cachePercentByteHit.setStatus("current")
_CacheRecentPercentByteHit_Type = Counter32
_CacheRecentPercentByteHit_Object = MibScalar
cacheRecentPercentByteHit = _CacheRecentPercentByteHit_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 41),
    _CacheRecentPercentByteHit_Type()
)
cacheRecentPercentByteHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheRecentPercentByteHit.setStatus("current")
_CachePercentOriginBandwidthSaved_Type = Counter32
_CachePercentOriginBandwidthSaved_Object = MibScalar
cachePercentOriginBandwidthSaved = _CachePercentOriginBandwidthSaved_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 42),
    _CachePercentOriginBandwidthSaved_Type()
)
cachePercentOriginBandwidthSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cachePercentOriginBandwidthSaved.setStatus("current")
_CacheRecentPercentOriginBandwidthSaved_Type = Counter32
_CacheRecentPercentOriginBandwidthSaved_Object = MibScalar
cacheRecentPercentOriginBandwidthSaved = _CacheRecentPercentOriginBandwidthSaved_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 43),
    _CacheRecentPercentOriginBandwidthSaved_Type()
)
cacheRecentPercentOriginBandwidthSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheRecentPercentOriginBandwidthSaved.setStatus("current")
_CacheErrMemAlloc_Type = Counter64
_CacheErrMemAlloc_Object = MibScalar
cacheErrMemAlloc = _CacheErrMemAlloc_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 44),
    _CacheErrMemAlloc_Type()
)
cacheErrMemAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheErrMemAlloc.setStatus("current")
_CacheTotRequests_Type = Counter64
_CacheTotRequests_Object = MibScalar
cacheTotRequests = _CacheTotRequests_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 45),
    _CacheTotRequests_Type()
)
cacheTotRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotRequests.setStatus("current")
_CacheTotHits_Type = Counter64
_CacheTotHits_Object = MibScalar
cacheTotHits = _CacheTotHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 46),
    _CacheTotHits_Type()
)
cacheTotHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotHits.setStatus("current")
_CacheTotMisses_Type = Counter64
_CacheTotMisses_Object = MibScalar
cacheTotMisses = _CacheTotMisses_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 47),
    _CacheTotMisses_Type()
)
cacheTotMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotMisses.setStatus("current")
_CacheTot304Hits_Type = Counter64
_CacheTot304Hits_Object = MibScalar
cacheTot304Hits = _CacheTot304Hits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 48),
    _CacheTot304Hits_Type()
)
cacheTot304Hits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTot304Hits.setStatus("current")
_CacheTotNon304Hits_Type = Counter64
_CacheTotNon304Hits_Object = MibScalar
cacheTotNon304Hits = _CacheTotNon304Hits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 49),
    _CacheTotNon304Hits_Type()
)
cacheTotNon304Hits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotNon304Hits.setStatus("current")
_CacheTotStoreAbleMisses_Type = Counter64
_CacheTotStoreAbleMisses_Object = MibScalar
cacheTotStoreAbleMisses = _CacheTotStoreAbleMisses_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 50),
    _CacheTotStoreAbleMisses_Type()
)
cacheTotStoreAbleMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotStoreAbleMisses.setStatus("current")
_CacheTotNonStoreAbleMisses_Type = Counter64
_CacheTotNonStoreAbleMisses_Object = MibScalar
cacheTotNonStoreAbleMisses = _CacheTotNonStoreAbleMisses_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 51),
    _CacheTotNonStoreAbleMisses_Type()
)
cacheTotNonStoreAbleMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotNonStoreAbleMisses.setStatus("current")
_CacheTotRevalidationMiss_Type = Counter64
_CacheTotRevalidationMiss_Object = MibScalar
cacheTotRevalidationMiss = _CacheTotRevalidationMiss_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 52),
    _CacheTotRevalidationMiss_Type()
)
cacheTotRevalidationMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotRevalidationMiss.setStatus("current")
_CacheTotFullToConditionalRequest_Type = Counter64
_CacheTotFullToConditionalRequest_Object = MibScalar
cacheTotFullToConditionalRequest = _CacheTotFullToConditionalRequest_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 53),
    _CacheTotFullToConditionalRequest_Type()
)
cacheTotFullToConditionalRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotFullToConditionalRequest.setStatus("current")
_CacheTotSuccessfulRevalidation_Type = Counter64
_CacheTotSuccessfulRevalidation_Object = MibScalar
cacheTotSuccessfulRevalidation = _CacheTotSuccessfulRevalidation_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 54),
    _CacheTotSuccessfulRevalidation_Type()
)
cacheTotSuccessfulRevalidation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotSuccessfulRevalidation.setStatus("current")
_CacheTotResponseBytes_Type = Counter64
_CacheTotResponseBytes_Object = MibScalar
cacheTotResponseBytes = _CacheTotResponseBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 55),
    _CacheTotResponseBytes_Type()
)
cacheTotResponseBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotResponseBytes.setStatus("current")
_CacheBytesServed_Type = Counter64
_CacheBytesServed_Object = MibScalar
cacheBytesServed = _CacheBytesServed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 56),
    _CacheBytesServed_Type()
)
cacheBytesServed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBytesServed.setStatus("current")
_CacheCompressedBytesServed_Type = Counter64
_CacheCompressedBytesServed_Object = MibScalar
cacheCompressedBytesServed = _CacheCompressedBytesServed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 57),
    _CacheCompressedBytesServed_Type()
)
cacheCompressedBytesServed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheCompressedBytesServed.setStatus("current")
_CacheTotPetRequests_Type = Counter64
_CacheTotPetRequests_Object = MibScalar
cacheTotPetRequests = _CacheTotPetRequests_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 58),
    _CacheTotPetRequests_Type()
)
cacheTotPetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotPetRequests.setStatus("current")
_CacheTotPetHits_Type = Counter64
_CacheTotPetHits_Object = MibScalar
cacheTotPetHits = _CacheTotPetHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 59),
    _CacheTotPetHits_Type()
)
cacheTotPetHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotPetHits.setStatus("current")
_CachePercentPetHits_Type = Counter32
_CachePercentPetHits_Object = MibScalar
cachePercentPetHits = _CachePercentPetHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 60),
    _CachePercentPetHits_Type()
)
cachePercentPetHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cachePercentPetHits.setStatus("current")
_CacheTotParameterizedRequests_Type = Counter64
_CacheTotParameterizedRequests_Object = MibScalar
cacheTotParameterizedRequests = _CacheTotParameterizedRequests_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 61),
    _CacheTotParameterizedRequests_Type()
)
cacheTotParameterizedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotParameterizedRequests.setStatus("current")
_CacheTotParameterizedHits_Type = Counter64
_CacheTotParameterizedHits_Object = MibScalar
cacheTotParameterizedHits = _CacheTotParameterizedHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 62),
    _CacheTotParameterizedHits_Type()
)
cacheTotParameterizedHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotParameterizedHits.setStatus("current")
_CacheTotParameterizedNon304Hits_Type = Counter64
_CacheTotParameterizedNon304Hits_Object = MibScalar
cacheTotParameterizedNon304Hits = _CacheTotParameterizedNon304Hits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 63),
    _CacheTotParameterizedNon304Hits_Type()
)
cacheTotParameterizedNon304Hits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotParameterizedNon304Hits.setStatus("current")
_CacheTotParameterized304Hits_Type = Counter64
_CacheTotParameterized304Hits_Object = MibScalar
cacheTotParameterized304Hits = _CacheTotParameterized304Hits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 64),
    _CacheTotParameterized304Hits_Type()
)
cacheTotParameterized304Hits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotParameterized304Hits.setStatus("current")
_CachePercentParameterized304Hits_Type = Counter32
_CachePercentParameterized304Hits_Object = MibScalar
cachePercentParameterized304Hits = _CachePercentParameterized304Hits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 65),
    _CachePercentParameterized304Hits_Type()
)
cachePercentParameterized304Hits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cachePercentParameterized304Hits.setStatus("current")
_CacheRecentPercentParameterizedHits_Type = Counter32
_CacheRecentPercentParameterizedHits_Object = MibScalar
cacheRecentPercentParameterizedHits = _CacheRecentPercentParameterizedHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 66),
    _CacheRecentPercentParameterizedHits_Type()
)
cacheRecentPercentParameterizedHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheRecentPercentParameterizedHits.setStatus("current")
_CacheTotInvalidationRequests_Type = Counter64
_CacheTotInvalidationRequests_Object = MibScalar
cacheTotInvalidationRequests = _CacheTotInvalidationRequests_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 67),
    _CacheTotInvalidationRequests_Type()
)
cacheTotInvalidationRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotInvalidationRequests.setStatus("current")
_CacheTotNonParameterizedInvalidationRequests_Type = Counter64
_CacheTotNonParameterizedInvalidationRequests_Object = MibScalar
cacheTotNonParameterizedInvalidationRequests = _CacheTotNonParameterizedInvalidationRequests_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 68),
    _CacheTotNonParameterizedInvalidationRequests_Type()
)
cacheTotNonParameterizedInvalidationRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotNonParameterizedInvalidationRequests.setStatus("current")
_CacheTotParameterizedInvalidationRequests_Type = Counter64
_CacheTotParameterizedInvalidationRequests_Object = MibScalar
cacheTotParameterizedInvalidationRequests = _CacheTotParameterizedInvalidationRequests_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 69),
    _CacheTotParameterizedInvalidationRequests_Type()
)
cacheTotParameterizedInvalidationRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotParameterizedInvalidationRequests.setStatus("current")
_CacheLargestResponseReceived_Type = Counter32
_CacheLargestResponseReceived_Object = MibScalar
cacheLargestResponseReceived = _CacheLargestResponseReceived_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 70),
    _CacheLargestResponseReceived_Type()
)
cacheLargestResponseReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheLargestResponseReceived.setStatus("current")
_CacheTotFlashcacheMisses_Type = Counter64
_CacheTotFlashcacheMisses_Object = MibScalar
cacheTotFlashcacheMisses = _CacheTotFlashcacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 71),
    _CacheTotFlashcacheMisses_Type()
)
cacheTotFlashcacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotFlashcacheMisses.setStatus("current")
_CacheTotFlashcacheHits_Type = Counter64
_CacheTotFlashcacheHits_Object = MibScalar
cacheTotFlashcacheHits = _CacheTotFlashcacheHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 72),
    _CacheTotFlashcacheHits_Type()
)
cacheTotFlashcacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotFlashcacheHits.setStatus("current")
_CacheTotExpireAtLastByte_Type = Counter64
_CacheTotExpireAtLastByte_Object = MibScalar
cacheTotExpireAtLastByte = _CacheTotExpireAtLastByte_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 73),
    _CacheTotExpireAtLastByte_Type()
)
cacheTotExpireAtLastByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotExpireAtLastByte.setStatus("current")
_CacheNumMarker_Type = Counter32
_CacheNumMarker_Object = MibScalar
cacheNumMarker = _CacheNumMarker_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 74),
    _CacheNumMarker_Type()
)
cacheNumMarker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheNumMarker.setStatus("current")
_CacheMaxMemoryActiveKB_Type = Counter64
_CacheMaxMemoryActiveKB_Object = MibScalar
cacheMaxMemoryActiveKB = _CacheMaxMemoryActiveKB_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 75),
    _CacheMaxMemoryActiveKB_Type()
)
cacheMaxMemoryActiveKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMaxMemoryActiveKB.setStatus("current")
_Cache64MaxMemoryKB_Type = Counter64
_Cache64MaxMemoryKB_Object = MibScalar
cache64MaxMemoryKB = _Cache64MaxMemoryKB_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 49, 76),
    _Cache64MaxMemoryKB_Type()
)
cache64MaxMemoryKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cache64MaxMemoryKB.setStatus("current")
_NsCompressionStatsGroup_ObjectIdentity = ObjectIdentity
nsCompressionStatsGroup = _NsCompressionStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50)
)
_CompTotalRequests_Type = Counter64
_CompTotalRequests_Object = MibScalar
compTotalRequests = _CompTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 1),
    _CompTotalRequests_Type()
)
compTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compTotalRequests.setStatus("current")
_CompTotalTxBytes_Type = Counter64
_CompTotalTxBytes_Object = MibScalar
compTotalTxBytes = _CompTotalTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 2),
    _CompTotalTxBytes_Type()
)
compTotalTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compTotalTxBytes.setStatus("current")
_CompTotalRxBytes_Type = Counter64
_CompTotalRxBytes_Object = MibScalar
compTotalRxBytes = _CompTotalRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 3),
    _CompTotalRxBytes_Type()
)
compTotalRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compTotalRxBytes.setStatus("current")
_CompTotalTxPackets_Type = Counter64
_CompTotalTxPackets_Object = MibScalar
compTotalTxPackets = _CompTotalTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 4),
    _CompTotalTxPackets_Type()
)
compTotalTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compTotalTxPackets.setStatus("current")
_CompTotalRxPackets_Type = Counter64
_CompTotalRxPackets_Object = MibScalar
compTotalRxPackets = _CompTotalRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 5),
    _CompTotalRxPackets_Type()
)
compTotalRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compTotalRxPackets.setStatus("current")
_CompRatio_Type = Gauge32
_CompRatio_Object = MibScalar
compRatio = _CompRatio_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 6),
    _CompRatio_Type()
)
compRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compRatio.setStatus("current")
_CompTotalDataCompressionRatio_Type = Gauge32
_CompTotalDataCompressionRatio_Object = MibScalar
compTotalDataCompressionRatio = _CompTotalDataCompressionRatio_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 7),
    _CompTotalDataCompressionRatio_Type()
)
compTotalDataCompressionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compTotalDataCompressionRatio.setStatus("current")
_CompTcpTotalTxBytes_Type = Counter64
_CompTcpTotalTxBytes_Object = MibScalar
compTcpTotalTxBytes = _CompTcpTotalTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 8),
    _CompTcpTotalTxBytes_Type()
)
compTcpTotalTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compTcpTotalTxBytes.setStatus("current")
_CompTcpTotalRxBytes_Type = Counter64
_CompTcpTotalRxBytes_Object = MibScalar
compTcpTotalRxBytes = _CompTcpTotalRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 9),
    _CompTcpTotalRxBytes_Type()
)
compTcpTotalRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compTcpTotalRxBytes.setStatus("current")
_CompTcpTotalTxPackets_Type = Counter64
_CompTcpTotalTxPackets_Object = MibScalar
compTcpTotalTxPackets = _CompTcpTotalTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 10),
    _CompTcpTotalTxPackets_Type()
)
compTcpTotalTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compTcpTotalTxPackets.setStatus("current")
_CompTcpTotalRxPackets_Type = Counter64
_CompTcpTotalRxPackets_Object = MibScalar
compTcpTotalRxPackets = _CompTcpTotalRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 11),
    _CompTcpTotalRxPackets_Type()
)
compTcpTotalRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compTcpTotalRxPackets.setStatus("current")
_CompTcpTotalQuantum_Type = Counter64
_CompTcpTotalQuantum_Object = MibScalar
compTcpTotalQuantum = _CompTcpTotalQuantum_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 12),
    _CompTcpTotalQuantum_Type()
)
compTcpTotalQuantum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compTcpTotalQuantum.setStatus("current")
_CompTcpTotalPush_Type = Counter64
_CompTcpTotalPush_Object = MibScalar
compTcpTotalPush = _CompTcpTotalPush_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 13),
    _CompTcpTotalPush_Type()
)
compTcpTotalPush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compTcpTotalPush.setStatus("current")
_CompTcpTotalEoi_Type = Counter64
_CompTcpTotalEoi_Object = MibScalar
compTcpTotalEoi = _CompTcpTotalEoi_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 14),
    _CompTcpTotalEoi_Type()
)
compTcpTotalEoi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compTcpTotalEoi.setStatus("current")
_CompTcpTotalTimer_Type = Counter64
_CompTcpTotalTimer_Object = MibScalar
compTcpTotalTimer = _CompTcpTotalTimer_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 15),
    _CompTcpTotalTimer_Type()
)
compTcpTotalTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compTcpTotalTimer.setStatus("current")
_CompTcpRatio_Type = Gauge32
_CompTcpRatio_Object = MibScalar
compTcpRatio = _CompTcpRatio_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 16),
    _CompTcpRatio_Type()
)
compTcpRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compTcpRatio.setStatus("current")
_CompTcpBandwidthSaving_Type = Integer32
_CompTcpBandwidthSaving_Object = MibScalar
compTcpBandwidthSaving = _CompTcpBandwidthSaving_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 17),
    _CompTcpBandwidthSaving_Type()
)
compTcpBandwidthSaving.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compTcpBandwidthSaving.setStatus("current")
_DeCompTcpRxPackets_Type = Counter64
_DeCompTcpRxPackets_Object = MibScalar
deCompTcpRxPackets = _DeCompTcpRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 18),
    _DeCompTcpRxPackets_Type()
)
deCompTcpRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deCompTcpRxPackets.setStatus("current")
_DeCompTcpTxPackets_Type = Counter64
_DeCompTcpTxPackets_Object = MibScalar
deCompTcpTxPackets = _DeCompTcpTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 19),
    _DeCompTcpTxPackets_Type()
)
deCompTcpTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deCompTcpTxPackets.setStatus("current")
_DeCompTcpRxBytes_Type = Counter64
_DeCompTcpRxBytes_Object = MibScalar
deCompTcpRxBytes = _DeCompTcpRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 20),
    _DeCompTcpRxBytes_Type()
)
deCompTcpRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deCompTcpRxBytes.setStatus("current")
_DeCompTcpTxBytes_Type = Counter64
_DeCompTcpTxBytes_Object = MibScalar
deCompTcpTxBytes = _DeCompTcpTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 21),
    _DeCompTcpTxBytes_Type()
)
deCompTcpTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deCompTcpTxBytes.setStatus("current")
_DeCompTcpErrData_Type = Counter64
_DeCompTcpErrData_Object = MibScalar
deCompTcpErrData = _DeCompTcpErrData_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 22),
    _DeCompTcpErrData_Type()
)
deCompTcpErrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deCompTcpErrData.setStatus("current")
_DeCompTcpErrLessData_Type = Counter64
_DeCompTcpErrLessData_Object = MibScalar
deCompTcpErrLessData = _DeCompTcpErrLessData_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 23),
    _DeCompTcpErrLessData_Type()
)
deCompTcpErrLessData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deCompTcpErrLessData.setStatus("current")
_DeCompTcpErrMoreData_Type = Counter64
_DeCompTcpErrMoreData_Object = MibScalar
deCompTcpErrMoreData = _DeCompTcpErrMoreData_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 24),
    _DeCompTcpErrMoreData_Type()
)
deCompTcpErrMoreData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deCompTcpErrMoreData.setStatus("current")
_DeCompTcpErrMemory_Type = Counter64
_DeCompTcpErrMemory_Object = MibScalar
deCompTcpErrMemory = _DeCompTcpErrMemory_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 25),
    _DeCompTcpErrMemory_Type()
)
deCompTcpErrMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deCompTcpErrMemory.setStatus("current")
_DeCompTcpErrUnknown_Type = Counter64
_DeCompTcpErrUnknown_Object = MibScalar
deCompTcpErrUnknown = _DeCompTcpErrUnknown_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 26),
    _DeCompTcpErrUnknown_Type()
)
deCompTcpErrUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deCompTcpErrUnknown.setStatus("current")
_DeCompTcpRatio_Type = Gauge32
_DeCompTcpRatio_Object = MibScalar
deCompTcpRatio = _DeCompTcpRatio_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 27),
    _DeCompTcpRatio_Type()
)
deCompTcpRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deCompTcpRatio.setStatus("current")
_DeCompTcpBandwidthSaving_Type = Integer32
_DeCompTcpBandwidthSaving_Object = MibScalar
deCompTcpBandwidthSaving = _DeCompTcpBandwidthSaving_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 28),
    _DeCompTcpBandwidthSaving_Type()
)
deCompTcpBandwidthSaving.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deCompTcpBandwidthSaving.setStatus("current")
_DelCompTotalRequests_Type = Counter64
_DelCompTotalRequests_Object = MibScalar
delCompTotalRequests = _DelCompTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 29),
    _DelCompTotalRequests_Type()
)
delCompTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delCompTotalRequests.setStatus("current")
_DelCompFirstAccess_Type = Counter64
_DelCompFirstAccess_Object = MibScalar
delCompFirstAccess = _DelCompFirstAccess_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 30),
    _DelCompFirstAccess_Type()
)
delCompFirstAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delCompFirstAccess.setStatus("current")
_DelCompDone_Type = Counter64
_DelCompDone_Object = MibScalar
delCompDone = _DelCompDone_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 31),
    _DelCompDone_Type()
)
delCompDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delCompDone.setStatus("current")
_DelCompTcpRxBytes_Type = Counter64
_DelCompTcpRxBytes_Object = MibScalar
delCompTcpRxBytes = _DelCompTcpRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 32),
    _DelCompTcpRxBytes_Type()
)
delCompTcpRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delCompTcpRxBytes.setStatus("current")
_DelCompTcpTxBytes_Type = Counter64
_DelCompTcpTxBytes_Object = MibScalar
delCompTcpTxBytes = _DelCompTcpTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 33),
    _DelCompTcpTxBytes_Type()
)
delCompTcpTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delCompTcpTxBytes.setStatus("current")
_DelCompTcpRxPackets_Type = Counter64
_DelCompTcpRxPackets_Object = MibScalar
delCompTcpRxPackets = _DelCompTcpRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 34),
    _DelCompTcpRxPackets_Type()
)
delCompTcpRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delCompTcpRxPackets.setStatus("current")
_DelCompTcpTxPackets_Type = Counter64
_DelCompTcpTxPackets_Object = MibScalar
delCompTcpTxPackets = _DelCompTcpTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 35),
    _DelCompTcpTxPackets_Type()
)
delCompTcpTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delCompTcpTxPackets.setStatus("current")
_DelCompBaseServed_Type = Counter64
_DelCompBaseServed_Object = MibScalar
delCompBaseServed = _DelCompBaseServed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 36),
    _DelCompBaseServed_Type()
)
delCompBaseServed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delCompBaseServed.setStatus("current")
_DelCompBaseTcpTxBytes_Type = Counter64
_DelCompBaseTcpTxBytes_Object = MibScalar
delCompBaseTcpTxBytes = _DelCompBaseTcpTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 37),
    _DelCompBaseTcpTxBytes_Type()
)
delCompBaseTcpTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delCompBaseTcpTxBytes.setStatus("current")
_DelCompErrBypassed_Type = Counter64
_DelCompErrBypassed_Object = MibScalar
delCompErrBypassed = _DelCompErrBypassed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 39),
    _DelCompErrBypassed_Type()
)
delCompErrBypassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delCompErrBypassed.setStatus("current")
_DelCompErrBFileWHdrFailed_Type = Counter64
_DelCompErrBFileWHdrFailed_Object = MibScalar
delCompErrBFileWHdrFailed = _DelCompErrBFileWHdrFailed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 40),
    _DelCompErrBFileWHdrFailed_Type()
)
delCompErrBFileWHdrFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delCompErrBFileWHdrFailed.setStatus("current")
_DelCompErrNostoreMiss_Type = Counter64
_DelCompErrNostoreMiss_Object = MibScalar
delCompErrNostoreMiss = _DelCompErrNostoreMiss_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 41),
    _DelCompErrNostoreMiss_Type()
)
delCompErrNostoreMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delCompErrNostoreMiss.setStatus("current")
_DelCompErrReqinfoToobig_Type = Counter64
_DelCompErrReqinfoToobig_Object = MibScalar
delCompErrReqinfoToobig = _DelCompErrReqinfoToobig_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 42),
    _DelCompErrReqinfoToobig_Type()
)
delCompErrReqinfoToobig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delCompErrReqinfoToobig.setStatus("current")
_DelCompErrReqinfoAllocfail_Type = Counter64
_DelCompErrReqinfoAllocfail_Object = MibScalar
delCompErrReqinfoAllocfail = _DelCompErrReqinfoAllocfail_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 43),
    _DelCompErrReqinfoAllocfail_Type()
)
delCompErrReqinfoAllocfail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delCompErrReqinfoAllocfail.setStatus("current")
_DelCompErrSessallocFail_Type = Counter64
_DelCompErrSessallocFail_Object = MibScalar
delCompErrSessallocFail = _DelCompErrSessallocFail_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 44),
    _DelCompErrSessallocFail_Type()
)
delCompErrSessallocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delCompErrSessallocFail.setStatus("current")
_DelCmpRatio_Type = Gauge32
_DelCmpRatio_Object = MibScalar
delCmpRatio = _DelCmpRatio_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 45),
    _DelCmpRatio_Type()
)
delCmpRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delCmpRatio.setStatus("current")
_DelBwSaving_Type = Integer32
_DelBwSaving_Object = MibScalar
delBwSaving = _DelBwSaving_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 46),
    _DelBwSaving_Type()
)
delBwSaving.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delBwSaving.setStatus("current")
_CompHttpBandwidthSaving_Type = Integer32
_CompHttpBandwidthSaving_Object = MibScalar
compHttpBandwidthSaving = _CompHttpBandwidthSaving_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 50, 47),
    _CompHttpBandwidthSaving_Type()
)
compHttpBandwidthSaving.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compHttpBandwidthSaving.setStatus("current")
_NsGslbGroup_ObjectIdentity = ObjectIdentity
nsGslbGroup = _NsGslbGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51)
)
_GslbGlobalStats_ObjectIdentity = ObjectIdentity
gslbGlobalStats = _GslbGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 1)
)
_CustomEntries_Type = Counter32
_CustomEntries_Object = MibScalar
customEntries = _CustomEntries_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 1, 1),
    _CustomEntries_Type()
)
customEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customEntries.setStatus("current")
_StaticEntries_Type = Counter32
_StaticEntries_Object = MibScalar
staticEntries = _StaticEntries_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 1, 2),
    _StaticEntries_Type()
)
staticEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticEntries.setStatus("current")
_GslbGlobalInfo_ObjectIdentity = ObjectIdentity
gslbGlobalInfo = _GslbGlobalInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 2)
)
_GslbSitesTable_Object = MibTable
gslbSitesTable = _GslbSitesTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 2, 1)
)
if mibBuilder.loadTexts:
    gslbSitesTable.setStatus("current")
_GslbSitesEntry_Object = MibTableRow
gslbSitesEntry = _GslbSitesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 2, 1, 1)
)
gslbSitesEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "siteName"),
)
if mibBuilder.loadTexts:
    gslbSitesEntry.setStatus("current")
_SiteName_Type = OctetString
_SiteName_Object = MibTableColumn
siteName = _SiteName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 2, 1, 1, 1),
    _SiteName_Type()
)
siteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteName.setStatus("current")
_SiteIp_Type = IpAddress
_SiteIp_Object = MibTableColumn
siteIp = _SiteIp_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 2, 1, 1, 2),
    _SiteIp_Type()
)
siteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteIp.setStatus("current")
_SiteType_Type = SiteType
_SiteType_Object = MibTableColumn
siteType = _SiteType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 2, 1, 1, 3),
    _SiteType_Type()
)
siteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteType.setStatus("current")
_SiteMetricExchange_Type = MetricExchange
_SiteMetricExchange_Object = MibTableColumn
siteMetricExchange = _SiteMetricExchange_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 2, 1, 1, 4),
    _SiteMetricExchange_Type()
)
siteMetricExchange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteMetricExchange.setStatus("current")
_SiteMepStatus_Type = MepStatus
_SiteMepStatus_Object = MibTableColumn
siteMepStatus = _SiteMepStatus_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 2, 1, 1, 5),
    _SiteMepStatus_Type()
)
siteMepStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteMepStatus.setStatus("obsolete")
_SitePublicIp_Type = IpAddress
_SitePublicIp_Object = MibTableColumn
sitePublicIp = _SitePublicIp_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 2, 1, 1, 6),
    _SitePublicIp_Type()
)
sitePublicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitePublicIp.setStatus("current")
_SiteTotalRequests_Type = Counter64
_SiteTotalRequests_Object = MibTableColumn
siteTotalRequests = _SiteTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 2, 1, 1, 7),
    _SiteTotalRequests_Type()
)
siteTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteTotalRequests.setStatus("current")
_SiteTotalRequestBytes_Type = Counter64
_SiteTotalRequestBytes_Object = MibTableColumn
siteTotalRequestBytes = _SiteTotalRequestBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 2, 1, 1, 8),
    _SiteTotalRequestBytes_Type()
)
siteTotalRequestBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteTotalRequestBytes.setStatus("current")
_SiteTotalResponses_Type = Counter64
_SiteTotalResponses_Object = MibTableColumn
siteTotalResponses = _SiteTotalResponses_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 2, 1, 1, 9),
    _SiteTotalResponses_Type()
)
siteTotalResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteTotalResponses.setStatus("current")
_SiteTotalResponseBytes_Type = Counter64
_SiteTotalResponseBytes_Object = MibTableColumn
siteTotalResponseBytes = _SiteTotalResponseBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 2, 1, 1, 10),
    _SiteTotalResponseBytes_Type()
)
siteTotalResponseBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteTotalResponseBytes.setStatus("current")
_SiteCurSrvrConnections_Type = Gauge32
_SiteCurSrvrConnections_Object = MibTableColumn
siteCurSrvrConnections = _SiteCurSrvrConnections_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 2, 1, 1, 11),
    _SiteCurSrvrConnections_Type()
)
siteCurSrvrConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteCurSrvrConnections.setStatus("current")
_SiteCurClntConnections_Type = Gauge32
_SiteCurClntConnections_Object = MibTableColumn
siteCurClntConnections = _SiteCurClntConnections_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 2, 1, 1, 12),
    _SiteCurClntConnections_Type()
)
siteCurClntConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteCurClntConnections.setStatus("current")
_SiteMetricMepStatus_Type = MepStatus
_SiteMetricMepStatus_Object = MibTableColumn
siteMetricMepStatus = _SiteMetricMepStatus_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 2, 1, 1, 13),
    _SiteMetricMepStatus_Type()
)
siteMetricMepStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteMetricMepStatus.setStatus("current")
_NwMetricMepStatus_Type = MepStatus
_NwMetricMepStatus_Object = MibTableColumn
nwMetricMepStatus = _NwMetricMepStatus_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 2, 1, 1, 14),
    _NwMetricMepStatus_Type()
)
nwMetricMepStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwMetricMepStatus.setStatus("current")
_NwMetricExchange_Type = MetricExchange
_NwMetricExchange_Object = MibTableColumn
nwMetricExchange = _NwMetricExchange_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 2, 1, 1, 15),
    _NwMetricExchange_Type()
)
nwMetricExchange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwMetricExchange.setStatus("current")
_PersExchange_Type = MetricExchange
_PersExchange_Object = MibTableColumn
persExchange = _PersExchange_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 2, 1, 1, 16),
    _PersExchange_Type()
)
persExchange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    persExchange.setStatus("current")
_GslbSiteInetAddressType_Type = InetAddressType
_GslbSiteInetAddressType_Object = MibTableColumn
gslbSiteInetAddressType = _GslbSiteInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 2, 1, 1, 17),
    _GslbSiteInetAddressType_Type()
)
gslbSiteInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbSiteInetAddressType.setStatus("current")
_GslbSiteInetAddress_Type = InetAddress
_GslbSiteInetAddress_Object = MibTableColumn
gslbSiteInetAddress = _GslbSiteInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 2, 1, 1, 18),
    _GslbSiteInetAddress_Type()
)
gslbSiteInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbSiteInetAddress.setStatus("current")
_GslbSitePublicInetAddressType_Type = InetAddressType
_GslbSitePublicInetAddressType_Object = MibTableColumn
gslbSitePublicInetAddressType = _GslbSitePublicInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 2, 1, 1, 19),
    _GslbSitePublicInetAddressType_Type()
)
gslbSitePublicInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbSitePublicInetAddressType.setStatus("current")
_GslbSitePublicInetAddress_Type = InetAddress
_GslbSitePublicInetAddress_Object = MibTableColumn
gslbSitePublicInetAddress = _GslbSitePublicInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 2, 1, 1, 20),
    _GslbSitePublicInetAddress_Type()
)
gslbSitePublicInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbSitePublicInetAddress.setStatus("current")
_GslbPoliciesTable_Object = MibTable
gslbPoliciesTable = _GslbPoliciesTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 2, 2)
)
if mibBuilder.loadTexts:
    gslbPoliciesTable.setStatus("current")
_GslbPoliciesEntry_Object = MibTableRow
gslbPoliciesEntry = _GslbPoliciesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 2, 2, 1)
)
gslbPoliciesEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "gslbPolicyName"),
)
if mibBuilder.loadTexts:
    gslbPoliciesEntry.setStatus("current")
_GslbPolicyName_Type = OctetString
_GslbPolicyName_Object = MibTableColumn
gslbPolicyName = _GslbPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 2, 2, 1, 1),
    _GslbPolicyName_Type()
)
gslbPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbPolicyName.setStatus("current")
_TotalHits_Type = Counter32
_TotalHits_Object = MibTableColumn
totalHits = _TotalHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 2, 2, 1, 2),
    _TotalHits_Type()
)
totalHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalHits.setStatus("current")
_GslbDomainStats_ObjectIdentity = ObjectIdentity
gslbDomainStats = _GslbDomainStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 3)
)
_NsDomainTable_Object = MibTable
nsDomainTable = _NsDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 3, 1)
)
if mibBuilder.loadTexts:
    nsDomainTable.setStatus("current")
_NsDomainEntry_Object = MibTableRow
nsDomainEntry = _NsDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 3, 1, 1)
)
nsDomainEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "domainName"),
)
if mibBuilder.loadTexts:
    nsDomainEntry.setStatus("current")
_DomainName_Type = OctetString
_DomainName_Object = MibTableColumn
domainName = _DomainName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 3, 1, 1, 1),
    _DomainName_Type()
)
domainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainName.setStatus("current")
_DnsTotalQueries_Type = Counter64
_DnsTotalQueries_Object = MibTableColumn
dnsTotalQueries = _DnsTotalQueries_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 51, 3, 1, 1, 2),
    _DnsTotalQueries_Type()
)
dnsTotalQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotalQueries.setStatus("current")
_NsPolicyEngineGroup_ObjectIdentity = ObjectIdentity
nsPolicyEngineGroup = _NsPolicyEngineGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 52)
)
_NsPolicyStatsTable_Object = MibTable
nsPolicyStatsTable = _NsPolicyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 52, 1)
)
if mibBuilder.loadTexts:
    nsPolicyStatsTable.setStatus("current")
_NsPolicyStatsEntry_Object = MibTableRow
nsPolicyStatsEntry = _NsPolicyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 52, 1, 1)
)
nsPolicyStatsEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "pengPolicyName"),
)
if mibBuilder.loadTexts:
    nsPolicyStatsEntry.setStatus("current")
_PengPolicyName_Type = OctetString
_PengPolicyName_Object = MibTableColumn
pengPolicyName = _PengPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 52, 1, 1, 1),
    _PengPolicyName_Type()
)
pengPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pengPolicyName.setStatus("current")
_PengPolicyHits_Type = Counter32
_PengPolicyHits_Object = MibTableColumn
pengPolicyHits = _PengPolicyHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 52, 1, 1, 2),
    _PengPolicyHits_Type()
)
pengPolicyHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pengPolicyHits.setStatus("current")
_PengBytesIn_Type = Counter32
_PengBytesIn_Object = MibTableColumn
pengBytesIn = _PengBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 52, 1, 1, 3),
    _PengBytesIn_Type()
)
pengBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pengBytesIn.setStatus("current")
_PengBytesOut_Type = Counter32
_PengBytesOut_Object = MibTableColumn
pengBytesOut = _PengBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 52, 1, 1, 4),
    _PengBytesOut_Type()
)
pengBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pengBytesOut.setStatus("current")
_PengPolicyFullName_Type = OctetString
_PengPolicyFullName_Object = MibTableColumn
pengPolicyFullName = _PengPolicyFullName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 52, 1, 1, 5),
    _PengPolicyFullName_Type()
)
pengPolicyFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pengPolicyFullName.setStatus("current")
_NsDomainNameServiceGroup_ObjectIdentity = ObjectIdentity
nsDomainNameServiceGroup = _NsDomainNameServiceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53)
)
_NsDnsServerStatsGroup_ObjectIdentity = ObjectIdentity
nsDnsServerStatsGroup = _NsDnsServerStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1)
)
_DnsTotQueries_Type = Counter64
_DnsTotQueries_Object = MibScalar
dnsTotQueries = _DnsTotQueries_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 1),
    _DnsTotQueries_Type()
)
dnsTotQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotQueries.setStatus("current")
_DnsTotAnswers_Type = Counter64
_DnsTotAnswers_Object = MibScalar
dnsTotAnswers = _DnsTotAnswers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 2),
    _DnsTotAnswers_Type()
)
dnsTotAnswers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotAnswers.setStatus("current")
_DnsTotArecQueries_Type = Counter64
_DnsTotArecQueries_Object = MibScalar
dnsTotArecQueries = _DnsTotArecQueries_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 3),
    _DnsTotArecQueries_Type()
)
dnsTotArecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotArecQueries.setStatus("current")
_DnsTotAresponse_Type = Counter64
_DnsTotAresponse_Object = MibScalar
dnsTotAresponse = _DnsTotAresponse_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 4),
    _DnsTotAresponse_Type()
)
dnsTotAresponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotAresponse.setStatus("current")
_DnsTotNSrecQueries_Type = Counter64
_DnsTotNSrecQueries_Object = MibScalar
dnsTotNSrecQueries = _DnsTotNSrecQueries_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 5),
    _DnsTotNSrecQueries_Type()
)
dnsTotNSrecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotNSrecQueries.setStatus("current")
_DnsTotNSresponse_Type = Counter64
_DnsTotNSresponse_Object = MibScalar
dnsTotNSresponse = _DnsTotNSresponse_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 6),
    _DnsTotNSresponse_Type()
)
dnsTotNSresponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotNSresponse.setStatus("current")
_DnsTotMXrecQueries_Type = Counter64
_DnsTotMXrecQueries_Object = MibScalar
dnsTotMXrecQueries = _DnsTotMXrecQueries_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 7),
    _DnsTotMXrecQueries_Type()
)
dnsTotMXrecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotMXrecQueries.setStatus("current")
_DnsTotMXresponse_Type = Counter64
_DnsTotMXresponse_Object = MibScalar
dnsTotMXresponse = _DnsTotMXresponse_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 8),
    _DnsTotMXresponse_Type()
)
dnsTotMXresponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotMXresponse.setStatus("current")
_DnsTotSOArecQueries_Type = Counter64
_DnsTotSOArecQueries_Object = MibScalar
dnsTotSOArecQueries = _DnsTotSOArecQueries_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 9),
    _DnsTotSOArecQueries_Type()
)
dnsTotSOArecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotSOArecQueries.setStatus("current")
_DnsTotSOAresponse_Type = Counter64
_DnsTotSOAresponse_Object = MibScalar
dnsTotSOAresponse = _DnsTotSOAresponse_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 10),
    _DnsTotSOAresponse_Type()
)
dnsTotSOAresponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotSOAresponse.setStatus("current")
_DnsTotCNAMErecQueries_Type = Counter64
_DnsTotCNAMErecQueries_Object = MibScalar
dnsTotCNAMErecQueries = _DnsTotCNAMErecQueries_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 11),
    _DnsTotCNAMErecQueries_Type()
)
dnsTotCNAMErecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotCNAMErecQueries.setStatus("current")
_DnsTotCNAMEresponse_Type = Counter64
_DnsTotCNAMEresponse_Object = MibScalar
dnsTotCNAMEresponse = _DnsTotCNAMEresponse_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 12),
    _DnsTotCNAMEresponse_Type()
)
dnsTotCNAMEresponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotCNAMEresponse.setStatus("current")
_DnsTotUnsupportedResponseClass_Type = Counter64
_DnsTotUnsupportedResponseClass_Object = MibScalar
dnsTotUnsupportedResponseClass = _DnsTotUnsupportedResponseClass_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 13),
    _DnsTotUnsupportedResponseClass_Type()
)
dnsTotUnsupportedResponseClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotUnsupportedResponseClass.setStatus("current")
_DnsTotUnsupportedResponseType_Type = Counter64
_DnsTotUnsupportedResponseType_Object = MibScalar
dnsTotUnsupportedResponseType = _DnsTotUnsupportedResponseType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 14),
    _DnsTotUnsupportedResponseType_Type()
)
dnsTotUnsupportedResponseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotUnsupportedResponseType.setStatus("current")
_DnsTotUnsupportedQueries_Type = Counter64
_DnsTotUnsupportedQueries_Object = MibScalar
dnsTotUnsupportedQueries = _DnsTotUnsupportedQueries_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 15),
    _DnsTotUnsupportedQueries_Type()
)
dnsTotUnsupportedQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotUnsupportedQueries.setStatus("current")
_DnsTotUnsupportedQueryClass_Type = Counter64
_DnsTotUnsupportedQueryClass_Object = MibScalar
dnsTotUnsupportedQueryClass = _DnsTotUnsupportedQueryClass_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 16),
    _DnsTotUnsupportedQueryClass_Type()
)
dnsTotUnsupportedQueryClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotUnsupportedQueryClass.setStatus("current")
_DnsTotInvalidQueryFormat_Type = Counter64
_DnsTotInvalidQueryFormat_Object = MibScalar
dnsTotInvalidQueryFormat = _DnsTotInvalidQueryFormat_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 17),
    _DnsTotInvalidQueryFormat_Type()
)
dnsTotInvalidQueryFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotInvalidQueryFormat.setStatus("current")
_DnsTotNonAuthNoDatas_Type = Counter64
_DnsTotNonAuthNoDatas_Object = MibScalar
dnsTotNonAuthNoDatas = _DnsTotNonAuthNoDatas_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 18),
    _DnsTotNonAuthNoDatas_Type()
)
dnsTotNonAuthNoDatas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotNonAuthNoDatas.setStatus("current")
_DnsTotMultiQuery_Type = Counter64
_DnsTotMultiQuery_Object = MibScalar
dnsTotMultiQuery = _DnsTotMultiQuery_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 19),
    _DnsTotMultiQuery_Type()
)
dnsTotMultiQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotMultiQuery.setStatus("current")
_DnsTotStrayAnswer_Type = Counter64
_DnsTotStrayAnswer_Object = MibScalar
dnsTotStrayAnswer = _DnsTotStrayAnswer_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 20),
    _DnsTotStrayAnswer_Type()
)
dnsTotStrayAnswer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotStrayAnswer.setStatus("current")
_DnsTotCacheFlush_Type = Counter64
_DnsTotCacheFlush_Object = MibScalar
dnsTotCacheFlush = _DnsTotCacheFlush_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 21),
    _DnsTotCacheFlush_Type()
)
dnsTotCacheFlush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotCacheFlush.setStatus("current")
_DnsTotCacheEntriesFlush_Type = Counter64
_DnsTotCacheEntriesFlush_Object = MibScalar
dnsTotCacheEntriesFlush = _DnsTotCacheEntriesFlush_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 22),
    _DnsTotCacheEntriesFlush_Type()
)
dnsTotCacheEntriesFlush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotCacheEntriesFlush.setStatus("current")
_DnsTotServerQuery_Type = Counter64
_DnsTotServerQuery_Object = MibScalar
dnsTotServerQuery = _DnsTotServerQuery_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 23),
    _DnsTotServerQuery_Type()
)
dnsTotServerQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotServerQuery.setStatus("current")
_DnsTotServerResponse_Type = Counter64
_DnsTotServerResponse_Object = MibScalar
dnsTotServerResponse = _DnsTotServerResponse_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 24),
    _DnsTotServerResponse_Type()
)
dnsTotServerResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotServerResponse.setStatus("current")
_DnsTotArecFailed_Type = Counter64
_DnsTotArecFailed_Object = MibScalar
dnsTotArecFailed = _DnsTotArecFailed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 25),
    _DnsTotArecFailed_Type()
)
dnsTotArecFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotArecFailed.setStatus("current")
_DnsTotNSrecFailed_Type = Counter64
_DnsTotNSrecFailed_Object = MibScalar
dnsTotNSrecFailed = _DnsTotNSrecFailed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 26),
    _DnsTotNSrecFailed_Type()
)
dnsTotNSrecFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotNSrecFailed.setStatus("current")
_DnsTotMXrecFailed_Type = Counter64
_DnsTotMXrecFailed_Object = MibScalar
dnsTotMXrecFailed = _DnsTotMXrecFailed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 27),
    _DnsTotMXrecFailed_Type()
)
dnsTotMXrecFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotMXrecFailed.setStatus("current")
_DnsTotCNAMErecFailed_Type = Counter64
_DnsTotCNAMErecFailed_Object = MibScalar
dnsTotCNAMErecFailed = _DnsTotCNAMErecFailed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 28),
    _DnsTotCNAMErecFailed_Type()
)
dnsTotCNAMErecFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotCNAMErecFailed.setStatus("current")
_DnsTotArecUpdate_Type = Counter64
_DnsTotArecUpdate_Object = MibScalar
dnsTotArecUpdate = _DnsTotArecUpdate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 29),
    _DnsTotArecUpdate_Type()
)
dnsTotArecUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotArecUpdate.setStatus("current")
_DnsTotNSrecUpdate_Type = Counter64
_DnsTotNSrecUpdate_Object = MibScalar
dnsTotNSrecUpdate = _DnsTotNSrecUpdate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 30),
    _DnsTotNSrecUpdate_Type()
)
dnsTotNSrecUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotNSrecUpdate.setStatus("current")
_DnsTotMXrecUpdate_Type = Counter64
_DnsTotMXrecUpdate_Object = MibScalar
dnsTotMXrecUpdate = _DnsTotMXrecUpdate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 31),
    _DnsTotMXrecUpdate_Type()
)
dnsTotMXrecUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotMXrecUpdate.setStatus("current")
_DnsTotSOArecUpdate_Type = Counter64
_DnsTotSOArecUpdate_Object = MibScalar
dnsTotSOArecUpdate = _DnsTotSOArecUpdate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 32),
    _DnsTotSOArecUpdate_Type()
)
dnsTotSOArecUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotSOArecUpdate.setStatus("current")
_DnsTotCNAMErecUpdate_Type = Counter64
_DnsTotCNAMErecUpdate_Object = MibScalar
dnsTotCNAMErecUpdate = _DnsTotCNAMErecUpdate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 33),
    _DnsTotCNAMErecUpdate_Type()
)
dnsTotCNAMErecUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotCNAMErecUpdate.setStatus("current")
_DnsTotRecUpdate_Type = Counter64
_DnsTotRecUpdate_Object = MibScalar
dnsTotRecUpdate = _DnsTotRecUpdate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 34),
    _DnsTotRecUpdate_Type()
)
dnsTotRecUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotRecUpdate.setStatus("current")
_DnsTotMultiQueryDisableError_Type = Counter64
_DnsTotMultiQueryDisableError_Object = MibScalar
dnsTotMultiQueryDisableError = _DnsTotMultiQueryDisableError_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 35),
    _DnsTotMultiQueryDisableError_Type()
)
dnsTotMultiQueryDisableError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotMultiQueryDisableError.setStatus("current")
_DnsCurArecord_Type = Gauge32
_DnsCurArecord_Object = MibScalar
dnsCurArecord = _DnsCurArecord_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 36),
    _DnsCurArecord_Type()
)
dnsCurArecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCurArecord.setStatus("current")
_DnsCurNSrecord_Type = Gauge32
_DnsCurNSrecord_Object = MibScalar
dnsCurNSrecord = _DnsCurNSrecord_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 37),
    _DnsCurNSrecord_Type()
)
dnsCurNSrecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCurNSrecord.setStatus("current")
_DnsCurMXrecord_Type = Gauge32
_DnsCurMXrecord_Object = MibScalar
dnsCurMXrecord = _DnsCurMXrecord_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 38),
    _DnsCurMXrecord_Type()
)
dnsCurMXrecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCurMXrecord.setStatus("current")
_DnsCurSOArecord_Type = Gauge32
_DnsCurSOArecord_Object = MibScalar
dnsCurSOArecord = _DnsCurSOArecord_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 39),
    _DnsCurSOArecord_Type()
)
dnsCurSOArecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCurSOArecord.setStatus("current")
_DnsCurCNAMErecord_Type = Gauge32
_DnsCurCNAMErecord_Object = MibScalar
dnsCurCNAMErecord = _DnsCurCNAMErecord_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 40),
    _DnsCurCNAMErecord_Type()
)
dnsCurCNAMErecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCurCNAMErecord.setStatus("current")
_DnsCurAuthEntries_Type = Gauge32
_DnsCurAuthEntries_Object = MibScalar
dnsCurAuthEntries = _DnsCurAuthEntries_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 41),
    _DnsCurAuthEntries_Type()
)
dnsCurAuthEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCurAuthEntries.setStatus("current")
_DnsCurNoAuthEntries_Type = Gauge32
_DnsCurNoAuthEntries_Object = MibScalar
dnsCurNoAuthEntries = _DnsCurNoAuthEntries_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 42),
    _DnsCurNoAuthEntries_Type()
)
dnsCurNoAuthEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCurNoAuthEntries.setStatus("current")
_DnsTotAuthAns_Type = Counter64
_DnsTotAuthAns_Object = MibScalar
dnsTotAuthAns = _DnsTotAuthAns_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 43),
    _DnsTotAuthAns_Type()
)
dnsTotAuthAns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotAuthAns.setStatus("current")
_DnsTotAuthNoNames_Type = Counter64
_DnsTotAuthNoNames_Object = MibScalar
dnsTotAuthNoNames = _DnsTotAuthNoNames_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 44),
    _DnsTotAuthNoNames_Type()
)
dnsTotAuthNoNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotAuthNoNames.setStatus("current")
_DnsTotNoDataResps_Type = Counter64
_DnsTotNoDataResps_Object = MibScalar
dnsTotNoDataResps = _DnsTotNoDataResps_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 45),
    _DnsTotNoDataResps_Type()
)
dnsTotNoDataResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotNoDataResps.setStatus("current")
_DnsTotResponseBadLen_Type = Counter64
_DnsTotResponseBadLen_Object = MibScalar
dnsTotResponseBadLen = _DnsTotResponseBadLen_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 46),
    _DnsTotResponseBadLen_Type()
)
dnsTotResponseBadLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotResponseBadLen.setStatus("current")
_DnsTotReqRefusals_Type = Counter64
_DnsTotReqRefusals_Object = MibScalar
dnsTotReqRefusals = _DnsTotReqRefusals_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 47),
    _DnsTotReqRefusals_Type()
)
dnsTotReqRefusals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotReqRefusals.setStatus("current")
_DnsTotOtherErrors_Type = Counter64
_DnsTotOtherErrors_Object = MibScalar
dnsTotOtherErrors = _DnsTotOtherErrors_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 48),
    _DnsTotOtherErrors_Type()
)
dnsTotOtherErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotOtherErrors.setStatus("current")
_DnsTotPTRrecQueries_Type = Counter64
_DnsTotPTRrecQueries_Object = MibScalar
dnsTotPTRrecQueries = _DnsTotPTRrecQueries_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 49),
    _DnsTotPTRrecQueries_Type()
)
dnsTotPTRrecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotPTRrecQueries.setStatus("current")
_DnsTotPTRresponse_Type = Counter64
_DnsTotPTRresponse_Object = MibScalar
dnsTotPTRresponse = _DnsTotPTRresponse_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 50),
    _DnsTotPTRresponse_Type()
)
dnsTotPTRresponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotPTRresponse.setStatus("current")
_DnsTotPTRrecUpdate_Type = Counter64
_DnsTotPTRrecUpdate_Object = MibScalar
dnsTotPTRrecUpdate = _DnsTotPTRrecUpdate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 51),
    _DnsTotPTRrecUpdate_Type()
)
dnsTotPTRrecUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotPTRrecUpdate.setStatus("current")
_DnsTotPTRrecFailed_Type = Counter64
_DnsTotPTRrecFailed_Object = MibScalar
dnsTotPTRrecFailed = _DnsTotPTRrecFailed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 52),
    _DnsTotPTRrecFailed_Type()
)
dnsTotPTRrecFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotPTRrecFailed.setStatus("current")
_DnsCurPTRrecord_Type = Gauge32
_DnsCurPTRrecord_Object = MibScalar
dnsCurPTRrecord = _DnsCurPTRrecord_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 53),
    _DnsCurPTRrecord_Type()
)
dnsCurPTRrecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCurPTRrecord.setStatus("current")
_DnsTotSRVrecQueries_Type = Counter64
_DnsTotSRVrecQueries_Object = MibScalar
dnsTotSRVrecQueries = _DnsTotSRVrecQueries_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 54),
    _DnsTotSRVrecQueries_Type()
)
dnsTotSRVrecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotSRVrecQueries.setStatus("current")
_DnsTotSRVresponse_Type = Counter64
_DnsTotSRVresponse_Object = MibScalar
dnsTotSRVresponse = _DnsTotSRVresponse_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 55),
    _DnsTotSRVresponse_Type()
)
dnsTotSRVresponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotSRVresponse.setStatus("current")
_DnsTotSRVrecUpdate_Type = Counter64
_DnsTotSRVrecUpdate_Object = MibScalar
dnsTotSRVrecUpdate = _DnsTotSRVrecUpdate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 56),
    _DnsTotSRVrecUpdate_Type()
)
dnsTotSRVrecUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotSRVrecUpdate.setStatus("current")
_DnsTotSRVrecFailed_Type = Counter64
_DnsTotSRVrecFailed_Object = MibScalar
dnsTotSRVrecFailed = _DnsTotSRVrecFailed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 57),
    _DnsTotSRVrecFailed_Type()
)
dnsTotSRVrecFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotSRVrecFailed.setStatus("current")
_DnsCurSRVrecord_Type = Gauge32
_DnsCurSRVrecord_Object = MibScalar
dnsCurSRVrecord = _DnsCurSRVrecord_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 58),
    _DnsCurSRVrecord_Type()
)
dnsCurSRVrecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCurSRVrecord.setStatus("current")
_DnsTotAAAArecQueries_Type = Counter64
_DnsTotAAAArecQueries_Object = MibScalar
dnsTotAAAArecQueries = _DnsTotAAAArecQueries_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 59),
    _DnsTotAAAArecQueries_Type()
)
dnsTotAAAArecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotAAAArecQueries.setStatus("current")
_DnsTotAAAAresponse_Type = Counter64
_DnsTotAAAAresponse_Object = MibScalar
dnsTotAAAAresponse = _DnsTotAAAAresponse_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 60),
    _DnsTotAAAAresponse_Type()
)
dnsTotAAAAresponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotAAAAresponse.setStatus("current")
_DnsTotAAAArecUpdate_Type = Counter64
_DnsTotAAAArecUpdate_Object = MibScalar
dnsTotAAAArecUpdate = _DnsTotAAAArecUpdate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 61),
    _DnsTotAAAArecUpdate_Type()
)
dnsTotAAAArecUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotAAAArecUpdate.setStatus("current")
_DnsTotAAAArecFailed_Type = Counter64
_DnsTotAAAArecFailed_Object = MibScalar
dnsTotAAAArecFailed = _DnsTotAAAArecFailed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 62),
    _DnsTotAAAArecFailed_Type()
)
dnsTotAAAArecFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotAAAArecFailed.setStatus("current")
_DnsCurAAAArecord_Type = Gauge32
_DnsCurAAAArecord_Object = MibScalar
dnsCurAAAArecord = _DnsCurAAAArecord_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 63),
    _DnsCurAAAArecord_Type()
)
dnsCurAAAArecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCurAAAArecord.setStatus("current")
_DnsTotANYqueries_Type = Counter64
_DnsTotANYqueries_Object = MibScalar
dnsTotANYqueries = _DnsTotANYqueries_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 64),
    _DnsTotANYqueries_Type()
)
dnsTotANYqueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotANYqueries.setStatus("current")
_DnsTotANYresponse_Type = Counter64
_DnsTotANYresponse_Object = MibScalar
dnsTotANYresponse = _DnsTotANYresponse_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 65),
    _DnsTotANYresponse_Type()
)
dnsTotANYresponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotANYresponse.setStatus("current")
_DnsTotANYrecFailed_Type = Counter64
_DnsTotANYrecFailed_Object = MibScalar
dnsTotANYrecFailed = _DnsTotANYrecFailed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 66),
    _DnsTotANYrecFailed_Type()
)
dnsTotANYrecFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotANYrecFailed.setStatus("current")
_DnsTotSOArecFailed_Type = Counter64
_DnsTotSOArecFailed_Object = MibScalar
dnsTotSOArecFailed = _DnsTotSOArecFailed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 53, 1, 67),
    _DnsTotSOArecFailed_Type()
)
dnsTotSOArecFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotSOArecFailed.setStatus("current")
_NsIfStatsTable_Object = MibTable
nsIfStatsTable = _NsIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54)
)
if mibBuilder.loadTexts:
    nsIfStatsTable.setStatus("current")
_NsIfStatsEntry_Object = MibTableRow
nsIfStatsEntry = _NsIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1)
)
nsIfStatsEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "ifName"),
)
if mibBuilder.loadTexts:
    nsIfStatsEntry.setStatus("current")
_IfName_Type = OctetString
_IfName_Object = MibTableColumn
ifName = _IfName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 1),
    _IfName_Type()
)
ifName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifName.setStatus("current")
_IfMedia_Type = OctetString
_IfMedia_Object = MibTableColumn
ifMedia = _IfMedia_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 2),
    _IfMedia_Type()
)
ifMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMedia.setStatus("current")
_IfTotRxBytes_Type = Counter64
_IfTotRxBytes_Object = MibTableColumn
ifTotRxBytes = _IfTotRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 3),
    _IfTotRxBytes_Type()
)
ifTotRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTotRxBytes.setStatus("current")
_IfRxAvgBandwidthUsage_Type = Gauge32
_IfRxAvgBandwidthUsage_Object = MibTableColumn
ifRxAvgBandwidthUsage = _IfRxAvgBandwidthUsage_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 4),
    _IfRxAvgBandwidthUsage_Type()
)
ifRxAvgBandwidthUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxAvgBandwidthUsage.setStatus("current")
_IfTotRxPkts_Type = Counter64
_IfTotRxPkts_Object = MibTableColumn
ifTotRxPkts = _IfTotRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 5),
    _IfTotRxPkts_Type()
)
ifTotRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTotRxPkts.setStatus("current")
_IfRxAvgPacketRate_Type = Gauge32
_IfRxAvgPacketRate_Object = MibTableColumn
ifRxAvgPacketRate = _IfRxAvgPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 6),
    _IfRxAvgPacketRate_Type()
)
ifRxAvgPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxAvgPacketRate.setStatus("current")
_IfTotTxBytes_Type = Counter64
_IfTotTxBytes_Object = MibTableColumn
ifTotTxBytes = _IfTotTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 7),
    _IfTotTxBytes_Type()
)
ifTotTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTotTxBytes.setStatus("current")
_IfTxAvgBandwidthUsage_Type = Gauge32
_IfTxAvgBandwidthUsage_Object = MibTableColumn
ifTxAvgBandwidthUsage = _IfTxAvgBandwidthUsage_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 8),
    _IfTxAvgBandwidthUsage_Type()
)
ifTxAvgBandwidthUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTxAvgBandwidthUsage.setStatus("current")
_IfTotTxPkts_Type = Counter64
_IfTotTxPkts_Object = MibTableColumn
ifTotTxPkts = _IfTotTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 9),
    _IfTotTxPkts_Type()
)
ifTotTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTotTxPkts.setStatus("current")
_IfTxAvgPacketRate_Type = Gauge32
_IfTxAvgPacketRate_Object = MibTableColumn
ifTxAvgPacketRate = _IfTxAvgPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 10),
    _IfTxAvgPacketRate_Type()
)
ifTxAvgPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTxAvgPacketRate.setStatus("current")
_IfRxCRCErrors_Type = Counter64
_IfRxCRCErrors_Object = MibTableColumn
ifRxCRCErrors = _IfRxCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 11),
    _IfRxCRCErrors_Type()
)
ifRxCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxCRCErrors.setStatus("current")
_IfRxFrameErrors_Type = Counter64
_IfRxFrameErrors_Object = MibTableColumn
ifRxFrameErrors = _IfRxFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 12),
    _IfRxFrameErrors_Type()
)
ifRxFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxFrameErrors.setStatus("current")
_IfRxAlignmentErrors_Type = Counter64
_IfRxAlignmentErrors_Object = MibTableColumn
ifRxAlignmentErrors = _IfRxAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 13),
    _IfRxAlignmentErrors_Type()
)
ifRxAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxAlignmentErrors.setStatus("current")
_IfTxCollisions_Type = Counter64
_IfTxCollisions_Object = MibTableColumn
ifTxCollisions = _IfTxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 14),
    _IfTxCollisions_Type()
)
ifTxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTxCollisions.setStatus("current")
_IfTxExcessCollisions_Type = Counter64
_IfTxExcessCollisions_Object = MibTableColumn
ifTxExcessCollisions = _IfTxExcessCollisions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 15),
    _IfTxExcessCollisions_Type()
)
ifTxExcessCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTxExcessCollisions.setStatus("current")
_IfTxLateCollisions_Type = Counter64
_IfTxLateCollisions_Object = MibTableColumn
ifTxLateCollisions = _IfTxLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 16),
    _IfTxLateCollisions_Type()
)
ifTxLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTxLateCollisions.setStatus("current")
_IfTxMultiCollisionErrors_Type = Counter64
_IfTxMultiCollisionErrors_Object = MibTableColumn
ifTxMultiCollisionErrors = _IfTxMultiCollisionErrors_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 17),
    _IfTxMultiCollisionErrors_Type()
)
ifTxMultiCollisionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTxMultiCollisionErrors.setStatus("current")
_IfTxCarrierError_Type = Counter64
_IfTxCarrierError_Object = MibTableColumn
ifTxCarrierError = _IfTxCarrierError_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 18),
    _IfTxCarrierError_Type()
)
ifTxCarrierError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTxCarrierError.setStatus("current")
_IfTotRxMbits_Type = Counter64
_IfTotRxMbits_Object = MibTableColumn
ifTotRxMbits = _IfTotRxMbits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 19),
    _IfTotRxMbits_Type()
)
ifTotRxMbits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTotRxMbits.setStatus("current")
_IfTotTxMbits_Type = Counter64
_IfTotTxMbits_Object = MibTableColumn
ifTotTxMbits = _IfTotTxMbits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 20),
    _IfTotTxMbits_Type()
)
ifTotTxMbits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTotTxMbits.setStatus("current")
_IfTotNetScalerPkts_Type = Counter64
_IfTotNetScalerPkts_Object = MibTableColumn
ifTotNetScalerPkts = _IfTotNetScalerPkts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 21),
    _IfTotNetScalerPkts_Type()
)
ifTotNetScalerPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTotNetScalerPkts.setStatus("current")
_IfErrDroppedRxPkts_Type = Counter64
_IfErrDroppedRxPkts_Object = MibTableColumn
ifErrDroppedRxPkts = _IfErrDroppedRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 22),
    _IfErrDroppedRxPkts_Type()
)
ifErrDroppedRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifErrDroppedRxPkts.setStatus("current")
_IfErrLinkHangs_Type = Counter32
_IfErrLinkHangs_Object = MibTableColumn
ifErrLinkHangs = _IfErrLinkHangs_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 23),
    _IfErrLinkHangs_Type()
)
ifErrLinkHangs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifErrLinkHangs.setStatus("current")
_IfLinkReinits_Type = Counter32
_IfLinkReinits_Object = MibTableColumn
ifLinkReinits = _IfLinkReinits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 24),
    _IfLinkReinits_Type()
)
ifLinkReinits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifLinkReinits.setStatus("current")
_IfErrDuplexMismatch_Type = Counter32
_IfErrDuplexMismatch_Object = MibTableColumn
ifErrDuplexMismatch = _IfErrDuplexMismatch_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 25),
    _IfErrDuplexMismatch_Type()
)
ifErrDuplexMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifErrDuplexMismatch.setStatus("current")
_IfErrCongestedPktsDrops_Type = Counter64
_IfErrCongestedPktsDrops_Object = MibTableColumn
ifErrCongestedPktsDrops = _IfErrCongestedPktsDrops_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 26),
    _IfErrCongestedPktsDrops_Type()
)
ifErrCongestedPktsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifErrCongestedPktsDrops.setStatus("current")
_IfErrCongestionLimitPktDrops_Type = Counter64
_IfErrCongestionLimitPktDrops_Object = MibTableColumn
ifErrCongestionLimitPktDrops = _IfErrCongestionLimitPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 27),
    _IfErrCongestionLimitPktDrops_Type()
)
ifErrCongestionLimitPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifErrCongestionLimitPktDrops.setStatus("current")
_IfErrPktRx_Type = Counter64
_IfErrPktRx_Object = MibTableColumn
ifErrPktRx = _IfErrPktRx_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 28),
    _IfErrPktRx_Type()
)
ifErrPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifErrPktRx.setStatus("current")
_IfErrRxFIFO_Type = Counter64
_IfErrRxFIFO_Object = MibTableColumn
ifErrRxFIFO = _IfErrRxFIFO_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 29),
    _IfErrRxFIFO_Type()
)
ifErrRxFIFO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifErrRxFIFO.setStatus("current")
_IfErrRxNoBuffs_Type = Counter64
_IfErrRxNoBuffs_Object = MibTableColumn
ifErrRxNoBuffs = _IfErrRxNoBuffs_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 30),
    _IfErrRxNoBuffs_Type()
)
ifErrRxNoBuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifErrRxNoBuffs.setStatus("current")
_IfErrTxNoNSB_Type = Counter64
_IfErrTxNoNSB_Object = MibTableColumn
ifErrTxNoNSB = _IfErrTxNoNSB_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 31),
    _IfErrTxNoNSB_Type()
)
ifErrTxNoNSB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifErrTxNoNSB.setStatus("current")
_IfErrRxFCS_Type = Counter64
_IfErrRxFCS_Object = MibTableColumn
ifErrRxFCS = _IfErrRxFCS_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 32),
    _IfErrRxFCS_Type()
)
ifErrRxFCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifErrRxFCS.setStatus("current")
_IfErrPktTx_Type = Counter64
_IfErrPktTx_Object = MibTableColumn
ifErrPktTx = _IfErrPktTx_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 33),
    _IfErrPktTx_Type()
)
ifErrPktTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifErrPktTx.setStatus("current")
_IfErrTxFIFO_Type = Counter64
_IfErrTxFIFO_Object = MibTableColumn
ifErrTxFIFO = _IfErrTxFIFO_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 34),
    _IfErrTxFIFO_Type()
)
ifErrTxFIFO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifErrTxFIFO.setStatus("current")
_IfErrTxHeartBeat_Type = Counter64
_IfErrTxHeartBeat_Object = MibTableColumn
ifErrTxHeartBeat = _IfErrTxHeartBeat_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 35),
    _IfErrTxHeartBeat_Type()
)
ifErrTxHeartBeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifErrTxHeartBeat.setStatus("current")
_IfErrTxOverflow_Type = Counter64
_IfErrTxOverflow_Object = MibTableColumn
ifErrTxOverflow = _IfErrTxOverflow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 36),
    _IfErrTxOverflow_Type()
)
ifErrTxOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifErrTxOverflow.setStatus("current")
_IfErrTxDeferred_Type = Counter64
_IfErrTxDeferred_Object = MibTableColumn
ifErrTxDeferred = _IfErrTxDeferred_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 37),
    _IfErrTxDeferred_Type()
)
ifErrTxDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifErrTxDeferred.setStatus("current")
_IfErrDroppedTxPkts_Type = Counter64
_IfErrDroppedTxPkts_Object = MibTableColumn
ifErrDroppedTxPkts = _IfErrDroppedTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 38),
    _IfErrDroppedTxPkts_Type()
)
ifErrDroppedTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifErrDroppedTxPkts.setStatus("current")
_IfTotRxXonPause_Type = Counter64
_IfTotRxXonPause_Object = MibTableColumn
ifTotRxXonPause = _IfTotRxXonPause_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 39),
    _IfTotRxXonPause_Type()
)
ifTotRxXonPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTotRxXonPause.setStatus("current")
_IfTotRxXoffPause_Type = Counter64
_IfTotRxXoffPause_Object = MibTableColumn
ifTotRxXoffPause = _IfTotRxXoffPause_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 40),
    _IfTotRxXoffPause_Type()
)
ifTotRxXoffPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTotRxXoffPause.setStatus("current")
_IfTotXoffStateEntered_Type = Counter64
_IfTotXoffStateEntered_Object = MibTableColumn
ifTotXoffStateEntered = _IfTotXoffStateEntered_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 41),
    _IfTotXoffStateEntered_Type()
)
ifTotXoffStateEntered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTotXoffStateEntered.setStatus("current")
_IfTotXonSent_Type = Counter64
_IfTotXonSent_Object = MibTableColumn
ifTotXonSent = _IfTotXonSent_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 42),
    _IfTotXonSent_Type()
)
ifTotXonSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTotXonSent.setStatus("current")
_IfTotXoffSent_Type = Counter64
_IfTotXoffSent_Object = MibTableColumn
ifTotXoffSent = _IfTotXoffSent_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 43),
    _IfTotXoffSent_Type()
)
ifTotXoffSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTotXoffSent.setStatus("current")
_IfnicStsStalls_Type = Counter32
_IfnicStsStalls_Object = MibTableColumn
ifnicStsStalls = _IfnicStsStalls_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 44),
    _IfnicStsStalls_Type()
)
ifnicStsStalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifnicStsStalls.setStatus("current")
_IfnicTxStalls_Type = Counter32
_IfnicTxStalls_Object = MibTableColumn
ifnicTxStalls = _IfnicTxStalls_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 45),
    _IfnicTxStalls_Type()
)
ifnicTxStalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifnicTxStalls.setStatus("current")
_IfnicRxStalls_Type = Counter32
_IfnicRxStalls_Object = MibTableColumn
ifnicRxStalls = _IfnicRxStalls_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 46),
    _IfnicRxStalls_Type()
)
ifnicRxStalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifnicRxStalls.setStatus("current")
_IfnicErrDisables_Type = Counter32
_IfnicErrDisables_Object = MibTableColumn
ifnicErrDisables = _IfnicErrDisables_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 47),
    _IfnicErrDisables_Type()
)
ifnicErrDisables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifnicErrDisables.setStatus("current")
_IfThroughput_Type = Gauge32
_IfThroughput_Object = MibTableColumn
ifThroughput = _IfThroughput_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 48),
    _IfThroughput_Type()
)
ifThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifThroughput.setStatus("current")
_IfMinThroughput_Type = Integer32
_IfMinThroughput_Object = MibTableColumn
ifMinThroughput = _IfMinThroughput_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 54, 1, 49),
    _IfMinThroughput_Type()
)
ifMinThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMinThroughput.setStatus("current")
_NsScPolicyGroup_ObjectIdentity = ObjectIdentity
nsScPolicyGroup = _NsScPolicyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 55)
)
_ScPolicyStatistics_ObjectIdentity = ObjectIdentity
scPolicyStatistics = _ScPolicyStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 55, 1)
)
_ScPolicyUrlHits_Type = Counter64
_ScPolicyUrlHits_Object = MibScalar
scPolicyUrlHits = _ScPolicyUrlHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 55, 1, 1),
    _ScPolicyUrlHits_Type()
)
scPolicyUrlHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scPolicyUrlHits.setStatus("current")
_ScPopUps_Type = Counter64
_ScPopUps_Object = MibScalar
scPopUps = _ScPopUps_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 55, 1, 2),
    _ScPopUps_Type()
)
scPopUps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scPopUps.setStatus("current")
_ScAltContUrls_Type = Counter64
_ScAltContUrls_Object = MibScalar
scAltContUrls = _ScAltContUrls_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 55, 1, 3),
    _ScAltContUrls_Type()
)
scAltContUrls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scAltContUrls.setStatus("current")
_ScSessionReqs_Type = Counter64
_ScSessionReqs_Object = MibScalar
scSessionReqs = _ScSessionReqs_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 55, 1, 4),
    _ScSessionReqs_Type()
)
scSessionReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scSessionReqs.setStatus("current")
_ScPostReqs_Type = Counter64
_ScPostReqs_Object = MibScalar
scPostReqs = _ScPostReqs_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 55, 1, 5),
    _ScPostReqs_Type()
)
scPostReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scPostReqs.setStatus("current")
_ScThresholdFail_Type = Counter64
_ScThresholdFail_Object = MibScalar
scThresholdFail = _ScThresholdFail_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 55, 1, 6),
    _ScThresholdFail_Type()
)
scThresholdFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scThresholdFail.setStatus("current")
_ScFaultyCookies_Type = Counter64
_ScFaultyCookies_Object = MibScalar
scFaultyCookies = _ScFaultyCookies_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 55, 1, 7),
    _ScFaultyCookies_Type()
)
scFaultyCookies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scFaultyCookies.setStatus("current")
_ScUnSupBrow_Type = Counter64
_ScUnSupBrow_Object = MibScalar
scUnSupBrow = _ScUnSupBrow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 55, 1, 8),
    _ScUnSupBrow_Type()
)
scUnSupBrow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scUnSupBrow.setStatus("current")
_ScResetStats_Type = Counter64
_ScResetStats_Object = MibScalar
scResetStats = _ScResetStats_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 55, 1, 9),
    _ScResetStats_Type()
)
scResetStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scResetStats.setStatus("current")
_ScTotCondTriggered_Type = Counter64
_ScTotCondTriggered_Object = MibScalar
scTotCondTriggered = _ScTotCondTriggered_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 55, 1, 10),
    _ScTotCondTriggered_Type()
)
scTotCondTriggered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scTotCondTriggered.setStatus("current")
_ScTotReissuedRequests_Type = Counter64
_ScTotReissuedRequests_Object = MibScalar
scTotReissuedRequests = _ScTotReissuedRequests_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 55, 1, 11),
    _ScTotReissuedRequests_Type()
)
scTotReissuedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scTotReissuedRequests.setStatus("current")
_ScPolicyConfig_ObjectIdentity = ObjectIdentity
scPolicyConfig = _ScPolicyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 55, 2)
)
_ScPolicyConfigTable_Object = MibTable
scPolicyConfigTable = _ScPolicyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 55, 2, 1)
)
if mibBuilder.loadTexts:
    scPolicyConfigTable.setStatus("current")
_ScPolicyConfigEntry_Object = MibTableRow
scPolicyConfigEntry = _ScPolicyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 55, 2, 1, 1)
)
scPolicyConfigEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "scPolicyName"),
)
if mibBuilder.loadTexts:
    scPolicyConfigEntry.setStatus("current")
_ScPolicyName_Type = OctetString
_ScPolicyName_Object = MibTableColumn
scPolicyName = _ScPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 55, 2, 1, 1, 1),
    _ScPolicyName_Type()
)
scPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scPolicyName.setStatus("current")
_ScPolUrl_Type = OctetString
_ScPolUrl_Object = MibTableColumn
scPolUrl = _ScPolUrl_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 55, 2, 1, 1, 2),
    _ScPolUrl_Type()
)
scPolUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scPolUrl.setStatus("current")
_ScDelayThreshold_Type = Integer32
_ScDelayThreshold_Object = MibTableColumn
scDelayThreshold = _ScDelayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 55, 2, 1, 1, 3),
    _ScDelayThreshold_Type()
)
scDelayThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDelayThreshold.setStatus("current")
_ScMaxConnections_Type = Integer32
_ScMaxConnections_Object = MibTableColumn
scMaxConnections = _ScMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 55, 2, 1, 1, 4),
    _ScMaxConnections_Type()
)
scMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scMaxConnections.setStatus("current")
_ScActionType_Type = ActionType
_ScActionType_Object = MibTableColumn
scActionType = _ScActionType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 55, 2, 1, 1, 5),
    _ScActionType_Type()
)
scActionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scActionType.setStatus("current")
_ScAlternateContentServiceName_Type = OctetString
_ScAlternateContentServiceName_Object = MibTableColumn
scAlternateContentServiceName = _ScAlternateContentServiceName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 55, 2, 1, 1, 6),
    _ScAlternateContentServiceName_Type()
)
scAlternateContentServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scAlternateContentServiceName.setStatus("current")
_ScRuleName_Type = OctetString
_ScRuleName_Object = MibTableColumn
scRuleName = _ScRuleName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 55, 2, 1, 1, 7),
    _ScRuleName_Type()
)
scRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scRuleName.setStatus("current")
_ScAlternateContentPath_Type = OctetString
_ScAlternateContentPath_Object = MibTableColumn
scAlternateContentPath = _ScAlternateContentPath_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 55, 2, 1, 1, 8),
    _ScAlternateContentPath_Type()
)
scAlternateContentPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scAlternateContentPath.setStatus("current")
_NsSslConfigGroup_ObjectIdentity = ObjectIdentity
nsSslConfigGroup = _NsSslConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 56)
)
_SslCertKeyTable_Object = MibTable
sslCertKeyTable = _SslCertKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 56, 1)
)
if mibBuilder.loadTexts:
    sslCertKeyTable.setStatus("current")
_SslCertKeyEntry_Object = MibTableRow
sslCertKeyEntry = _SslCertKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 56, 1, 1)
)
sslCertKeyEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "sslCertKeyName"),
)
if mibBuilder.loadTexts:
    sslCertKeyEntry.setStatus("current")
_SslCertKeyName_Type = OctetString
_SslCertKeyName_Object = MibTableColumn
sslCertKeyName = _SslCertKeyName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 56, 1, 1, 1),
    _SslCertKeyName_Type()
)
sslCertKeyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCertKeyName.setStatus("current")
_SslCertPath_Type = OctetString
_SslCertPath_Object = MibTableColumn
sslCertPath = _SslCertPath_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 56, 1, 1, 2),
    _SslCertPath_Type()
)
sslCertPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCertPath.setStatus("current")
_SslKeyPath_Type = OctetString
_SslKeyPath_Object = MibTableColumn
sslKeyPath = _SslKeyPath_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 56, 1, 1, 3),
    _SslKeyPath_Type()
)
sslKeyPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslKeyPath.setStatus("current")
_SslInputFormat_Type = InputFormat
_SslInputFormat_Object = MibTableColumn
sslInputFormat = _SslInputFormat_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 56, 1, 1, 4),
    _SslInputFormat_Type()
)
sslInputFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslInputFormat.setStatus("current")
_SslDaysToExpire_Type = Integer32
_SslDaysToExpire_Object = MibTableColumn
sslDaysToExpire = _SslDaysToExpire_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 56, 1, 1, 5),
    _SslDaysToExpire_Type()
)
sslDaysToExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslDaysToExpire.setStatus("current")
_SslCrlTable_Object = MibTable
sslCrlTable = _SslCrlTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 56, 2)
)
if mibBuilder.loadTexts:
    sslCrlTable.setStatus("current")
_SslCrlEntry_Object = MibTableRow
sslCrlEntry = _SslCrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 56, 2, 1)
)
sslCrlEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "sslCrlName"),
)
if mibBuilder.loadTexts:
    sslCrlEntry.setStatus("current")
_SslCrlName_Type = OctetString
_SslCrlName_Object = MibTableColumn
sslCrlName = _SslCrlName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 56, 2, 1, 1),
    _SslCrlName_Type()
)
sslCrlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCrlName.setStatus("current")
_SslCrlPath_Type = OctetString
_SslCrlPath_Object = MibTableColumn
sslCrlPath = _SslCrlPath_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 56, 2, 1, 2),
    _SslCrlPath_Type()
)
sslCrlPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCrlPath.setStatus("current")
_SslCrlInputFormat_Type = InputFormat
_SslCrlInputFormat_Object = MibTableColumn
sslCrlInputFormat = _SslCrlInputFormat_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 56, 2, 1, 3),
    _SslCrlInputFormat_Type()
)
sslCrlInputFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCrlInputFormat.setStatus("current")
_SslCipherGroupTable_Object = MibTable
sslCipherGroupTable = _SslCipherGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 56, 3)
)
if mibBuilder.loadTexts:
    sslCipherGroupTable.setStatus("current")
_SslCipherGroupEntry_Object = MibTableRow
sslCipherGroupEntry = _SslCipherGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 56, 3, 1)
)
sslCipherGroupEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "sslCipherGroupName"),
    (0, "NS-ROOT-MIB", "sslCipherName"),
)
if mibBuilder.loadTexts:
    sslCipherGroupEntry.setStatus("current")
_SslCipherGroupName_Type = OctetString
_SslCipherGroupName_Object = MibTableColumn
sslCipherGroupName = _SslCipherGroupName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 56, 3, 1, 1),
    _SslCipherGroupName_Type()
)
sslCipherGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherGroupName.setStatus("current")
_SslCipherName_Type = OctetString
_SslCipherName_Object = MibTableColumn
sslCipherName = _SslCipherName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 56, 3, 1, 2),
    _SslCipherName_Type()
)
sslCipherName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherName.setStatus("current")
_SslCipherDesc_Type = OctetString
_SslCipherDesc_Object = MibTableColumn
sslCipherDesc = _SslCipherDesc_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 56, 3, 1, 3),
    _SslCipherDesc_Type()
)
sslCipherDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherDesc.setStatus("current")
_NsDosPolicyGroup_ObjectIdentity = ObjectIdentity
nsDosPolicyGroup = _NsDosPolicyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 57)
)
_DosPolicyTable_Object = MibTable
dosPolicyTable = _DosPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 57, 1)
)
if mibBuilder.loadTexts:
    dosPolicyTable.setStatus("current")
_DosPolicyEntry_Object = MibTableRow
dosPolicyEntry = _DosPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 57, 1, 1)
)
dosPolicyEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "dosPolicyName"),
)
if mibBuilder.loadTexts:
    dosPolicyEntry.setStatus("current")
_DosPolicyName_Type = OctetString
_DosPolicyName_Object = MibTableColumn
dosPolicyName = _DosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 57, 1, 1, 1),
    _DosPolicyName_Type()
)
dosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosPolicyName.setStatus("current")
_ThresholdValue_Type = Integer32
_ThresholdValue_Object = MibTableColumn
thresholdValue = _ThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 57, 1, 1, 2),
    _ThresholdValue_Type()
)
thresholdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdValue.setStatus("current")
_DosPolicyStatistics_ObjectIdentity = ObjectIdentity
dosPolicyStatistics = _DosPolicyStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 57, 2)
)
_DosTotConditionTriggered_Type = Counter64
_DosTotConditionTriggered_Object = MibScalar
dosTotConditionTriggered = _DosTotConditionTriggered_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 57, 2, 1),
    _DosTotConditionTriggered_Type()
)
dosTotConditionTriggered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosTotConditionTriggered.setStatus("current")
_DosTotValidCookies_Type = Counter64
_DosTotValidCookies_Object = MibScalar
dosTotValidCookies = _DosTotValidCookies_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 57, 2, 2),
    _DosTotValidCookies_Type()
)
dosTotValidCookies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosTotValidCookies.setStatus("current")
_DosTotDosPriorityClients_Type = Counter64
_DosTotDosPriorityClients_Object = MibScalar
dosTotDosPriorityClients = _DosTotDosPriorityClients_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 57, 2, 3),
    _DosTotDosPriorityClients_Type()
)
dosTotDosPriorityClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosTotDosPriorityClients.setStatus("current")
_DosAvgValidClients_Type = Gauge32
_DosAvgValidClients_Object = MibScalar
dosAvgValidClients = _DosAvgValidClients_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 57, 2, 4),
    _DosAvgValidClients_Type()
)
dosAvgValidClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosAvgValidClients.setStatus("current")
_DosAvgDospriClients_Type = Gauge32
_DosAvgDospriClients_Object = MibScalar
dosAvgDospriClients = _DosAvgDospriClients_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 57, 2, 5),
    _DosAvgDospriClients_Type()
)
dosAvgDospriClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosAvgDospriClients.setStatus("current")
_NsExpressionTable_Object = MibTable
nsExpressionTable = _NsExpressionTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 58)
)
if mibBuilder.loadTexts:
    nsExpressionTable.setStatus("current")
_NsExpressionEntry_Object = MibTableRow
nsExpressionEntry = _NsExpressionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 58, 1)
)
nsExpressionEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "expressionName"),
)
if mibBuilder.loadTexts:
    nsExpressionEntry.setStatus("current")
_ExpressionName_Type = OctetString
_ExpressionName_Object = MibTableColumn
expressionName = _ExpressionName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 58, 1, 1),
    _ExpressionName_Type()
)
expressionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressionName.setStatus("current")
_ExpressionTotalHits_Type = Counter64
_ExpressionTotalHits_Object = MibTableColumn
expressionTotalHits = _ExpressionTotalHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 58, 1, 2),
    _ExpressionTotalHits_Type()
)
expressionTotalHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressionTotalHits.setStatus("current")
_NsPqPolicyGroup_ObjectIdentity = ObjectIdentity
nsPqPolicyGroup = _NsPqPolicyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 59)
)
_PqPolicyConfigTable_Object = MibTable
pqPolicyConfigTable = _PqPolicyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 59, 1)
)
if mibBuilder.loadTexts:
    pqPolicyConfigTable.setStatus("current")
_PqPolicyConfigEntry_Object = MibTableRow
pqPolicyConfigEntry = _PqPolicyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 59, 1, 1)
)
pqPolicyConfigEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "pqName"),
)
if mibBuilder.loadTexts:
    pqPolicyConfigEntry.setStatus("current")
_PqName_Type = OctetString
_PqName_Object = MibTableColumn
pqName = _PqName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 59, 1, 1, 1),
    _PqName_Type()
)
pqName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqName.setStatus("current")
_PqRuleName_Type = OctetString
_PqRuleName_Object = MibTableColumn
pqRuleName = _PqRuleName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 59, 1, 1, 2),
    _PqRuleName_Type()
)
pqRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqRuleName.setStatus("current")
_PqQdepthThreshold_Type = Integer32
_PqQdepthThreshold_Object = MibTableColumn
pqQdepthThreshold = _PqQdepthThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 59, 1, 1, 3),
    _PqQdepthThreshold_Type()
)
pqQdepthThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqQdepthThreshold.setStatus("current")
_PqPolQdepthThreshold_Type = Integer32
_PqPolQdepthThreshold_Object = MibTableColumn
pqPolQdepthThreshold = _PqPolQdepthThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 59, 1, 1, 4),
    _PqPolQdepthThreshold_Type()
)
pqPolQdepthThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqPolQdepthThreshold.setStatus("current")
_PqPriority_Type = Integer32
_PqPriority_Object = MibTableColumn
pqPriority = _PqPriority_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 59, 1, 1, 5),
    _PqPriority_Type()
)
pqPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqPriority.setStatus("current")
_PqPolicyWeight_Type = Integer32
_PqPolicyWeight_Object = MibTableColumn
pqPolicyWeight = _PqPolicyWeight_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 59, 1, 1, 6),
    _PqPolicyWeight_Type()
)
pqPolicyWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqPolicyWeight.setStatus("current")
_PqPolicyStatistics_ObjectIdentity = ObjectIdentity
pqPolicyStatistics = _PqPolicyStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 59, 2)
)
_PqTotalPolicyMatches_Type = Counter64
_PqTotalPolicyMatches_Object = MibScalar
pqTotalPolicyMatches = _PqTotalPolicyMatches_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 59, 2, 1),
    _PqTotalPolicyMatches_Type()
)
pqTotalPolicyMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqTotalPolicyMatches.setStatus("current")
_PqTotalThresholdFailed_Type = Counter64
_PqTotalThresholdFailed_Object = MibScalar
pqTotalThresholdFailed = _PqTotalThresholdFailed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 59, 2, 2),
    _PqTotalThresholdFailed_Type()
)
pqTotalThresholdFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqTotalThresholdFailed.setStatus("current")
_PqPriority1Requests_Type = Counter64
_PqPriority1Requests_Object = MibScalar
pqPriority1Requests = _PqPriority1Requests_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 59, 2, 3),
    _PqPriority1Requests_Type()
)
pqPriority1Requests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqPriority1Requests.setStatus("current")
_PqPriority2Requests_Type = Counter64
_PqPriority2Requests_Object = MibScalar
pqPriority2Requests = _PqPriority2Requests_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 59, 2, 4),
    _PqPriority2Requests_Type()
)
pqPriority2Requests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqPriority2Requests.setStatus("current")
_PqPriority3Requests_Type = Counter64
_PqPriority3Requests_Object = MibScalar
pqPriority3Requests = _PqPriority3Requests_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 59, 2, 5),
    _PqPriority3Requests_Type()
)
pqPriority3Requests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqPriority3Requests.setStatus("current")
_CrConfigGroup_ObjectIdentity = ObjectIdentity
crConfigGroup = _CrConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 60)
)
_CrPolicyMapConfigTable_Object = MibTable
crPolicyMapConfigTable = _CrPolicyMapConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 60, 1)
)
if mibBuilder.loadTexts:
    crPolicyMapConfigTable.setStatus("current")
_CrPolicyMapConfigEntry_Object = MibTableRow
crPolicyMapConfigEntry = _CrPolicyMapConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 60, 1, 1)
)
crPolicyMapConfigEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "crMapName"),
)
if mibBuilder.loadTexts:
    crPolicyMapConfigEntry.setStatus("current")
_CrMapName_Type = OctetString
_CrMapName_Object = MibTableColumn
crMapName = _CrMapName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 60, 1, 1, 1),
    _CrMapName_Type()
)
crMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crMapName.setStatus("current")
_CrMapSrcName_Type = OctetString
_CrMapSrcName_Object = MibTableColumn
crMapSrcName = _CrMapSrcName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 60, 1, 1, 2),
    _CrMapSrcName_Type()
)
crMapSrcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crMapSrcName.setStatus("current")
_CrMapDstName_Type = OctetString
_CrMapDstName_Object = MibTableColumn
crMapDstName = _CrMapDstName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 60, 1, 1, 3),
    _CrMapDstName_Type()
)
crMapDstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crMapDstName.setStatus("current")
_CrMapSrcUrl_Type = OctetString
_CrMapSrcUrl_Object = MibTableColumn
crMapSrcUrl = _CrMapSrcUrl_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 60, 1, 1, 4),
    _CrMapSrcUrl_Type()
)
crMapSrcUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crMapSrcUrl.setStatus("current")
_CrMapDstUrl_Type = OctetString
_CrMapDstUrl_Object = MibTableColumn
crMapDstUrl = _CrMapDstUrl_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 60, 1, 1, 5),
    _CrMapDstUrl_Type()
)
crMapDstUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crMapDstUrl.setStatus("current")
_MonitorCount_Type = Integer32
_MonitorCount_Object = MibScalar
monitorCount = _MonitorCount_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 61),
    _MonitorCount_Type()
)
monitorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorCount.setStatus("current")
_MonitorBindCount_Type = Integer32
_MonitorBindCount_Object = MibScalar
monitorBindCount = _MonitorBindCount_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 62),
    _MonitorBindCount_Type()
)
monitorBindCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorBindCount.setStatus("current")
_HtmlInjectionStatsGroup_ObjectIdentity = ObjectIdentity
htmlInjectionStatsGroup = _HtmlInjectionStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 63)
)
_HtmlInjectedBytes_Type = Counter64
_HtmlInjectedBytes_Object = MibScalar
htmlInjectedBytes = _HtmlInjectedBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 63, 1),
    _HtmlInjectedBytes_Type()
)
htmlInjectedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htmlInjectedBytes.setStatus("current")
_HtmlInjectionSessions_Type = Counter64
_HtmlInjectionSessions_Object = MibScalar
htmlInjectionSessions = _HtmlInjectionSessions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 63, 2),
    _HtmlInjectionSessions_Type()
)
htmlInjectionSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htmlInjectionSessions.setStatus("current")
_HtmlInjectionTotalSessions_Type = Counter64
_HtmlInjectionTotalSessions_Object = MibScalar
htmlInjectionTotalSessions = _HtmlInjectionTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 63, 3),
    _HtmlInjectionTotalSessions_Type()
)
htmlInjectionTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htmlInjectionTotalSessions.setStatus("current")
_HtmlInjectMemAllocFailed_Type = Counter64
_HtmlInjectMemAllocFailed_Object = MibScalar
htmlInjectMemAllocFailed = _HtmlInjectMemAllocFailed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 63, 4),
    _HtmlInjectMemAllocFailed_Type()
)
htmlInjectMemAllocFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htmlInjectMemAllocFailed.setStatus("current")
_HtmlInitFailed_Type = Counter64
_HtmlInitFailed_Object = MibScalar
htmlInitFailed = _HtmlInitFailed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 63, 5),
    _HtmlInitFailed_Type()
)
htmlInitFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htmlInitFailed.setStatus("current")
_AppFirewallGroup_ObjectIdentity = ObjectIdentity
appFirewallGroup = _AppFirewallGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64)
)
_AppFirewallStatistics_ObjectIdentity = ObjectIdentity
appFirewallStatistics = _AppFirewallStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1)
)
_AppFirewallRequests_Type = Counter64
_AppFirewallRequests_Object = MibScalar
appFirewallRequests = _AppFirewallRequests_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1, 1),
    _AppFirewallRequests_Type()
)
appFirewallRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFirewallRequests.setStatus("current")
_AppFirewallResponses_Type = Counter64
_AppFirewallResponses_Object = MibScalar
appFirewallResponses = _AppFirewallResponses_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1, 2),
    _AppFirewallResponses_Type()
)
appFirewallResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFirewallResponses.setStatus("current")
_AppFirewallAborts_Type = Counter64
_AppFirewallAborts_Object = MibScalar
appFirewallAborts = _AppFirewallAborts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1, 3),
    _AppFirewallAborts_Type()
)
appFirewallAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFirewallAborts.setStatus("current")
_AppFirewallRedirects_Type = Counter64
_AppFirewallRedirects_Object = MibScalar
appFirewallRedirects = _AppFirewallRedirects_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1, 4),
    _AppFirewallRedirects_Type()
)
appFirewallRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFirewallRedirects.setStatus("current")
_AppFirewallViolStartURL_Type = Counter64
_AppFirewallViolStartURL_Object = MibScalar
appFirewallViolStartURL = _AppFirewallViolStartURL_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1, 5),
    _AppFirewallViolStartURL_Type()
)
appFirewallViolStartURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFirewallViolStartURL.setStatus("current")
_AppFirewallViolDenyURL_Type = Counter64
_AppFirewallViolDenyURL_Object = MibScalar
appFirewallViolDenyURL = _AppFirewallViolDenyURL_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1, 6),
    _AppFirewallViolDenyURL_Type()
)
appFirewallViolDenyURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFirewallViolDenyURL.setStatus("current")
_AppFirewallViolBufferOverflow_Type = Counter64
_AppFirewallViolBufferOverflow_Object = MibScalar
appFirewallViolBufferOverflow = _AppFirewallViolBufferOverflow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1, 7),
    _AppFirewallViolBufferOverflow_Type()
)
appFirewallViolBufferOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFirewallViolBufferOverflow.setStatus("current")
_AppFirewallViolCookie_Type = Counter64
_AppFirewallViolCookie_Object = MibScalar
appFirewallViolCookie = _AppFirewallViolCookie_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1, 8),
    _AppFirewallViolCookie_Type()
)
appFirewallViolCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFirewallViolCookie.setStatus("current")
_AppFirewallViolXSS_Type = Counter64
_AppFirewallViolXSS_Object = MibScalar
appFirewallViolXSS = _AppFirewallViolXSS_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1, 9),
    _AppFirewallViolXSS_Type()
)
appFirewallViolXSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFirewallViolXSS.setStatus("current")
_AppFirewallViolSQL_Type = Counter64
_AppFirewallViolSQL_Object = MibScalar
appFirewallViolSQL = _AppFirewallViolSQL_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1, 10),
    _AppFirewallViolSQL_Type()
)
appFirewallViolSQL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFirewallViolSQL.setStatus("current")
_AppFirewallViolFieldformat_Type = Counter64
_AppFirewallViolFieldformat_Object = MibScalar
appFirewallViolFieldformat = _AppFirewallViolFieldformat_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1, 11),
    _AppFirewallViolFieldformat_Type()
)
appFirewallViolFieldformat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFirewallViolFieldformat.setStatus("current")
_AppFirewallViolFieldConsistency_Type = Counter64
_AppFirewallViolFieldConsistency_Object = MibScalar
appFirewallViolFieldConsistency = _AppFirewallViolFieldConsistency_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1, 12),
    _AppFirewallViolFieldConsistency_Type()
)
appFirewallViolFieldConsistency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFirewallViolFieldConsistency.setStatus("current")
_AppFirewallViolCreditCard_Type = Counter64
_AppFirewallViolCreditCard_Object = MibScalar
appFirewallViolCreditCard = _AppFirewallViolCreditCard_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1, 13),
    _AppFirewallViolCreditCard_Type()
)
appFirewallViolCreditCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFirewallViolCreditCard.setStatus("current")
_AppFirewallViolSafeObject_Type = Counter64
_AppFirewallViolSafeObject_Object = MibScalar
appFirewallViolSafeObject = _AppFirewallViolSafeObject_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1, 14),
    _AppFirewallViolSafeObject_Type()
)
appFirewallViolSafeObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFirewallViolSafeObject.setStatus("current")
_AppFirewallTotalViol_Type = Counter64
_AppFirewallTotalViol_Object = MibScalar
appFirewallTotalViol = _AppFirewallTotalViol_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1, 15),
    _AppFirewallTotalViol_Type()
)
appFirewallTotalViol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFirewallTotalViol.setStatus("current")
_AppFirewallViolWellformednessViolations_Type = Counter64
_AppFirewallViolWellformednessViolations_Object = MibScalar
appFirewallViolWellformednessViolations = _AppFirewallViolWellformednessViolations_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1, 16),
    _AppFirewallViolWellformednessViolations_Type()
)
appFirewallViolWellformednessViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFirewallViolWellformednessViolations.setStatus("current")
_AppFirewallViolXdosViolations_Type = Counter64
_AppFirewallViolXdosViolations_Object = MibScalar
appFirewallViolXdosViolations = _AppFirewallViolXdosViolations_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1, 17),
    _AppFirewallViolXdosViolations_Type()
)
appFirewallViolXdosViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFirewallViolXdosViolations.setStatus("current")
_AppFirewallViolMsgValViolations_Type = Counter64
_AppFirewallViolMsgValViolations_Object = MibScalar
appFirewallViolMsgValViolations = _AppFirewallViolMsgValViolations_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1, 18),
    _AppFirewallViolMsgValViolations_Type()
)
appFirewallViolMsgValViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFirewallViolMsgValViolations.setStatus("current")
_AppFirewallViolWSIViolations_Type = Counter64
_AppFirewallViolWSIViolations_Object = MibScalar
appFirewallViolWSIViolations = _AppFirewallViolWSIViolations_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1, 19),
    _AppFirewallViolWSIViolations_Type()
)
appFirewallViolWSIViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFirewallViolWSIViolations.setStatus("current")
_AppFirewallViolXmlSqlViolations_Type = Counter64
_AppFirewallViolXmlSqlViolations_Object = MibScalar
appFirewallViolXmlSqlViolations = _AppFirewallViolXmlSqlViolations_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1, 20),
    _AppFirewallViolXmlSqlViolations_Type()
)
appFirewallViolXmlSqlViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFirewallViolXmlSqlViolations.setStatus("current")
_AppFirewallViolXmlXssViolations_Type = Counter64
_AppFirewallViolXmlXssViolations_Object = MibScalar
appFirewallViolXmlXssViolations = _AppFirewallViolXmlXssViolations_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1, 21),
    _AppFirewallViolXmlXssViolations_Type()
)
appFirewallViolXmlXssViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFirewallViolXmlXssViolations.setStatus("current")
_AppFirewallViolXmlAttachmentViolations_Type = Counter64
_AppFirewallViolXmlAttachmentViolations_Object = MibScalar
appFirewallViolXmlAttachmentViolations = _AppFirewallViolXmlAttachmentViolations_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1, 22),
    _AppFirewallViolXmlAttachmentViolations_Type()
)
appFirewallViolXmlAttachmentViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFirewallViolXmlAttachmentViolations.setStatus("current")
_AppFirewallViolCSRFtag_Type = Counter64
_AppFirewallViolCSRFtag_Object = MibScalar
appFirewallViolCSRFtag = _AppFirewallViolCSRFtag_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1, 23),
    _AppFirewallViolCSRFtag_Type()
)
appFirewallViolCSRFtag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFirewallViolCSRFtag.setStatus("current")
_AppFirewallViolRefererHeader_Type = Counter64
_AppFirewallViolRefererHeader_Object = MibScalar
appFirewallViolRefererHeader = _AppFirewallViolRefererHeader_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1, 24),
    _AppFirewallViolRefererHeader_Type()
)
appFirewallViolRefererHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFirewallViolRefererHeader.setStatus("current")
_AppFirewallViolXmlSoapFaultViolations_Type = Counter64
_AppFirewallViolXmlSoapFaultViolations_Object = MibScalar
appFirewallViolXmlSoapFaultViolations = _AppFirewallViolXmlSoapFaultViolations_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1, 25),
    _AppFirewallViolXmlSoapFaultViolations_Type()
)
appFirewallViolXmlSoapFaultViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFirewallViolXmlSoapFaultViolations.setStatus("current")
_AppFirewallRet4xx_Type = Counter64
_AppFirewallRet4xx_Object = MibScalar
appFirewallRet4xx = _AppFirewallRet4xx_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1, 26),
    _AppFirewallRet4xx_Type()
)
appFirewallRet4xx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFirewallRet4xx.setStatus("current")
_AppFirewallRet5xx_Type = Counter64
_AppFirewallRet5xx_Object = MibScalar
appFirewallRet5xx = _AppFirewallRet5xx_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1, 27),
    _AppFirewallRet5xx_Type()
)
appFirewallRet5xx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFirewallRet5xx.setStatus("current")
_AppFirewallReqBytes_Type = Counter64
_AppFirewallReqBytes_Object = MibScalar
appFirewallReqBytes = _AppFirewallReqBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1, 28),
    _AppFirewallReqBytes_Type()
)
appFirewallReqBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFirewallReqBytes.setStatus("current")
_AppFirewallResBytes_Type = Counter64
_AppFirewallResBytes_Object = MibScalar
appFirewallResBytes = _AppFirewallResBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1, 29),
    _AppFirewallResBytes_Type()
)
appFirewallResBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFirewallResBytes.setStatus("current")
_AppFirewallLongAvgRespTime_Type = Counter64
_AppFirewallLongAvgRespTime_Object = MibScalar
appFirewallLongAvgRespTime = _AppFirewallLongAvgRespTime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1, 30),
    _AppFirewallLongAvgRespTime_Type()
)
appFirewallLongAvgRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFirewallLongAvgRespTime.setStatus("current")
_AppFirewallShortAvgRespTime_Type = Counter64
_AppFirewallShortAvgRespTime_Object = MibScalar
appFirewallShortAvgRespTime = _AppFirewallShortAvgRespTime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 1, 31),
    _AppFirewallShortAvgRespTime_Type()
)
appFirewallShortAvgRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFirewallShortAvgRespTime.setStatus("current")
_AppfwProfileTable_Object = MibTable
appfwProfileTable = _AppfwProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2)
)
if mibBuilder.loadTexts:
    appfwProfileTable.setStatus("current")
_AppfwProfileEntry_Object = MibTableRow
appfwProfileEntry = _AppfwProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1)
)
appfwProfileEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "appfwprofileName"),
)
if mibBuilder.loadTexts:
    appfwProfileEntry.setStatus("current")
_AppfwprofileName_Type = OctetString
_AppfwprofileName_Object = MibTableColumn
appfwprofileName = _AppfwprofileName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 1),
    _AppfwprofileName_Type()
)
appfwprofileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwprofileName.setStatus("current")
_AppfwappFirewallRequestsPerProfile_Type = Counter64
_AppfwappFirewallRequestsPerProfile_Object = MibTableColumn
appfwappFirewallRequestsPerProfile = _AppfwappFirewallRequestsPerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 2),
    _AppfwappFirewallRequestsPerProfile_Type()
)
appfwappFirewallRequestsPerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwappFirewallRequestsPerProfile.setStatus("current")
_AppfwappFirewallResponsesPerProfile_Type = Counter64
_AppfwappFirewallResponsesPerProfile_Object = MibTableColumn
appfwappFirewallResponsesPerProfile = _AppfwappFirewallResponsesPerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 3),
    _AppfwappFirewallResponsesPerProfile_Type()
)
appfwappFirewallResponsesPerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwappFirewallResponsesPerProfile.setStatus("current")
_AppfwappFirewallAbortsPerProfile_Type = Counter64
_AppfwappFirewallAbortsPerProfile_Object = MibTableColumn
appfwappFirewallAbortsPerProfile = _AppfwappFirewallAbortsPerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 4),
    _AppfwappFirewallAbortsPerProfile_Type()
)
appfwappFirewallAbortsPerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwappFirewallAbortsPerProfile.setStatus("current")
_AppfwappFirewallRedirectsPerProfile_Type = Counter64
_AppfwappFirewallRedirectsPerProfile_Object = MibTableColumn
appfwappFirewallRedirectsPerProfile = _AppfwappFirewallRedirectsPerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 5),
    _AppfwappFirewallRedirectsPerProfile_Type()
)
appfwappFirewallRedirectsPerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwappFirewallRedirectsPerProfile.setStatus("current")
_AppfwappFirewallViolStartURLPerProfile_Type = Counter64
_AppfwappFirewallViolStartURLPerProfile_Object = MibTableColumn
appfwappFirewallViolStartURLPerProfile = _AppfwappFirewallViolStartURLPerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 6),
    _AppfwappFirewallViolStartURLPerProfile_Type()
)
appfwappFirewallViolStartURLPerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwappFirewallViolStartURLPerProfile.setStatus("current")
_AppfwappFirewallViolDenyURLPerProfile_Type = Counter64
_AppfwappFirewallViolDenyURLPerProfile_Object = MibTableColumn
appfwappFirewallViolDenyURLPerProfile = _AppfwappFirewallViolDenyURLPerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 7),
    _AppfwappFirewallViolDenyURLPerProfile_Type()
)
appfwappFirewallViolDenyURLPerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwappFirewallViolDenyURLPerProfile.setStatus("current")
_AppfwappFirewallViolRefererHeaderPerProfile_Type = Counter64
_AppfwappFirewallViolRefererHeaderPerProfile_Object = MibTableColumn
appfwappFirewallViolRefererHeaderPerProfile = _AppfwappFirewallViolRefererHeaderPerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 8),
    _AppfwappFirewallViolRefererHeaderPerProfile_Type()
)
appfwappFirewallViolRefererHeaderPerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwappFirewallViolRefererHeaderPerProfile.setStatus("current")
_AppfwappFirewallViolBufferOverflowPerProfile_Type = Counter64
_AppfwappFirewallViolBufferOverflowPerProfile_Object = MibTableColumn
appfwappFirewallViolBufferOverflowPerProfile = _AppfwappFirewallViolBufferOverflowPerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 9),
    _AppfwappFirewallViolBufferOverflowPerProfile_Type()
)
appfwappFirewallViolBufferOverflowPerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwappFirewallViolBufferOverflowPerProfile.setStatus("current")
_AppfwappFirewallViolCSRFtagPerProfile_Type = Counter64
_AppfwappFirewallViolCSRFtagPerProfile_Object = MibTableColumn
appfwappFirewallViolCSRFtagPerProfile = _AppfwappFirewallViolCSRFtagPerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 10),
    _AppfwappFirewallViolCSRFtagPerProfile_Type()
)
appfwappFirewallViolCSRFtagPerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwappFirewallViolCSRFtagPerProfile.setStatus("current")
_AppfwappFirewallViolCookiePerProfile_Type = Counter64
_AppfwappFirewallViolCookiePerProfile_Object = MibTableColumn
appfwappFirewallViolCookiePerProfile = _AppfwappFirewallViolCookiePerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 11),
    _AppfwappFirewallViolCookiePerProfile_Type()
)
appfwappFirewallViolCookiePerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwappFirewallViolCookiePerProfile.setStatus("current")
_AppfwappFirewallViolXSSPerProfile_Type = Counter64
_AppfwappFirewallViolXSSPerProfile_Object = MibTableColumn
appfwappFirewallViolXSSPerProfile = _AppfwappFirewallViolXSSPerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 12),
    _AppfwappFirewallViolXSSPerProfile_Type()
)
appfwappFirewallViolXSSPerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwappFirewallViolXSSPerProfile.setStatus("current")
_AppfwappFirewallViolSQLPerProfile_Type = Counter64
_AppfwappFirewallViolSQLPerProfile_Object = MibTableColumn
appfwappFirewallViolSQLPerProfile = _AppfwappFirewallViolSQLPerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 13),
    _AppfwappFirewallViolSQLPerProfile_Type()
)
appfwappFirewallViolSQLPerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwappFirewallViolSQLPerProfile.setStatus("current")
_AppfwappFirewallViolFieldformatPerProfile_Type = Counter64
_AppfwappFirewallViolFieldformatPerProfile_Object = MibTableColumn
appfwappFirewallViolFieldformatPerProfile = _AppfwappFirewallViolFieldformatPerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 14),
    _AppfwappFirewallViolFieldformatPerProfile_Type()
)
appfwappFirewallViolFieldformatPerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwappFirewallViolFieldformatPerProfile.setStatus("current")
_AppfwappFirewallViolFieldConsistencyPerProfile_Type = Counter64
_AppfwappFirewallViolFieldConsistencyPerProfile_Object = MibTableColumn
appfwappFirewallViolFieldConsistencyPerProfile = _AppfwappFirewallViolFieldConsistencyPerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 15),
    _AppfwappFirewallViolFieldConsistencyPerProfile_Type()
)
appfwappFirewallViolFieldConsistencyPerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwappFirewallViolFieldConsistencyPerProfile.setStatus("current")
_AppfwappFirewallViolCreditCardPerProfile_Type = Counter64
_AppfwappFirewallViolCreditCardPerProfile_Object = MibTableColumn
appfwappFirewallViolCreditCardPerProfile = _AppfwappFirewallViolCreditCardPerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 16),
    _AppfwappFirewallViolCreditCardPerProfile_Type()
)
appfwappFirewallViolCreditCardPerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwappFirewallViolCreditCardPerProfile.setStatus("current")
_AppfwappFirewallViolSafeObjectPerProfile_Type = Counter64
_AppfwappFirewallViolSafeObjectPerProfile_Object = MibTableColumn
appfwappFirewallViolSafeObjectPerProfile = _AppfwappFirewallViolSafeObjectPerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 17),
    _AppfwappFirewallViolSafeObjectPerProfile_Type()
)
appfwappFirewallViolSafeObjectPerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwappFirewallViolSafeObjectPerProfile.setStatus("current")
_AppfwappFirewallViolWellformednessViolationsPerProfile_Type = Counter64
_AppfwappFirewallViolWellformednessViolationsPerProfile_Object = MibTableColumn
appfwappFirewallViolWellformednessViolationsPerProfile = _AppfwappFirewallViolWellformednessViolationsPerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 18),
    _AppfwappFirewallViolWellformednessViolationsPerProfile_Type()
)
appfwappFirewallViolWellformednessViolationsPerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwappFirewallViolWellformednessViolationsPerProfile.setStatus("current")
_AppfwappFirewallViolXdosViolationsPerProfile_Type = Counter64
_AppfwappFirewallViolXdosViolationsPerProfile_Object = MibTableColumn
appfwappFirewallViolXdosViolationsPerProfile = _AppfwappFirewallViolXdosViolationsPerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 19),
    _AppfwappFirewallViolXdosViolationsPerProfile_Type()
)
appfwappFirewallViolXdosViolationsPerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwappFirewallViolXdosViolationsPerProfile.setStatus("current")
_AppfwappFirewallViolMsgValViolationsPerProfile_Type = Counter64
_AppfwappFirewallViolMsgValViolationsPerProfile_Object = MibTableColumn
appfwappFirewallViolMsgValViolationsPerProfile = _AppfwappFirewallViolMsgValViolationsPerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 20),
    _AppfwappFirewallViolMsgValViolationsPerProfile_Type()
)
appfwappFirewallViolMsgValViolationsPerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwappFirewallViolMsgValViolationsPerProfile.setStatus("current")
_AppfwappFirewallViolWSIViolationsPerProfile_Type = Counter64
_AppfwappFirewallViolWSIViolationsPerProfile_Object = MibTableColumn
appfwappFirewallViolWSIViolationsPerProfile = _AppfwappFirewallViolWSIViolationsPerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 21),
    _AppfwappFirewallViolWSIViolationsPerProfile_Type()
)
appfwappFirewallViolWSIViolationsPerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwappFirewallViolWSIViolationsPerProfile.setStatus("current")
_AppfwappFirewallViolXmlSqlViolationsPerProfile_Type = Counter64
_AppfwappFirewallViolXmlSqlViolationsPerProfile_Object = MibTableColumn
appfwappFirewallViolXmlSqlViolationsPerProfile = _AppfwappFirewallViolXmlSqlViolationsPerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 22),
    _AppfwappFirewallViolXmlSqlViolationsPerProfile_Type()
)
appfwappFirewallViolXmlSqlViolationsPerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwappFirewallViolXmlSqlViolationsPerProfile.setStatus("current")
_AppfwappFirewallViolXmlXssViolationsPerProfile_Type = Counter64
_AppfwappFirewallViolXmlXssViolationsPerProfile_Object = MibTableColumn
appfwappFirewallViolXmlXssViolationsPerProfile = _AppfwappFirewallViolXmlXssViolationsPerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 23),
    _AppfwappFirewallViolXmlXssViolationsPerProfile_Type()
)
appfwappFirewallViolXmlXssViolationsPerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwappFirewallViolXmlXssViolationsPerProfile.setStatus("current")
_AppfwappFirewallViolXmlAttachmentViolationsPerProfile_Type = Counter64
_AppfwappFirewallViolXmlAttachmentViolationsPerProfile_Object = MibTableColumn
appfwappFirewallViolXmlAttachmentViolationsPerProfile = _AppfwappFirewallViolXmlAttachmentViolationsPerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 24),
    _AppfwappFirewallViolXmlAttachmentViolationsPerProfile_Type()
)
appfwappFirewallViolXmlAttachmentViolationsPerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwappFirewallViolXmlAttachmentViolationsPerProfile.setStatus("current")
_AppfwappFirewallTotalViolPerProfile_Type = Counter64
_AppfwappFirewallTotalViolPerProfile_Object = MibTableColumn
appfwappFirewallTotalViolPerProfile = _AppfwappFirewallTotalViolPerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 25),
    _AppfwappFirewallTotalViolPerProfile_Type()
)
appfwappFirewallTotalViolPerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwappFirewallTotalViolPerProfile.setStatus("current")
_AppfwappFirewallRet4xxPerProfile_Type = Counter64
_AppfwappFirewallRet4xxPerProfile_Object = MibTableColumn
appfwappFirewallRet4xxPerProfile = _AppfwappFirewallRet4xxPerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 26),
    _AppfwappFirewallRet4xxPerProfile_Type()
)
appfwappFirewallRet4xxPerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwappFirewallRet4xxPerProfile.setStatus("current")
_AppfwappFirewallRet5xxPerProfile_Type = Counter64
_AppfwappFirewallRet5xxPerProfile_Object = MibTableColumn
appfwappFirewallRet5xxPerProfile = _AppfwappFirewallRet5xxPerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 27),
    _AppfwappFirewallRet5xxPerProfile_Type()
)
appfwappFirewallRet5xxPerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwappFirewallRet5xxPerProfile.setStatus("current")
_AppfwappFirewallViolXmlSoapFaultViolationsPerProfile_Type = Counter64
_AppfwappFirewallViolXmlSoapFaultViolationsPerProfile_Object = MibTableColumn
appfwappFirewallViolXmlSoapFaultViolationsPerProfile = _AppfwappFirewallViolXmlSoapFaultViolationsPerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 28),
    _AppfwappFirewallViolXmlSoapFaultViolationsPerProfile_Type()
)
appfwappFirewallViolXmlSoapFaultViolationsPerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwappFirewallViolXmlSoapFaultViolationsPerProfile.setStatus("current")
_AppfwappFirewallReqBytesPerProfile_Type = Counter64
_AppfwappFirewallReqBytesPerProfile_Object = MibTableColumn
appfwappFirewallReqBytesPerProfile = _AppfwappFirewallReqBytesPerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 29),
    _AppfwappFirewallReqBytesPerProfile_Type()
)
appfwappFirewallReqBytesPerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwappFirewallReqBytesPerProfile.setStatus("current")
_AppfwappFirewallResBytesPerProfile_Type = Counter64
_AppfwappFirewallResBytesPerProfile_Object = MibTableColumn
appfwappFirewallResBytesPerProfile = _AppfwappFirewallResBytesPerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 30),
    _AppfwappFirewallResBytesPerProfile_Type()
)
appfwappFirewallResBytesPerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwappFirewallResBytesPerProfile.setStatus("current")
_AppfwappFirewallLongAvgRespTimePerProfile_Type = Counter64
_AppfwappFirewallLongAvgRespTimePerProfile_Object = MibTableColumn
appfwappFirewallLongAvgRespTimePerProfile = _AppfwappFirewallLongAvgRespTimePerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 31),
    _AppfwappFirewallLongAvgRespTimePerProfile_Type()
)
appfwappFirewallLongAvgRespTimePerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwappFirewallLongAvgRespTimePerProfile.setStatus("current")
_AppfwappFirewallShortAvgRespTimePerProfile_Type = Counter64
_AppfwappFirewallShortAvgRespTimePerProfile_Object = MibTableColumn
appfwappFirewallShortAvgRespTimePerProfile = _AppfwappFirewallShortAvgRespTimePerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 64, 2, 1, 32),
    _AppfwappFirewallShortAvgRespTimePerProfile_Type()
)
appfwappFirewallShortAvgRespTimePerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appfwappFirewallShortAvgRespTimePerProfile.setStatus("current")
_NsRnatStatsGroup_ObjectIdentity = ObjectIdentity
nsRnatStatsGroup = _NsRnatStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 65)
)
_NsRnatGlobalStats_ObjectIdentity = ObjectIdentity
nsRnatGlobalStats = _NsRnatGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 65, 1)
)
_RnatTotRxBytes_Type = Counter64
_RnatTotRxBytes_Object = MibScalar
rnatTotRxBytes = _RnatTotRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 65, 1, 1),
    _RnatTotRxBytes_Type()
)
rnatTotRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnatTotRxBytes.setStatus("current")
_RnatTotTxBytes_Type = Counter64
_RnatTotTxBytes_Object = MibScalar
rnatTotTxBytes = _RnatTotTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 65, 1, 2),
    _RnatTotTxBytes_Type()
)
rnatTotTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnatTotTxBytes.setStatus("current")
_RnatTotRxPkts_Type = Counter64
_RnatTotRxPkts_Object = MibScalar
rnatTotRxPkts = _RnatTotRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 65, 1, 3),
    _RnatTotRxPkts_Type()
)
rnatTotRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnatTotRxPkts.setStatus("current")
_RnatTotTxPkts_Type = Counter64
_RnatTotTxPkts_Object = MibScalar
rnatTotTxPkts = _RnatTotTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 65, 1, 4),
    _RnatTotTxPkts_Type()
)
rnatTotTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnatTotTxPkts.setStatus("current")
_RnatTotTxSyn_Type = Counter64
_RnatTotTxSyn_Object = MibScalar
rnatTotTxSyn = _RnatTotTxSyn_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 65, 1, 5),
    _RnatTotTxSyn_Type()
)
rnatTotTxSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnatTotTxSyn.setStatus("current")
_RnatCurSessions_Type = Gauge32
_RnatCurSessions_Object = MibScalar
rnatCurSessions = _RnatCurSessions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 65, 1, 6),
    _RnatCurSessions_Type()
)
rnatCurSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnatCurSessions.setStatus("current")
_NsRnatPerIPStatsTable_Object = MibTable
nsRnatPerIPStatsTable = _NsRnatPerIPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 65, 2)
)
if mibBuilder.loadTexts:
    nsRnatPerIPStatsTable.setStatus("current")
_NsRnatPerIPStatsEntry_Object = MibTableRow
nsRnatPerIPStatsEntry = _NsRnatPerIPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 65, 2, 1)
)
nsRnatPerIPStatsEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "ipAddr"),
)
if mibBuilder.loadTexts:
    nsRnatPerIPStatsEntry.setStatus("current")
_IpRnatTotRxBytes_Type = Counter64
_IpRnatTotRxBytes_Object = MibTableColumn
ipRnatTotRxBytes = _IpRnatTotRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 65, 2, 1, 1),
    _IpRnatTotRxBytes_Type()
)
ipRnatTotRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRnatTotRxBytes.setStatus("current")
_IpRnatTotTxBytes_Type = Counter64
_IpRnatTotTxBytes_Object = MibTableColumn
ipRnatTotTxBytes = _IpRnatTotTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 65, 2, 1, 2),
    _IpRnatTotTxBytes_Type()
)
ipRnatTotTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRnatTotTxBytes.setStatus("current")
_IpRnatTotRxPkts_Type = Counter64
_IpRnatTotRxPkts_Object = MibTableColumn
ipRnatTotRxPkts = _IpRnatTotRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 65, 2, 1, 3),
    _IpRnatTotRxPkts_Type()
)
ipRnatTotRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRnatTotRxPkts.setStatus("current")
_IpRnatTotTxPkts_Type = Counter64
_IpRnatTotTxPkts_Object = MibTableColumn
ipRnatTotTxPkts = _IpRnatTotTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 65, 2, 1, 4),
    _IpRnatTotTxPkts_Type()
)
ipRnatTotTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRnatTotTxPkts.setStatus("current")
_IpRnatTotTxSyn_Type = Counter64
_IpRnatTotTxSyn_Object = MibTableColumn
ipRnatTotTxSyn = _IpRnatTotTxSyn_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 65, 2, 1, 5),
    _IpRnatTotTxSyn_Type()
)
ipRnatTotTxSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRnatTotTxSyn.setStatus("current")
_IpRnatCurSessions_Type = Gauge32
_IpRnatCurSessions_Object = MibTableColumn
ipRnatCurSessions = _IpRnatCurSessions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 65, 2, 1, 6),
    _IpRnatCurSessions_Type()
)
ipRnatCurSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRnatCurSessions.setStatus("current")
_NsSslVpnStatsGroup_ObjectIdentity = ObjectIdentity
nsSslVpnStatsGroup = _NsSslVpnStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66)
)
_IndexHtmlHit_Type = Counter64
_IndexHtmlHit_Object = MibScalar
indexHtmlHit = _IndexHtmlHit_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 1),
    _IndexHtmlHit_Type()
)
indexHtmlHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    indexHtmlHit.setStatus("current")
_IndexHtmlNoServed_Type = Counter64
_IndexHtmlNoServed_Object = MibScalar
indexHtmlNoServed = _IndexHtmlNoServed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 2),
    _IndexHtmlNoServed_Type()
)
indexHtmlNoServed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    indexHtmlNoServed.setStatus("current")
_CfgHtmlServed_Type = Counter64
_CfgHtmlServed_Object = MibScalar
cfgHtmlServed = _CfgHtmlServed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 3),
    _CfgHtmlServed_Type()
)
cfgHtmlServed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgHtmlServed.setStatus("current")
_DnsReqHit_Type = Counter64
_DnsReqHit_Object = MibScalar
dnsReqHit = _DnsReqHit_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 4),
    _DnsReqHit_Type()
)
dnsReqHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsReqHit.setStatus("current")
_WinsRequestHit_Type = Counter64
_WinsRequestHit_Object = MibScalar
winsRequestHit = _WinsRequestHit_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 5),
    _WinsRequestHit_Type()
)
winsRequestHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winsRequestHit.setStatus("current")
_CsRequestHit_Type = Counter64
_CsRequestHit_Object = MibScalar
csRequestHit = _CsRequestHit_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 6),
    _CsRequestHit_Type()
)
csRequestHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csRequestHit.setStatus("current")
_CsNonHttpProbeHit_Type = Counter64
_CsNonHttpProbeHit_Object = MibScalar
csNonHttpProbeHit = _CsNonHttpProbeHit_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 7),
    _CsNonHttpProbeHit_Type()
)
csNonHttpProbeHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csNonHttpProbeHit.setStatus("current")
_CsHttpProbeHit_Type = Counter64
_CsHttpProbeHit_Object = MibScalar
csHttpProbeHit = _CsHttpProbeHit_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 8),
    _CsHttpProbeHit_Type()
)
csHttpProbeHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csHttpProbeHit.setStatus("current")
_TotalCsConnSucc_Type = Counter64
_TotalCsConnSucc_Object = MibScalar
totalCsConnSucc = _TotalCsConnSucc_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 9),
    _TotalCsConnSucc_Type()
)
totalCsConnSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalCsConnSucc.setStatus("current")
_TotalFsRequest_Type = Counter64
_TotalFsRequest_Object = MibScalar
totalFsRequest = _TotalFsRequest_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 10),
    _TotalFsRequest_Type()
)
totalFsRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalFsRequest.setStatus("current")
_IipDisabledMIPdisabled_Type = Counter64
_IipDisabledMIPdisabled_Object = MibScalar
iipDisabledMIPdisabled = _IipDisabledMIPdisabled_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 11),
    _IipDisabledMIPdisabled_Type()
)
iipDisabledMIPdisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iipDisabledMIPdisabled.setStatus("current")
_IipFailedMIPdisabled_Type = Counter64
_IipFailedMIPdisabled_Object = MibScalar
iipFailedMIPdisabled = _IipFailedMIPdisabled_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 12),
    _IipFailedMIPdisabled_Type()
)
iipFailedMIPdisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iipFailedMIPdisabled.setStatus("current")
_IipDisabledMIPused_Type = Counter64
_IipDisabledMIPused_Object = MibScalar
iipDisabledMIPused = _IipDisabledMIPused_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 13),
    _IipDisabledMIPused_Type()
)
iipDisabledMIPused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iipDisabledMIPused.setStatus("current")
_IipFailedMIPused_Type = Counter64
_IipFailedMIPused_Object = MibScalar
iipFailedMIPused = _IipFailedMIPused_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 14),
    _IipFailedMIPused_Type()
)
iipFailedMIPused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iipFailedMIPused.setStatus("current")
_SocksMethReqRcvd_Type = Counter64
_SocksMethReqRcvd_Object = MibScalar
socksMethReqRcvd = _SocksMethReqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 15),
    _SocksMethReqRcvd_Type()
)
socksMethReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    socksMethReqRcvd.setStatus("current")
_SocksMethReqSent_Type = Counter64
_SocksMethReqSent_Object = MibScalar
socksMethReqSent = _SocksMethReqSent_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 16),
    _SocksMethReqSent_Type()
)
socksMethReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    socksMethReqSent.setStatus("current")
_SocksMethRespRcvd_Type = Counter64
_SocksMethRespRcvd_Object = MibScalar
socksMethRespRcvd = _SocksMethRespRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 17),
    _SocksMethRespRcvd_Type()
)
socksMethRespRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    socksMethRespRcvd.setStatus("current")
_SocksMethRespSent_Type = Counter64
_SocksMethRespSent_Object = MibScalar
socksMethRespSent = _SocksMethRespSent_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 18),
    _SocksMethRespSent_Type()
)
socksMethRespSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    socksMethRespSent.setStatus("current")
_SocksConnReqRcvd_Type = Counter64
_SocksConnReqRcvd_Object = MibScalar
socksConnReqRcvd = _SocksConnReqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 19),
    _SocksConnReqRcvd_Type()
)
socksConnReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    socksConnReqRcvd.setStatus("current")
_SocksConnReqSent_Type = Counter64
_SocksConnReqSent_Object = MibScalar
socksConnReqSent = _SocksConnReqSent_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 20),
    _SocksConnReqSent_Type()
)
socksConnReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    socksConnReqSent.setStatus("current")
_SocksConnRespRcvd_Type = Counter64
_SocksConnRespRcvd_Object = MibScalar
socksConnRespRcvd = _SocksConnRespRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 21),
    _SocksConnRespRcvd_Type()
)
socksConnRespRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    socksConnRespRcvd.setStatus("current")
_SocksConnRespSent_Type = Counter64
_SocksConnRespSent_Object = MibScalar
socksConnRespSent = _SocksConnRespSent_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 22),
    _SocksConnRespSent_Type()
)
socksConnRespSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    socksConnRespSent.setStatus("current")
_SocksServerError_Type = Counter64
_SocksServerError_Object = MibScalar
socksServerError = _SocksServerError_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 23),
    _SocksServerError_Type()
)
socksServerError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    socksServerError.setStatus("current")
_SocksClientError_Type = Counter64
_SocksClientError_Object = MibScalar
socksClientError = _SocksClientError_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 24),
    _SocksClientError_Type()
)
socksClientError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    socksClientError.setStatus("current")
_StaConnSuccess_Type = Counter64
_StaConnSuccess_Object = MibScalar
staConnSuccess = _StaConnSuccess_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 25),
    _StaConnSuccess_Type()
)
staConnSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staConnSuccess.setStatus("current")
_StaConnFailure_Type = Counter64
_StaConnFailure_Object = MibScalar
staConnFailure = _StaConnFailure_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 26),
    _StaConnFailure_Type()
)
staConnFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staConnFailure.setStatus("current")
_CpsConnSuccess_Type = Counter64
_CpsConnSuccess_Object = MibScalar
cpsConnSuccess = _CpsConnSuccess_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 27),
    _CpsConnSuccess_Type()
)
cpsConnSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsConnSuccess.setStatus("current")
_CpsConnFailure_Type = Counter64
_CpsConnFailure_Object = MibScalar
cpsConnFailure = _CpsConnFailure_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 28),
    _CpsConnFailure_Type()
)
cpsConnFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsConnFailure.setStatus("current")
_StaRequestSent_Type = Counter64
_StaRequestSent_Object = MibScalar
staRequestSent = _StaRequestSent_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 29),
    _StaRequestSent_Type()
)
staRequestSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staRequestSent.setStatus("current")
_StaResponseRecvd_Type = Counter64
_StaResponseRecvd_Object = MibScalar
staResponseRecvd = _StaResponseRecvd_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 30),
    _StaResponseRecvd_Type()
)
staResponseRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staResponseRecvd.setStatus("current")
_IcaLicenseFailure_Type = Counter64
_IcaLicenseFailure_Object = MibScalar
icaLicenseFailure = _IcaLicenseFailure_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 31),
    _IcaLicenseFailure_Type()
)
icaLicenseFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icaLicenseFailure.setStatus("current")
_StaRenewSent_Type = Counter64
_StaRenewSent_Object = MibScalar
staRenewSent = _StaRenewSent_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 32),
    _StaRenewSent_Type()
)
staRenewSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staRenewSent.setStatus("current")
_StaRenewRecvd_Type = Counter64
_StaRenewRecvd_Object = MibScalar
staRenewRecvd = _StaRenewRecvd_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 33),
    _StaRenewRecvd_Type()
)
staRenewRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staRenewRecvd.setStatus("current")
_StaReassErr_Type = Counter64
_StaReassErr_Object = MibScalar
staReassErr = _StaReassErr_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 34),
    _StaReassErr_Type()
)
staReassErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staReassErr.setStatus("current")
_StaRnewNoClnt_Type = Counter64
_StaRnewNoClnt_Object = MibScalar
staRnewNoClnt = _StaRnewNoClnt_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 35),
    _StaRnewNoClnt_Type()
)
staRnewNoClnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staRnewNoClnt.setStatus("current")
_StaRenewNoRfsh_Type = Counter64
_StaRenewNoRfsh_Object = MibScalar
staRenewNoRfsh = _StaRenewNoRfsh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 36),
    _StaRenewNoRfsh_Type()
)
staRenewNoRfsh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staRenewNoRfsh.setStatus("current")
_StaValidNoClnt_Type = Counter64
_StaValidNoClnt_Object = MibScalar
staValidNoClnt = _StaValidNoClnt_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 37),
    _StaValidNoClnt_Type()
)
staValidNoClnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staValidNoClnt.setStatus("current")
_StaValidNoEst_Type = Counter64
_StaValidNoEst_Object = MibScalar
staValidNoEst = _StaValidNoEst_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 38),
    _StaValidNoEst_Type()
)
staValidNoEst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staValidNoEst.setStatus("current")
_StaMonSent_Type = Counter64
_StaMonSent_Object = MibScalar
staMonSent = _StaMonSent_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 39),
    _StaMonSent_Type()
)
staMonSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staMonSent.setStatus("current")
_StaMonRcvd_Type = Counter64
_StaMonRcvd_Object = MibScalar
staMonRcvd = _StaMonRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 40),
    _StaMonRcvd_Type()
)
staMonRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staMonRcvd.setStatus("current")
_StaMonSucc_Type = Counter64
_StaMonSucc_Object = MibScalar
staMonSucc = _StaMonSucc_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 41),
    _StaMonSucc_Type()
)
staMonSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staMonSucc.setStatus("current")
_StaMonFail_Type = Counter64
_StaMonFail_Object = MibScalar
staMonFail = _StaMonFail_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 42),
    _StaMonFail_Type()
)
staMonFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staMonFail.setStatus("current")
_IipSpilloverMIPused_Type = Counter64
_IipSpilloverMIPused_Object = MibScalar
iipSpilloverMIPused = _IipSpilloverMIPused_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 66, 43),
    _IipSpilloverMIPused_Type()
)
iipSpilloverMIPused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iipSpilloverMIPused.setStatus("current")
_NsAaaStatsGroup_ObjectIdentity = ObjectIdentity
nsAaaStatsGroup = _NsAaaStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 67)
)
_AaaAuthFail_Type = Counter64
_AaaAuthFail_Object = MibScalar
aaaAuthFail = _AaaAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 67, 1),
    _AaaAuthFail_Type()
)
aaaAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaAuthFail.setStatus("current")
_AaaAuthSuccess_Type = Counter64
_AaaAuthSuccess_Object = MibScalar
aaaAuthSuccess = _AaaAuthSuccess_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 67, 2),
    _AaaAuthSuccess_Type()
)
aaaAuthSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaAuthSuccess.setStatus("current")
_AaaAuthNonHttpFail_Type = Counter64
_AaaAuthNonHttpFail_Object = MibScalar
aaaAuthNonHttpFail = _AaaAuthNonHttpFail_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 67, 3),
    _AaaAuthNonHttpFail_Type()
)
aaaAuthNonHttpFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaAuthNonHttpFail.setStatus("current")
_AaaAuthOnlyHttpFail_Type = Counter64
_AaaAuthOnlyHttpFail_Object = MibScalar
aaaAuthOnlyHttpFail = _AaaAuthOnlyHttpFail_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 67, 4),
    _AaaAuthOnlyHttpFail_Type()
)
aaaAuthOnlyHttpFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaAuthOnlyHttpFail.setStatus("current")
_AaaAuthNonHttpSuccess_Type = Counter64
_AaaAuthNonHttpSuccess_Object = MibScalar
aaaAuthNonHttpSuccess = _AaaAuthNonHttpSuccess_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 67, 5),
    _AaaAuthNonHttpSuccess_Type()
)
aaaAuthNonHttpSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaAuthNonHttpSuccess.setStatus("current")
_AaaAuthOnlyHttpSuccess_Type = Counter64
_AaaAuthOnlyHttpSuccess_Object = MibScalar
aaaAuthOnlyHttpSuccess = _AaaAuthOnlyHttpSuccess_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 67, 6),
    _AaaAuthOnlyHttpSuccess_Type()
)
aaaAuthOnlyHttpSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaAuthOnlyHttpSuccess.setStatus("current")
_AaaTotSessions_Type = Counter64
_AaaTotSessions_Object = MibScalar
aaaTotSessions = _AaaTotSessions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 67, 7),
    _AaaTotSessions_Type()
)
aaaTotSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaTotSessions.setStatus("current")
_AaaTotSessionTimeout_Type = Counter64
_AaaTotSessionTimeout_Object = MibScalar
aaaTotSessionTimeout = _AaaTotSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 67, 8),
    _AaaTotSessionTimeout_Type()
)
aaaTotSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaTotSessionTimeout.setStatus("current")
_AaaCurSessions_Type = Counter64
_AaaCurSessions_Object = MibScalar
aaaCurSessions = _AaaCurSessions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 67, 9),
    _AaaCurSessions_Type()
)
aaaCurSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaCurSessions.setStatus("current")
_NsGlobalConfigSettings_ObjectIdentity = ObjectIdentity
nsGlobalConfigSettings = _NsGlobalConfigSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 68)
)
_WebServerHttpPorts_Type = OctetString
_WebServerHttpPorts_Object = MibScalar
webServerHttpPorts = _WebServerHttpPorts_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 68, 1),
    _WebServerHttpPorts_Type()
)
webServerHttpPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webServerHttpPorts.setStatus("current")
_MaxTcpConnections_Type = Integer32
_MaxTcpConnections_Object = MibScalar
maxTcpConnections = _MaxTcpConnections_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 68, 2),
    _MaxTcpConnections_Type()
)
maxTcpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxTcpConnections.setStatus("current")
_MaxReqPerConnection_Type = Integer32
_MaxReqPerConnection_Object = MibScalar
maxReqPerConnection = _MaxReqPerConnection_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 68, 3),
    _MaxReqPerConnection_Type()
)
maxReqPerConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxReqPerConnection.setStatus("current")
_CipInsertionStatus_Type = ModeStatus
_CipInsertionStatus_Object = MibScalar
cipInsertionStatus = _CipInsertionStatus_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 68, 4),
    _CipInsertionStatus_Type()
)
cipInsertionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipInsertionStatus.setStatus("current")
_CipInsertionHeader_Type = OctetString
_CipInsertionHeader_Object = MibScalar
cipInsertionHeader = _CipInsertionHeader_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 68, 5),
    _CipInsertionHeader_Type()
)
cipInsertionHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipInsertionHeader.setStatus("current")
_CookieVersionInserted_Type = Integer32
_CookieVersionInserted_Object = MibScalar
cookieVersionInserted = _CookieVersionInserted_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 68, 6),
    _CookieVersionInserted_Type()
)
cookieVersionInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cookieVersionInserted.setStatus("current")
_MinPathMTU_Type = Integer32
_MinPathMTU_Object = MibScalar
minPathMTU = _MinPathMTU_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 68, 7),
    _MinPathMTU_Type()
)
minPathMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minPathMTU.setStatus("current")
_MtuEntryTimeoutValue_Type = TimeTicks
_MtuEntryTimeoutValue_Object = MibScalar
mtuEntryTimeoutValue = _MtuEntryTimeoutValue_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 68, 8),
    _MtuEntryTimeoutValue_Type()
)
mtuEntryTimeoutValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtuEntryTimeoutValue.setStatus("current")
_FtpPortRange_Type = OctetString
_FtpPortRange_Object = MibScalar
ftpPortRange = _FtpPortRange_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 68, 9),
    _FtpPortRange_Type()
)
ftpPortRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpPortRange.setStatus("current")
_NsPolicyInfrastructureGroup_ObjectIdentity = ObjectIdentity
nsPolicyInfrastructureGroup = _NsPolicyInfrastructureGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 69)
)
_PiPolicyTable_Object = MibTable
piPolicyTable = _PiPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 69, 1)
)
if mibBuilder.loadTexts:
    piPolicyTable.setStatus("current")
_PiPolicyEntry_Object = MibTableRow
piPolicyEntry = _PiPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 69, 1, 1)
)
piPolicyEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "piPolName"),
)
if mibBuilder.loadTexts:
    piPolicyEntry.setStatus("current")
_PiPolName_Type = OctetString
_PiPolName_Object = MibTableColumn
piPolName = _PiPolName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 69, 1, 1, 1),
    _PiPolName_Type()
)
piPolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    piPolName.setStatus("current")
_PiPolicyHits_Type = Counter64
_PiPolicyHits_Object = MibTableColumn
piPolicyHits = _PiPolicyHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 69, 1, 1, 2),
    _PiPolicyHits_Type()
)
piPolicyHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    piPolicyHits.setStatus("current")
_PiPolicyUndefHits_Type = Counter64
_PiPolicyUndefHits_Object = MibTableColumn
piPolicyUndefHits = _PiPolicyUndefHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 69, 1, 1, 3),
    _PiPolicyUndefHits_Type()
)
piPolicyUndefHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    piPolicyUndefHits.setStatus("current")
_PiPolFullName_Type = OctetString
_PiPolFullName_Object = MibTableColumn
piPolFullName = _PiPolFullName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 1, 69, 1, 1, 4),
    _PiPolFullName_Type()
)
piPolFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    piPolFullName.setStatus("current")
_NsSvcGroup_ObjectIdentity = ObjectIdentity
nsSvcGroup = _NsSvcGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2)
)
_ServiceTable_Object = MibTable
serviceTable = _ServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    serviceTable.setStatus("current")
_ServiceEntry_Object = MibTableRow
serviceEntry = _ServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1)
)
serviceEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "svcServiceName"),
)
if mibBuilder.loadTexts:
    serviceEntry.setStatus("current")
_SvcServiceName_Type = OctetString
_SvcServiceName_Object = MibTableColumn
svcServiceName = _SvcServiceName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 1),
    _SvcServiceName_Type()
)
svcServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcServiceName.setStatus("current")
_SvcIpAddress_Type = IpAddress
_SvcIpAddress_Object = MibTableColumn
svcIpAddress = _SvcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 2),
    _SvcIpAddress_Type()
)
svcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcIpAddress.setStatus("current")
_SvcPort_Type = Integer32
_SvcPort_Object = MibTableColumn
svcPort = _SvcPort_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 3),
    _SvcPort_Type()
)
svcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcPort.setStatus("current")
_SvcServiceType_Type = EntityProtocolType
_SvcServiceType_Object = MibTableColumn
svcServiceType = _SvcServiceType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 4),
    _SvcServiceType_Type()
)
svcServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcServiceType.setStatus("current")
_SvcState_Type = EntityState
_SvcState_Object = MibTableColumn
svcState = _SvcState_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 5),
    _SvcState_Type()
)
svcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcState.setStatus("current")
_SvcMaxReqPerConn_Type = Integer32
_SvcMaxReqPerConn_Object = MibTableColumn
svcMaxReqPerConn = _SvcMaxReqPerConn_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 6),
    _SvcMaxReqPerConn_Type()
)
svcMaxReqPerConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcMaxReqPerConn.setStatus("current")
_SvcAvgTransactionTime_Type = TimeTicks
_SvcAvgTransactionTime_Object = MibTableColumn
svcAvgTransactionTime = _SvcAvgTransactionTime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 7),
    _SvcAvgTransactionTime_Type()
)
svcAvgTransactionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAvgTransactionTime.setStatus("current")
_SvcEstablishedConn_Type = Counter32
_SvcEstablishedConn_Object = MibTableColumn
svcEstablishedConn = _SvcEstablishedConn_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 8),
    _SvcEstablishedConn_Type()
)
svcEstablishedConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcEstablishedConn.setStatus("current")
_SvcActiveConn_Type = Gauge32
_SvcActiveConn_Object = MibTableColumn
svcActiveConn = _SvcActiveConn_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 9),
    _SvcActiveConn_Type()
)
svcActiveConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcActiveConn.setStatus("current")
_SvcSurgeCount_Type = Counter32
_SvcSurgeCount_Object = MibTableColumn
svcSurgeCount = _SvcSurgeCount_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 10),
    _SvcSurgeCount_Type()
)
svcSurgeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcSurgeCount.setStatus("current")
_SvcTotalRequestsLow_Type = Counter32
_SvcTotalRequestsLow_Object = MibTableColumn
svcTotalRequestsLow = _SvcTotalRequestsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 11),
    _SvcTotalRequestsLow_Type()
)
svcTotalRequestsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTotalRequestsLow.setStatus("obsolete")
_SvcTotalRequestsHigh_Type = Counter32
_SvcTotalRequestsHigh_Object = MibTableColumn
svcTotalRequestsHigh = _SvcTotalRequestsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 12),
    _SvcTotalRequestsHigh_Type()
)
svcTotalRequestsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTotalRequestsHigh.setStatus("obsolete")
_SvcTotalRequestBytesLow_Type = Counter32
_SvcTotalRequestBytesLow_Object = MibTableColumn
svcTotalRequestBytesLow = _SvcTotalRequestBytesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 13),
    _SvcTotalRequestBytesLow_Type()
)
svcTotalRequestBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTotalRequestBytesLow.setStatus("obsolete")
_SvcTotalRequestBytesHigh_Type = Counter32
_SvcTotalRequestBytesHigh_Object = MibTableColumn
svcTotalRequestBytesHigh = _SvcTotalRequestBytesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 14),
    _SvcTotalRequestBytesHigh_Type()
)
svcTotalRequestBytesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTotalRequestBytesHigh.setStatus("obsolete")
_SvcTotalResponsesLow_Type = Counter32
_SvcTotalResponsesLow_Object = MibTableColumn
svcTotalResponsesLow = _SvcTotalResponsesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 15),
    _SvcTotalResponsesLow_Type()
)
svcTotalResponsesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTotalResponsesLow.setStatus("obsolete")
_SvcTotalResponsesHigh_Type = Counter32
_SvcTotalResponsesHigh_Object = MibTableColumn
svcTotalResponsesHigh = _SvcTotalResponsesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 16),
    _SvcTotalResponsesHigh_Type()
)
svcTotalResponsesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTotalResponsesHigh.setStatus("obsolete")
_SvcTotalResponseBytesLow_Type = Counter32
_SvcTotalResponseBytesLow_Object = MibTableColumn
svcTotalResponseBytesLow = _SvcTotalResponseBytesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 17),
    _SvcTotalResponseBytesLow_Type()
)
svcTotalResponseBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTotalResponseBytesLow.setStatus("obsolete")
_SvcTotalResponseBytesHigh_Type = Counter32
_SvcTotalResponseBytesHigh_Object = MibTableColumn
svcTotalResponseBytesHigh = _SvcTotalResponseBytesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 18),
    _SvcTotalResponseBytesHigh_Type()
)
svcTotalResponseBytesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTotalResponseBytesHigh.setStatus("obsolete")
_SvcTotalPktsRecvdLow_Type = Counter32
_SvcTotalPktsRecvdLow_Object = MibTableColumn
svcTotalPktsRecvdLow = _SvcTotalPktsRecvdLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 19),
    _SvcTotalPktsRecvdLow_Type()
)
svcTotalPktsRecvdLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTotalPktsRecvdLow.setStatus("obsolete")
_SvcTotalPktsRecvdHigh_Type = Counter32
_SvcTotalPktsRecvdHigh_Object = MibTableColumn
svcTotalPktsRecvdHigh = _SvcTotalPktsRecvdHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 20),
    _SvcTotalPktsRecvdHigh_Type()
)
svcTotalPktsRecvdHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTotalPktsRecvdHigh.setStatus("obsolete")
_SvcTotalPktsSentLow_Type = Counter32
_SvcTotalPktsSentLow_Object = MibTableColumn
svcTotalPktsSentLow = _SvcTotalPktsSentLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 21),
    _SvcTotalPktsSentLow_Type()
)
svcTotalPktsSentLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTotalPktsSentLow.setStatus("obsolete")
_SvcTotalPktsSentHigh_Type = Counter32
_SvcTotalPktsSentHigh_Object = MibTableColumn
svcTotalPktsSentHigh = _SvcTotalPktsSentHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 22),
    _SvcTotalPktsSentHigh_Type()
)
svcTotalPktsSentHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTotalPktsSentHigh.setStatus("obsolete")
_SvcTotalSynsRecvdLow_Type = Counter32
_SvcTotalSynsRecvdLow_Object = MibTableColumn
svcTotalSynsRecvdLow = _SvcTotalSynsRecvdLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 23),
    _SvcTotalSynsRecvdLow_Type()
)
svcTotalSynsRecvdLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTotalSynsRecvdLow.setStatus("obsolete")
_SvcTotalSynsRecvdHigh_Type = Counter32
_SvcTotalSynsRecvdHigh_Object = MibTableColumn
svcTotalSynsRecvdHigh = _SvcTotalSynsRecvdHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 24),
    _SvcTotalSynsRecvdHigh_Type()
)
svcTotalSynsRecvdHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTotalSynsRecvdHigh.setStatus("obsolete")
_SvcTotalRequests_Type = Counter64
_SvcTotalRequests_Object = MibTableColumn
svcTotalRequests = _SvcTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 30),
    _SvcTotalRequests_Type()
)
svcTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTotalRequests.setStatus("current")
_SvcTotalRequestBytes_Type = Counter64
_SvcTotalRequestBytes_Object = MibTableColumn
svcTotalRequestBytes = _SvcTotalRequestBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 31),
    _SvcTotalRequestBytes_Type()
)
svcTotalRequestBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTotalRequestBytes.setStatus("current")
_SvcTotalResponses_Type = Counter64
_SvcTotalResponses_Object = MibTableColumn
svcTotalResponses = _SvcTotalResponses_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 32),
    _SvcTotalResponses_Type()
)
svcTotalResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTotalResponses.setStatus("current")
_SvcTotalResponseBytes_Type = Counter64
_SvcTotalResponseBytes_Object = MibTableColumn
svcTotalResponseBytes = _SvcTotalResponseBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 33),
    _SvcTotalResponseBytes_Type()
)
svcTotalResponseBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTotalResponseBytes.setStatus("current")
_SvcTotalPktsRecvd_Type = Counter64
_SvcTotalPktsRecvd_Object = MibTableColumn
svcTotalPktsRecvd = _SvcTotalPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 34),
    _SvcTotalPktsRecvd_Type()
)
svcTotalPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTotalPktsRecvd.setStatus("current")
_SvcTotalPktsSent_Type = Counter64
_SvcTotalPktsSent_Object = MibTableColumn
svcTotalPktsSent = _SvcTotalPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 35),
    _SvcTotalPktsSent_Type()
)
svcTotalPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTotalPktsSent.setStatus("current")
_SvcTotalSynsRecvd_Type = Counter64
_SvcTotalSynsRecvd_Object = MibTableColumn
svcTotalSynsRecvd = _SvcTotalSynsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 36),
    _SvcTotalSynsRecvd_Type()
)
svcTotalSynsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTotalSynsRecvd.setStatus("current")
_SvcGslbSiteName_Type = OctetString
_SvcGslbSiteName_Object = MibTableColumn
svcGslbSiteName = _SvcGslbSiteName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 37),
    _SvcGslbSiteName_Type()
)
svcGslbSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGslbSiteName.setStatus("current")
_SvcAvgSvrTTFB_Type = Gauge32
_SvcAvgSvrTTFB_Object = MibTableColumn
svcAvgSvrTTFB = _SvcAvgSvrTTFB_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 38),
    _SvcAvgSvrTTFB_Type()
)
svcAvgSvrTTFB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcAvgSvrTTFB.setStatus("current")
_SvctotalJsTransactions_Type = Counter64
_SvctotalJsTransactions_Object = MibTableColumn
svctotalJsTransactions = _SvctotalJsTransactions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 39),
    _SvctotalJsTransactions_Type()
)
svctotalJsTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svctotalJsTransactions.setStatus("current")
_SvcdosQDepth_Type = Counter32
_SvcdosQDepth_Object = MibTableColumn
svcdosQDepth = _SvcdosQDepth_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 40),
    _SvcdosQDepth_Type()
)
svcdosQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcdosQDepth.setStatus("current")
_SvcCurClntConnections_Type = Gauge32
_SvcCurClntConnections_Object = MibTableColumn
svcCurClntConnections = _SvcCurClntConnections_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 41),
    _SvcCurClntConnections_Type()
)
svcCurClntConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcCurClntConnections.setStatus("current")
_SvcRequestRate_Type = OctetString
_SvcRequestRate_Object = MibTableColumn
svcRequestRate = _SvcRequestRate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 42),
    _SvcRequestRate_Type()
)
svcRequestRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRequestRate.setStatus("current")
_SvcRxBytesRate_Type = OctetString
_SvcRxBytesRate_Object = MibTableColumn
svcRxBytesRate = _SvcRxBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 43),
    _SvcRxBytesRate_Type()
)
svcRxBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRxBytesRate.setStatus("current")
_SvcTxBytesRate_Type = OctetString
_SvcTxBytesRate_Object = MibTableColumn
svcTxBytesRate = _SvcTxBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 44),
    _SvcTxBytesRate_Type()
)
svcTxBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTxBytesRate.setStatus("current")
_SvcSynfloodRate_Type = OctetString
_SvcSynfloodRate_Object = MibTableColumn
svcSynfloodRate = _SvcSynfloodRate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 45),
    _SvcSynfloodRate_Type()
)
svcSynfloodRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcSynfloodRate.setStatus("current")
_SvcTicksSinceLastStateChange_Type = TimeTicks
_SvcTicksSinceLastStateChange_Object = MibTableColumn
svcTicksSinceLastStateChange = _SvcTicksSinceLastStateChange_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 47),
    _SvcTicksSinceLastStateChange_Type()
)
svcTicksSinceLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTicksSinceLastStateChange.setStatus("current")
_SvcTotalClients_Type = Counter64
_SvcTotalClients_Object = MibTableColumn
svcTotalClients = _SvcTotalClients_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 48),
    _SvcTotalClients_Type()
)
svcTotalClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTotalClients.setStatus("current")
_SvcTotalServers_Type = Counter64
_SvcTotalServers_Object = MibTableColumn
svcTotalServers = _SvcTotalServers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 49),
    _SvcTotalServers_Type()
)
svcTotalServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTotalServers.setStatus("current")
_SvcMaxClients_Type = Integer32
_SvcMaxClients_Object = MibTableColumn
svcMaxClients = _SvcMaxClients_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 52),
    _SvcMaxClients_Type()
)
svcMaxClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcMaxClients.setStatus("current")
_SvcActiveTransactions_Type = Gauge32
_SvcActiveTransactions_Object = MibTableColumn
svcActiveTransactions = _SvcActiveTransactions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 53),
    _SvcActiveTransactions_Type()
)
svcActiveTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcActiveTransactions.setStatus("current")
_SvcServiceFullName_Type = OctetString
_SvcServiceFullName_Object = MibTableColumn
svcServiceFullName = _SvcServiceFullName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 54),
    _SvcServiceFullName_Type()
)
svcServiceFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcServiceFullName.setStatus("current")
_SvcInetAddressType_Type = InetAddressType
_SvcInetAddressType_Object = MibTableColumn
svcInetAddressType = _SvcInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 55),
    _SvcInetAddressType_Type()
)
svcInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcInetAddressType.setStatus("current")
_SvcInetAddress_Type = InetAddress
_SvcInetAddress_Object = MibTableColumn
svcInetAddress = _SvcInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 1, 1, 56),
    _SvcInetAddress_Type()
)
svcInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcInetAddress.setStatus("current")
_ServerTable_Object = MibTable
serverTable = _ServerTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    serverTable.setStatus("current")
_ServerEntry_Object = MibTableRow
serverEntry = _ServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 2, 1)
)
serverEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "serverName"),
)
if mibBuilder.loadTexts:
    serverEntry.setStatus("current")
_ServerName_Type = OctetString
_ServerName_Object = MibTableColumn
serverName = _ServerName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 2, 1, 1),
    _ServerName_Type()
)
serverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverName.setStatus("current")
_ServerIpAddress_Type = IpAddress
_ServerIpAddress_Object = MibTableColumn
serverIpAddress = _ServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 2, 1, 2),
    _ServerIpAddress_Type()
)
serverIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverIpAddress.setStatus("current")
_ServerState_Type = EntityState
_ServerState_Object = MibTableColumn
serverState = _ServerState_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 2, 1, 3),
    _ServerState_Type()
)
serverState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverState.setStatus("current")
_ServerDelay_Type = Integer32
_ServerDelay_Object = MibTableColumn
serverDelay = _ServerDelay_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 2, 1, 4),
    _ServerDelay_Type()
)
serverDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverDelay.setStatus("current")
_ServerFullName_Type = OctetString
_ServerFullName_Object = MibTableColumn
serverFullName = _ServerFullName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 2, 1, 5),
    _ServerFullName_Type()
)
serverFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverFullName.setStatus("current")
_ServerInetAddressType_Type = InetAddressType
_ServerInetAddressType_Object = MibTableColumn
serverInetAddressType = _ServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 2, 1, 6),
    _ServerInetAddressType_Type()
)
serverInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverInetAddressType.setStatus("current")
_ServerInetAddress_Type = InetAddress
_ServerInetAddress_Object = MibTableColumn
serverInetAddress = _ServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 2, 1, 7),
    _ServerInetAddress_Type()
)
serverInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverInetAddress.setStatus("current")
_ServiceScpolicyTable_Object = MibTable
serviceScpolicyTable = _ServiceScpolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3)
)
if mibBuilder.loadTexts:
    serviceScpolicyTable.setStatus("current")
_ServiceScpolicyEntry_Object = MibTableRow
serviceScpolicyEntry = _ServiceScpolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1)
)
serviceScpolicyEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "svcServiceName"),
    (0, "NS-ROOT-MIB", "scPolicyName"),
)
if mibBuilder.loadTexts:
    serviceScpolicyEntry.setStatus("current")
_SvcscpolicyPrimaryIPAddress_Type = IpAddress
_SvcscpolicyPrimaryIPAddress_Object = MibTableColumn
svcscpolicyPrimaryIPAddress = _SvcscpolicyPrimaryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1, 3),
    _SvcscpolicyPrimaryIPAddress_Type()
)
svcscpolicyPrimaryIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcscpolicyPrimaryIPAddress.setStatus("current")
_SvcscpolicyPrimaryPort_Type = Integer32
_SvcscpolicyPrimaryPort_Object = MibTableColumn
svcscpolicyPrimaryPort = _SvcscpolicyPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1, 4),
    _SvcscpolicyPrimaryPort_Type()
)
svcscpolicyPrimaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcscpolicyPrimaryPort.setStatus("current")
_SvcscpolicyDesIpAddress_Type = IpAddress
_SvcscpolicyDesIpAddress_Object = MibTableColumn
svcscpolicyDesIpAddress = _SvcscpolicyDesIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1, 5),
    _SvcscpolicyDesIpAddress_Type()
)
svcscpolicyDesIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcscpolicyDesIpAddress.setStatus("obsolete")
_SvcscpolicyDestPort_Type = Integer32
_SvcscpolicyDestPort_Object = MibTableColumn
svcscpolicyDestPort = _SvcscpolicyDestPort_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1, 6),
    _SvcscpolicyDestPort_Type()
)
svcscpolicyDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcscpolicyDestPort.setStatus("obsolete")
_SvcscpolicyAvgServerTransactionTime_Type = Gauge32
_SvcscpolicyAvgServerTransactionTime_Object = MibTableColumn
svcscpolicyAvgServerTransactionTime = _SvcscpolicyAvgServerTransactionTime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1, 7),
    _SvcscpolicyAvgServerTransactionTime_Type()
)
svcscpolicyAvgServerTransactionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcscpolicyAvgServerTransactionTime.setStatus("obsolete")
_SvcscpolicyTotClientTransaction_Type = Counter64
_SvcscpolicyTotClientTransaction_Object = MibTableColumn
svcscpolicyTotClientTransaction = _SvcscpolicyTotClientTransaction_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1, 8),
    _SvcscpolicyTotClientTransaction_Type()
)
svcscpolicyTotClientTransaction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcscpolicyTotClientTransaction.setStatus("obsolete")
_SvcscpolicyTotOpenConn_Type = Counter32
_SvcscpolicyTotOpenConn_Object = MibTableColumn
svcscpolicyTotOpenConn = _SvcscpolicyTotOpenConn_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1, 9),
    _SvcscpolicyTotOpenConn_Type()
)
svcscpolicyTotOpenConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcscpolicyTotOpenConn.setStatus("obsolete")
_SvcscpolicydesIpAddress_Type = IpAddress
_SvcscpolicydesIpAddress_Object = MibTableColumn
svcscpolicydesIpAddress = _SvcscpolicydesIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1, 10),
    _SvcscpolicydesIpAddress_Type()
)
svcscpolicydesIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcscpolicydesIpAddress.setStatus("current")
_SvcscpolicydestPort_Type = Integer32
_SvcscpolicydestPort_Object = MibTableColumn
svcscpolicydestPort = _SvcscpolicydestPort_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1, 11),
    _SvcscpolicydestPort_Type()
)
svcscpolicydestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcscpolicydestPort.setStatus("current")
_SvcscpolicyavgServerTransactionTime_Type = Gauge32
_SvcscpolicyavgServerTransactionTime_Object = MibTableColumn
svcscpolicyavgServerTransactionTime = _SvcscpolicyavgServerTransactionTime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1, 12),
    _SvcscpolicyavgServerTransactionTime_Type()
)
svcscpolicyavgServerTransactionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcscpolicyavgServerTransactionTime.setStatus("current")
_SvcscpolicytotClientTransaction_Type = Counter64
_SvcscpolicytotClientTransaction_Object = MibTableColumn
svcscpolicytotClientTransaction = _SvcscpolicytotClientTransaction_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1, 13),
    _SvcscpolicytotClientTransaction_Type()
)
svcscpolicytotClientTransaction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcscpolicytotClientTransaction.setStatus("current")
_SvcscpolicytotOpenConn_Type = Gauge32
_SvcscpolicytotOpenConn_Object = MibTableColumn
svcscpolicytotOpenConn = _SvcscpolicytotOpenConn_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1, 14),
    _SvcscpolicytotOpenConn_Type()
)
svcscpolicytotOpenConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcscpolicytotOpenConn.setStatus("current")
_SvcscpolicyscPhysicalServiceIP_Type = IpAddress
_SvcscpolicyscPhysicalServiceIP_Object = MibTableColumn
svcscpolicyscPhysicalServiceIP = _SvcscpolicyscPhysicalServiceIP_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1, 15),
    _SvcscpolicyscPhysicalServiceIP_Type()
)
svcscpolicyscPhysicalServiceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcscpolicyscPhysicalServiceIP.setStatus("current")
_SvcscpolicyscPhysicalServicePort_Type = Integer32
_SvcscpolicyscPhysicalServicePort_Object = MibTableColumn
svcscpolicyscPhysicalServicePort = _SvcscpolicyscPhysicalServicePort_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1, 16),
    _SvcscpolicyscPhysicalServicePort_Type()
)
svcscpolicyscPhysicalServicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcscpolicyscPhysicalServicePort.setStatus("current")
_SvcscpolicyscCurrentWaitingTime_Type = Gauge32
_SvcscpolicyscCurrentWaitingTime_Object = MibTableColumn
svcscpolicyscCurrentWaitingTime = _SvcscpolicyscCurrentWaitingTime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1, 17),
    _SvcscpolicyscCurrentWaitingTime_Type()
)
svcscpolicyscCurrentWaitingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcscpolicyscCurrentWaitingTime.setStatus("current")
_SvcscpolicyscCurrentClientConnections_Type = Gauge32
_SvcscpolicyscCurrentClientConnections_Object = MibTableColumn
svcscpolicyscCurrentClientConnections = _SvcscpolicyscCurrentClientConnections_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1, 18),
    _SvcscpolicyscCurrentClientConnections_Type()
)
svcscpolicyscCurrentClientConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcscpolicyscCurrentClientConnections.setStatus("current")
_SvcscpolicyscTotalClientConnections_Type = Counter64
_SvcscpolicyscTotalClientConnections_Object = MibTableColumn
svcscpolicyscTotalClientConnections = _SvcscpolicyscTotalClientConnections_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1, 19),
    _SvcscpolicyscTotalClientConnections_Type()
)
svcscpolicyscTotalClientConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcscpolicyscTotalClientConnections.setStatus("current")
_SvcscpolicyscTotalServerConnections_Type = Counter64
_SvcscpolicyscTotalServerConnections_Object = MibTableColumn
svcscpolicyscTotalServerConnections = _SvcscpolicyscTotalServerConnections_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1, 20),
    _SvcscpolicyscTotalServerConnections_Type()
)
svcscpolicyscTotalServerConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcscpolicyscTotalServerConnections.setStatus("current")
_SvcscpolicyscTotalRequestsReceived_Type = Counter64
_SvcscpolicyscTotalRequestsReceived_Object = MibTableColumn
svcscpolicyscTotalRequestsReceived = _SvcscpolicyscTotalRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1, 21),
    _SvcscpolicyscTotalRequestsReceived_Type()
)
svcscpolicyscTotalRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcscpolicyscTotalRequestsReceived.setStatus("current")
_SvcscpolicyscTotalRequestBytes_Type = Counter64
_SvcscpolicyscTotalRequestBytes_Object = MibTableColumn
svcscpolicyscTotalRequestBytes = _SvcscpolicyscTotalRequestBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1, 22),
    _SvcscpolicyscTotalRequestBytes_Type()
)
svcscpolicyscTotalRequestBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcscpolicyscTotalRequestBytes.setStatus("current")
_SvcscpolicyscTotalResponsesReceived_Type = Counter64
_SvcscpolicyscTotalResponsesReceived_Object = MibTableColumn
svcscpolicyscTotalResponsesReceived = _SvcscpolicyscTotalResponsesReceived_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1, 23),
    _SvcscpolicyscTotalResponsesReceived_Type()
)
svcscpolicyscTotalResponsesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcscpolicyscTotalResponsesReceived.setStatus("current")
_SvcscpolicyscTotalResponseBytes_Type = Counter64
_SvcscpolicyscTotalResponseBytes_Object = MibTableColumn
svcscpolicyscTotalResponseBytes = _SvcscpolicyscTotalResponseBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1, 24),
    _SvcscpolicyscTotalResponseBytes_Type()
)
svcscpolicyscTotalResponseBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcscpolicyscTotalResponseBytes.setStatus("current")
_SvcscpolicyscCurrentSurgeQClients_Type = Gauge32
_SvcscpolicyscCurrentSurgeQClients_Object = MibTableColumn
svcscpolicyscCurrentSurgeQClients = _SvcscpolicyscCurrentSurgeQClients_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1, 25),
    _SvcscpolicyscCurrentSurgeQClients_Type()
)
svcscpolicyscCurrentSurgeQClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcscpolicyscCurrentSurgeQClients.setStatus("current")
_SvcscpolicyscCurrentWaitingClients_Type = Gauge32
_SvcscpolicyscCurrentWaitingClients_Object = MibTableColumn
svcscpolicyscCurrentWaitingClients = _SvcscpolicyscCurrentWaitingClients_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1, 26),
    _SvcscpolicyscCurrentWaitingClients_Type()
)
svcscpolicyscCurrentWaitingClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcscpolicyscCurrentWaitingClients.setStatus("current")
_SvcscpolicyscTotalServerTransactions_Type = Counter64
_SvcscpolicyscTotalServerTransactions_Object = MibTableColumn
svcscpolicyscTotalServerTransactions = _SvcscpolicyscTotalServerTransactions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1, 27),
    _SvcscpolicyscTotalServerTransactions_Type()
)
svcscpolicyscTotalServerTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcscpolicyscTotalServerTransactions.setStatus("current")
_SvcscpolicyscTotalServerTTFBTransactions_Type = Counter64
_SvcscpolicyscTotalServerTTFBTransactions_Object = MibTableColumn
svcscpolicyscTotalServerTTFBTransactions = _SvcscpolicyscTotalServerTTFBTransactions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1, 28),
    _SvcscpolicyscTotalServerTTFBTransactions_Type()
)
svcscpolicyscTotalServerTTFBTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcscpolicyscTotalServerTTFBTransactions.setStatus("current")
_SvcscpolicyscTotalServerTTLB_Type = Counter64
_SvcscpolicyscTotalServerTTLB_Object = MibTableColumn
svcscpolicyscTotalServerTTLB = _SvcscpolicyscTotalServerTTLB_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1, 29),
    _SvcscpolicyscTotalServerTTLB_Type()
)
svcscpolicyscTotalServerTTLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcscpolicyscTotalServerTTLB.setStatus("current")
_SvcscpolicyscTotalClientTTLB_Type = Counter64
_SvcscpolicyscTotalClientTTLB_Object = MibTableColumn
svcscpolicyscTotalClientTTLB = _SvcscpolicyscTotalClientTTLB_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1, 30),
    _SvcscpolicyscTotalClientTTLB_Type()
)
svcscpolicyscTotalClientTTLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcscpolicyscTotalClientTTLB.setStatus("current")
_SvcscpolicyscTotalServerTTFB_Type = Counter64
_SvcscpolicyscTotalServerTTFB_Object = MibTableColumn
svcscpolicyscTotalServerTTFB = _SvcscpolicyscTotalServerTTFB_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1, 31),
    _SvcscpolicyscTotalServerTTFB_Type()
)
svcscpolicyscTotalServerTTFB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcscpolicyscTotalServerTTFB.setStatus("current")
_SvcscpolicyscAverageClientTTLB_Type = Gauge32
_SvcscpolicyscAverageClientTTLB_Object = MibTableColumn
svcscpolicyscAverageClientTTLB = _SvcscpolicyscAverageClientTTLB_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1, 32),
    _SvcscpolicyscAverageClientTTLB_Type()
)
svcscpolicyscAverageClientTTLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcscpolicyscAverageClientTTLB.setStatus("current")
_SvcscpolicyscAverageServerTTFB_Type = Gauge32
_SvcscpolicyscAverageServerTTFB_Object = MibTableColumn
svcscpolicyscAverageServerTTFB = _SvcscpolicyscAverageServerTTFB_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 3, 1, 33),
    _SvcscpolicyscAverageServerTTFB_Type()
)
svcscpolicyscAverageServerTTFB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcscpolicyscAverageServerTTFB.setStatus("current")
_ServiceAdvanceSslConfigTable_Object = MibTable
serviceAdvanceSslConfigTable = _ServiceAdvanceSslConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 4)
)
if mibBuilder.loadTexts:
    serviceAdvanceSslConfigTable.setStatus("current")
_ServiceAdvanceSslConfigEntry_Object = MibTableRow
serviceAdvanceSslConfigEntry = _ServiceAdvanceSslConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 4, 1)
)
serviceAdvanceSslConfigEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "svcServiceName"),
)
if mibBuilder.loadTexts:
    serviceAdvanceSslConfigEntry.setStatus("current")
_SvcSslDH_Type = AdminStatus
_SvcSslDH_Object = MibTableColumn
svcSslDH = _SvcSslDH_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 4, 1, 1),
    _SvcSslDH_Type()
)
svcSslDH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcSslDH.setStatus("current")
_SvcSslDHCount_Type = Integer32
_SvcSslDHCount_Object = MibTableColumn
svcSslDHCount = _SvcSslDHCount_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 4, 1, 2),
    _SvcSslDHCount_Type()
)
svcSslDHCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcSslDHCount.setStatus("current")
_SvcSslDHFilePath_Type = OctetString
_SvcSslDHFilePath_Object = MibTableColumn
svcSslDHFilePath = _SvcSslDHFilePath_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 4, 1, 3),
    _SvcSslDHFilePath_Type()
)
svcSslDHFilePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcSslDHFilePath.setStatus("current")
_SvcSsleRSA_Type = AdminStatus
_SvcSsleRSA_Object = MibTableColumn
svcSsleRSA = _SvcSsleRSA_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 4, 1, 4),
    _SvcSsleRSA_Type()
)
svcSsleRSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcSsleRSA.setStatus("current")
_SvcSsleRSACount_Type = Integer32
_SvcSsleRSACount_Object = MibTableColumn
svcSsleRSACount = _SvcSsleRSACount_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 4, 1, 5),
    _SvcSsleRSACount_Type()
)
svcSsleRSACount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcSsleRSACount.setStatus("current")
_SvcSslv2Protocol_Type = AdminStatus
_SvcSslv2Protocol_Object = MibTableColumn
svcSslv2Protocol = _SvcSslv2Protocol_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 4, 1, 6),
    _SvcSslv2Protocol_Type()
)
svcSslv2Protocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcSslv2Protocol.setStatus("current")
_SvcSslv3Protocol_Type = AdminStatus
_SvcSslv3Protocol_Object = MibTableColumn
svcSslv3Protocol = _SvcSslv3Protocol_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 4, 1, 7),
    _SvcSslv3Protocol_Type()
)
svcSslv3Protocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcSslv3Protocol.setStatus("current")
_SvcSslTLSv1Protocol_Type = AdminStatus
_SvcSslTLSv1Protocol_Object = MibTableColumn
svcSslTLSv1Protocol = _SvcSslTLSv1Protocol_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 4, 1, 8),
    _SvcSslTLSv1Protocol_Type()
)
svcSslTLSv1Protocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcSslTLSv1Protocol.setStatus("current")
_SvcSslRedirectSupport_Type = AdminStatus
_SvcSslRedirectSupport_Object = MibTableColumn
svcSslRedirectSupport = _SvcSslRedirectSupport_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 4, 1, 9),
    _SvcSslRedirectSupport_Type()
)
svcSslRedirectSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcSslRedirectSupport.setStatus("current")
_SvcSslClearTextPort_Type = Integer32
_SvcSslClearTextPort_Object = MibTableColumn
svcSslClearTextPort = _SvcSslClearTextPort_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 4, 1, 10),
    _SvcSslClearTextPort_Type()
)
svcSslClearTextPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcSslClearTextPort.setStatus("current")
_ServiceCipherBindingTable_Object = MibTable
serviceCipherBindingTable = _ServiceCipherBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 5)
)
if mibBuilder.loadTexts:
    serviceCipherBindingTable.setStatus("current")
_ServiceCipherBindingEntry_Object = MibTableRow
serviceCipherBindingEntry = _ServiceCipherBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 5, 1)
)
serviceCipherBindingEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "svcServiceName"),
    (0, "NS-ROOT-MIB", "svcSslCipherBindName"),
)
if mibBuilder.loadTexts:
    serviceCipherBindingEntry.setStatus("current")
_SvcSslCipherBindName_Type = OctetString
_SvcSslCipherBindName_Object = MibTableColumn
svcSslCipherBindName = _SvcSslCipherBindName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 5, 1, 1),
    _SvcSslCipherBindName_Type()
)
svcSslCipherBindName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcSslCipherBindName.setStatus("current")
_SvcSslCipherBindDesc_Type = OctetString
_SvcSslCipherBindDesc_Object = MibTableColumn
svcSslCipherBindDesc = _SvcSslCipherBindDesc_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 5, 1, 2),
    _SvcSslCipherBindDesc_Type()
)
svcSslCipherBindDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcSslCipherBindDesc.setStatus("current")
_ServiceGlobalStatsGroup_ObjectIdentity = ObjectIdentity
serviceGlobalStatsGroup = _ServiceGlobalStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 6)
)
_SvcCount_Type = Integer32
_SvcCount_Object = MibScalar
svcCount = _SvcCount_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 6, 1),
    _SvcCount_Type()
)
svcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcCount.setStatus("current")
_ServerCount_Type = Integer32
_ServerCount_Object = MibScalar
serverCount = _ServerCount_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 6, 2),
    _ServerCount_Type()
)
serverCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCount.setStatus("current")
_SvcgroupCount_Type = Integer32
_SvcgroupCount_Object = MibScalar
svcgroupCount = _SvcgroupCount_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 6, 3),
    _SvcgroupCount_Type()
)
svcgroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcgroupCount.setStatus("current")
_SvcgroupmemCount_Type = Integer32
_SvcgroupmemCount_Object = MibScalar
svcgroupmemCount = _SvcgroupmemCount_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 6, 4),
    _SvcgroupmemCount_Type()
)
svcgroupmemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcgroupmemCount.setStatus("current")
_ServiceGroupMemberTable_Object = MibTable
serviceGroupMemberTable = _ServiceGroupMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7)
)
if mibBuilder.loadTexts:
    serviceGroupMemberTable.setStatus("current")
_ServiceGroupMemberEntry_Object = MibTableRow
serviceGroupMemberEntry = _ServiceGroupMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1)
)
serviceGroupMemberEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "svcGrpMemberGroupName"),
    (0, "NS-ROOT-MIB", "svcGrpMemberName"),
)
if mibBuilder.loadTexts:
    serviceGroupMemberEntry.setStatus("current")
_SvcGrpMemberGroupName_Type = OctetString
_SvcGrpMemberGroupName_Object = MibTableColumn
svcGrpMemberGroupName = _SvcGrpMemberGroupName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 1),
    _SvcGrpMemberGroupName_Type()
)
svcGrpMemberGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMemberGroupName.setStatus("current")
_SvcGrpMemberName_Type = OctetString
_SvcGrpMemberName_Object = MibTableColumn
svcGrpMemberName = _SvcGrpMemberName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 2),
    _SvcGrpMemberName_Type()
)
svcGrpMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMemberName.setStatus("current")
_SvcGrpMemberPrimaryIPAddress_Type = IpAddress
_SvcGrpMemberPrimaryIPAddress_Object = MibTableColumn
svcGrpMemberPrimaryIPAddress = _SvcGrpMemberPrimaryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 3),
    _SvcGrpMemberPrimaryIPAddress_Type()
)
svcGrpMemberPrimaryIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMemberPrimaryIPAddress.setStatus("current")
_SvcGrpMemberPrimaryPort_Type = Integer32
_SvcGrpMemberPrimaryPort_Object = MibTableColumn
svcGrpMemberPrimaryPort = _SvcGrpMemberPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 4),
    _SvcGrpMemberPrimaryPort_Type()
)
svcGrpMemberPrimaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMemberPrimaryPort.setStatus("current")
_SvcGrpMemberServiceType_Type = EntityProtocolType
_SvcGrpMemberServiceType_Object = MibTableColumn
svcGrpMemberServiceType = _SvcGrpMemberServiceType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 5),
    _SvcGrpMemberServiceType_Type()
)
svcGrpMemberServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMemberServiceType.setStatus("current")
_SvcGrpMemberState_Type = EntityState
_SvcGrpMemberState_Object = MibTableColumn
svcGrpMemberState = _SvcGrpMemberState_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 6),
    _SvcGrpMemberState_Type()
)
svcGrpMemberState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMemberState.setStatus("current")
_SvcGrpMemberWeight_Type = Integer32
_SvcGrpMemberWeight_Object = MibTableColumn
svcGrpMemberWeight = _SvcGrpMemberWeight_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 7),
    _SvcGrpMemberWeight_Type()
)
svcGrpMemberWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcGrpMemberWeight.setStatus("current")
_SvcGrpMemberMaxReqPerConn_Type = Integer32
_SvcGrpMemberMaxReqPerConn_Object = MibTableColumn
svcGrpMemberMaxReqPerConn = _SvcGrpMemberMaxReqPerConn_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 8),
    _SvcGrpMemberMaxReqPerConn_Type()
)
svcGrpMemberMaxReqPerConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMemberMaxReqPerConn.setStatus("current")
_SvcGrpMemberAvgTransactionTime_Type = TimeTicks
_SvcGrpMemberAvgTransactionTime_Object = MibTableColumn
svcGrpMemberAvgTransactionTime = _SvcGrpMemberAvgTransactionTime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 9),
    _SvcGrpMemberAvgTransactionTime_Type()
)
svcGrpMemberAvgTransactionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMemberAvgTransactionTime.setStatus("current")
_SvcGrpMemberEstablishedConn_Type = Counter32
_SvcGrpMemberEstablishedConn_Object = MibTableColumn
svcGrpMemberEstablishedConn = _SvcGrpMemberEstablishedConn_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 10),
    _SvcGrpMemberEstablishedConn_Type()
)
svcGrpMemberEstablishedConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMemberEstablishedConn.setStatus("current")
_SvcGrpMemberActiveConn_Type = Gauge32
_SvcGrpMemberActiveConn_Object = MibTableColumn
svcGrpMemberActiveConn = _SvcGrpMemberActiveConn_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 11),
    _SvcGrpMemberActiveConn_Type()
)
svcGrpMemberActiveConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMemberActiveConn.setStatus("current")
_SvcGrpMemberSurgeCount_Type = Counter32
_SvcGrpMemberSurgeCount_Object = MibTableColumn
svcGrpMemberSurgeCount = _SvcGrpMemberSurgeCount_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 12),
    _SvcGrpMemberSurgeCount_Type()
)
svcGrpMemberSurgeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMemberSurgeCount.setStatus("current")
_SvcGrpMemberTotalRequests_Type = Counter64
_SvcGrpMemberTotalRequests_Object = MibTableColumn
svcGrpMemberTotalRequests = _SvcGrpMemberTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 13),
    _SvcGrpMemberTotalRequests_Type()
)
svcGrpMemberTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMemberTotalRequests.setStatus("current")
_SvcGrpMemberTotalRequestBytes_Type = Counter64
_SvcGrpMemberTotalRequestBytes_Object = MibTableColumn
svcGrpMemberTotalRequestBytes = _SvcGrpMemberTotalRequestBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 14),
    _SvcGrpMemberTotalRequestBytes_Type()
)
svcGrpMemberTotalRequestBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMemberTotalRequestBytes.setStatus("current")
_SvcGrpMemberTotalResponses_Type = Counter64
_SvcGrpMemberTotalResponses_Object = MibTableColumn
svcGrpMemberTotalResponses = _SvcGrpMemberTotalResponses_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 15),
    _SvcGrpMemberTotalResponses_Type()
)
svcGrpMemberTotalResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMemberTotalResponses.setStatus("current")
_SvcGrpMemberTotalResponseBytes_Type = Counter64
_SvcGrpMemberTotalResponseBytes_Object = MibTableColumn
svcGrpMemberTotalResponseBytes = _SvcGrpMemberTotalResponseBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 16),
    _SvcGrpMemberTotalResponseBytes_Type()
)
svcGrpMemberTotalResponseBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMemberTotalResponseBytes.setStatus("current")
_SvcGrpMemberTotalPktsRecvd_Type = Counter64
_SvcGrpMemberTotalPktsRecvd_Object = MibTableColumn
svcGrpMemberTotalPktsRecvd = _SvcGrpMemberTotalPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 17),
    _SvcGrpMemberTotalPktsRecvd_Type()
)
svcGrpMemberTotalPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMemberTotalPktsRecvd.setStatus("current")
_SvcGrpMemberTotalPktsSent_Type = Counter64
_SvcGrpMemberTotalPktsSent_Object = MibTableColumn
svcGrpMemberTotalPktsSent = _SvcGrpMemberTotalPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 18),
    _SvcGrpMemberTotalPktsSent_Type()
)
svcGrpMemberTotalPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMemberTotalPktsSent.setStatus("current")
_SvcGrpMemberTotalSynsRecvd_Type = Counter64
_SvcGrpMemberTotalSynsRecvd_Object = MibTableColumn
svcGrpMemberTotalSynsRecvd = _SvcGrpMemberTotalSynsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 19),
    _SvcGrpMemberTotalSynsRecvd_Type()
)
svcGrpMemberTotalSynsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMemberTotalSynsRecvd.setStatus("current")
_SvcGrpMemberGslbSiteName_Type = OctetString
_SvcGrpMemberGslbSiteName_Object = MibTableColumn
svcGrpMemberGslbSiteName = _SvcGrpMemberGslbSiteName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 20),
    _SvcGrpMemberGslbSiteName_Type()
)
svcGrpMemberGslbSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMemberGslbSiteName.setStatus("current")
_SvcGrpMemberAvgSvrTTFB_Type = Gauge32
_SvcGrpMemberAvgSvrTTFB_Object = MibTableColumn
svcGrpMemberAvgSvrTTFB = _SvcGrpMemberAvgSvrTTFB_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 21),
    _SvcGrpMemberAvgSvrTTFB_Type()
)
svcGrpMemberAvgSvrTTFB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMemberAvgSvrTTFB.setStatus("current")
_SvcGrpMembertotalJsTransactions_Type = Counter64
_SvcGrpMembertotalJsTransactions_Object = MibTableColumn
svcGrpMembertotalJsTransactions = _SvcGrpMembertotalJsTransactions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 22),
    _SvcGrpMembertotalJsTransactions_Type()
)
svcGrpMembertotalJsTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMembertotalJsTransactions.setStatus("current")
_SvcGrpMemberdosQDepth_Type = Counter32
_SvcGrpMemberdosQDepth_Object = MibTableColumn
svcGrpMemberdosQDepth = _SvcGrpMemberdosQDepth_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 23),
    _SvcGrpMemberdosQDepth_Type()
)
svcGrpMemberdosQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMemberdosQDepth.setStatus("current")
_SvcGrpMemberCurClntConnections_Type = Gauge32
_SvcGrpMemberCurClntConnections_Object = MibTableColumn
svcGrpMemberCurClntConnections = _SvcGrpMemberCurClntConnections_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 24),
    _SvcGrpMemberCurClntConnections_Type()
)
svcGrpMemberCurClntConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMemberCurClntConnections.setStatus("current")
_SvcGrpMemberRequestRate_Type = OctetString
_SvcGrpMemberRequestRate_Object = MibTableColumn
svcGrpMemberRequestRate = _SvcGrpMemberRequestRate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 25),
    _SvcGrpMemberRequestRate_Type()
)
svcGrpMemberRequestRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMemberRequestRate.setStatus("current")
_SvcGrpMemberRxBytesRate_Type = OctetString
_SvcGrpMemberRxBytesRate_Object = MibTableColumn
svcGrpMemberRxBytesRate = _SvcGrpMemberRxBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 26),
    _SvcGrpMemberRxBytesRate_Type()
)
svcGrpMemberRxBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMemberRxBytesRate.setStatus("current")
_SvcGrpMemberTxBytesRate_Type = OctetString
_SvcGrpMemberTxBytesRate_Object = MibTableColumn
svcGrpMemberTxBytesRate = _SvcGrpMemberTxBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 27),
    _SvcGrpMemberTxBytesRate_Type()
)
svcGrpMemberTxBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMemberTxBytesRate.setStatus("current")
_SvcGrpMemberSynfloodRate_Type = OctetString
_SvcGrpMemberSynfloodRate_Object = MibTableColumn
svcGrpMemberSynfloodRate = _SvcGrpMemberSynfloodRate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 28),
    _SvcGrpMemberSynfloodRate_Type()
)
svcGrpMemberSynfloodRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMemberSynfloodRate.setStatus("current")
_SvcGrpMemberTicksSinceLastStateChange_Type = TimeTicks
_SvcGrpMemberTicksSinceLastStateChange_Object = MibTableColumn
svcGrpMemberTicksSinceLastStateChange = _SvcGrpMemberTicksSinceLastStateChange_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 31),
    _SvcGrpMemberTicksSinceLastStateChange_Type()
)
svcGrpMemberTicksSinceLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMemberTicksSinceLastStateChange.setStatus("current")
_SvcGrpMemberGroupFullName_Type = OctetString
_SvcGrpMemberGroupFullName_Object = MibTableColumn
svcGrpMemberGroupFullName = _SvcGrpMemberGroupFullName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 32),
    _SvcGrpMemberGroupFullName_Type()
)
svcGrpMemberGroupFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMemberGroupFullName.setStatus("current")
_SvcGrpMemberFullName_Type = OctetString
_SvcGrpMemberFullName_Object = MibTableColumn
svcGrpMemberFullName = _SvcGrpMemberFullName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 33),
    _SvcGrpMemberFullName_Type()
)
svcGrpMemberFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMemberFullName.setStatus("current")
_SvcGrpMemberPrimaryInetAddressType_Type = InetAddressType
_SvcGrpMemberPrimaryInetAddressType_Object = MibTableColumn
svcGrpMemberPrimaryInetAddressType = _SvcGrpMemberPrimaryInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 34),
    _SvcGrpMemberPrimaryInetAddressType_Type()
)
svcGrpMemberPrimaryInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMemberPrimaryInetAddressType.setStatus("current")
_SvcGrpMemberPrimaryInetAddress_Type = InetAddress
_SvcGrpMemberPrimaryInetAddress_Object = MibTableColumn
svcGrpMemberPrimaryInetAddress = _SvcGrpMemberPrimaryInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 7, 1, 35),
    _SvcGrpMemberPrimaryInetAddress_Type()
)
svcGrpMemberPrimaryInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcGrpMemberPrimaryInetAddress.setStatus("current")
_ServiceDospolicyTable_Object = MibTable
serviceDospolicyTable = _ServiceDospolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 8)
)
if mibBuilder.loadTexts:
    serviceDospolicyTable.setStatus("current")
_ServiceDospolicyEntry_Object = MibTableRow
serviceDospolicyEntry = _ServiceDospolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 8, 1)
)
serviceDospolicyEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "svcServiceName"),
    (0, "NS-ROOT-MIB", "dosPolicyName"),
)
if mibBuilder.loadTexts:
    serviceDospolicyEntry.setStatus("current")
_SvcdospolicydosTotJSSent_Type = Counter64
_SvcdospolicydosTotJSSent_Object = MibTableColumn
svcdospolicydosTotJSSent = _SvcdospolicydosTotJSSent_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 8, 1, 1),
    _SvcdospolicydosTotJSSent_Type()
)
svcdospolicydosTotJSSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcdospolicydosTotJSSent.setStatus("current")
_SvcdospolicydosTotJSBytesSent_Type = Counter64
_SvcdospolicydosTotJSBytesSent_Object = MibTableColumn
svcdospolicydosTotJSBytesSent = _SvcdospolicydosTotJSBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 8, 1, 2),
    _SvcdospolicydosTotJSBytesSent_Type()
)
svcdospolicydosTotJSBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcdospolicydosTotJSBytesSent.setStatus("current")
_SvcdospolicydosTotJSRefused_Type = Counter64
_SvcdospolicydosTotJSRefused_Object = MibTableColumn
svcdospolicydosTotJSRefused = _SvcdospolicydosTotJSRefused_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 8, 1, 3),
    _SvcdospolicydosTotJSRefused_Type()
)
svcdospolicydosTotJSRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcdospolicydosTotJSRefused.setStatus("current")
_SvcdospolicydosTotNonGetPostRequests_Type = Counter64
_SvcdospolicydosTotNonGetPostRequests_Object = MibTableColumn
svcdospolicydosTotNonGetPostRequests = _SvcdospolicydosTotNonGetPostRequests_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 8, 1, 4),
    _SvcdospolicydosTotNonGetPostRequests_Type()
)
svcdospolicydosTotNonGetPostRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcdospolicydosTotNonGetPostRequests.setStatus("current")
_SvcdospolicydosPhysicalServiceIP_Type = IpAddress
_SvcdospolicydosPhysicalServiceIP_Object = MibTableColumn
svcdospolicydosPhysicalServiceIP = _SvcdospolicydosPhysicalServiceIP_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 8, 1, 5),
    _SvcdospolicydosPhysicalServiceIP_Type()
)
svcdospolicydosPhysicalServiceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcdospolicydosPhysicalServiceIP.setStatus("current")
_SvcdospolicydosPhysicalServicePort_Type = Integer32
_SvcdospolicydosPhysicalServicePort_Object = MibTableColumn
svcdospolicydosPhysicalServicePort = _SvcdospolicydosPhysicalServicePort_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 8, 1, 6),
    _SvcdospolicydosPhysicalServicePort_Type()
)
svcdospolicydosPhysicalServicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcdospolicydosPhysicalServicePort.setStatus("current")
_SvcdospolicydosCurrentQueueSize_Type = Gauge32
_SvcdospolicydosCurrentQueueSize_Object = MibTableColumn
svcdospolicydosCurrentQueueSize = _SvcdospolicydosCurrentQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 8, 1, 7),
    _SvcdospolicydosCurrentQueueSize_Type()
)
svcdospolicydosCurrentQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcdospolicydosCurrentQueueSize.setStatus("current")
_SvcdospolicydosCurrentJSRate_Type = Gauge32
_SvcdospolicydosCurrentJSRate_Object = MibTableColumn
svcdospolicydosCurrentJSRate = _SvcdospolicydosCurrentJSRate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 8, 1, 8),
    _SvcdospolicydosCurrentJSRate_Type()
)
svcdospolicydosCurrentJSRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcdospolicydosCurrentJSRate.setStatus("current")
_SvcdospolicydosTotValidClients_Type = Counter64
_SvcdospolicydosTotValidClients_Object = MibTableColumn
svcdospolicydosTotValidClients = _SvcdospolicydosTotValidClients_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 8, 1, 9),
    _SvcdospolicydosTotValidClients_Type()
)
svcdospolicydosTotValidClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcdospolicydosTotValidClients.setStatus("current")
_SvcdospolicydosCurServerRespRate_Type = Gauge32
_SvcdospolicydosCurServerRespRate_Object = MibTableColumn
svcdospolicydosCurServerRespRate = _SvcdospolicydosCurServerRespRate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 8, 1, 10),
    _SvcdospolicydosCurServerRespRate_Type()
)
svcdospolicydosCurServerRespRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcdospolicydosCurServerRespRate.setStatus("current")
_MonitorMemberTable_Object = MibTable
monitorMemberTable = _MonitorMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 9)
)
if mibBuilder.loadTexts:
    monitorMemberTable.setStatus("current")
_MonitorMemberEntry_Object = MibTableRow
monitorMemberEntry = _MonitorMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 9, 1)
)
monitorMemberEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "monitorName"),
)
if mibBuilder.loadTexts:
    monitorMemberEntry.setStatus("current")
_MonitorName_Type = OctetString
_MonitorName_Object = MibTableColumn
monitorName = _MonitorName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 9, 1, 1),
    _MonitorName_Type()
)
monitorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorName.setStatus("current")
_ResponseTimeoutThreshold_Type = Integer32
_ResponseTimeoutThreshold_Object = MibTableColumn
responseTimeoutThreshold = _ResponseTimeoutThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 9, 1, 2),
    _ResponseTimeoutThreshold_Type()
)
responseTimeoutThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    responseTimeoutThreshold.setStatus("current")
_MonitorType_Type = MonitorType
_MonitorType_Object = MibTableColumn
monitorType = _MonitorType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 9, 1, 3),
    _MonitorType_Type()
)
monitorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorType.setStatus("current")
_MonitorInterval_Type = Integer32
_MonitorInterval_Object = MibTableColumn
monitorInterval = _MonitorInterval_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 9, 1, 4),
    _MonitorInterval_Type()
)
monitorInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorInterval.setStatus("current")
_MonitorResponseTimeout_Type = Integer32
_MonitorResponseTimeout_Object = MibTableColumn
monitorResponseTimeout = _MonitorResponseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 9, 1, 5),
    _MonitorResponseTimeout_Type()
)
monitorResponseTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorResponseTimeout.setStatus("current")
_MonitorDowntime_Type = Integer32
_MonitorDowntime_Object = MibTableColumn
monitorDowntime = _MonitorDowntime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 9, 1, 6),
    _MonitorDowntime_Type()
)
monitorDowntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorDowntime.setStatus("current")
_MonitorRetrys_Type = Integer32
_MonitorRetrys_Object = MibTableColumn
monitorRetrys = _MonitorRetrys_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 9, 1, 7),
    _MonitorRetrys_Type()
)
monitorRetrys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorRetrys.setStatus("current")
_DestinationIP_Type = IpAddress
_DestinationIP_Object = MibTableColumn
destinationIP = _DestinationIP_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 9, 1, 8),
    _DestinationIP_Type()
)
destinationIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destinationIP.setStatus("current")
_DestinationPort_Type = Integer32
_DestinationPort_Object = MibTableColumn
destinationPort = _DestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 9, 1, 9),
    _DestinationPort_Type()
)
destinationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destinationPort.setStatus("current")
_DrtmDeviation_Type = Integer32
_DrtmDeviation_Object = MibTableColumn
drtmDeviation = _DrtmDeviation_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 9, 1, 10),
    _DrtmDeviation_Type()
)
drtmDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drtmDeviation.setStatus("current")
_DrtmActiveMonitors_Type = Integer32
_DrtmActiveMonitors_Object = MibTableColumn
drtmActiveMonitors = _DrtmActiveMonitors_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 9, 1, 11),
    _DrtmActiveMonitors_Type()
)
drtmActiveMonitors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drtmActiveMonitors.setStatus("current")
_DrtmCumResponseTimeout_Type = Gauge32
_DrtmCumResponseTimeout_Object = MibTableColumn
drtmCumResponseTimeout = _DrtmCumResponseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 9, 1, 12),
    _DrtmCumResponseTimeout_Type()
)
drtmCumResponseTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drtmCumResponseTimeout.setStatus("current")
_AlarmProbeFailedRetries_Type = Integer32
_AlarmProbeFailedRetries_Object = MibTableColumn
alarmProbeFailedRetries = _AlarmProbeFailedRetries_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 9, 1, 13),
    _AlarmProbeFailedRetries_Type()
)
alarmProbeFailedRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmProbeFailedRetries.setStatus("current")
_DestinationInetAddressType_Type = InetAddressType
_DestinationInetAddressType_Object = MibTableColumn
destinationInetAddressType = _DestinationInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 9, 1, 14),
    _DestinationInetAddressType_Type()
)
destinationInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destinationInetAddressType.setStatus("current")
_DestinationInetAddress_Type = InetAddress
_DestinationInetAddress_Object = MibTableColumn
destinationInetAddress = _DestinationInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 9, 1, 15),
    _DestinationInetAddress_Type()
)
destinationInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destinationInetAddress.setStatus("current")
_MonServiceMemberTable_Object = MibTable
monServiceMemberTable = _MonServiceMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 10)
)
if mibBuilder.loadTexts:
    monServiceMemberTable.setStatus("current")
_MonServiceMemberEntry_Object = MibTableRow
monServiceMemberEntry = _MonServiceMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 10, 1)
)
monServiceMemberEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "monServiceName"),
    (0, "NS-ROOT-MIB", "monitorName"),
)
if mibBuilder.loadTexts:
    monServiceMemberEntry.setStatus("current")
_MonServiceName_Type = OctetString
_MonServiceName_Object = MibTableColumn
monServiceName = _MonServiceName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 10, 1, 1),
    _MonServiceName_Type()
)
monServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monServiceName.setStatus("current")
_MonitorRTO_Type = Gauge32
_MonitorRTO_Object = MibTableColumn
monitorRTO = _MonitorRTO_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 10, 1, 2),
    _MonitorRTO_Type()
)
monitorRTO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorRTO.setStatus("current")
_MonitorState_Type = MonitorState
_MonitorState_Object = MibTableColumn
monitorState = _MonitorState_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 10, 1, 3),
    _MonitorState_Type()
)
monitorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorState.setStatus("current")
_DrtmRTO_Type = Gauge32
_DrtmRTO_Object = MibTableColumn
drtmRTO = _DrtmRTO_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 10, 1, 4),
    _DrtmRTO_Type()
)
drtmRTO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drtmRTO.setStatus("current")
_DrtmLearningProbes_Type = Gauge32
_DrtmLearningProbes_Object = MibTableColumn
drtmLearningProbes = _DrtmLearningProbes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 10, 1, 5),
    _DrtmLearningProbes_Type()
)
drtmLearningProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drtmLearningProbes.setStatus("current")
_MonitorCurFailedCount_Type = Gauge32
_MonitorCurFailedCount_Object = MibTableColumn
monitorCurFailedCount = _MonitorCurFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 10, 1, 6),
    _MonitorCurFailedCount_Type()
)
monitorCurFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorCurFailedCount.setStatus("current")
_MonitorWeight_Type = Integer32
_MonitorWeight_Object = MibTableColumn
monitorWeight = _MonitorWeight_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 10, 1, 7),
    _MonitorWeight_Type()
)
monitorWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorWeight.setStatus("current")
_AlarmMonrespto_Type = Gauge32
_AlarmMonrespto_Object = MibTableColumn
alarmMonrespto = _AlarmMonrespto_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 10, 1, 8),
    _AlarmMonrespto_Type()
)
alarmMonrespto.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmMonrespto.setStatus("current")
_MonitorProbes_Type = Counter32
_MonitorProbes_Object = MibTableColumn
monitorProbes = _MonitorProbes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 10, 1, 9),
    _MonitorProbes_Type()
)
monitorProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorProbes.setStatus("current")
_MonitorFailed_Type = Counter32
_MonitorFailed_Object = MibTableColumn
monitorFailed = _MonitorFailed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 10, 1, 10),
    _MonitorFailed_Type()
)
monitorFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorFailed.setStatus("current")
_MonitorMaxClient_Type = Counter32
_MonitorMaxClient_Object = MibTableColumn
monitorMaxClient = _MonitorMaxClient_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 10, 1, 11),
    _MonitorMaxClient_Type()
)
monitorMaxClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorMaxClient.setStatus("current")
_MonitorFailedCon_Type = Counter32
_MonitorFailedCon_Object = MibTableColumn
monitorFailedCon = _MonitorFailedCon_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 10, 1, 12),
    _MonitorFailedCon_Type()
)
monitorFailedCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorFailedCon.setStatus("current")
_MonitorFailedCode_Type = Counter32
_MonitorFailedCode_Object = MibTableColumn
monitorFailedCode = _MonitorFailedCode_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 10, 1, 13),
    _MonitorFailedCode_Type()
)
monitorFailedCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorFailedCode.setStatus("current")
_MonitorFailedStr_Type = Counter32
_MonitorFailedStr_Object = MibTableColumn
monitorFailedStr = _MonitorFailedStr_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 10, 1, 14),
    _MonitorFailedStr_Type()
)
monitorFailedStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorFailedStr.setStatus("current")
_MonitorFailedTimeout_Type = Counter32
_MonitorFailedTimeout_Object = MibTableColumn
monitorFailedTimeout = _MonitorFailedTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 10, 1, 15),
    _MonitorFailedTimeout_Type()
)
monitorFailedTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorFailedTimeout.setStatus("current")
_MonitorFailedSend_Type = Counter32
_MonitorFailedSend_Object = MibTableColumn
monitorFailedSend = _MonitorFailedSend_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 10, 1, 16),
    _MonitorFailedSend_Type()
)
monitorFailedSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorFailedSend.setStatus("current")
_MonitorFailedFTP_Type = Counter32
_MonitorFailedFTP_Object = MibTableColumn
monitorFailedFTP = _MonitorFailedFTP_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 10, 1, 17),
    _MonitorFailedFTP_Type()
)
monitorFailedFTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorFailedFTP.setStatus("current")
_MonitorFailedPort_Type = Counter32
_MonitorFailedPort_Object = MibTableColumn
monitorFailedPort = _MonitorFailedPort_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 10, 1, 18),
    _MonitorFailedPort_Type()
)
monitorFailedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorFailedPort.setStatus("current")
_MonitorFailedResponse_Type = Counter32
_MonitorFailedResponse_Object = MibTableColumn
monitorFailedResponse = _MonitorFailedResponse_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 10, 1, 19),
    _MonitorFailedResponse_Type()
)
monitorFailedResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorFailedResponse.setStatus("current")
_MonitorFailedId_Type = Counter32
_MonitorFailedId_Object = MibTableColumn
monitorFailedId = _MonitorFailedId_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 10, 1, 20),
    _MonitorFailedId_Type()
)
monitorFailedId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorFailedId.setStatus("current")
_MonitorProbesNoChange_Type = Counter32
_MonitorProbesNoChange_Object = MibTableColumn
monitorProbesNoChange = _MonitorProbesNoChange_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 10, 1, 21),
    _MonitorProbesNoChange_Type()
)
monitorProbesNoChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorProbesNoChange.setStatus("current")
_MonitorResponseTimeoutThreshExceed_Type = Counter32
_MonitorResponseTimeoutThreshExceed_Object = MibTableColumn
monitorResponseTimeoutThreshExceed = _MonitorResponseTimeoutThreshExceed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 10, 1, 22),
    _MonitorResponseTimeoutThreshExceed_Type()
)
monitorResponseTimeoutThreshExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorResponseTimeoutThreshExceed.setStatus("current")
_ServiceGroupTable_Object = MibTable
serviceGroupTable = _ServiceGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 11)
)
if mibBuilder.loadTexts:
    serviceGroupTable.setStatus("current")
_ServiceGroupEntry_Object = MibTableRow
serviceGroupEntry = _ServiceGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 11, 1)
)
serviceGroupEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "svcgrpSvcGroupName"),
)
if mibBuilder.loadTexts:
    serviceGroupEntry.setStatus("current")
_SvcgrpSvcGroupName_Type = OctetString
_SvcgrpSvcGroupName_Object = MibTableColumn
svcgrpSvcGroupName = _SvcgrpSvcGroupName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 11, 1, 1),
    _SvcgrpSvcGroupName_Type()
)
svcgrpSvcGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcgrpSvcGroupName.setStatus("current")
_SvcgrpSvcGroupType_Type = EntityProtocolType
_SvcgrpSvcGroupType_Object = MibTableColumn
svcgrpSvcGroupType = _SvcgrpSvcGroupType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 11, 1, 2),
    _SvcgrpSvcGroupType_Type()
)
svcgrpSvcGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcgrpSvcGroupType.setStatus("current")
_SvcgrpSvcGroupState_Type = ServiceGroupState
_SvcgrpSvcGroupState_Object = MibTableColumn
svcgrpSvcGroupState = _SvcgrpSvcGroupState_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 11, 1, 3),
    _SvcgrpSvcGroupState_Type()
)
svcgrpSvcGroupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcgrpSvcGroupState.setStatus("current")
_SvcgrpSvcGroupFullName_Type = OctetString
_SvcgrpSvcGroupFullName_Object = MibTableColumn
svcgrpSvcGroupFullName = _SvcgrpSvcGroupFullName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 2, 11, 1, 4),
    _SvcgrpSvcGroupFullName_Type()
)
svcgrpSvcGroupFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcgrpSvcGroupFullName.setStatus("current")
_NsVserverGroup_ObjectIdentity = ObjectIdentity
nsVserverGroup = _NsVserverGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3)
)
_VserverTable_Object = MibTable
vserverTable = _VserverTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    vserverTable.setStatus("current")
_VserverEntry_Object = MibTableRow
vserverEntry = _VserverEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1)
)
vserverEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "vsvrName"),
)
if mibBuilder.loadTexts:
    vserverEntry.setStatus("current")
_VsvrName_Type = OctetString
_VsvrName_Object = MibTableColumn
vsvrName = _VsvrName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 1),
    _VsvrName_Type()
)
vsvrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrName.setStatus("current")
_VsvrIpAddress_Type = IpAddress
_VsvrIpAddress_Object = MibTableColumn
vsvrIpAddress = _VsvrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 2),
    _VsvrIpAddress_Type()
)
vsvrIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrIpAddress.setStatus("current")
_VsvrPort_Type = Integer32
_VsvrPort_Object = MibTableColumn
vsvrPort = _VsvrPort_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 3),
    _VsvrPort_Type()
)
vsvrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrPort.setStatus("current")
_VsvrType_Type = EntityProtocolType
_VsvrType_Object = MibTableColumn
vsvrType = _VsvrType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 4),
    _VsvrType_Type()
)
vsvrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrType.setStatus("current")
_VsvrState_Type = EntityState
_VsvrState_Object = MibTableColumn
vsvrState = _VsvrState_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 5),
    _VsvrState_Type()
)
vsvrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrState.setStatus("current")
_VsvrMaxReqPerConn_Type = Counter32
_VsvrMaxReqPerConn_Object = MibTableColumn
vsvrMaxReqPerConn = _VsvrMaxReqPerConn_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 6),
    _VsvrMaxReqPerConn_Type()
)
vsvrMaxReqPerConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrMaxReqPerConn.setStatus("obsolete")
_VsvrCurClntConnections_Type = Gauge32
_VsvrCurClntConnections_Object = MibTableColumn
vsvrCurClntConnections = _VsvrCurClntConnections_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 7),
    _VsvrCurClntConnections_Type()
)
vsvrCurClntConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrCurClntConnections.setStatus("current")
_VsvrCurSrvrConnections_Type = Gauge32
_VsvrCurSrvrConnections_Object = MibTableColumn
vsvrCurSrvrConnections = _VsvrCurSrvrConnections_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 8),
    _VsvrCurSrvrConnections_Type()
)
vsvrCurSrvrConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrCurSrvrConnections.setStatus("current")
_VsvrAvgTransactionTime_Type = TimeTicks
_VsvrAvgTransactionTime_Object = MibTableColumn
vsvrAvgTransactionTime = _VsvrAvgTransactionTime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 9),
    _VsvrAvgTransactionTime_Type()
)
vsvrAvgTransactionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrAvgTransactionTime.setStatus("obsolete")
_VsvrSurgeCount_Type = Counter32
_VsvrSurgeCount_Object = MibTableColumn
vsvrSurgeCount = _VsvrSurgeCount_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 10),
    _VsvrSurgeCount_Type()
)
vsvrSurgeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrSurgeCount.setStatus("current")
_VsvrTotalRequestsLow_Type = Counter32
_VsvrTotalRequestsLow_Object = MibTableColumn
vsvrTotalRequestsLow = _VsvrTotalRequestsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 11),
    _VsvrTotalRequestsLow_Type()
)
vsvrTotalRequestsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrTotalRequestsLow.setStatus("obsolete")
_VsvrTotalRequestsHigh_Type = Counter32
_VsvrTotalRequestsHigh_Object = MibTableColumn
vsvrTotalRequestsHigh = _VsvrTotalRequestsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 12),
    _VsvrTotalRequestsHigh_Type()
)
vsvrTotalRequestsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrTotalRequestsHigh.setStatus("obsolete")
_VsvrTotalRequestBytesLow_Type = Counter32
_VsvrTotalRequestBytesLow_Object = MibTableColumn
vsvrTotalRequestBytesLow = _VsvrTotalRequestBytesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 13),
    _VsvrTotalRequestBytesLow_Type()
)
vsvrTotalRequestBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrTotalRequestBytesLow.setStatus("obsolete")
_VsvrTotalRequestBytesHigh_Type = Counter32
_VsvrTotalRequestBytesHigh_Object = MibTableColumn
vsvrTotalRequestBytesHigh = _VsvrTotalRequestBytesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 14),
    _VsvrTotalRequestBytesHigh_Type()
)
vsvrTotalRequestBytesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrTotalRequestBytesHigh.setStatus("obsolete")
_VsvrTotalResponsesLow_Type = Counter32
_VsvrTotalResponsesLow_Object = MibTableColumn
vsvrTotalResponsesLow = _VsvrTotalResponsesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 15),
    _VsvrTotalResponsesLow_Type()
)
vsvrTotalResponsesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrTotalResponsesLow.setStatus("obsolete")
_VsvrTotalResponsesHigh_Type = Counter32
_VsvrTotalResponsesHigh_Object = MibTableColumn
vsvrTotalResponsesHigh = _VsvrTotalResponsesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 16),
    _VsvrTotalResponsesHigh_Type()
)
vsvrTotalResponsesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrTotalResponsesHigh.setStatus("obsolete")
_VsvrTotalResponseBytesLow_Type = Counter32
_VsvrTotalResponseBytesLow_Object = MibTableColumn
vsvrTotalResponseBytesLow = _VsvrTotalResponseBytesLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 17),
    _VsvrTotalResponseBytesLow_Type()
)
vsvrTotalResponseBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrTotalResponseBytesLow.setStatus("obsolete")
_VsvrTotalResponseBytesHigh_Type = Counter32
_VsvrTotalResponseBytesHigh_Object = MibTableColumn
vsvrTotalResponseBytesHigh = _VsvrTotalResponseBytesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 18),
    _VsvrTotalResponseBytesHigh_Type()
)
vsvrTotalResponseBytesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrTotalResponseBytesHigh.setStatus("obsolete")
_VsvrTotalPktsRecvdLow_Type = Counter32
_VsvrTotalPktsRecvdLow_Object = MibTableColumn
vsvrTotalPktsRecvdLow = _VsvrTotalPktsRecvdLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 19),
    _VsvrTotalPktsRecvdLow_Type()
)
vsvrTotalPktsRecvdLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrTotalPktsRecvdLow.setStatus("obsolete")
_VsvrTotalPktsRecvdHigh_Type = Counter32
_VsvrTotalPktsRecvdHigh_Object = MibTableColumn
vsvrTotalPktsRecvdHigh = _VsvrTotalPktsRecvdHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 20),
    _VsvrTotalPktsRecvdHigh_Type()
)
vsvrTotalPktsRecvdHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrTotalPktsRecvdHigh.setStatus("obsolete")
_VsvrTotalPktsSentLow_Type = Counter32
_VsvrTotalPktsSentLow_Object = MibTableColumn
vsvrTotalPktsSentLow = _VsvrTotalPktsSentLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 21),
    _VsvrTotalPktsSentLow_Type()
)
vsvrTotalPktsSentLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrTotalPktsSentLow.setStatus("obsolete")
_VsvrTotalPktsSentHigh_Type = Counter32
_VsvrTotalPktsSentHigh_Object = MibTableColumn
vsvrTotalPktsSentHigh = _VsvrTotalPktsSentHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 22),
    _VsvrTotalPktsSentHigh_Type()
)
vsvrTotalPktsSentHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrTotalPktsSentHigh.setStatus("obsolete")
_VsvrTotalSynsRecvdLow_Type = Counter32
_VsvrTotalSynsRecvdLow_Object = MibTableColumn
vsvrTotalSynsRecvdLow = _VsvrTotalSynsRecvdLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 23),
    _VsvrTotalSynsRecvdLow_Type()
)
vsvrTotalSynsRecvdLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrTotalSynsRecvdLow.setStatus("obsolete")
_VsvrTotalSynsRecvdHigh_Type = Counter32
_VsvrTotalSynsRecvdHigh_Object = MibTableColumn
vsvrTotalSynsRecvdHigh = _VsvrTotalSynsRecvdHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 24),
    _VsvrTotalSynsRecvdHigh_Type()
)
vsvrTotalSynsRecvdHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrTotalSynsRecvdHigh.setStatus("obsolete")
_VsvrTotalRequests_Type = Counter64
_VsvrTotalRequests_Object = MibTableColumn
vsvrTotalRequests = _VsvrTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 30),
    _VsvrTotalRequests_Type()
)
vsvrTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrTotalRequests.setStatus("current")
_VsvrTotalRequestBytes_Type = Counter64
_VsvrTotalRequestBytes_Object = MibTableColumn
vsvrTotalRequestBytes = _VsvrTotalRequestBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 31),
    _VsvrTotalRequestBytes_Type()
)
vsvrTotalRequestBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrTotalRequestBytes.setStatus("current")
_VsvrTotalResponses_Type = Counter64
_VsvrTotalResponses_Object = MibTableColumn
vsvrTotalResponses = _VsvrTotalResponses_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 32),
    _VsvrTotalResponses_Type()
)
vsvrTotalResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrTotalResponses.setStatus("current")
_VsvrTotalResponseBytes_Type = Counter64
_VsvrTotalResponseBytes_Object = MibTableColumn
vsvrTotalResponseBytes = _VsvrTotalResponseBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 33),
    _VsvrTotalResponseBytes_Type()
)
vsvrTotalResponseBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrTotalResponseBytes.setStatus("current")
_VsvrTotalPktsRecvd_Type = Counter64
_VsvrTotalPktsRecvd_Object = MibTableColumn
vsvrTotalPktsRecvd = _VsvrTotalPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 34),
    _VsvrTotalPktsRecvd_Type()
)
vsvrTotalPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrTotalPktsRecvd.setStatus("current")
_VsvrTotalPktsSent_Type = Counter64
_VsvrTotalPktsSent_Object = MibTableColumn
vsvrTotalPktsSent = _VsvrTotalPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 35),
    _VsvrTotalPktsSent_Type()
)
vsvrTotalPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrTotalPktsSent.setStatus("current")
_VsvrTotalSynsRecvd_Type = Counter64
_VsvrTotalSynsRecvd_Object = MibTableColumn
vsvrTotalSynsRecvd = _VsvrTotalSynsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 36),
    _VsvrTotalSynsRecvd_Type()
)
vsvrTotalSynsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrTotalSynsRecvd.setStatus("current")
_VsvrCurServicesDown_Type = Gauge32
_VsvrCurServicesDown_Object = MibTableColumn
vsvrCurServicesDown = _VsvrCurServicesDown_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 37),
    _VsvrCurServicesDown_Type()
)
vsvrCurServicesDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrCurServicesDown.setStatus("current")
_VsvrCurServicesUnKnown_Type = Gauge32
_VsvrCurServicesUnKnown_Object = MibTableColumn
vsvrCurServicesUnKnown = _VsvrCurServicesUnKnown_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 38),
    _VsvrCurServicesUnKnown_Type()
)
vsvrCurServicesUnKnown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrCurServicesUnKnown.setStatus("current")
_VsvrCurServicesOutOfSvc_Type = Gauge32
_VsvrCurServicesOutOfSvc_Object = MibTableColumn
vsvrCurServicesOutOfSvc = _VsvrCurServicesOutOfSvc_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 39),
    _VsvrCurServicesOutOfSvc_Type()
)
vsvrCurServicesOutOfSvc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrCurServicesOutOfSvc.setStatus("current")
_VsvrCurServicesTransToOutOfSvc_Type = Gauge32
_VsvrCurServicesTransToOutOfSvc_Object = MibTableColumn
vsvrCurServicesTransToOutOfSvc = _VsvrCurServicesTransToOutOfSvc_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 40),
    _VsvrCurServicesTransToOutOfSvc_Type()
)
vsvrCurServicesTransToOutOfSvc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrCurServicesTransToOutOfSvc.setStatus("current")
_VsvrCurServicesUp_Type = Gauge32
_VsvrCurServicesUp_Object = MibTableColumn
vsvrCurServicesUp = _VsvrCurServicesUp_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 41),
    _VsvrCurServicesUp_Type()
)
vsvrCurServicesUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrCurServicesUp.setStatus("current")
_VsvrTotMiss_Type = Counter64
_VsvrTotMiss_Object = MibTableColumn
vsvrTotMiss = _VsvrTotMiss_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 42),
    _VsvrTotMiss_Type()
)
vsvrTotMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrTotMiss.setStatus("current")
_VsvrRequestRate_Type = OctetString
_VsvrRequestRate_Object = MibTableColumn
vsvrRequestRate = _VsvrRequestRate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 43),
    _VsvrRequestRate_Type()
)
vsvrRequestRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrRequestRate.setStatus("current")
_VsvrRxBytesRate_Type = OctetString
_VsvrRxBytesRate_Object = MibTableColumn
vsvrRxBytesRate = _VsvrRxBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 44),
    _VsvrRxBytesRate_Type()
)
vsvrRxBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrRxBytesRate.setStatus("current")
_VsvrTxBytesRate_Type = OctetString
_VsvrTxBytesRate_Object = MibTableColumn
vsvrTxBytesRate = _VsvrTxBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 45),
    _VsvrTxBytesRate_Type()
)
vsvrTxBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrTxBytesRate.setStatus("current")
_VsvrSynfloodRate_Type = OctetString
_VsvrSynfloodRate_Object = MibTableColumn
vsvrSynfloodRate = _VsvrSynfloodRate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 46),
    _VsvrSynfloodRate_Type()
)
vsvrSynfloodRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrSynfloodRate.setStatus("current")
_VsvrIp6Address_Type = Ipv6Address
_VsvrIp6Address_Object = MibTableColumn
vsvrIp6Address = _VsvrIp6Address_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 47),
    _VsvrIp6Address_Type()
)
vsvrIp6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrIp6Address.setStatus("current")
_VsvrTotHits_Type = Counter64
_VsvrTotHits_Object = MibTableColumn
vsvrTotHits = _VsvrTotHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 48),
    _VsvrTotHits_Type()
)
vsvrTotHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrTotHits.setStatus("current")
_VsvrTotSpillOvers_Type = Counter32
_VsvrTotSpillOvers_Object = MibTableColumn
vsvrTotSpillOvers = _VsvrTotSpillOvers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 54),
    _VsvrTotSpillOvers_Type()
)
vsvrTotSpillOvers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrTotSpillOvers.setStatus("current")
_VsvrTotalClients_Type = Counter64
_VsvrTotalClients_Object = MibTableColumn
vsvrTotalClients = _VsvrTotalClients_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 56),
    _VsvrTotalClients_Type()
)
vsvrTotalClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrTotalClients.setStatus("current")
_VsvrClientConnOpenRate_Type = OctetString
_VsvrClientConnOpenRate_Object = MibTableColumn
vsvrClientConnOpenRate = _VsvrClientConnOpenRate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 58),
    _VsvrClientConnOpenRate_Type()
)
vsvrClientConnOpenRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrClientConnOpenRate.setStatus("current")
_VsvrFullName_Type = OctetString
_VsvrFullName_Object = MibTableColumn
vsvrFullName = _VsvrFullName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 59),
    _VsvrFullName_Type()
)
vsvrFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrFullName.setStatus("current")
_VsvrCurSslVpnUsers_Type = Gauge32
_VsvrCurSslVpnUsers_Object = MibTableColumn
vsvrCurSslVpnUsers = _VsvrCurSslVpnUsers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 60),
    _VsvrCurSslVpnUsers_Type()
)
vsvrCurSslVpnUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrCurSslVpnUsers.setStatus("current")
_VsvrTotalServicesBound_Type = Gauge32
_VsvrTotalServicesBound_Object = MibTableColumn
vsvrTotalServicesBound = _VsvrTotalServicesBound_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 61),
    _VsvrTotalServicesBound_Type()
)
vsvrTotalServicesBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrTotalServicesBound.setStatus("current")
_VsvrHealth_Type = Integer32
_VsvrHealth_Object = MibTableColumn
vsvrHealth = _VsvrHealth_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 62),
    _VsvrHealth_Type()
)
vsvrHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrHealth.setStatus("current")
_VsvrTicksSinceLastStateChange_Type = TimeTicks
_VsvrTicksSinceLastStateChange_Object = MibTableColumn
vsvrTicksSinceLastStateChange = _VsvrTicksSinceLastStateChange_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 63),
    _VsvrTicksSinceLastStateChange_Type()
)
vsvrTicksSinceLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrTicksSinceLastStateChange.setStatus("current")
_VsvrEntityType_Type = VServerType
_VsvrEntityType_Object = MibTableColumn
vsvrEntityType = _VsvrEntityType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 64),
    _VsvrEntityType_Type()
)
vsvrEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrEntityType.setStatus("current")
_VsvrTotalServers_Type = Counter64
_VsvrTotalServers_Object = MibTableColumn
vsvrTotalServers = _VsvrTotalServers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 65),
    _VsvrTotalServers_Type()
)
vsvrTotalServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrTotalServers.setStatus("current")
_VsvrActiveActiveState_Type = ActiveActiveState
_VsvrActiveActiveState_Object = MibTableColumn
vsvrActiveActiveState = _VsvrActiveActiveState_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 1, 1, 66),
    _VsvrActiveActiveState_Type()
)
vsvrActiveActiveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrActiveActiveState.setStatus("current")
_VserverServiceTable_Object = MibTable
vserverServiceTable = _VserverServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 2)
)
if mibBuilder.loadTexts:
    vserverServiceTable.setStatus("current")
_VserverServiceEntry_Object = MibTableRow
vserverServiceEntry = _VserverServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 2, 1)
)
vserverServiceEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "vsvrName"),
    (0, "NS-ROOT-MIB", "vsvrServiceName"),
)
if mibBuilder.loadTexts:
    vserverServiceEntry.setStatus("current")
_ServiceHitsLow_Type = Counter32
_ServiceHitsLow_Object = MibTableColumn
serviceHitsLow = _ServiceHitsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 2, 1, 1),
    _ServiceHitsLow_Type()
)
serviceHitsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceHitsLow.setStatus("obsolete")
_ServiceHitsHigh_Type = Counter32
_ServiceHitsHigh_Object = MibTableColumn
serviceHitsHigh = _ServiceHitsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 2, 1, 2),
    _ServiceHitsHigh_Type()
)
serviceHitsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceHitsHigh.setStatus("obsolete")
_ServicePersistentHitsLow_Type = Counter32
_ServicePersistentHitsLow_Object = MibTableColumn
servicePersistentHitsLow = _ServicePersistentHitsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 2, 1, 3),
    _ServicePersistentHitsLow_Type()
)
servicePersistentHitsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servicePersistentHitsLow.setStatus("obsolete")
_ServicePersistentHitsHigh_Type = Counter32
_ServicePersistentHitsHigh_Object = MibTableColumn
servicePersistentHitsHigh = _ServicePersistentHitsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 2, 1, 4),
    _ServicePersistentHitsHigh_Type()
)
servicePersistentHitsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servicePersistentHitsHigh.setStatus("obsolete")
_VsvrServiceHits_Type = Counter64
_VsvrServiceHits_Object = MibTableColumn
vsvrServiceHits = _VsvrServiceHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 2, 1, 5),
    _VsvrServiceHits_Type()
)
vsvrServiceHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrServiceHits.setStatus("current")
_ServicePersistentHits_Type = Counter64
_ServicePersistentHits_Object = MibTableColumn
servicePersistentHits = _ServicePersistentHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 2, 1, 6),
    _ServicePersistentHits_Type()
)
servicePersistentHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servicePersistentHits.setStatus("current")
_ServiceWeight_Type = Integer32
_ServiceWeight_Object = MibTableColumn
serviceWeight = _ServiceWeight_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 2, 1, 7),
    _ServiceWeight_Type()
)
serviceWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serviceWeight.setStatus("current")
_VsvrServiceName_Type = OctetString
_VsvrServiceName_Object = MibTableColumn
vsvrServiceName = _VsvrServiceName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 2, 1, 8),
    _VsvrServiceName_Type()
)
vsvrServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrServiceName.setStatus("current")
_VsvrServiceFullName_Type = OctetString
_VsvrServiceFullName_Object = MibTableColumn
vsvrServiceFullName = _VsvrServiceFullName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 2, 1, 9),
    _VsvrServiceFullName_Type()
)
vsvrServiceFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrServiceFullName.setStatus("current")
_VserverFullName_Type = OctetString
_VserverFullName_Object = MibTableColumn
vserverFullName = _VserverFullName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 2, 1, 10),
    _VserverFullName_Type()
)
vserverFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vserverFullName.setStatus("current")
_VsvrServiceEntityType_Type = SvcEntityType
_VsvrServiceEntityType_Object = MibTableColumn
vsvrServiceEntityType = _VsvrServiceEntityType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 2, 1, 11),
    _VsvrServiceEntityType_Type()
)
vsvrServiceEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrServiceEntityType.setStatus("current")
_VserverCspolicyTable_Object = MibTable
vserverCspolicyTable = _VserverCspolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 3)
)
if mibBuilder.loadTexts:
    vserverCspolicyTable.setStatus("current")
_VserverCspolicyEntry_Object = MibTableRow
vserverCspolicyEntry = _VserverCspolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 3, 1)
)
vserverCspolicyEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "vsvrName"),
    (0, "NS-ROOT-MIB", "cspolicyName"),
)
if mibBuilder.loadTexts:
    vserverCspolicyEntry.setStatus("current")
_CspolicyName_Type = OctetString
_CspolicyName_Object = MibTableColumn
cspolicyName = _CspolicyName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 3, 1, 1),
    _CspolicyName_Type()
)
cspolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspolicyName.setStatus("current")
_CspolicyDestVserverName_Type = OctetString
_CspolicyDestVserverName_Object = MibTableColumn
cspolicyDestVserverName = _CspolicyDestVserverName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 3, 1, 2),
    _CspolicyDestVserverName_Type()
)
cspolicyDestVserverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspolicyDestVserverName.setStatus("current")
_CspolicyHitsLow_Type = Counter32
_CspolicyHitsLow_Object = MibTableColumn
cspolicyHitsLow = _CspolicyHitsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 3, 1, 3),
    _CspolicyHitsLow_Type()
)
cspolicyHitsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspolicyHitsLow.setStatus("obsolete")
_CspolicyHitsHigh_Type = Counter32
_CspolicyHitsHigh_Object = MibTableColumn
cspolicyHitsHigh = _CspolicyHitsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 3, 1, 4),
    _CspolicyHitsHigh_Type()
)
cspolicyHitsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspolicyHitsHigh.setStatus("obsolete")
_CspolicyHits_Type = Counter64
_CspolicyHits_Object = MibTableColumn
cspolicyHits = _CspolicyHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 3, 1, 5),
    _CspolicyHits_Type()
)
cspolicyHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspolicyHits.setStatus("current")
_CsIndexVserverFullName_Type = OctetString
_CsIndexVserverFullName_Object = MibTableColumn
csIndexVserverFullName = _CsIndexVserverFullName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 3, 1, 6),
    _CsIndexVserverFullName_Type()
)
csIndexVserverFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csIndexVserverFullName.setStatus("current")
_VserverCrpolicyTable_Object = MibTable
vserverCrpolicyTable = _VserverCrpolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 4)
)
if mibBuilder.loadTexts:
    vserverCrpolicyTable.setStatus("current")
_VserverCrpolicyEntry_Object = MibTableRow
vserverCrpolicyEntry = _VserverCrpolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 4, 1)
)
vserverCrpolicyEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "vsvrName"),
    (0, "NS-ROOT-MIB", "crpolicyName"),
)
if mibBuilder.loadTexts:
    vserverCrpolicyEntry.setStatus("current")
_CrpolicyName_Type = OctetString
_CrpolicyName_Object = MibTableColumn
crpolicyName = _CrpolicyName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 4, 1, 1),
    _CrpolicyName_Type()
)
crpolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crpolicyName.setStatus("current")
_CrpolicyHitsLow_Type = Counter32
_CrpolicyHitsLow_Object = MibTableColumn
crpolicyHitsLow = _CrpolicyHitsLow_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 4, 1, 2),
    _CrpolicyHitsLow_Type()
)
crpolicyHitsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crpolicyHitsLow.setStatus("obsolete")
_CrpolicyHitsHigh_Type = Counter32
_CrpolicyHitsHigh_Object = MibTableColumn
crpolicyHitsHigh = _CrpolicyHitsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 4, 1, 3),
    _CrpolicyHitsHigh_Type()
)
crpolicyHitsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crpolicyHitsHigh.setStatus("obsolete")
_CrpolicyHits_Type = Counter64
_CrpolicyHits_Object = MibTableColumn
crpolicyHits = _CrpolicyHits_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 4, 1, 4),
    _CrpolicyHits_Type()
)
crpolicyHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crpolicyHits.setStatus("current")
_CrIndexVserverFullName_Type = OctetString
_CrIndexVserverFullName_Object = MibTableColumn
crIndexVserverFullName = _CrIndexVserverFullName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 4, 1, 5),
    _CrIndexVserverFullName_Type()
)
crIndexVserverFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crIndexVserverFullName.setStatus("current")
_VserverGlobalStatsGroup_ObjectIdentity = ObjectIdentity
vserverGlobalStatsGroup = _VserverGlobalStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 5)
)
_CurConfigVservers_Type = Gauge32
_CurConfigVservers_Object = MibScalar
curConfigVservers = _CurConfigVservers_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 5, 1),
    _CurConfigVservers_Type()
)
curConfigVservers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curConfigVservers.setStatus("current")
_VsvrBindCount_Type = Integer32
_VsvrBindCount_Object = MibScalar
vsvrBindCount = _VsvrBindCount_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 5, 2),
    _VsvrBindCount_Type()
)
vsvrBindCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrBindCount.setStatus("current")
_VsvrSvcGrpBindCount_Type = Integer32
_VsvrSvcGrpBindCount_Object = MibScalar
vsvrSvcGrpBindCount = _VsvrSvcGrpBindCount_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 5, 3),
    _VsvrSvcGrpBindCount_Type()
)
vsvrSvcGrpBindCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrSvcGrpBindCount.setStatus("current")
_LbvserverTable_Object = MibTable
lbvserverTable = _LbvserverTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 6)
)
if mibBuilder.loadTexts:
    lbvserverTable.setStatus("current")
_LbvserverEntry_Object = MibTableRow
lbvserverEntry = _LbvserverEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 6, 1)
)
lbvserverEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "vsvrName"),
)
if mibBuilder.loadTexts:
    lbvserverEntry.setStatus("current")
_LbvsvrLBMethod_Type = LbPolicy
_LbvsvrLBMethod_Object = MibTableColumn
lbvsvrLBMethod = _LbvsvrLBMethod_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 6, 1, 1),
    _LbvsvrLBMethod_Type()
)
lbvsvrLBMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbvsvrLBMethod.setStatus("current")
_LbvsvrPersistanceType_Type = PersistanceType
_LbvsvrPersistanceType_Object = MibTableColumn
lbvsvrPersistanceType = _LbvsvrPersistanceType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 6, 1, 2),
    _LbvsvrPersistanceType_Type()
)
lbvsvrPersistanceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbvsvrPersistanceType.setStatus("current")
_LbvsvrPersistenceTimeOut_Type = Integer32
_LbvsvrPersistenceTimeOut_Object = MibTableColumn
lbvsvrPersistenceTimeOut = _LbvsvrPersistenceTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 6, 1, 3),
    _LbvsvrPersistenceTimeOut_Type()
)
lbvsvrPersistenceTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbvsvrPersistenceTimeOut.setStatus("current")
_LbvsvrActiveConn_Type = Gauge32
_LbvsvrActiveConn_Object = MibTableColumn
lbvsvrActiveConn = _LbvsvrActiveConn_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 6, 1, 4),
    _LbvsvrActiveConn_Type()
)
lbvsvrActiveConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbvsvrActiveConn.setStatus("current")
_LbvsvrAvgSvrTTFB_Type = Gauge32
_LbvsvrAvgSvrTTFB_Object = MibTableColumn
lbvsvrAvgSvrTTFB = _LbvsvrAvgSvrTTFB_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 6, 1, 5),
    _LbvsvrAvgSvrTTFB_Type()
)
lbvsvrAvgSvrTTFB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbvsvrAvgSvrTTFB.setStatus("current")
_VserverPqpolicyTable_Object = MibTable
vserverPqpolicyTable = _VserverPqpolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 7)
)
if mibBuilder.loadTexts:
    vserverPqpolicyTable.setStatus("current")
_VserverPqpolicyEntry_Object = MibTableRow
vserverPqpolicyEntry = _VserverPqpolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 7, 1)
)
vserverPqpolicyEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "vsvrName"),
    (0, "NS-ROOT-MIB", "pqName"),
)
if mibBuilder.loadTexts:
    vserverPqpolicyEntry.setStatus("current")
_PqpolicyTotClientTransactionTime_Type = Counter64
_PqpolicyTotClientTransactionTime_Object = MibTableColumn
pqpolicyTotClientTransactionTime = _PqpolicyTotClientTransactionTime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 7, 1, 1),
    _PqpolicyTotClientTransactionTime_Type()
)
pqpolicyTotClientTransactionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqpolicyTotClientTransactionTime.setStatus("obsolete")
_PqpolicyTotClientTransactions_Type = Counter64
_PqpolicyTotClientTransactions_Object = MibTableColumn
pqpolicyTotClientTransactions = _PqpolicyTotClientTransactions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 7, 1, 2),
    _PqpolicyTotClientTransactions_Type()
)
pqpolicyTotClientTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqpolicyTotClientTransactions.setStatus("obsolete")
_PqpolicyDropped_Type = Counter64
_PqpolicyDropped_Object = MibTableColumn
pqpolicyDropped = _PqpolicyDropped_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 7, 1, 3),
    _PqpolicyDropped_Type()
)
pqpolicyDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqpolicyDropped.setStatus("obsolete")
_PqpolicyQdepth_Type = Counter32
_PqpolicyQdepth_Object = MibTableColumn
pqpolicyQdepth = _PqpolicyQdepth_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 7, 1, 4),
    _PqpolicyQdepth_Type()
)
pqpolicyQdepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqpolicyQdepth.setStatus("obsolete")
_PqpolicytotClientTransactionTime_Type = Counter64
_PqpolicytotClientTransactionTime_Object = MibTableColumn
pqpolicytotClientTransactionTime = _PqpolicytotClientTransactionTime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 7, 1, 5),
    _PqpolicytotClientTransactionTime_Type()
)
pqpolicytotClientTransactionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqpolicytotClientTransactionTime.setStatus("current")
_PqpolicytotClientTransactions_Type = Counter64
_PqpolicytotClientTransactions_Object = MibTableColumn
pqpolicytotClientTransactions = _PqpolicytotClientTransactions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 7, 1, 6),
    _PqpolicytotClientTransactions_Type()
)
pqpolicytotClientTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqpolicytotClientTransactions.setStatus("current")
_PqpolicypqDropped_Type = Counter64
_PqpolicypqDropped_Object = MibTableColumn
pqpolicypqDropped = _PqpolicypqDropped_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 7, 1, 7),
    _PqpolicypqDropped_Type()
)
pqpolicypqDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqpolicypqDropped.setStatus("current")
_PqpolicypqQdepth_Type = Gauge32
_PqpolicypqQdepth_Object = MibTableColumn
pqpolicypqQdepth = _PqpolicypqQdepth_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 7, 1, 8),
    _PqpolicypqQdepth_Type()
)
pqpolicypqQdepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqpolicypqQdepth.setStatus("current")
_PqpolicypqAvgClientTransactionTime_Type = Gauge32
_PqpolicypqAvgClientTransactionTime_Object = MibTableColumn
pqpolicypqAvgClientTransactionTime = _PqpolicypqAvgClientTransactionTime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 7, 1, 9),
    _PqpolicypqAvgClientTransactionTime_Type()
)
pqpolicypqAvgClientTransactionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqpolicypqAvgClientTransactionTime.setStatus("current")
_PqpolicypqVserverIP_Type = IpAddress
_PqpolicypqVserverIP_Object = MibTableColumn
pqpolicypqVserverIP = _PqpolicypqVserverIP_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 7, 1, 10),
    _PqpolicypqVserverIP_Type()
)
pqpolicypqVserverIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqpolicypqVserverIP.setStatus("current")
_PqpolicypqVserverPort_Type = Integer32
_PqpolicypqVserverPort_Object = MibTableColumn
pqpolicypqVserverPort = _PqpolicypqVserverPort_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 7, 1, 11),
    _PqpolicypqVserverPort_Type()
)
pqpolicypqVserverPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqpolicypqVserverPort.setStatus("current")
_PqpolicypqCurrentClientConnections_Type = Gauge32
_PqpolicypqCurrentClientConnections_Object = MibTableColumn
pqpolicypqCurrentClientConnections = _PqpolicypqCurrentClientConnections_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 7, 1, 12),
    _PqpolicypqCurrentClientConnections_Type()
)
pqpolicypqCurrentClientConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqpolicypqCurrentClientConnections.setStatus("current")
_PqpolicypqTotQueueDepth_Type = Counter64
_PqpolicypqTotQueueDepth_Object = MibTableColumn
pqpolicypqTotQueueDepth = _PqpolicypqTotQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 7, 1, 13),
    _PqpolicypqTotQueueDepth_Type()
)
pqpolicypqTotQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqpolicypqTotQueueDepth.setStatus("current")
_PqpolicypqTotClientConnections_Type = Counter64
_PqpolicypqTotClientConnections_Object = MibTableColumn
pqpolicypqTotClientConnections = _PqpolicypqTotClientConnections_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 7, 1, 14),
    _PqpolicypqTotClientConnections_Type()
)
pqpolicypqTotClientConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqpolicypqTotClientConnections.setStatus("current")
_PqpolicypqTotQueueWaitTime_Type = Counter64
_PqpolicypqTotQueueWaitTime_Object = MibTableColumn
pqpolicypqTotQueueWaitTime = _PqpolicypqTotQueueWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 7, 1, 15),
    _PqpolicypqTotQueueWaitTime_Type()
)
pqpolicypqTotQueueWaitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqpolicypqTotQueueWaitTime.setStatus("current")
_PqpolicypqTotAvgQueueDepth_Type = Gauge32
_PqpolicypqTotAvgQueueDepth_Object = MibTableColumn
pqpolicypqTotAvgQueueDepth = _PqpolicypqTotAvgQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 7, 1, 16),
    _PqpolicypqTotAvgQueueDepth_Type()
)
pqpolicypqTotAvgQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqpolicypqTotAvgQueueDepth.setStatus("current")
_PqpolicypqTotAvgQueueWaitTime_Type = Gauge32
_PqpolicypqTotAvgQueueWaitTime_Object = MibTableColumn
pqpolicypqTotAvgQueueWaitTime = _PqpolicypqTotAvgQueueWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 7, 1, 17),
    _PqpolicypqTotAvgQueueWaitTime_Type()
)
pqpolicypqTotAvgQueueWaitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqpolicypqTotAvgQueueWaitTime.setStatus("current")
_PqpolicytotClientTransactionTimems_Type = Counter64
_PqpolicytotClientTransactionTimems_Object = MibTableColumn
pqpolicytotClientTransactionTimems = _PqpolicytotClientTransactionTimems_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 7, 1, 18),
    _PqpolicytotClientTransactionTimems_Type()
)
pqpolicytotClientTransactionTimems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqpolicytotClientTransactionTimems.setStatus("current")
_PqpolicypqAvgClientTransactionTimems_Type = Gauge32
_PqpolicypqAvgClientTransactionTimems_Object = MibTableColumn
pqpolicypqAvgClientTransactionTimems = _PqpolicypqAvgClientTransactionTimems_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 7, 1, 19),
    _PqpolicypqAvgClientTransactionTimems_Type()
)
pqpolicypqAvgClientTransactionTimems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqpolicypqAvgClientTransactionTimems.setStatus("current")
_VserverScpolicyTable_Object = MibTable
vserverScpolicyTable = _VserverScpolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8)
)
if mibBuilder.loadTexts:
    vserverScpolicyTable.setStatus("current")
_VserverScpolicyEntry_Object = MibTableRow
vserverScpolicyEntry = _VserverScpolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1)
)
vserverScpolicyEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "svcServiceName"),
    (0, "NS-ROOT-MIB", "scPolicyName"),
)
if mibBuilder.loadTexts:
    vserverScpolicyEntry.setStatus("current")
_VsvrscpolicyPrimaryIPAddress_Type = IpAddress
_VsvrscpolicyPrimaryIPAddress_Object = MibTableColumn
vsvrscpolicyPrimaryIPAddress = _VsvrscpolicyPrimaryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1, 1),
    _VsvrscpolicyPrimaryIPAddress_Type()
)
vsvrscpolicyPrimaryIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrscpolicyPrimaryIPAddress.setStatus("current")
_VsvrscpolicyPrimaryPort_Type = Integer32
_VsvrscpolicyPrimaryPort_Object = MibTableColumn
vsvrscpolicyPrimaryPort = _VsvrscpolicyPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1, 2),
    _VsvrscpolicyPrimaryPort_Type()
)
vsvrscpolicyPrimaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrscpolicyPrimaryPort.setStatus("current")
_VsvrscpolicyDesIpAddress_Type = IpAddress
_VsvrscpolicyDesIpAddress_Object = MibTableColumn
vsvrscpolicyDesIpAddress = _VsvrscpolicyDesIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1, 3),
    _VsvrscpolicyDesIpAddress_Type()
)
vsvrscpolicyDesIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrscpolicyDesIpAddress.setStatus("obsolete")
_VsvrscpolicyDestPort_Type = Integer32
_VsvrscpolicyDestPort_Object = MibTableColumn
vsvrscpolicyDestPort = _VsvrscpolicyDestPort_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1, 4),
    _VsvrscpolicyDestPort_Type()
)
vsvrscpolicyDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrscpolicyDestPort.setStatus("obsolete")
_VsvrscpolicyAvgServerTransactionTime_Type = Gauge32
_VsvrscpolicyAvgServerTransactionTime_Object = MibTableColumn
vsvrscpolicyAvgServerTransactionTime = _VsvrscpolicyAvgServerTransactionTime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1, 5),
    _VsvrscpolicyAvgServerTransactionTime_Type()
)
vsvrscpolicyAvgServerTransactionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrscpolicyAvgServerTransactionTime.setStatus("obsolete")
_VsvrscpolicyTotClientTransaction_Type = Counter64
_VsvrscpolicyTotClientTransaction_Object = MibTableColumn
vsvrscpolicyTotClientTransaction = _VsvrscpolicyTotClientTransaction_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1, 6),
    _VsvrscpolicyTotClientTransaction_Type()
)
vsvrscpolicyTotClientTransaction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrscpolicyTotClientTransaction.setStatus("obsolete")
_VsvrscpolicyTotOpenConn_Type = Counter32
_VsvrscpolicyTotOpenConn_Object = MibTableColumn
vsvrscpolicyTotOpenConn = _VsvrscpolicyTotOpenConn_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1, 7),
    _VsvrscpolicyTotOpenConn_Type()
)
vsvrscpolicyTotOpenConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrscpolicyTotOpenConn.setStatus("obsolete")
_VsvrscpolicydesIpAddress_Type = IpAddress
_VsvrscpolicydesIpAddress_Object = MibTableColumn
vsvrscpolicydesIpAddress = _VsvrscpolicydesIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1, 8),
    _VsvrscpolicydesIpAddress_Type()
)
vsvrscpolicydesIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrscpolicydesIpAddress.setStatus("current")
_VsvrscpolicydestPort_Type = Integer32
_VsvrscpolicydestPort_Object = MibTableColumn
vsvrscpolicydestPort = _VsvrscpolicydestPort_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1, 9),
    _VsvrscpolicydestPort_Type()
)
vsvrscpolicydestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrscpolicydestPort.setStatus("current")
_VsvrscpolicyavgServerTransactionTime_Type = Gauge32
_VsvrscpolicyavgServerTransactionTime_Object = MibTableColumn
vsvrscpolicyavgServerTransactionTime = _VsvrscpolicyavgServerTransactionTime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1, 10),
    _VsvrscpolicyavgServerTransactionTime_Type()
)
vsvrscpolicyavgServerTransactionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrscpolicyavgServerTransactionTime.setStatus("current")
_VsvrscpolicytotClientTransaction_Type = Counter64
_VsvrscpolicytotClientTransaction_Object = MibTableColumn
vsvrscpolicytotClientTransaction = _VsvrscpolicytotClientTransaction_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1, 11),
    _VsvrscpolicytotClientTransaction_Type()
)
vsvrscpolicytotClientTransaction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrscpolicytotClientTransaction.setStatus("current")
_VsvrscpolicytotOpenConn_Type = Gauge32
_VsvrscpolicytotOpenConn_Object = MibTableColumn
vsvrscpolicytotOpenConn = _VsvrscpolicytotOpenConn_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1, 12),
    _VsvrscpolicytotOpenConn_Type()
)
vsvrscpolicytotOpenConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrscpolicytotOpenConn.setStatus("current")
_VsvrscpolicyscPhysicalServiceIP_Type = IpAddress
_VsvrscpolicyscPhysicalServiceIP_Object = MibTableColumn
vsvrscpolicyscPhysicalServiceIP = _VsvrscpolicyscPhysicalServiceIP_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1, 13),
    _VsvrscpolicyscPhysicalServiceIP_Type()
)
vsvrscpolicyscPhysicalServiceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrscpolicyscPhysicalServiceIP.setStatus("current")
_VsvrscpolicyscPhysicalServicePort_Type = Integer32
_VsvrscpolicyscPhysicalServicePort_Object = MibTableColumn
vsvrscpolicyscPhysicalServicePort = _VsvrscpolicyscPhysicalServicePort_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1, 14),
    _VsvrscpolicyscPhysicalServicePort_Type()
)
vsvrscpolicyscPhysicalServicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrscpolicyscPhysicalServicePort.setStatus("current")
_VsvrscpolicyscCurrentWaitingTime_Type = Gauge32
_VsvrscpolicyscCurrentWaitingTime_Object = MibTableColumn
vsvrscpolicyscCurrentWaitingTime = _VsvrscpolicyscCurrentWaitingTime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1, 15),
    _VsvrscpolicyscCurrentWaitingTime_Type()
)
vsvrscpolicyscCurrentWaitingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrscpolicyscCurrentWaitingTime.setStatus("current")
_VsvrscpolicyscCurrentClientConnections_Type = Gauge32
_VsvrscpolicyscCurrentClientConnections_Object = MibTableColumn
vsvrscpolicyscCurrentClientConnections = _VsvrscpolicyscCurrentClientConnections_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1, 16),
    _VsvrscpolicyscCurrentClientConnections_Type()
)
vsvrscpolicyscCurrentClientConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrscpolicyscCurrentClientConnections.setStatus("current")
_VsvrscpolicyscTotalClientConnections_Type = Counter64
_VsvrscpolicyscTotalClientConnections_Object = MibTableColumn
vsvrscpolicyscTotalClientConnections = _VsvrscpolicyscTotalClientConnections_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1, 17),
    _VsvrscpolicyscTotalClientConnections_Type()
)
vsvrscpolicyscTotalClientConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrscpolicyscTotalClientConnections.setStatus("current")
_VsvrscpolicyscTotalServerConnections_Type = Counter64
_VsvrscpolicyscTotalServerConnections_Object = MibTableColumn
vsvrscpolicyscTotalServerConnections = _VsvrscpolicyscTotalServerConnections_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1, 18),
    _VsvrscpolicyscTotalServerConnections_Type()
)
vsvrscpolicyscTotalServerConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrscpolicyscTotalServerConnections.setStatus("current")
_VsvrscpolicyscTotalRequestsReceived_Type = Counter64
_VsvrscpolicyscTotalRequestsReceived_Object = MibTableColumn
vsvrscpolicyscTotalRequestsReceived = _VsvrscpolicyscTotalRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1, 19),
    _VsvrscpolicyscTotalRequestsReceived_Type()
)
vsvrscpolicyscTotalRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrscpolicyscTotalRequestsReceived.setStatus("current")
_VsvrscpolicyscTotalRequestBytes_Type = Counter64
_VsvrscpolicyscTotalRequestBytes_Object = MibTableColumn
vsvrscpolicyscTotalRequestBytes = _VsvrscpolicyscTotalRequestBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1, 20),
    _VsvrscpolicyscTotalRequestBytes_Type()
)
vsvrscpolicyscTotalRequestBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrscpolicyscTotalRequestBytes.setStatus("current")
_VsvrscpolicyscTotalResponsesReceived_Type = Counter64
_VsvrscpolicyscTotalResponsesReceived_Object = MibTableColumn
vsvrscpolicyscTotalResponsesReceived = _VsvrscpolicyscTotalResponsesReceived_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1, 21),
    _VsvrscpolicyscTotalResponsesReceived_Type()
)
vsvrscpolicyscTotalResponsesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrscpolicyscTotalResponsesReceived.setStatus("current")
_VsvrscpolicyscTotalResponseBytes_Type = Counter64
_VsvrscpolicyscTotalResponseBytes_Object = MibTableColumn
vsvrscpolicyscTotalResponseBytes = _VsvrscpolicyscTotalResponseBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1, 22),
    _VsvrscpolicyscTotalResponseBytes_Type()
)
vsvrscpolicyscTotalResponseBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrscpolicyscTotalResponseBytes.setStatus("current")
_VsvrscpolicyscCurrentSurgeQClients_Type = Gauge32
_VsvrscpolicyscCurrentSurgeQClients_Object = MibTableColumn
vsvrscpolicyscCurrentSurgeQClients = _VsvrscpolicyscCurrentSurgeQClients_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1, 23),
    _VsvrscpolicyscCurrentSurgeQClients_Type()
)
vsvrscpolicyscCurrentSurgeQClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrscpolicyscCurrentSurgeQClients.setStatus("current")
_VsvrscpolicyscCurrentWaitingClients_Type = Gauge32
_VsvrscpolicyscCurrentWaitingClients_Object = MibTableColumn
vsvrscpolicyscCurrentWaitingClients = _VsvrscpolicyscCurrentWaitingClients_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1, 24),
    _VsvrscpolicyscCurrentWaitingClients_Type()
)
vsvrscpolicyscCurrentWaitingClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrscpolicyscCurrentWaitingClients.setStatus("current")
_VsvrscpolicyscTotalServerTransactions_Type = Counter64
_VsvrscpolicyscTotalServerTransactions_Object = MibTableColumn
vsvrscpolicyscTotalServerTransactions = _VsvrscpolicyscTotalServerTransactions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1, 25),
    _VsvrscpolicyscTotalServerTransactions_Type()
)
vsvrscpolicyscTotalServerTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrscpolicyscTotalServerTransactions.setStatus("current")
_VsvrscpolicyscTotalServerTTFBTransactions_Type = Counter64
_VsvrscpolicyscTotalServerTTFBTransactions_Object = MibTableColumn
vsvrscpolicyscTotalServerTTFBTransactions = _VsvrscpolicyscTotalServerTTFBTransactions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1, 26),
    _VsvrscpolicyscTotalServerTTFBTransactions_Type()
)
vsvrscpolicyscTotalServerTTFBTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrscpolicyscTotalServerTTFBTransactions.setStatus("current")
_VsvrscpolicyscTotalServerTTLB_Type = Counter64
_VsvrscpolicyscTotalServerTTLB_Object = MibTableColumn
vsvrscpolicyscTotalServerTTLB = _VsvrscpolicyscTotalServerTTLB_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1, 27),
    _VsvrscpolicyscTotalServerTTLB_Type()
)
vsvrscpolicyscTotalServerTTLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrscpolicyscTotalServerTTLB.setStatus("current")
_VsvrscpolicyscTotalClientTTLB_Type = Counter64
_VsvrscpolicyscTotalClientTTLB_Object = MibTableColumn
vsvrscpolicyscTotalClientTTLB = _VsvrscpolicyscTotalClientTTLB_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1, 28),
    _VsvrscpolicyscTotalClientTTLB_Type()
)
vsvrscpolicyscTotalClientTTLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrscpolicyscTotalClientTTLB.setStatus("current")
_VsvrscpolicyscTotalServerTTFB_Type = Counter64
_VsvrscpolicyscTotalServerTTFB_Object = MibTableColumn
vsvrscpolicyscTotalServerTTFB = _VsvrscpolicyscTotalServerTTFB_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1, 29),
    _VsvrscpolicyscTotalServerTTFB_Type()
)
vsvrscpolicyscTotalServerTTFB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrscpolicyscTotalServerTTFB.setStatus("current")
_VsvrscpolicyscAverageClientTTLB_Type = Gauge32
_VsvrscpolicyscAverageClientTTLB_Object = MibTableColumn
vsvrscpolicyscAverageClientTTLB = _VsvrscpolicyscAverageClientTTLB_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1, 30),
    _VsvrscpolicyscAverageClientTTLB_Type()
)
vsvrscpolicyscAverageClientTTLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrscpolicyscAverageClientTTLB.setStatus("current")
_VsvrscpolicyscAverageServerTTFB_Type = Gauge32
_VsvrscpolicyscAverageServerTTFB_Object = MibTableColumn
vsvrscpolicyscAverageServerTTFB = _VsvrscpolicyscAverageServerTTFB_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 8, 1, 31),
    _VsvrscpolicyscAverageServerTTFB_Type()
)
vsvrscpolicyscAverageServerTTFB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrscpolicyscAverageServerTTFB.setStatus("current")
_VserverAdvanceSslConfigTable_Object = MibTable
vserverAdvanceSslConfigTable = _VserverAdvanceSslConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 9)
)
if mibBuilder.loadTexts:
    vserverAdvanceSslConfigTable.setStatus("current")
_VserverAdvanceSslConfigEntry_Object = MibTableRow
vserverAdvanceSslConfigEntry = _VserverAdvanceSslConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 9, 1)
)
vserverAdvanceSslConfigEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "vsvrName"),
)
if mibBuilder.loadTexts:
    vserverAdvanceSslConfigEntry.setStatus("current")
_VsvrSslDH_Type = AdminStatus
_VsvrSslDH_Object = MibTableColumn
vsvrSslDH = _VsvrSslDH_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 9, 1, 1),
    _VsvrSslDH_Type()
)
vsvrSslDH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrSslDH.setStatus("current")
_VsvrSslDHCount_Type = Integer32
_VsvrSslDHCount_Object = MibTableColumn
vsvrSslDHCount = _VsvrSslDHCount_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 9, 1, 2),
    _VsvrSslDHCount_Type()
)
vsvrSslDHCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrSslDHCount.setStatus("current")
_VsvrSslDHFilePath_Type = OctetString
_VsvrSslDHFilePath_Object = MibTableColumn
vsvrSslDHFilePath = _VsvrSslDHFilePath_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 9, 1, 3),
    _VsvrSslDHFilePath_Type()
)
vsvrSslDHFilePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrSslDHFilePath.setStatus("current")
_VsvrSsleRSA_Type = AdminStatus
_VsvrSsleRSA_Object = MibTableColumn
vsvrSsleRSA = _VsvrSsleRSA_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 9, 1, 4),
    _VsvrSsleRSA_Type()
)
vsvrSsleRSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrSsleRSA.setStatus("current")
_VsvrSsleRSACount_Type = Integer32
_VsvrSsleRSACount_Object = MibTableColumn
vsvrSsleRSACount = _VsvrSsleRSACount_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 9, 1, 5),
    _VsvrSsleRSACount_Type()
)
vsvrSsleRSACount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrSsleRSACount.setStatus("current")
_VsvrSslv2Protocol_Type = AdminStatus
_VsvrSslv2Protocol_Object = MibTableColumn
vsvrSslv2Protocol = _VsvrSslv2Protocol_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 9, 1, 6),
    _VsvrSslv2Protocol_Type()
)
vsvrSslv2Protocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrSslv2Protocol.setStatus("current")
_VsvrSslv3Protocol_Type = AdminStatus
_VsvrSslv3Protocol_Object = MibTableColumn
vsvrSslv3Protocol = _VsvrSslv3Protocol_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 9, 1, 7),
    _VsvrSslv3Protocol_Type()
)
vsvrSslv3Protocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrSslv3Protocol.setStatus("current")
_VsvrSslTLSv1Protocol_Type = AdminStatus
_VsvrSslTLSv1Protocol_Object = MibTableColumn
vsvrSslTLSv1Protocol = _VsvrSslTLSv1Protocol_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 9, 1, 8),
    _VsvrSslTLSv1Protocol_Type()
)
vsvrSslTLSv1Protocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrSslTLSv1Protocol.setStatus("current")
_VsvrSslRedirectSupport_Type = AdminStatus
_VsvrSslRedirectSupport_Object = MibTableColumn
vsvrSslRedirectSupport = _VsvrSslRedirectSupport_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 9, 1, 9),
    _VsvrSslRedirectSupport_Type()
)
vsvrSslRedirectSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrSslRedirectSupport.setStatus("current")
_VsvrSslClearTextPort_Type = Integer32
_VsvrSslClearTextPort_Object = MibTableColumn
vsvrSslClearTextPort = _VsvrSslClearTextPort_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 9, 1, 10),
    _VsvrSslClearTextPort_Type()
)
vsvrSslClearTextPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrSslClearTextPort.setStatus("current")
_VserverCipherBindingTable_Object = MibTable
vserverCipherBindingTable = _VserverCipherBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 10)
)
if mibBuilder.loadTexts:
    vserverCipherBindingTable.setStatus("current")
_VserverCipherBindingEntry_Object = MibTableRow
vserverCipherBindingEntry = _VserverCipherBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 10, 1)
)
vserverCipherBindingEntry.setIndexNames(
    (0, "NS-ROOT-MIB", "vsvrName"),
    (0, "NS-ROOT-MIB", "vsvrSslCipherBindName"),
)
if mibBuilder.loadTexts:
    vserverCipherBindingEntry.setStatus("current")
_VsvrSslCipherBindName_Type = OctetString
_VsvrSslCipherBindName_Object = MibTableColumn
vsvrSslCipherBindName = _VsvrSslCipherBindName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 10, 1, 1),
    _VsvrSslCipherBindName_Type()
)
vsvrSslCipherBindName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrSslCipherBindName.setStatus("current")
_VsvrSslCipherBindDesc_Type = OctetString
_VsvrSslCipherBindDesc_Object = MibTableColumn
vsvrSslCipherBindDesc = _VsvrSslCipherBindDesc_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 3, 10, 1, 2),
    _VsvrSslCipherBindDesc_Type()
)
vsvrSslCipherBindDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvrSslCipherBindDesc.setStatus("current")
_NsSnmpEventsGroup_ObjectIdentity = ObjectIdentity
nsSnmpEventsGroup = _NsSnmpEventsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 10)
)
_SnmpTrapVarBindOidsGroup_ObjectIdentity = ObjectIdentity
snmpTrapVarBindOidsGroup = _SnmpTrapVarBindOidsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 10, 2)
)
_AlarmHighThreshold_Type = Gauge32
_AlarmHighThreshold_Object = MibScalar
alarmHighThreshold = _AlarmHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 10, 2, 1),
    _AlarmHighThreshold_Type()
)
alarmHighThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmHighThreshold.setStatus("current")
_AlarmNormalThreshold_Type = Gauge32
_AlarmNormalThreshold_Object = MibScalar
alarmNormalThreshold = _AlarmNormalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 10, 2, 2),
    _AlarmNormalThreshold_Type()
)
alarmNormalThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmNormalThreshold.setStatus("current")
_EntityName_Type = OctetString
_EntityName_Object = MibScalar
entityName = _EntityName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 10, 2, 3),
    _EntityName_Type()
)
entityName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    entityName.setStatus("current")
_NsUserName_Type = OctetString
_NsUserName_Object = MibScalar
nsUserName = _NsUserName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 10, 2, 4),
    _NsUserName_Type()
)
nsUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsUserName.setStatus("current")
_ConfigurationCmd_Type = OctetString
_ConfigurationCmd_Object = MibScalar
configurationCmd = _ConfigurationCmd_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 10, 2, 5),
    _ConfigurationCmd_Type()
)
configurationCmd.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    configurationCmd.setStatus("current")
_AuthorizationStatus_Type = AuthorizationStatus
_AuthorizationStatus_Object = MibScalar
authorizationStatus = _AuthorizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 10, 2, 6),
    _AuthorizationStatus_Type()
)
authorizationStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    authorizationStatus.setStatus("current")
_CommandExecutionStatus_Type = CommandExecutionStatus
_CommandExecutionStatus_Object = MibScalar
commandExecutionStatus = _CommandExecutionStatus_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 10, 2, 7),
    _CommandExecutionStatus_Type()
)
commandExecutionStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    commandExecutionStatus.setStatus("current")
_UnackSynCount_Type = OctetString
_UnackSynCount_Object = MibScalar
unackSynCount = _UnackSynCount_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 10, 2, 8),
    _UnackSynCount_Type()
)
unackSynCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    unackSynCount.setStatus("current")
_AlarmLowThreshold_Type = Gauge32
_AlarmLowThreshold_Object = MibScalar
alarmLowThreshold = _AlarmLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 10, 2, 9),
    _AlarmLowThreshold_Type()
)
alarmLowThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmLowThreshold.setStatus("current")
_AlarmProbeFailedErrorString_Type = OctetString
_AlarmProbeFailedErrorString_Object = MibScalar
alarmProbeFailedErrorString = _AlarmProbeFailedErrorString_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 10, 2, 10),
    _AlarmProbeFailedErrorString_Type()
)
alarmProbeFailedErrorString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmProbeFailedErrorString.setStatus("current")
_AlarmVipRhiIpAddr_Type = IpAddress
_AlarmVipRhiIpAddr_Object = MibScalar
alarmVipRhiIpAddr = _AlarmVipRhiIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 10, 2, 11),
    _AlarmVipRhiIpAddr_Type()
)
alarmVipRhiIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmVipRhiIpAddr.setStatus("current")
_AlarmVipRhiState_Type = EntityState
_AlarmVipRhiState_Object = MibScalar
alarmVipRhiState = _AlarmVipRhiState_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 10, 2, 12),
    _AlarmVipRhiState_Type()
)
alarmVipRhiState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmVipRhiState.setStatus("current")
_AlarmRateLmtThresholdExceeded_Type = OctetString
_AlarmRateLmtThresholdExceeded_Object = MibScalar
alarmRateLmtThresholdExceeded = _AlarmRateLmtThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 10, 2, 13),
    _AlarmRateLmtThresholdExceeded_Type()
)
alarmRateLmtThresholdExceeded.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmRateLmtThresholdExceeded.setStatus("current")
_IpAddressGathered_Type = OctetString
_IpAddressGathered_Object = MibScalar
ipAddressGathered = _IpAddressGathered_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 10, 2, 14),
    _IpAddressGathered_Type()
)
ipAddressGathered.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipAddressGathered.setStatus("current")
_StringComputed_Type = OctetString
_StringComputed_Object = MibScalar
stringComputed = _StringComputed_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 10, 2, 15),
    _StringComputed_Type()
)
stringComputed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    stringComputed.setStatus("current")
_AlarmEntityCurState_Type = EntityState
_AlarmEntityCurState_Object = MibScalar
alarmEntityCurState = _AlarmEntityCurState_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 10, 2, 16),
    _AlarmEntityCurState_Type()
)
alarmEntityCurState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmEntityCurState.setStatus("current")
_SysHealthPowerSupplyStatus_Type = OctetString
_SysHealthPowerSupplyStatus_Object = MibScalar
sysHealthPowerSupplyStatus = _SysHealthPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 10, 2, 17),
    _SysHealthPowerSupplyStatus_Type()
)
sysHealthPowerSupplyStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sysHealthPowerSupplyStatus.setStatus("current")
_AlarmCurrentValue_Type = Gauge32
_AlarmCurrentValue_Object = MibScalar
alarmCurrentValue = _AlarmCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 10, 2, 18),
    _AlarmCurrentValue_Type()
)
alarmCurrentValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmCurrentValue.setStatus("current")
_AlarmVipRhiInetAddressType_Type = InetAddressType
_AlarmVipRhiInetAddressType_Object = MibScalar
alarmVipRhiInetAddressType = _AlarmVipRhiInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 10, 2, 19),
    _AlarmVipRhiInetAddressType_Type()
)
alarmVipRhiInetAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmVipRhiInetAddressType.setStatus("current")
_AlarmVipRhiInetAddress_Type = InetAddress
_AlarmVipRhiInetAddress_Object = MibScalar
alarmVipRhiInetAddress = _AlarmVipRhiInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 10, 2, 20),
    _AlarmVipRhiInetAddress_Type()
)
alarmVipRhiInetAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmVipRhiInetAddress.setStatus("current")
_AlarmVsvrOldName_Type = OctetString
_AlarmVsvrOldName_Object = MibScalar
alarmVsvrOldName = _AlarmVsvrOldName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 10, 2, 21),
    _AlarmVsvrOldName_Type()
)
alarmVsvrOldName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmVsvrOldName.setStatus("current")
_AlarmVsvrNewName_Type = OctetString
_AlarmVsvrNewName_Object = MibScalar
alarmVsvrNewName = _AlarmVsvrNewName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 10, 2, 22),
    _AlarmVsvrNewName_Type()
)
alarmVsvrNewName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmVsvrNewName.setStatus("current")
_NsClientIPAddr_Type = IpAddress
_NsClientIPAddr_Object = MibScalar
nsClientIPAddr = _NsClientIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 10, 2, 23),
    _NsClientIPAddr_Type()
)
nsClientIPAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsClientIPAddr.setStatus("current")
_IpConflictAddr_Type = IpAddress
_IpConflictAddr_Object = MibScalar
ipConflictAddr = _IpConflictAddr_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 10, 2, 24),
    _IpConflictAddr_Type()
)
ipConflictAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipConflictAddr.setStatus("current")
_AppfwLogMsg_Type = OctetString
_AppfwLogMsg_Object = MibScalar
appfwLogMsg = _AppfwLogMsg_Object(
    (1, 3, 6, 1, 4, 1, 5951, 4, 1, 10, 2, 25),
    _AppfwLogMsg_Type()
)
appfwLogMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    appfwLogMsg.setStatus("current")

# Managed Objects groups


# Notification objects

changeToPrimary = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 1)
)
changeToPrimary.setObjects(
    ("NS-ROOT-MIB", "sysIpAddress")
)
if mibBuilder.loadTexts:
    changeToPrimary.setStatus(
        "current"
    )

changeToSecondary = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 2)
)
changeToSecondary.setObjects(
    ("NS-ROOT-MIB", "sysIpAddress")
)
if mibBuilder.loadTexts:
    changeToSecondary.setStatus(
        "current"
    )

cpuUtilization = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 3)
)
cpuUtilization.setObjects(
      *(("NS-ROOT-MIB", "nsCPUusage"),
        ("NS-ROOT-MIB", "alarmHighThreshold"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    cpuUtilization.setStatus(
        "current"
    )

linkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 4)
)
if mibBuilder.loadTexts:
    linkUp.setStatus(
        "obsolete"
    )

linkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 5)
)
if mibBuilder.loadTexts:
    linkDown.setStatus(
        "obsolete"
    )

discoverFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 6)
)
if mibBuilder.loadTexts:
    discoverFailure.setStatus(
        "obsolete"
    )

memUtilization = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 7)
)
if mibBuilder.loadTexts:
    memUtilization.setStatus(
        "obsolete"
    )

entitydown = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 8)
)
entitydown.setObjects(
      *(("NS-ROOT-MIB", "entityName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    entitydown.setStatus(
        "current"
    )

entityup = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 9)
)
entityup.setObjects(
      *(("NS-ROOT-MIB", "entityName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    entityup.setStatus(
        "current"
    )

synflood = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 10)
)
synflood.setObjects(
      *(("NS-ROOT-MIB", "unackSynCount"),
        ("NS-ROOT-MIB", "alarmHighThreshold"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    synflood.setStatus(
        "current"
    )

cpuUtilizationNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 11)
)
cpuUtilizationNormal.setObjects(
      *(("NS-ROOT-MIB", "nsCPUusage"),
        ("NS-ROOT-MIB", "alarmNormalThreshold"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    cpuUtilizationNormal.setStatus(
        "current"
    )

synfloodNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 12)
)
synfloodNormal.setObjects(
      *(("NS-ROOT-MIB", "unackSynCount"),
        ("NS-ROOT-MIB", "alarmNormalThreshold"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    synfloodNormal.setStatus(
        "current"
    )

memoryUtilization = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 13)
)
memoryUtilization.setObjects(
      *(("NS-ROOT-MIB", "resMemUsage"),
        ("NS-ROOT-MIB", "alarmHighThreshold"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    memoryUtilization.setStatus(
        "current"
    )

memoryUtilizationNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 14)
)
memoryUtilizationNormal.setObjects(
      *(("NS-ROOT-MIB", "resMemUsage"),
        ("NS-ROOT-MIB", "alarmNormalThreshold"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    memoryUtilizationNormal.setStatus(
        "current"
    )

vServerRequestRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 15)
)
vServerRequestRate.setObjects(
      *(("NS-ROOT-MIB", "vsvrName"),
        ("NS-ROOT-MIB", "vsvrRequestRate"),
        ("NS-ROOT-MIB", "alarmHighThreshold"),
        ("NS-ROOT-MIB", "vsvrFullName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    vServerRequestRate.setStatus(
        "current"
    )

vServerRequestRateNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 16)
)
vServerRequestRateNormal.setObjects(
      *(("NS-ROOT-MIB", "vsvrName"),
        ("NS-ROOT-MIB", "vsvrRequestRate"),
        ("NS-ROOT-MIB", "alarmNormalThreshold"),
        ("NS-ROOT-MIB", "vsvrFullName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    vServerRequestRateNormal.setStatus(
        "current"
    )

serviceRequestRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 17)
)
serviceRequestRate.setObjects(
      *(("NS-ROOT-MIB", "svcServiceName"),
        ("NS-ROOT-MIB", "svcRequestRate"),
        ("NS-ROOT-MIB", "alarmHighThreshold"),
        ("NS-ROOT-MIB", "svcServiceFullName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    serviceRequestRate.setStatus(
        "current"
    )

serviceRequestRateNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 18)
)
serviceRequestRateNormal.setObjects(
      *(("NS-ROOT-MIB", "svcServiceName"),
        ("NS-ROOT-MIB", "svcRequestRate"),
        ("NS-ROOT-MIB", "alarmNormalThreshold"),
        ("NS-ROOT-MIB", "svcServiceFullName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    serviceRequestRateNormal.setStatus(
        "current"
    )

entityRxRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 19)
)
if mibBuilder.loadTexts:
    entityRxRate.setStatus(
        "obsolete"
    )

entityRxRateNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 20)
)
if mibBuilder.loadTexts:
    entityRxRateNormal.setStatus(
        "obsolete"
    )

entityTxRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 21)
)
if mibBuilder.loadTexts:
    entityTxRate.setStatus(
        "obsolete"
    )

entityTxRateNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 22)
)
if mibBuilder.loadTexts:
    entityTxRateNormal.setStatus(
        "obsolete"
    )

entitySynflood = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 23)
)
if mibBuilder.loadTexts:
    entitySynflood.setStatus(
        "obsolete"
    )

entitySynfloodNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 24)
)
if mibBuilder.loadTexts:
    entitySynfloodNormal.setStatus(
        "obsolete"
    )

netScalerConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 25)
)
netScalerConfigChange.setObjects(
      *(("NS-ROOT-MIB", "nsUserName"),
        ("NS-ROOT-MIB", "configurationCmd"),
        ("NS-ROOT-MIB", "authorizationStatus"),
        ("NS-ROOT-MIB", "commandExecutionStatus"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    netScalerConfigChange.setStatus(
        "current"
    )

maxClients = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 26)
)
maxClients.setObjects(
      *(("NS-ROOT-MIB", "svcServiceName"),
        ("NS-ROOT-MIB", "svcEstablishedConn"),
        ("NS-ROOT-MIB", "alarmHighThreshold"),
        ("NS-ROOT-MIB", "svcServiceFullName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    maxClients.setStatus(
        "current"
    )

maxClientsNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 27)
)
maxClientsNormal.setObjects(
      *(("NS-ROOT-MIB", "svcServiceName"),
        ("NS-ROOT-MIB", "svcEstablishedConn"),
        ("NS-ROOT-MIB", "alarmNormalThreshold"),
        ("NS-ROOT-MIB", "svcServiceFullName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    maxClientsNormal.setStatus(
        "current"
    )

netScalerConfigSave = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 28)
)
netScalerConfigSave.setObjects(
      *(("NS-ROOT-MIB", "nsUserName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    netScalerConfigSave.setStatus(
        "current"
    )

serviceRxBytesRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 29)
)
serviceRxBytesRate.setObjects(
      *(("NS-ROOT-MIB", "svcServiceName"),
        ("NS-ROOT-MIB", "svcRxBytesRate"),
        ("NS-ROOT-MIB", "alarmHighThreshold"),
        ("NS-ROOT-MIB", "svcServiceFullName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    serviceRxBytesRate.setStatus(
        "current"
    )

serviceRxBytesRateNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 30)
)
serviceRxBytesRateNormal.setObjects(
      *(("NS-ROOT-MIB", "svcServiceName"),
        ("NS-ROOT-MIB", "svcRxBytesRate"),
        ("NS-ROOT-MIB", "alarmNormalThreshold"),
        ("NS-ROOT-MIB", "svcServiceFullName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    serviceRxBytesRateNormal.setStatus(
        "current"
    )

vserverRxBytesRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 31)
)
vserverRxBytesRate.setObjects(
      *(("NS-ROOT-MIB", "vsvrName"),
        ("NS-ROOT-MIB", "vsvrRxBytesRate"),
        ("NS-ROOT-MIB", "alarmHighThreshold"),
        ("NS-ROOT-MIB", "vsvrFullName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    vserverRxBytesRate.setStatus(
        "current"
    )

vserverRxBytesRateNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 32)
)
vserverRxBytesRateNormal.setObjects(
      *(("NS-ROOT-MIB", "vsvrName"),
        ("NS-ROOT-MIB", "vsvrRxBytesRate"),
        ("NS-ROOT-MIB", "alarmNormalThreshold"),
        ("NS-ROOT-MIB", "vsvrFullName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    vserverRxBytesRateNormal.setStatus(
        "current"
    )

serviceTxBytesRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 33)
)
serviceTxBytesRate.setObjects(
      *(("NS-ROOT-MIB", "svcServiceName"),
        ("NS-ROOT-MIB", "svcTxBytesRate"),
        ("NS-ROOT-MIB", "alarmHighThreshold"),
        ("NS-ROOT-MIB", "svcServiceFullName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    serviceTxBytesRate.setStatus(
        "current"
    )

serviceTxBytesRateNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 34)
)
serviceTxBytesRateNormal.setObjects(
      *(("NS-ROOT-MIB", "svcServiceName"),
        ("NS-ROOT-MIB", "svcTxBytesRate"),
        ("NS-ROOT-MIB", "alarmNormalThreshold"),
        ("NS-ROOT-MIB", "svcServiceFullName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    serviceTxBytesRateNormal.setStatus(
        "current"
    )

vserverTxBytesRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 35)
)
vserverTxBytesRate.setObjects(
      *(("NS-ROOT-MIB", "vsvrName"),
        ("NS-ROOT-MIB", "vsvrTxBytesRate"),
        ("NS-ROOT-MIB", "alarmHighThreshold"),
        ("NS-ROOT-MIB", "vsvrFullName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    vserverTxBytesRate.setStatus(
        "current"
    )

vserverTxBytesRateNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 36)
)
vserverTxBytesRateNormal.setObjects(
      *(("NS-ROOT-MIB", "vsvrName"),
        ("NS-ROOT-MIB", "vsvrTxBytesRate"),
        ("NS-ROOT-MIB", "alarmNormalThreshold"),
        ("NS-ROOT-MIB", "vsvrFullName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    vserverTxBytesRateNormal.setStatus(
        "current"
    )

serviceSynfloodRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 37)
)
serviceSynfloodRate.setObjects(
      *(("NS-ROOT-MIB", "svcServiceName"),
        ("NS-ROOT-MIB", "svcSynfloodRate"),
        ("NS-ROOT-MIB", "alarmHighThreshold"),
        ("NS-ROOT-MIB", "svcServiceFullName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    serviceSynfloodRate.setStatus(
        "current"
    )

serviceSynfloodNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 38)
)
serviceSynfloodNormal.setObjects(
      *(("NS-ROOT-MIB", "svcServiceName"),
        ("NS-ROOT-MIB", "svcSynfloodRate"),
        ("NS-ROOT-MIB", "alarmNormalThreshold"),
        ("NS-ROOT-MIB", "svcServiceFullName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    serviceSynfloodNormal.setStatus(
        "current"
    )

vserverSynfloodRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 39)
)
vserverSynfloodRate.setObjects(
      *(("NS-ROOT-MIB", "vsvrName"),
        ("NS-ROOT-MIB", "vsvrSynfloodRate"),
        ("NS-ROOT-MIB", "alarmHighThreshold"),
        ("NS-ROOT-MIB", "vsvrFullName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    vserverSynfloodRate.setStatus(
        "current"
    )

vserverSynfloodNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 40)
)
vserverSynfloodNormal.setObjects(
      *(("NS-ROOT-MIB", "vsvrName"),
        ("NS-ROOT-MIB", "vsvrSynfloodRate"),
        ("NS-ROOT-MIB", "alarmNormalThreshold"),
        ("NS-ROOT-MIB", "vsvrFullName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    vserverSynfloodNormal.setStatus(
        "current"
    )

svcGroupMemberRequestRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 41)
)
svcGroupMemberRequestRate.setObjects(
      *(("NS-ROOT-MIB", "svcGrpMemberName"),
        ("NS-ROOT-MIB", "svcGrpMemberRequestRate"),
        ("NS-ROOT-MIB", "alarmHighThreshold"),
        ("NS-ROOT-MIB", "svcGrpMemberFullName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    svcGroupMemberRequestRate.setStatus(
        "current"
    )

svcGroupMemberRequestRateNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 42)
)
svcGroupMemberRequestRateNormal.setObjects(
      *(("NS-ROOT-MIB", "svcGrpMemberName"),
        ("NS-ROOT-MIB", "svcGrpMemberRequestRate"),
        ("NS-ROOT-MIB", "alarmNormalThreshold"),
        ("NS-ROOT-MIB", "svcGrpMemberFullName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    svcGroupMemberRequestRateNormal.setStatus(
        "current"
    )

svcGroupMemberRxBytesRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 43)
)
svcGroupMemberRxBytesRate.setObjects(
      *(("NS-ROOT-MIB", "svcGrpMemberName"),
        ("NS-ROOT-MIB", "svcGrpMemberRxBytesRate"),
        ("NS-ROOT-MIB", "alarmHighThreshold"),
        ("NS-ROOT-MIB", "svcGrpMemberFullName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    svcGroupMemberRxBytesRate.setStatus(
        "current"
    )

svcGroupMemberRxBytesRateNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 44)
)
svcGroupMemberRxBytesRateNormal.setObjects(
      *(("NS-ROOT-MIB", "svcGrpMemberName"),
        ("NS-ROOT-MIB", "svcGrpMemberRxBytesRate"),
        ("NS-ROOT-MIB", "alarmNormalThreshold"),
        ("NS-ROOT-MIB", "svcGrpMemberFullName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    svcGroupMemberRxBytesRateNormal.setStatus(
        "current"
    )

svcGroupMemberTxBytesRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 45)
)
svcGroupMemberTxBytesRate.setObjects(
      *(("NS-ROOT-MIB", "svcGrpMemberName"),
        ("NS-ROOT-MIB", "svcGrpMemberTxBytesRate"),
        ("NS-ROOT-MIB", "alarmHighThreshold"),
        ("NS-ROOT-MIB", "svcGrpMemberFullName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    svcGroupMemberTxBytesRate.setStatus(
        "current"
    )

svcGroupMemberTxBytesRateNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 46)
)
svcGroupMemberTxBytesRateNormal.setObjects(
      *(("NS-ROOT-MIB", "svcGrpMemberName"),
        ("NS-ROOT-MIB", "svcGrpMemberTxBytesRate"),
        ("NS-ROOT-MIB", "alarmNormalThreshold"),
        ("NS-ROOT-MIB", "svcGrpMemberFullName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    svcGroupMemberTxBytesRateNormal.setStatus(
        "current"
    )

svcGroupMemberSynfloodRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 47)
)
svcGroupMemberSynfloodRate.setObjects(
      *(("NS-ROOT-MIB", "svcGrpMemberName"),
        ("NS-ROOT-MIB", "svcGrpMemberSynfloodRate"),
        ("NS-ROOT-MIB", "alarmHighThreshold"),
        ("NS-ROOT-MIB", "svcGrpMemberFullName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    svcGroupMemberSynfloodRate.setStatus(
        "current"
    )

svcGroupMemberSynfloodNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 48)
)
svcGroupMemberSynfloodNormal.setObjects(
      *(("NS-ROOT-MIB", "svcGrpMemberName"),
        ("NS-ROOT-MIB", "svcGrpMemberSynfloodRate"),
        ("NS-ROOT-MIB", "alarmNormalThreshold"),
        ("NS-ROOT-MIB", "svcGrpMemberFullName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    svcGroupMemberSynfloodNormal.setStatus(
        "current"
    )

svcGroupMemberMaxClients = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 49)
)
svcGroupMemberMaxClients.setObjects(
      *(("NS-ROOT-MIB", "svcGrpMemberName"),
        ("NS-ROOT-MIB", "svcGrpMemberEstablishedConn"),
        ("NS-ROOT-MIB", "alarmHighThreshold"),
        ("NS-ROOT-MIB", "svcGrpMemberFullName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    svcGroupMemberMaxClients.setStatus(
        "current"
    )

svcGroupMemberMaxClientsNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 50)
)
svcGroupMemberMaxClientsNormal.setObjects(
      *(("NS-ROOT-MIB", "svcGrpMemberName"),
        ("NS-ROOT-MIB", "svcGrpMemberEstablishedConn"),
        ("NS-ROOT-MIB", "alarmNormalThreshold"),
        ("NS-ROOT-MIB", "svcGrpMemberFullName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    svcGroupMemberMaxClientsNormal.setStatus(
        "current"
    )

averageCpuUtilization = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 51)
)
averageCpuUtilization.setObjects(
      *(("NS-ROOT-MIB", "resCpuUsage"),
        ("NS-ROOT-MIB", "alarmHighThreshold"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    averageCpuUtilization.setStatus(
        "current"
    )

averageCpuUtilizationNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 52)
)
averageCpuUtilizationNormal.setObjects(
      *(("NS-ROOT-MIB", "resCpuUsage"),
        ("NS-ROOT-MIB", "alarmNormalThreshold"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    averageCpuUtilizationNormal.setStatus(
        "current"
    )

monRespTimeoutAboveThresh = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 53)
)
monRespTimeoutAboveThresh.setObjects(
      *(("NS-ROOT-MIB", "monServiceName"),
        ("NS-ROOT-MIB", "monitorName"),
        ("NS-ROOT-MIB", "responseTimeoutThreshold"),
        ("NS-ROOT-MIB", "alarmMonrespto"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    monRespTimeoutAboveThresh.setStatus(
        "current"
    )

monRespTimeoutBelowThresh = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 54)
)
monRespTimeoutBelowThresh.setObjects(
      *(("NS-ROOT-MIB", "monServiceName"),
        ("NS-ROOT-MIB", "monitorName"),
        ("NS-ROOT-MIB", "responseTimeoutThreshold"),
        ("NS-ROOT-MIB", "alarmMonrespto"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    monRespTimeoutBelowThresh.setStatus(
        "current"
    )

netScalerLoginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 55)
)
netScalerLoginFailure.setObjects(
      *(("NS-ROOT-MIB", "nsUserName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    netScalerLoginFailure.setStatus(
        "current"
    )

sslCertificateExpiry = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 56)
)
sslCertificateExpiry.setObjects(
      *(("NS-ROOT-MIB", "sslCertKeyName"),
        ("NS-ROOT-MIB", "sslDaysToExpire"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    sslCertificateExpiry.setStatus(
        "current"
    )

fanSpeedLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 57)
)
fanSpeedLow.setObjects(
      *(("NS-ROOT-MIB", "sysHealthCounterName"),
        ("NS-ROOT-MIB", "sysHealthCounterValue"),
        ("NS-ROOT-MIB", "alarmLowThreshold"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    fanSpeedLow.setStatus(
        "current"
    )

fanSpeedNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 58)
)
fanSpeedNormal.setObjects(
      *(("NS-ROOT-MIB", "sysHealthCounterName"),
        ("NS-ROOT-MIB", "sysHealthCounterValue"),
        ("NS-ROOT-MIB", "alarmNormalThreshold"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    fanSpeedNormal.setStatus(
        "current"
    )

voltageLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 59)
)
voltageLow.setObjects(
      *(("NS-ROOT-MIB", "sysHealthCounterName"),
        ("NS-ROOT-MIB", "sysHealthCounterValue"),
        ("NS-ROOT-MIB", "alarmLowThreshold"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    voltageLow.setStatus(
        "current"
    )

voltageNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 60)
)
voltageNormal.setObjects(
      *(("NS-ROOT-MIB", "sysHealthCounterName"),
        ("NS-ROOT-MIB", "sysHealthCounterValue"),
        ("NS-ROOT-MIB", "alarmNormalThreshold"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    voltageNormal.setStatus(
        "current"
    )

voltageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 61)
)
voltageHigh.setObjects(
      *(("NS-ROOT-MIB", "sysHealthCounterName"),
        ("NS-ROOT-MIB", "sysHealthCounterValue"),
        ("NS-ROOT-MIB", "alarmHighThreshold"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    voltageHigh.setStatus(
        "current"
    )

temperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 62)
)
temperatureHigh.setObjects(
      *(("NS-ROOT-MIB", "sysHealthCounterName"),
        ("NS-ROOT-MIB", "sysHealthCounterValue"),
        ("NS-ROOT-MIB", "alarmHighThreshold"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    temperatureHigh.setStatus(
        "current"
    )

temperatureNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 63)
)
temperatureNormal.setObjects(
      *(("NS-ROOT-MIB", "sysHealthCounterName"),
        ("NS-ROOT-MIB", "sysHealthCounterValue"),
        ("NS-ROOT-MIB", "alarmNormalThreshold"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    temperatureNormal.setStatus(
        "current"
    )

diskUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 64)
)
diskUsageHigh.setObjects(
      *(("NS-ROOT-MIB", "sysHealthDiskName"),
        ("NS-ROOT-MIB", "sysHealthDiskPerusage"),
        ("NS-ROOT-MIB", "alarmHighThreshold"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    diskUsageHigh.setStatus(
        "current"
    )

diskUsageNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 65)
)
diskUsageNormal.setObjects(
      *(("NS-ROOT-MIB", "sysHealthDiskName"),
        ("NS-ROOT-MIB", "sysHealthDiskPerusage"),
        ("NS-ROOT-MIB", "alarmNormalThreshold"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    diskUsageNormal.setStatus(
        "current"
    )

interfaceThroughputLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 66)
)
interfaceThroughputLow.setObjects(
      *(("NS-ROOT-MIB", "ifName"),
        ("NS-ROOT-MIB", "ifThroughput"),
        ("NS-ROOT-MIB", "ifMinThroughput"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    interfaceThroughputLow.setStatus(
        "current"
    )

interfaceThroughputNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 67)
)
interfaceThroughputNormal.setObjects(
      *(("NS-ROOT-MIB", "ifName"),
        ("NS-ROOT-MIB", "ifThroughput"),
        ("NS-ROOT-MIB", "ifMinThroughput"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    interfaceThroughputNormal.setStatus(
        "current"
    )

haVersionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 68)
)
haVersionMismatch.setObjects(
    ("NS-ROOT-MIB", "sysIpAddress")
)
if mibBuilder.loadTexts:
    haVersionMismatch.setStatus(
        "current"
    )

haSyncFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 69)
)
haSyncFailure.setObjects(
    ("NS-ROOT-MIB", "sysIpAddress")
)
if mibBuilder.loadTexts:
    haSyncFailure.setStatus(
        "current"
    )

haNoHeartbeats = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 70)
)
haNoHeartbeats.setObjects(
      *(("NS-ROOT-MIB", "haNicsMonitorFailed"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    haNoHeartbeats.setStatus(
        "current"
    )

haBadSecState = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 71)
)
haBadSecState.setObjects(
      *(("NS-ROOT-MIB", "haPeerSystemState"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    haBadSecState.setStatus(
        "current"
    )

interfaceBWUseHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 72)
)
interfaceBWUseHigh.setObjects(
      *(("NS-ROOT-MIB", "ifName"),
        ("NS-ROOT-MIB", "alarmHighThreshold"),
        ("NS-ROOT-MIB", "alarmCurrentValue"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    interfaceBWUseHigh.setStatus(
        "current"
    )

interfaceBWUseNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 73)
)
interfaceBWUseNormal.setObjects(
      *(("NS-ROOT-MIB", "ifName"),
        ("NS-ROOT-MIB", "alarmNormalThreshold"),
        ("NS-ROOT-MIB", "alarmCurrentValue"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    interfaceBWUseNormal.setStatus(
        "current"
    )

aggregateBWUseHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 74)
)
aggregateBWUseHigh.setObjects(
      *(("NS-ROOT-MIB", "alarmHighThreshold"),
        ("NS-ROOT-MIB", "alarmCurrentValue"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    aggregateBWUseHigh.setStatus(
        "current"
    )

aggregateBWUseNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 75)
)
aggregateBWUseNormal.setObjects(
      *(("NS-ROOT-MIB", "alarmNormalThreshold"),
        ("NS-ROOT-MIB", "alarmCurrentValue"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    aggregateBWUseNormal.setStatus(
        "current"
    )

vserverRhiStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 76)
)
vserverRhiStateChange.setObjects(
      *(("NS-ROOT-MIB", "alarmVipRhiState"),
        ("NS-ROOT-MIB", "alarmVipRhiInetAddressType"),
        ("NS-ROOT-MIB", "alarmVipRhiInetAddress"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    vserverRhiStateChange.setStatus(
        "current"
    )

rateLmtThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 77)
)
rateLmtThresholdExceed.setObjects(
      *(("NS-ROOT-MIB", "alarmRateLmtThresholdExceeded"),
        ("NS-ROOT-MIB", "ipAddressGathered"),
        ("NS-ROOT-MIB", "stringComputed"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    rateLmtThresholdExceed.setStatus(
        "current"
    )

monProbeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 78)
)
monProbeFailed.setObjects(
      *(("NS-ROOT-MIB", "monServiceName"),
        ("NS-ROOT-MIB", "monitorName"),
        ("NS-ROOT-MIB", "alarmProbeFailedRetries"),
        ("NS-ROOT-MIB", "monitorRetrys"),
        ("NS-ROOT-MIB", "alarmProbeFailedErrorString"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    monProbeFailed.setStatus(
        "current"
    )

temperatureCpuHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 79)
)
temperatureCpuHigh.setObjects(
      *(("NS-ROOT-MIB", "sysHealthCounterName"),
        ("NS-ROOT-MIB", "sysHealthCounterValue"),
        ("NS-ROOT-MIB", "alarmHighThreshold"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    temperatureCpuHigh.setStatus(
        "current"
    )

temperatureCpuNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 80)
)
temperatureCpuNormal.setObjects(
      *(("NS-ROOT-MIB", "sysHealthCounterName"),
        ("NS-ROOT-MIB", "sysHealthCounterValue"),
        ("NS-ROOT-MIB", "alarmNormalThreshold"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    temperatureCpuNormal.setStatus(
        "current"
    )

entityofs = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 81)
)
entityofs.setObjects(
      *(("NS-ROOT-MIB", "entityName"),
        ("NS-ROOT-MIB", "alarmEntityCurState"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    entityofs.setStatus(
        "current"
    )

powerSupplyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 82)
)
powerSupplyFailed.setObjects(
      *(("NS-ROOT-MIB", "sysHealthCounterName"),
        ("NS-ROOT-MIB", "sysHealthCounterValue"),
        ("NS-ROOT-MIB", "sysHealthPowerSupplyStatus"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    powerSupplyFailed.setStatus(
        "current"
    )

powerSupplyNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 83)
)
powerSupplyNormal.setObjects(
      *(("NS-ROOT-MIB", "sysHealthCounterName"),
        ("NS-ROOT-MIB", "sysHealthCounterValue"),
        ("NS-ROOT-MIB", "sysHealthPowerSupplyStatus"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    powerSupplyNormal.setStatus(
        "current"
    )

entityNameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 84)
)
entityNameChanged.setObjects(
      *(("NS-ROOT-MIB", "entityName"),
        ("NS-ROOT-MIB", "alarmVsvrNewName"),
        ("NS-ROOT-MIB", "alarmVsvrOldName"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    entityNameChanged.setStatus(
        "current"
    )

haPropFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 85)
)
haPropFailure.setObjects(
    ("NS-ROOT-MIB", "sysIpAddress")
)
if mibBuilder.loadTexts:
    haPropFailure.setStatus(
        "current"
    )

ipConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 86)
)
ipConflict.setObjects(
      *(("NS-ROOT-MIB", "ipConflictAddr"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    ipConflict.setStatus(
        "current"
    )

appfwStartUrl = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 87)
)
appfwStartUrl.setObjects(
      *(("NS-ROOT-MIB", "appfwLogMsg"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    appfwStartUrl.setStatus(
        "current"
    )

appfwDenyUrl = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 88)
)
appfwDenyUrl.setObjects(
      *(("NS-ROOT-MIB", "appfwLogMsg"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    appfwDenyUrl.setStatus(
        "current"
    )

appfwRefererHeader = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 89)
)
appfwRefererHeader.setObjects(
      *(("NS-ROOT-MIB", "appfwLogMsg"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    appfwRefererHeader.setStatus(
        "current"
    )

appfwCSRFTag = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 90)
)
appfwCSRFTag.setObjects(
      *(("NS-ROOT-MIB", "appfwLogMsg"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    appfwCSRFTag.setStatus(
        "current"
    )

appfwCookie = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 91)
)
appfwCookie.setObjects(
      *(("NS-ROOT-MIB", "appfwLogMsg"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    appfwCookie.setStatus(
        "current"
    )

appfwFieldConsistency = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 92)
)
appfwFieldConsistency.setObjects(
      *(("NS-ROOT-MIB", "appfwLogMsg"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    appfwFieldConsistency.setStatus(
        "current"
    )

appfwBufferOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 93)
)
appfwBufferOverflow.setObjects(
      *(("NS-ROOT-MIB", "appfwLogMsg"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    appfwBufferOverflow.setStatus(
        "current"
    )

appfwFieldFormat = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 94)
)
appfwFieldFormat.setObjects(
      *(("NS-ROOT-MIB", "appfwLogMsg"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    appfwFieldFormat.setStatus(
        "current"
    )

appfwSafeCommerce = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 95)
)
appfwSafeCommerce.setObjects(
      *(("NS-ROOT-MIB", "appfwLogMsg"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    appfwSafeCommerce.setStatus(
        "current"
    )

appfwSafeObject = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 96)
)
appfwSafeObject.setObjects(
      *(("NS-ROOT-MIB", "appfwLogMsg"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    appfwSafeObject.setStatus(
        "current"
    )

appfwPolicyHit = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 97)
)
appfwPolicyHit.setObjects(
      *(("NS-ROOT-MIB", "appfwLogMsg"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    appfwPolicyHit.setStatus(
        "current"
    )

appfwXSS = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 98)
)
appfwXSS.setObjects(
      *(("NS-ROOT-MIB", "appfwLogMsg"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    appfwXSS.setStatus(
        "current"
    )

appfwXMLXSS = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 99)
)
appfwXMLXSS.setObjects(
      *(("NS-ROOT-MIB", "appfwLogMsg"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    appfwXMLXSS.setStatus(
        "current"
    )

appfwSQL = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 100)
)
appfwSQL.setObjects(
      *(("NS-ROOT-MIB", "appfwLogMsg"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    appfwSQL.setStatus(
        "current"
    )

appfwXMLSQL = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 101)
)
appfwXMLSQL.setObjects(
      *(("NS-ROOT-MIB", "appfwLogMsg"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    appfwXMLSQL.setStatus(
        "current"
    )

appfwXMLAttachment = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 102)
)
appfwXMLAttachment.setObjects(
      *(("NS-ROOT-MIB", "appfwLogMsg"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    appfwXMLAttachment.setStatus(
        "current"
    )

appfwXMLDos = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 103)
)
appfwXMLDos.setObjects(
      *(("NS-ROOT-MIB", "appfwLogMsg"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    appfwXMLDos.setStatus(
        "current"
    )

appfwXMLValidation = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 104)
)
appfwXMLValidation.setObjects(
      *(("NS-ROOT-MIB", "appfwLogMsg"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    appfwXMLValidation.setStatus(
        "current"
    )

appfwXMLWSI = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 105)
)
appfwXMLWSI.setObjects(
      *(("NS-ROOT-MIB", "appfwLogMsg"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    appfwXMLWSI.setStatus(
        "current"
    )

appfwXMLSchemaCompile = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 106)
)
appfwXMLSchemaCompile.setObjects(
      *(("NS-ROOT-MIB", "appfwLogMsg"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    appfwXMLSchemaCompile.setStatus(
        "current"
    )

appfwXMLSoapFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 1, 1, 0, 107)
)
appfwXMLSoapFault.setObjects(
      *(("NS-ROOT-MIB", "appfwLogMsg"),
        ("NS-ROOT-MIB", "sysIpAddress"))
)
if mibBuilder.loadTexts:
    appfwXMLSoapFault.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NS-ROOT-MIB",
    **{"EntityProtocolType": EntityProtocolType,
       "EntityState": EntityState,
       "MepStatus": MepStatus,
       "SiteType": SiteType,
       "MetricExchange": MetricExchange,
       "AdminStatus": AdminStatus,
       "HAMode": HAMode,
       "HAState": HAState,
       "HAON": HAON,
       "FeatureStatus": FeatureStatus,
       "FeaturePlatform": FeaturePlatform,
       "ModeStatus": ModeStatus,
       "LbPolicy": LbPolicy,
       "PersistanceType": PersistanceType,
       "ActionType": ActionType,
       "InputFormat": InputFormat,
       "IpAddressType": IpAddressType,
       "IpAddressMode": IpAddressMode,
       "AuthorizationStatus": AuthorizationStatus,
       "CommandExecutionStatus": CommandExecutionStatus,
       "MonitorType": MonitorType,
       "MonitorState": MonitorState,
       "ServiceGroupState": ServiceGroupState,
       "VServerType": VServerType,
       "SvcEntityType": SvcEntityType,
       "ActiveActiveState": ActiveActiveState,
       "netScaler": netScaler,
       "nsRoot": nsRoot,
       "netScalerEvents": netScalerEvents,
       "netScalerEventsV2": netScalerEventsV2,
       "changeToPrimary": changeToPrimary,
       "changeToSecondary": changeToSecondary,
       "cpuUtilization": cpuUtilization,
       "linkUp": linkUp,
       "linkDown": linkDown,
       "discoverFailure": discoverFailure,
       "memUtilization": memUtilization,
       "entitydown": entitydown,
       "entityup": entityup,
       "synflood": synflood,
       "cpuUtilizationNormal": cpuUtilizationNormal,
       "synfloodNormal": synfloodNormal,
       "memoryUtilization": memoryUtilization,
       "memoryUtilizationNormal": memoryUtilizationNormal,
       "vServerRequestRate": vServerRequestRate,
       "vServerRequestRateNormal": vServerRequestRateNormal,
       "serviceRequestRate": serviceRequestRate,
       "serviceRequestRateNormal": serviceRequestRateNormal,
       "entityRxRate": entityRxRate,
       "entityRxRateNormal": entityRxRateNormal,
       "entityTxRate": entityTxRate,
       "entityTxRateNormal": entityTxRateNormal,
       "entitySynflood": entitySynflood,
       "entitySynfloodNormal": entitySynfloodNormal,
       "netScalerConfigChange": netScalerConfigChange,
       "maxClients": maxClients,
       "maxClientsNormal": maxClientsNormal,
       "netScalerConfigSave": netScalerConfigSave,
       "serviceRxBytesRate": serviceRxBytesRate,
       "serviceRxBytesRateNormal": serviceRxBytesRateNormal,
       "vserverRxBytesRate": vserverRxBytesRate,
       "vserverRxBytesRateNormal": vserverRxBytesRateNormal,
       "serviceTxBytesRate": serviceTxBytesRate,
       "serviceTxBytesRateNormal": serviceTxBytesRateNormal,
       "vserverTxBytesRate": vserverTxBytesRate,
       "vserverTxBytesRateNormal": vserverTxBytesRateNormal,
       "serviceSynfloodRate": serviceSynfloodRate,
       "serviceSynfloodNormal": serviceSynfloodNormal,
       "vserverSynfloodRate": vserverSynfloodRate,
       "vserverSynfloodNormal": vserverSynfloodNormal,
       "svcGroupMemberRequestRate": svcGroupMemberRequestRate,
       "svcGroupMemberRequestRateNormal": svcGroupMemberRequestRateNormal,
       "svcGroupMemberRxBytesRate": svcGroupMemberRxBytesRate,
       "svcGroupMemberRxBytesRateNormal": svcGroupMemberRxBytesRateNormal,
       "svcGroupMemberTxBytesRate": svcGroupMemberTxBytesRate,
       "svcGroupMemberTxBytesRateNormal": svcGroupMemberTxBytesRateNormal,
       "svcGroupMemberSynfloodRate": svcGroupMemberSynfloodRate,
       "svcGroupMemberSynfloodNormal": svcGroupMemberSynfloodNormal,
       "svcGroupMemberMaxClients": svcGroupMemberMaxClients,
       "svcGroupMemberMaxClientsNormal": svcGroupMemberMaxClientsNormal,
       "averageCpuUtilization": averageCpuUtilization,
       "averageCpuUtilizationNormal": averageCpuUtilizationNormal,
       "monRespTimeoutAboveThresh": monRespTimeoutAboveThresh,
       "monRespTimeoutBelowThresh": monRespTimeoutBelowThresh,
       "netScalerLoginFailure": netScalerLoginFailure,
       "sslCertificateExpiry": sslCertificateExpiry,
       "fanSpeedLow": fanSpeedLow,
       "fanSpeedNormal": fanSpeedNormal,
       "voltageLow": voltageLow,
       "voltageNormal": voltageNormal,
       "voltageHigh": voltageHigh,
       "temperatureHigh": temperatureHigh,
       "temperatureNormal": temperatureNormal,
       "diskUsageHigh": diskUsageHigh,
       "diskUsageNormal": diskUsageNormal,
       "interfaceThroughputLow": interfaceThroughputLow,
       "interfaceThroughputNormal": interfaceThroughputNormal,
       "haVersionMismatch": haVersionMismatch,
       "haSyncFailure": haSyncFailure,
       "haNoHeartbeats": haNoHeartbeats,
       "haBadSecState": haBadSecState,
       "interfaceBWUseHigh": interfaceBWUseHigh,
       "interfaceBWUseNormal": interfaceBWUseNormal,
       "aggregateBWUseHigh": aggregateBWUseHigh,
       "aggregateBWUseNormal": aggregateBWUseNormal,
       "vserverRhiStateChange": vserverRhiStateChange,
       "rateLmtThresholdExceed": rateLmtThresholdExceed,
       "monProbeFailed": monProbeFailed,
       "temperatureCpuHigh": temperatureCpuHigh,
       "temperatureCpuNormal": temperatureCpuNormal,
       "entityofs": entityofs,
       "powerSupplyFailed": powerSupplyFailed,
       "powerSupplyNormal": powerSupplyNormal,
       "entityNameChanged": entityNameChanged,
       "haPropFailure": haPropFailure,
       "ipConflict": ipConflict,
       "appfwStartUrl": appfwStartUrl,
       "appfwDenyUrl": appfwDenyUrl,
       "appfwRefererHeader": appfwRefererHeader,
       "appfwCSRFTag": appfwCSRFTag,
       "appfwCookie": appfwCookie,
       "appfwFieldConsistency": appfwFieldConsistency,
       "appfwBufferOverflow": appfwBufferOverflow,
       "appfwFieldFormat": appfwFieldFormat,
       "appfwSafeCommerce": appfwSafeCommerce,
       "appfwSafeObject": appfwSafeObject,
       "appfwPolicyHit": appfwPolicyHit,
       "appfwXSS": appfwXSS,
       "appfwXMLXSS": appfwXMLXSS,
       "appfwSQL": appfwSQL,
       "appfwXMLSQL": appfwXMLSQL,
       "appfwXMLAttachment": appfwXMLAttachment,
       "appfwXMLDos": appfwXMLDos,
       "appfwXMLValidation": appfwXMLValidation,
       "appfwXMLWSI": appfwXMLWSI,
       "appfwXMLSchemaCompile": appfwXMLSchemaCompile,
       "appfwXMLSoapFault": appfwXMLSoapFault,
       "wsSystem": wsSystem,
       "sysStatistics": sysStatistics,
       "totalClientConnections": totalClientConnections,
       "curClientConnections": curClientConnections,
       "totalServerConnections": totalServerConnections,
       "curServerConnections": curServerConnections,
       "clientConnRefused": clientConnRefused,
       "reuseHit": reuseHit,
       "reuseMiss": reuseMiss,
       "totClientDontReuse": totClientDontReuse,
       "totServerDontReuse": totServerDontReuse,
       "curPhysicalServers": curPhysicalServers,
       "totPhysicalServers": totPhysicalServers,
       "cookiePacketSeqReject": cookiePacketSeqReject,
       "cookieSignatureReject": cookieSignatureReject,
       "cpuUsage": cpuUsage,
       "unackSyn": unackSyn,
       "curClientEstablishedConn": curClientEstablishedConn,
       "curServerEstablishedConn": curServerEstablishedConn,
       "wsHttpGroup": wsHttpGroup,
       "totalRequests": totalRequests,
       "totalGets": totalGets,
       "totalRequests1-0": totalRequests1_0,
       "totalPosts": totalPosts,
       "totalResponses": totalResponses,
       "totalResponses1-0": totalResponses1_0,
       "totalContentLenResponses": totalContentLenResponses,
       "totalChunkedResponses": totalChunkedResponses,
       "totalMultiPartResponses": totalMultiPartResponses,
       "totalIncompleteHeaders": totalIncompleteHeaders,
       "totalIncompleteRequests": totalIncompleteRequests,
       "totalIncompleteResponses": totalIncompleteResponses,
       "totalPipeLinedRequests": totalPipeLinedRequests,
       "serverBusyErrs": serverBusyErrs,
       "wsIfStatsTable": wsIfStatsTable,
       "wsIfStatsEntry": wsIfStatsEntry,
       "index": index,
       "wsIfName": wsIfName,
       "wsIfMedia": wsIfMedia,
       "rxRawBandwidthUsage": rxRawBandwidthUsage,
       "rxAveragePacketRate": rxAveragePacketRate,
       "rxCurrentPacketRate": rxCurrentPacketRate,
       "rxAveragePacketsSize": rxAveragePacketsSize,
       "rxFrameErrors": rxFrameErrors,
       "rxCrcErrors": rxCrcErrors,
       "rxAlignmentErrors": rxAlignmentErrors,
       "txRawBandwidthUsage": txRawBandwidthUsage,
       "txAveragePacketRate": txAveragePacketRate,
       "txCurrentPacketRate": txCurrentPacketRate,
       "txAveragePacketsSize": txAveragePacketsSize,
       "txExcessCollisions": txExcessCollisions,
       "txLateCollisions": txLateCollisions,
       "txCollisions": txCollisions,
       "txMultiCollisionsErrors": txMultiCollisionsErrors,
       "txCarrierErrors": txCarrierErrors,
       "wsudpgroup": wsudpgroup,
       "totudpsessions": totudpsessions,
       "currudpsessions": currudpsessions,
       "sysConfig": sysConfig,
       "wsIpAddress": wsIpAddress,
       "wsNetmask": wsNetmask,
       "wsMappedIpAddress": wsMappedIpAddress,
       "wsLastMappedIpAddress": wsLastMappedIpAddress,
       "wsMappedIpAddressRange": wsMappedIpAddressRange,
       "wsFailOver": wsFailOver,
       "wsPriority": wsPriority,
       "wsMaxClientList": wsMaxClientList,
       "wsClientIp": wsClientIp,
       "wsFailoverTime": wsFailoverTime,
       "wsMaxRequestsPerConn": wsMaxRequestsPerConn,
       "wsSmoothConnection": wsSmoothConnection,
       "loadBalancing": loadBalancing,
       "lbStatisticsTable": lbStatisticsTable,
       "lbStatisticsEntry": lbStatisticsEntry,
       "vsId": vsId,
       "psId": psId,
       "vsIpAddress": vsIpAddress,
       "vsPort": vsPort,
       "psIpAddress": psIpAddress,
       "psPort": psPort,
       "protocolType": protocolType,
       "lbMethod": lbMethod,
       "serviceHits": serviceHits,
       "latency": latency,
       "connections": connections,
       "lbConfig": lbConfig,
       "virServiceTable": virServiceTable,
       "virServiceEntry": virServiceEntry,
       "vserId": vserId,
       "ipAddress": ipAddress,
       "port": port,
       "vsProtocolType": vsProtocolType,
       "name": name,
       "vsLbMethod": vsLbMethod,
       "persistanceType": persistanceType,
       "persistanceTimeout": persistanceTimeout,
       "state": state,
       "phyServiceTable": phyServiceTable,
       "phyServiceEntry": phyServiceEntry,
       "pserId": pserId,
       "pserIpAddress": pserIpAddress,
       "pserPort": pserPort,
       "psProtocolType": psProtocolType,
       "psName": psName,
       "psState": psState,
       "weight": weight,
       "psVsIpAddress": psVsIpAddress,
       "psVsPort": psVsPort,
       "sureConnect": sureConnect,
       "scStatistics": scStatistics,
       "scperServiceStatisticsTable": scperServiceStatisticsTable,
       "scperServiceStatisticsEntry": scperServiceStatisticsEntry,
       "devno": devno,
       "phyIpAddress": phyIpAddress,
       "phyPort": phyPort,
       "scProtocolType": scProtocolType,
       "currentDelay": currentDelay,
       "avgTxTime": avgTxTime,
       "surgeCount": surgeCount,
       "iohCount": iohCount,
       "scperPolicyStatisticsTable": scperPolicyStatisticsTable,
       "scperPolicyStatisticsEntry": scperPolicyStatisticsEntry,
       "policydevno": policydevno,
       "primaryserviceIp": primaryserviceIp,
       "primaryserviceport": primaryserviceport,
       "destserviceIp": destserviceIp,
       "destserviceport": destserviceport,
       "transactiontime": transactiontime,
       "totaltransaction": totaltransaction,
       "totalopenconnection": totalopenconnection,
       "scGlobalStats": scGlobalStats,
       "scUrlHits": scUrlHits,
       "popUps": popUps,
       "altContUrls": altContUrls,
       "sessReqs": sessReqs,
       "postReqs": postReqs,
       "thresholdFail": thresholdFail,
       "faultyCookies": faultyCookies,
       "unSupBrow": unSupBrow,
       "resetStats": resetStats,
       "scConfig": scConfig,
       "scPolicyconfigTable": scPolicyconfigTable,
       "scPolicyconfigEntry": scPolicyconfigEntry,
       "policyIndex": policyIndex,
       "policyName": policyName,
       "scPolicyUrl": scPolicyUrl,
       "delayThreshold": delayThreshold,
       "maxConnections": maxConnections,
       "actionType": actionType,
       "alternatecontentServicename": alternatecontentServicename,
       "ruleName": ruleName,
       "alternatecontentPath": alternatecontentPath,
       "contentSwitching": contentSwitching,
       "cswStatisticsTable": cswStatisticsTable,
       "cswStatisticsEntry": cswStatisticsEntry,
       "cswIndex": cswIndex,
       "cswVsIpAddress": cswVsIpAddress,
       "cswVsPort": cswVsPort,
       "cswProtocolType": cswProtocolType,
       "virServiceName": virServiceName,
       "vsHits": vsHits,
       "vsMiss": vsMiss,
       "cswConfigTable": cswConfigTable,
       "cswConfigEntry": cswConfigEntry,
       "cswVsId": cswVsId,
       "policyId": policyId,
       "vServerName": vServerName,
       "policyname": policyname,
       "policyvalue": policyvalue,
       "policyHits": policyHits,
       "domain": domain,
       "cacheRedirection": cacheRedirection,
       "crStatisticsTable": crStatisticsTable,
       "crStatisticsEntry": crStatisticsEntry,
       "crVsIndex": crVsIndex,
       "crVsIpAddress": crVsIpAddress,
       "crVsPort": crVsPort,
       "crProtocolType": crProtocolType,
       "crVirServiceName": crVirServiceName,
       "crVsHits": crVsHits,
       "crVsMiss": crVsMiss,
       "crConfig": crConfig,
       "crPolBindConfigTable": crPolBindConfigTable,
       "crPolBindConfigEntry": crPolBindConfigEntry,
       "bindId": bindId,
       "crbVServerName": crbVServerName,
       "crbPolicyname": crbPolicyname,
       "crbPolicyvalue": crbPolicyvalue,
       "crbPolicyHits": crbPolicyHits,
       "crMapBindConfigTable": crMapBindConfigTable,
       "crMapBindConfigEntry": crMapBindConfigEntry,
       "mapbindId": mapbindId,
       "mapName": mapName,
       "mapHits": mapHits,
       "vserverName": vserverName,
       "crMapConfigTable": crMapConfigTable,
       "crMapConfigEntry": crMapConfigEntry,
       "crmIndex": crmIndex,
       "crmMapName": crmMapName,
       "srcDomain": srcDomain,
       "dstDomain": dstDomain,
       "srcUrl": srcUrl,
       "dstUrl": dstUrl,
       "compression": compression,
       "compressionStats": compressionStats,
       "cmpTotRequests": cmpTotRequests,
       "cmpTotTxbytes": cmpTotTxbytes,
       "cmpTotRxbytes": cmpTotRxbytes,
       "cmpTotTxpkts": cmpTotTxpkts,
       "cmpTotRxpkts": cmpTotRxpkts,
       "compressionRatio": compressionRatio,
       "totalDataCompressionRatio": totalDataCompressionRatio,
       "vlan": vlan,
       "vlanstatsTable": vlanstatsTable,
       "vlanstatsEntry": vlanstatsEntry,
       "vlansDevno": vlansDevno,
       "totalrxpkts": totalrxpkts,
       "totaltxpkts": totaltxpkts,
       "totalrxbytes": totalrxbytes,
       "totaltxbytes": totaltxbytes,
       "totaldroppedpkts": totaldroppedpkts,
       "totalbroadcastpackets": totalbroadcastpackets,
       "vlanconfigTable": vlanconfigTable,
       "vlanconfigEntry": vlanconfigEntry,
       "vlancDevno": vlancDevno,
       "tagId": tagId,
       "vlancInterfaces": vlancInterfaces,
       "ipaddress": ipaddress,
       "netmask": netmask,
       "tagging": tagging,
       "domainNameService": domainNameService,
       "dnsServer": dnsServer,
       "dnsServerStatistics": dnsServerStatistics,
       "totQueries": totQueries,
       "totAnswers": totAnswers,
       "totAuthAns": totAuthAns,
       "totAuthNoNames": totAuthNoNames,
       "totAuthNoDataResps": totAuthNoDataResps,
       "totNonAuthDatas": totNonAuthDatas,
       "totNonAuthNoDatas": totNonAuthNoDatas,
       "totReqRefusals": totReqRefusals,
       "totReqUnparses": totReqUnparses,
       "totOtherErrors": totOtherErrors,
       "aRecQueries": aRecQueries,
       "nsRecQueries": nsRecQueries,
       "mxRecQueries": mxRecQueries,
       "soaRecQueries": soaRecQueries,
       "cnameRecQueries": cnameRecQueries,
       "totUnsupportedQueries": totUnsupportedQueries,
       "dnsServerConfig": dnsServerConfig,
       "dnsServerRecursion": dnsServerRecursion,
       "dnsServerZoneTable": dnsServerZoneTable,
       "dnsServerZoneEntry": dnsServerZoneEntry,
       "zoneIndex": zoneIndex,
       "zoneName": zoneName,
       "globalServerLB": globalServerLB,
       "gslbStatistics": gslbStatistics,
       "gslbDomainStatsTable": gslbDomainStatsTable,
       "gslbDomainStatsEntry": gslbDomainStatsEntry,
       "gslbDomainIndex": gslbDomainIndex,
       "domainname": domainname,
       "gslbDomainQueries": gslbDomainQueries,
       "gslbConfig": gslbConfig,
       "gslbDomainConfigTable": gslbDomainConfigTable,
       "gslbDomainConfigEntry": gslbDomainConfigEntry,
       "gslbcDomainIndex": gslbcDomainIndex,
       "gslbcDomainName": gslbcDomainName,
       "gslbVipName": gslbVipName,
       "reOrderInterval": reOrderInterval,
       "pq": pq,
       "pqstatistics": pqstatistics,
       "pqStatsperLBVipTable": pqStatsperLBVipTable,
       "pqStatsperLBVipEntry": pqStatsperLBVipEntry,
       "pqDevno": pqDevno,
       "totclienttransactiontime": totclienttransactiontime,
       "totclienttransaction": totclienttransaction,
       "dropped": dropped,
       "qdepth": qdepth,
       "pqStatsperpqpolicyandperLBVipTable": pqStatsperpqpolicyandperLBVipTable,
       "pqStatsperpqpolicyandperLBVipEntry": pqStatsperpqpolicyandperLBVipEntry,
       "pqvsdevno": pqvsdevno,
       "pqpoldevno": pqpoldevno,
       "pqtotclienttransactiontime": pqtotclienttransactiontime,
       "pqtotclienttransaction": pqtotclienttransaction,
       "pqDropped": pqDropped,
       "pqQdepth": pqQdepth,
       "pqconfig": pqconfig,
       "pqpolicyconfigTable": pqpolicyconfigTable,
       "pqpolicyconfigEntry": pqpolicyconfigEntry,
       "pqPolDevno": pqPolDevno,
       "pqpolicyname": pqpolicyname,
       "rulename": rulename,
       "qdepthThreshval": qdepthThreshval,
       "polqdepthThreshval": polqdepthThreshval,
       "priority": priority,
       "pqPolWeight": pqPolWeight,
       "dos": dos,
       "dosstatistics": dosstatistics,
       "dosservicestatsTable": dosservicestatsTable,
       "dosservicestatsEntry": dosservicestatsEntry,
       "dosDevno": dosDevno,
       "surgecnt": surgecnt,
       "dosqdepth": dosqdepth,
       "totaljstransaction": totaljstransaction,
       "dosconfig": dosconfig,
       "dospolicyconfigTable": dospolicyconfigTable,
       "dospolicyconfigEntry": dospolicyconfigEntry,
       "dosPolDevno": dosPolDevno,
       "dospolicyname": dospolicyname,
       "thresholdvalue": thresholdvalue,
       "ssloffloading": ssloffloading,
       "sslstatistics": sslstatistics,
       "sslglobalstats": sslglobalstats,
       "currSPS": currSPS,
       "sslV2TxCount": sslV2TxCount,
       "sslV3TxCount": sslV3TxCount,
       "tlsV1TxCount": tlsV1TxCount,
       "keyExRSA512": keyExRSA512,
       "keyExRSA1024": keyExRSA1024,
       "keyExDH512": keyExDH512,
       "keyExDH1024": keyExDH1024,
       "authRSA": authRSA,
       "authDH": authDH,
       "authDS": authDS,
       "cipher40BitRC4": cipher40BitRC4,
       "cipher56BitRC4": cipher56BitRC4,
       "cipher64BitRC4": cipher64BitRC4,
       "cipher128BitRC4": cipher128BitRC4,
       "cipher40BitDES": cipher40BitDES,
       "cipher56BitDES": cipher56BitDES,
       "cipher168Bit3DES": cipher168Bit3DES,
       "cipher40BitRC2": cipher40BitRC2,
       "cipher56BitRC2": cipher56BitRC2,
       "cipher128BitRC2": cipher128BitRC2,
       "cipher128BitIDEA": cipher128BitIDEA,
       "hashMD5": hashMD5,
       "hashSHA": hashSHA,
       "sslConfig": sslConfig,
       "certKeyTable": certKeyTable,
       "certKeyEntry": certKeyEntry,
       "certKeyId": certKeyId,
       "certKeyName": certKeyName,
       "certPath": certPath,
       "keyPath": keyPath,
       "inputFormat": inputFormat,
       "crlTable": crlTable,
       "crlEntry": crlEntry,
       "crlId": crlId,
       "crlName": crlName,
       "crlPath": crlPath,
       "crlInputFormat": crlInputFormat,
       "cipherGroupTable": cipherGroupTable,
       "cipherGroupEntry": cipherGroupEntry,
       "cipherGroupId": cipherGroupId,
       "cipherId": cipherId,
       "cipherGroupName": cipherGroupName,
       "cipherName": cipherName,
       "cipherDesc": cipherDesc,
       "advanceSSLConfigTable": advanceSSLConfigTable,
       "advanceSSLConfigEntry": advanceSSLConfigEntry,
       "id": id,
       "serviceName": serviceName,
       "dh": dh,
       "dhCount": dhCount,
       "dhFile": dhFile,
       "eRSA": eRSA,
       "eRSACount": eRSACount,
       "certHeader": certHeader,
       "certHeaderTag": certHeaderTag,
       "sessHeader": sessHeader,
       "sessHeaderTag": sessHeaderTag,
       "sslv2": sslv2,
       "sslv3": sslv3,
       "tlsv1": tlsv1,
       "owaSupport": owaSupport,
       "sslRedirect": sslRedirect,
       "clearTextPort": clearTextPort,
       "serviceType": serviceType,
       "certBindingConfigTable": certBindingConfigTable,
       "certBindingConfigEntry": certBindingConfigEntry,
       "certBindId": certBindId,
       "certKeyID": certKeyID,
       "certType": certType,
       "certBindServiceName": certBindServiceName,
       "certBindKeyName": certBindKeyName,
       "certBindServiceType": certBindServiceType,
       "cipherBindingConfigTable": cipherBindingConfigTable,
       "cipherBindingConfigEntry": cipherBindingConfigEntry,
       "cipherBindId": cipherBindId,
       "cipherID": cipherID,
       "cipherBindServiceName": cipherBindServiceName,
       "cipherbName": cipherbName,
       "cipherbDesc": cipherbDesc,
       "cipherBindServiceType": cipherBindServiceType,
       "cpe": cpe,
       "cpestatistics": cpestatistics,
       "cpestatspolicyTable": cpestatspolicyTable,
       "cpestatspolicyEntry": cpestatspolicyEntry,
       "cpesDevno": cpesDevno,
       "cpesPolicyname": cpesPolicyname,
       "cpesPolicyhits": cpesPolicyhits,
       "cpestatsactionTable": cpestatsactionTable,
       "cpestatsactionEntry": cpestatsactionEntry,
       "cpeaDevno": cpeaDevno,
       "actionname": actionname,
       "actionhits": actionhits,
       "cpeconfig": cpeconfig,
       "cpeconfigpolicyTable": cpeconfigpolicyTable,
       "cpeconfigpolicyEntry": cpeconfigpolicyEntry,
       "cpecDevno": cpecDevno,
       "cpecPolicyname": cpecPolicyname,
       "reqrule": reqrule,
       "reqaction": reqaction,
       "cpeconfigactionTable": cpeconfigactionTable,
       "cpeconfigactionEntry": cpeconfigactionEntry,
       "cpecaDevno": cpecaDevno,
       "cpecaActionname": cpecaActionname,
       "directive": directive,
       "qualifier": qualifier,
       "value": value,
       "page": page,
       "server": server,
       "cpeExprConfigStatsTable": cpeExprConfigStatsTable,
       "cpeExprConfigStatsEntry": cpeExprConfigStatsEntry,
       "cpeeIndex": cpeeIndex,
       "exprName": exprName,
       "cpeeQualifier": cpeeQualifier,
       "operator": operator,
       "hdrName": hdrName,
       "cpeeValue": cpeeValue,
       "length": length,
       "offset": offset,
       "cpeeNetmask": cpeeNetmask,
       "nsProducts": nsProducts,
       "rs9000": rs9000,
       "nsSysGroup": nsSysGroup,
       "sysBuildVersion": sysBuildVersion,
       "sysIpAddress": sysIpAddress,
       "sysNetmask": sysNetmask,
       "sysMappedIpAddress": sysMappedIpAddress,
       "sysMappedIpAddressRange": sysMappedIpAddressRange,
       "sysHighAvailabilityMode": sysHighAvailabilityMode,
       "sysGateway": sysGateway,
       "sysCurMappedIpCount": sysCurMappedIpCount,
       "sysCustomID": sysCustomID,
       "sysHardwareVersionId": sysHardwareVersionId,
       "sysHardwareVersionDesc": sysHardwareVersionDesc,
       "sysTotConfigChanges": sysTotConfigChanges,
       "sysTotSaveConfigs": sysTotSaveConfigs,
       "sysHardwareSerialNumber": sysHardwareSerialNumber,
       "sysHardwareEncodedSerialNumber": sysHardwareEncodedSerialNumber,
       "nsFeatureInfo": nsFeatureInfo,
       "featureWebLogging": featureWebLogging,
       "featureSurgeProtection": featureSurgeProtection,
       "featureLoadBalancing": featureLoadBalancing,
       "featureContentSwitching": featureContentSwitching,
       "featureCacheRedirection": featureCacheRedirection,
       "featureSureConnect": featureSureConnect,
       "featureCompression": featureCompression,
       "featurePriorityQueuing": featurePriorityQueuing,
       "featureSslOffloading": featureSslOffloading,
       "featureGslb": featureGslb,
       "featureHttpDosProtection": featureHttpDosProtection,
       "featureDynamicRouting": featureDynamicRouting,
       "featureContentFiltering": featureContentFiltering,
       "featureInternalCaching": featureInternalCaching,
       "featureSSLVPN": featureSSLVPN,
       "featureOSPF": featureOSPF,
       "featureRIP": featureRIP,
       "featureBGP": featureBGP,
       "featureRewrite": featureRewrite,
       "featureDeltaCompression": featureDeltaCompression,
       "featureGSLBProximity": featureGSLBProximity,
       "featureIPv6ProtocolTranslation": featureIPv6ProtocolTranslation,
       "featureApplicationFirewall": featureApplicationFirewall,
       "featureResponder": featureResponder,
       "featureHtmlInjection": featureHtmlInjection,
       "featureAGEE": featureAGEE,
       "featureAAA": featureAAA,
       "featurePLATFORM": featurePLATFORM,
       "nsModeInfo": nsModeInfo,
       "modeFastRamp": modeFastRamp,
       "l2Mode": l2Mode,
       "modeUseSrcIp": modeUseSrcIp,
       "modeClientKeepAlive": modeClientKeepAlive,
       "modeTcpBuffering": modeTcpBuffering,
       "modeMacBasedForwarding": modeMacBasedForwarding,
       "modeUseSubnetIp": modeUseSubnetIp,
       "modeEdgeConfiguration": modeEdgeConfiguration,
       "l3mode": l3mode,
       "modePathMTUDiscovery": modePathMTUDiscovery,
       "modeStaticRouteAdv": modeStaticRouteAdv,
       "modeDirectRouteAdv": modeDirectRouteAdv,
       "modeIntranetRouteAdv": modeIntranetRouteAdv,
       "brgBpdu": brgBpdu,
       "modeIpv6StaticRouteAdv": modeIpv6StaticRouteAdv,
       "modeIpv6DirectRouteAdv": modeIpv6DirectRouteAdv,
       "nsFiltersGroup": nsFiltersGroup,
       "aclStatsGroup": aclStatsGroup,
       "aclTotPktsBridgedLow": aclTotPktsBridgedLow,
       "aclTotPktsBridgedHigh": aclTotPktsBridgedHigh,
       "aclTotPktsDeniedLow": aclTotPktsDeniedLow,
       "aclTotPktsDeniedHigh": aclTotPktsDeniedHigh,
       "aclTotPktsAllowedLow": aclTotPktsAllowedLow,
       "aclTotPktsAllowedHigh": aclTotPktsAllowedHigh,
       "aclTotPktsReusedLow": aclTotPktsReusedLow,
       "aclTotPktsReusedHigh": aclTotPktsReusedHigh,
       "aclTotPktsBridged": aclTotPktsBridged,
       "aclTotPktsDenied": aclTotPktsDenied,
       "aclTotPktsAllowed": aclTotPktsAllowed,
       "aclTotHits": aclTotHits,
       "aclTotMisses": aclTotMisses,
       "aclTotPktsNAT": aclTotPktsNAT,
       "nsAclTable": nsAclTable,
       "nsAclEntry": nsAclEntry,
       "aclName": aclName,
       "aclPriority": aclPriority,
       "aclHits": aclHits,
       "aclperHits": aclperHits,
       "aclFullName": aclFullName,
       "contentFiltersTable": contentFiltersTable,
       "contentFiltersEntry": contentFiltersEntry,
       "contentFilterName": contentFilterName,
       "contentFilterHitsLow": contentFilterHitsLow,
       "contentFilterHitsHigh": contentFilterHitsHigh,
       "contentFilterHits": contentFilterHits,
       "saclStatsGroup": saclStatsGroup,
       "saclTotPktsBridged": saclTotPktsBridged,
       "saclTotPktsDenied": saclTotPktsDenied,
       "saclTotPktsAllowed": saclTotPktsAllowed,
       "saclTotHits": saclTotHits,
       "saclTotMisses": saclTotMisses,
       "saclsCount": saclsCount,
       "acl6StatsGroup": acl6StatsGroup,
       "nsAcl6Table": nsAcl6Table,
       "nsAcl6Entry": nsAcl6Entry,
       "acAclName": acAclName,
       "acl6Priority": acl6Priority,
       "acl6perHits": acl6perHits,
       "acl6FullName": acl6FullName,
       "acl6TotPktsBridged": acl6TotPktsBridged,
       "acl6TotPktsDenied": acl6TotPktsDenied,
       "acl6TotPktsAllowed": acl6TotPktsAllowed,
       "acl6TotPktsNAT": acl6TotPktsNAT,
       "acl6TotHits": acl6TotHits,
       "acl6TotMisses": acl6TotMisses,
       "pbrStatsGroup": pbrStatsGroup,
       "nsPbrTable": nsPbrTable,
       "nsPbrEntry": nsPbrEntry,
       "pbrName": pbrName,
       "pbrFullName": pbrFullName,
       "pbrPriority": pbrPriority,
       "pbrperHits": pbrperHits,
       "pbrTotPktsAllowed": pbrTotPktsAllowed,
       "pbrTotPktsDenied": pbrTotPktsDenied,
       "pbrTotHits": pbrTotHits,
       "pbrTotMisses": pbrTotMisses,
       "nsHighAvailabilityGroup": nsHighAvailabilityGroup,
       "haPeerId": haPeerId,
       "haPeerIpAddress": haPeerIpAddress,
       "haPeerState": haPeerState,
       "haTotStateTransitions": haTotStateTransitions,
       "haTimeofLastStateTransition": haTimeofLastStateTransition,
       "haTotStateFail": haTotStateFail,
       "haErrSyncFailure": haErrSyncFailure,
       "haErrTotNodeDown": haErrTotNodeDown,
       "haErrPropMemFail": haErrPropMemFail,
       "haErrNsbMemFail": haErrNsbMemFail,
       "haErrPortSilent": haErrPortSilent,
       "haTotTimerRecoveries": haTotTimerRecoveries,
       "haErrSwMonitorFail": haErrSwMonitorFail,
       "haNicsMonitorFailed": haNicsMonitorFailed,
       "haLastMasterStateTransitionReason": haLastMasterStateTransitionReason,
       "haPeerSystemState": haPeerSystemState,
       "haErrPropTimeout": haErrPropTimeout,
       "haCurDerivedInc": haCurDerivedInc,
       "haCurPeerInc": haCurPeerInc,
       "haErrMasterDispute": haErrMasterDispute,
       "haTotPktTx": haTotPktTx,
       "haTotPktRx": haTotPktRx,
       "haCurStatus": haCurStatus,
       "haCurState": haCurState,
       "haPeerInetAddrType": haPeerInetAddrType,
       "haPeerInetAddr": haPeerInetAddr,
       "vlanTable": vlanTable,
       "vlanEntry": vlanEntry,
       "vlanId": vlanId,
       "vlanMemberInterfaces": vlanMemberInterfaces,
       "vlanTaggedInterfaces": vlanTaggedInterfaces,
       "vlanTotRxPktsLow": vlanTotRxPktsLow,
       "vlanTotRxPktsHigh": vlanTotRxPktsHigh,
       "vlanTotRxBytesLow": vlanTotRxBytesLow,
       "vlanTotRxBytesHigh": vlanTotRxBytesHigh,
       "vlanTotTxPktsLow": vlanTotTxPktsLow,
       "vlanTotTxPktsHigh": vlanTotTxPktsHigh,
       "vlanTotTxBytesLow": vlanTotTxBytesLow,
       "vlanTotTxBytesHigh": vlanTotTxBytesHigh,
       "vlanTotDroppedPktsLow": vlanTotDroppedPktsLow,
       "vlanTotDroppedPktsHigh": vlanTotDroppedPktsHigh,
       "vlanTotBroadcastPktsLow": vlanTotBroadcastPktsLow,
       "vlanTotBroadcastPktsHigh": vlanTotBroadcastPktsHigh,
       "vlanTotRxPkts": vlanTotRxPkts,
       "vlanTotRxBytes": vlanTotRxBytes,
       "vlanTotTxPkts": vlanTotTxPkts,
       "vlanTotTxBytes": vlanTotTxBytes,
       "vlanTotDroppedPkts": vlanTotDroppedPkts,
       "vlanTotBroadcastPkts": vlanTotBroadcastPkts,
       "vlanBindIpAddress": vlanBindIpAddress,
       "vlanBindIpNetmask": vlanBindIpNetmask,
       "vlanBridgeGroup": vlanBridgeGroup,
       "nsIpAddrTable": nsIpAddrTable,
       "nsIpAddrEntry": nsIpAddrEntry,
       "ipAddr": ipAddr,
       "ipNetmask": ipNetmask,
       "ipType": ipType,
       "ipMode": ipMode,
       "ipFreePorts": ipFreePorts,
       "ipVlan": ipVlan,
       "ipBridgeGroup": ipBridgeGroup,
       "nsResourceGroup": nsResourceGroup,
       "resCpuUsage": resCpuUsage,
       "resMemUsage": resMemUsage,
       "numCPUs": numCPUs,
       "memSizeMB": memSizeMB,
       "numSSLCards": numSSLCards,
       "nsCPUTable": nsCPUTable,
       "nsCPUEntry": nsCPUEntry,
       "nsCPUname": nsCPUname,
       "nsCPUusage": nsCPUusage,
       "nsSysHealthTable": nsSysHealthTable,
       "nsSysHealthEntry": nsSysHealthEntry,
       "sysHealthCounterName": sysHealthCounterName,
       "sysHealthCounterValue": sysHealthCounterValue,
       "nsSysHealthDiskTable": nsSysHealthDiskTable,
       "nsSysHealthDiskEntry": nsSysHealthDiskEntry,
       "sysHealthDiskName": sysHealthDiskName,
       "sysHealthDiskSize": sysHealthDiskSize,
       "sysHealthDiskAvail": sysHealthDiskAvail,
       "sysHealthDiskUsed": sysHealthDiskUsed,
       "sysHealthDiskPerusage": sysHealthDiskPerusage,
       "cpuSpeedMHz": cpuSpeedMHz,
       "numPEs": numPEs,
       "nsIpStatsGroup": nsIpStatsGroup,
       "ipTotRxPktsLow": ipTotRxPktsLow,
       "ipTotRxPktsHigh": ipTotRxPktsHigh,
       "ipTotRxBytesLow": ipTotRxBytesLow,
       "ipTotRxBytesHigh": ipTotRxBytesHigh,
       "ipTotRxMbitsLow": ipTotRxMbitsLow,
       "ipTotRxMbitsHigh": ipTotRxMbitsHigh,
       "ipTotTxPktsLow": ipTotTxPktsLow,
       "ipTotTxPktsHigh": ipTotTxPktsHigh,
       "ipTotTxBytesLow": ipTotTxBytesLow,
       "ipTotTxBytesHigh": ipTotTxBytesHigh,
       "ipTotTxMbitsLow": ipTotTxMbitsLow,
       "ipTotTxMbitsHigh": ipTotTxMbitsHigh,
       "ipTotFragmentsLow": ipTotFragmentsLow,
       "ipTotFragmentsHigh": ipTotFragmentsHigh,
       "ipTotBadlensLow": ipTotBadlensLow,
       "ipTotBadlensHigh": ipTotBadlensHigh,
       "ipTotBadMacAddrsLow": ipTotBadMacAddrsLow,
       "ipTotBadMacAddrsHigh": ipTotBadMacAddrsHigh,
       "ipTotMaxClientsLow": ipTotMaxClientsLow,
       "ipTotMaxClientsHigh": ipTotMaxClientsHigh,
       "ipTotUnknownSvcsLow": ipTotUnknownSvcsLow,
       "ipTotUnknownSvcsHigh": ipTotUnknownSvcsHigh,
       "ipTotLandattacksLow": ipTotLandattacksLow,
       "ipTotLandattacksHigh": ipTotLandattacksHigh,
       "ipTotRxPkts": ipTotRxPkts,
       "ipTotRxBytes": ipTotRxBytes,
       "ipTotRxMbits": ipTotRxMbits,
       "ipTotTxPkts": ipTotTxPkts,
       "ipTotTxBytes": ipTotTxBytes,
       "ipTotTxMbits": ipTotTxMbits,
       "ipTotFragments": ipTotFragments,
       "ipTotBadlens": ipTotBadlens,
       "ipTotBadMacAddrs": ipTotBadMacAddrs,
       "ipTotMaxClients": ipTotMaxClients,
       "ipTotUnknownSvcs": ipTotUnknownSvcs,
       "ipTotLandattacks": ipTotLandattacks,
       "ipTotBadChecksums": ipTotBadChecksums,
       "ipTotReassemblyAttempt": ipTotReassemblyAttempt,
       "ipTotSuccReassembly": ipTotSuccReassembly,
       "ipTotUnsuccReassembly": ipTotUnsuccReassembly,
       "ipTotTooBig": ipTotTooBig,
       "ipTotZeroFragmentLen": ipTotZeroFragmentLen,
       "ipTotDupFragments": ipTotDupFragments,
       "ipTotOutOfOrderFrag": ipTotOutOfOrderFrag,
       "ipTotUnknownDstRcvd": ipTotUnknownDstRcvd,
       "ipTotBadTransport": ipTotBadTransport,
       "ipTotVIPDown": ipTotVIPDown,
       "ipTotFixHeaderFail": ipTotFixHeaderFail,
       "ipTotAddrLookup": ipTotAddrLookup,
       "ipTotAddrLookupFail": ipTotAddrLookupFail,
       "ipTotUDPfragmentsFwd": ipTotUDPfragmentsFwd,
       "ipTotTCPfragmentsFwd": ipTotTCPfragmentsFwd,
       "ipTotFragPktsGen": ipTotFragPktsGen,
       "ipTotInvalidHeaderSz": ipTotInvalidHeaderSz,
       "ipTotInvalidPacketSize": ipTotInvalidPacketSize,
       "ipTotTruncatedPackets": ipTotTruncatedPackets,
       "ipTotZeroNextHop": ipTotZeroNextHop,
       "ipTotTtlExpired": ipTotTtlExpired,
       "nonIpTotTruncatedPackets": nonIpTotTruncatedPackets,
       "nsIcmpStatsGroup": nsIcmpStatsGroup,
       "icmpTotRxPktsLow": icmpTotRxPktsLow,
       "icmpTotRxPktsHigh": icmpTotRxPktsHigh,
       "icmpTotRxBytesLow": icmpTotRxBytesLow,
       "icmpTotRxBytesHigh": icmpTotRxBytesHigh,
       "icmpTotTxPktsLow": icmpTotTxPktsLow,
       "icmpTotTxPktsHigh": icmpTotTxPktsHigh,
       "icmpTotTxBytesLow": icmpTotTxBytesLow,
       "icmpTotTxBytesHigh": icmpTotTxBytesHigh,
       "icmpTotRxEchoReplyLow": icmpTotRxEchoReplyLow,
       "icmpTotRxEchoReplyHigh": icmpTotRxEchoReplyHigh,
       "icmpTotTxEchoReplyLow": icmpTotTxEchoReplyLow,
       "icmpTotTxEchoReplyHigh": icmpTotTxEchoReplyHigh,
       "icmpTotRxEchoLow": icmpTotRxEchoLow,
       "icmpTotRxEchoHigh": icmpTotRxEchoHigh,
       "icmpTotPktsDroppedLow": icmpTotPktsDroppedLow,
       "icmpTotPktsDroppedHigh": icmpTotPktsDroppedHigh,
       "icmpCurRateThreshold": icmpCurRateThreshold,
       "icmpCurRateThresholdInterval": icmpCurRateThresholdInterval,
       "icmpCurRateCounter": icmpCurRateCounter,
       "icmpTotThresholdExceedsLow": icmpTotThresholdExceedsLow,
       "icmpTotThresholdExceedsHigh": icmpTotThresholdExceedsHigh,
       "icmpTotRxPkts": icmpTotRxPkts,
       "icmpTotRxBytes": icmpTotRxBytes,
       "icmpTotTxPkts": icmpTotTxPkts,
       "icmpTotTxBytes": icmpTotTxBytes,
       "icmpTotRxEchoReply": icmpTotRxEchoReply,
       "icmpTotTxEchoReply": icmpTotTxEchoReply,
       "icmpTotRxEcho": icmpTotRxEcho,
       "icmpTotPktsDropped": icmpTotPktsDropped,
       "icmpTotThresholdExceeds": icmpTotThresholdExceeds,
       "icmpTotPortUnreachableRx": icmpTotPortUnreachableRx,
       "icmpTotPortUnreachableTx": icmpTotPortUnreachableTx,
       "icmpTotBadChecksum": icmpTotBadChecksum,
       "icmpTotNeedFragRx": icmpTotNeedFragRx,
       "icmpTotNonFirstIpFrag": icmpTotNonFirstIpFrag,
       "icmpTotInvalidBodyLen": icmpTotInvalidBodyLen,
       "icmpTotNoTcpConn": icmpTotNoTcpConn,
       "icmpTotNoUdpConn": icmpTotNoUdpConn,
       "icmpTotInvalidTcpSeqno": icmpTotInvalidTcpSeqno,
       "icmpTotInvalidNextMTUval": icmpTotInvalidNextMTUval,
       "icmpTotDstIpLookup": icmpTotDstIpLookup,
       "icmpTotBigNextMTU": icmpTotBigNextMTU,
       "icmpTotInvalidProtocol": icmpTotInvalidProtocol,
       "icmpTotBadPMTUIpChecksum": icmpTotBadPMTUIpChecksum,
       "icmpTotPMTUnoLink": icmpTotPMTUnoLink,
       "icmpTotPMTUDiscoveryDisabled": icmpTotPMTUDiscoveryDisabled,
       "nsUdpStatsGroup": nsUdpStatsGroup,
       "udpTotUnknownSvcPktsLow": udpTotUnknownSvcPktsLow,
       "udpTotUnknownSvcPktsHigh": udpTotUnknownSvcPktsHigh,
       "udpTotRxPktsLow": udpTotRxPktsLow,
       "udpTotRxPktsHigh": udpTotRxPktsHigh,
       "udpTotRxBytesLow": udpTotRxBytesLow,
       "udpTotRxBytesHigh": udpTotRxBytesHigh,
       "udpTotTxPktsLow": udpTotTxPktsLow,
       "udpTotTxPktsHigh": udpTotTxPktsHigh,
       "udpTotTxBytesLow": udpTotTxBytesLow,
       "udpTotTxBytesHigh": udpTotTxBytesHigh,
       "udpCurRateThreshold": udpCurRateThreshold,
       "udpRateInterval": udpRateInterval,
       "udpCurRateCounter": udpCurRateCounter,
       "udpCurRateThresholdExceedsLow": udpCurRateThresholdExceedsLow,
       "udpCurRateThresholdExceedsHigh": udpCurRateThresholdExceedsHigh,
       "udpTotUnknownSvcPkts": udpTotUnknownSvcPkts,
       "udpTotRxPkts": udpTotRxPkts,
       "udpTotRxBytes": udpTotRxBytes,
       "udpTotTxPkts": udpTotTxPkts,
       "udpTotTxBytes": udpTotTxBytes,
       "udpCurRateThresholdExceeds": udpCurRateThresholdExceeds,
       "udpBadChecksum": udpBadChecksum,
       "nsTcpStatsGroup": nsTcpStatsGroup,
       "tcpCurServerConn": tcpCurServerConn,
       "tcpCurClientConn": tcpCurClientConn,
       "tcpCurPendingConn": tcpCurPendingConn,
       "tcpCurResetCount": tcpCurResetCount,
       "tcpMaxServerConnections": tcpMaxServerConnections,
       "tcpMaxReqsperConn": tcpMaxReqsperConn,
       "tcpMaxPerSrvrReusePool": tcpMaxPerSrvrReusePool,
       "tcpActiveServerConn": tcpActiveServerConn,
       "tcpCurClientConnClosing": tcpCurClientConnClosing,
       "tcpCurServerConnEstablished": tcpCurServerConnEstablished,
       "tcpCurClientConnOpening": tcpCurClientConnOpening,
       "tcpCurClientConnEstablished": tcpCurClientConnEstablished,
       "tcpCurServerConnClosing": tcpCurServerConnClosing,
       "tcpSpareConn": tcpSpareConn,
       "tcpSurgeQueueLen": tcpSurgeQueueLen,
       "tcpCurServerConnOpening": tcpCurServerConnOpening,
       "tcpTotServerConnOpened": tcpTotServerConnOpened,
       "tcpTotServerConnClosed": tcpTotServerConnClosed,
       "tcpTotClientConnOpened": tcpTotClientConnOpened,
       "tcpTotClientConnClosed": tcpTotClientConnClosed,
       "tcpTotSyn": tcpTotSyn,
       "tcpTotSynProbe": tcpTotSynProbe,
       "tcpTotSvrFin": tcpTotSvrFin,
       "tcpTotCltFin": tcpTotCltFin,
       "tcpWaitToSyn": tcpWaitToSyn,
       "tcpTotZombieCltConnFlushed": tcpTotZombieCltConnFlushed,
       "tcpTotZombieSvrConnFlushed": tcpTotZombieSvrConnFlushed,
       "tcpTotZombieHalfOpenCltConnFlushed": tcpTotZombieHalfOpenCltConnFlushed,
       "tcpTotZombieHalfOpenSvrConnFlushed": tcpTotZombieHalfOpenSvrConnFlushed,
       "tcpTotZombieActiveHalfCloseCltConnFlushed": tcpTotZombieActiveHalfCloseCltConnFlushed,
       "tcpTotZombieActiveHalfCloseSvrConnFlushed": tcpTotZombieActiveHalfCloseSvrConnFlushed,
       "tcpTotZombiePassiveHalfCloseCltConnFlushed": tcpTotZombiePassiveHalfCloseCltConnFlushed,
       "tcpTotZombiePassiveHalfCloseSrvConnFlushed": tcpTotZombiePassiveHalfCloseSrvConnFlushed,
       "tcpErrBadCheckSum": tcpErrBadCheckSum,
       "tcpErrSynInSynRcvd": tcpErrSynInSynRcvd,
       "tcpErrSynInEst": tcpErrSynInEst,
       "tcpErrSynGiveUp": tcpErrSynGiveUp,
       "tcpErrSynSentBadAck": tcpErrSynSentBadAck,
       "tcpErrSynRetry": tcpErrSynRetry,
       "tcpErrFinRetry": tcpErrFinRetry,
       "tcpErrFinGiveUp": tcpErrFinGiveUp,
       "tcpErrFinDup": tcpErrFinDup,
       "tcpErrRst": tcpErrRst,
       "tcpErrRstNonEst": tcpErrRstNonEst,
       "tcpErrRstOutOfWindow": tcpErrRstOutOfWindow,
       "tcpErrRstInTimewait": tcpErrRstInTimewait,
       "tcpErrSvrRetrasmit": tcpErrSvrRetrasmit,
       "tcpErrCltRetrasmit": tcpErrCltRetrasmit,
       "tcpErrFullRetrasmit": tcpErrFullRetrasmit,
       "tcpErrPartialRetrasmit": tcpErrPartialRetrasmit,
       "tcpErrSvrOutOfOrder": tcpErrSvrOutOfOrder,
       "tcpErrCltOutOfOrder": tcpErrCltOutOfOrder,
       "tcpErrCltHole": tcpErrCltHole,
       "tcpErrSvrHole": tcpErrSvrHole,
       "tcpErrCookiePktSeqReject": tcpErrCookiePktSeqReject,
       "tcpErrCookiePktSigReject": tcpErrCookiePktSigReject,
       "tcpErrCookiePktSeqDrop": tcpErrCookiePktSeqDrop,
       "tcpErrCookiePktMssReject": tcpErrCookiePktMssReject,
       "tcpErrRetransmit": tcpErrRetransmit,
       "tcpErrRetransmitGiveUp": tcpErrRetransmitGiveUp,
       "tcpTotRxPkts": tcpTotRxPkts,
       "tcpTotRxBytes": tcpTotRxBytes,
       "tcpTotTxPkts": tcpTotTxPkts,
       "tcpTotTxBytes": tcpTotTxBytes,
       "pcbTotZombieCall": pcbTotZombieCall,
       "tcpTotSynHeld": tcpTotSynHeld,
       "tcpTotSynFlush": tcpTotSynFlush,
       "tcpTotFinWaitClosed": tcpTotFinWaitClosed,
       "tcpErrAnyPortFail": tcpErrAnyPortFail,
       "tcpErrIpPortFail": tcpErrIpPortFail,
       "tcpErrSentRst": tcpErrSentRst,
       "tcpErrBadStateConn": tcpErrBadStateConn,
       "tcpErrFastRetransmissions": tcpErrFastRetransmissions,
       "tcpErrFirstRetransmissions": tcpErrFirstRetransmissions,
       "tcpErrSecondRetransmissions": tcpErrSecondRetransmissions,
       "tcpErrThirdRetransmissions": tcpErrThirdRetransmissions,
       "tcpErrForthRetransmissions": tcpErrForthRetransmissions,
       "tcpErrFifthRetransmissions": tcpErrFifthRetransmissions,
       "tcpErrSixthRetransmissions": tcpErrSixthRetransmissions,
       "tcpErrSeventhRetransmissions": tcpErrSeventhRetransmissions,
       "tcpErrDataAfterFin": tcpErrDataAfterFin,
       "tcpErrRstThreshold": tcpErrRstThreshold,
       "tcpErrOutOfWindowPkts": tcpErrOutOfWindowPkts,
       "tcpErrSynDroppedCongestion": tcpErrSynDroppedCongestion,
       "tcpCurPhysicalServers": tcpCurPhysicalServers,
       "tcpReuseHit": tcpReuseHit,
       "tcpWaitToData": tcpWaitToData,
       "tcpErrStrayPkt": tcpErrStrayPkt,
       "tcpTotClientConnOpenRate": tcpTotClientConnOpenRate,
       "nsSslStatsGroup": nsSslStatsGroup,
       "sslCardStatus": sslCardStatus,
       "sslEngineStatus": sslEngineStatus,
       "sslSessionsPerSec": sslSessionsPerSec,
       "sslTotTransactionsLow": sslTotTransactionsLow,
       "sslTotTransactionsHigh": sslTotTransactionsHigh,
       "sslTotSSLv2TransactionsLow": sslTotSSLv2TransactionsLow,
       "sslTotSSLv2TransactionsHigh": sslTotSSLv2TransactionsHigh,
       "sslTotSSLv3TransactionsLow": sslTotSSLv3TransactionsLow,
       "sslTotSSLv3TransactionsHigh": sslTotSSLv3TransactionsHigh,
       "sslTotTLSv1TransactionsLow": sslTotTLSv1TransactionsLow,
       "sslTotTLSv1TransactionsHigh": sslTotTLSv1TransactionsHigh,
       "sslTotSessionsLow": sslTotSessionsLow,
       "sslTotSessionsHigh": sslTotSessionsHigh,
       "sslTotSSLv2SessionsLow": sslTotSSLv2SessionsLow,
       "sslTotSSLv2SessionsHigh": sslTotSSLv2SessionsHigh,
       "sslTotSSLv3SessionsLow": sslTotSSLv3SessionsLow,
       "sslTotSSLv3SessionsHigh": sslTotSSLv3SessionsHigh,
       "sslTotTLSv1SessionsLow": sslTotTLSv1SessionsLow,
       "sslTotTLSv1SessionsHigh": sslTotTLSv1SessionsHigh,
       "sslTotExpiredSessionsLow": sslTotExpiredSessionsLow,
       "sslTotExpiredSessionsHigh": sslTotExpiredSessionsHigh,
       "sslTotNewSessionsLow": sslTotNewSessionsLow,
       "sslTotNewSessionsHigh": sslTotNewSessionsHigh,
       "sslTotSessionHitsLow": sslTotSessionHitsLow,
       "sslTotSessionHitsHigh": sslTotSessionHitsHigh,
       "sslTotSessionMissLow": sslTotSessionMissLow,
       "sslTotSessionMissHigh": sslTotSessionMissHigh,
       "sslTotRenegSessionsLow": sslTotRenegSessionsLow,
       "sslTotRenegSessionsHigh": sslTotRenegSessionsHigh,
       "sslTotSSLv3RenegSessionsLow": sslTotSSLv3RenegSessionsLow,
       "sslTotSSLv3RenegSessionsHigh": sslTotSSLv3RenegSessionsHigh,
       "sslTotTLSv1RenegSessionsLow": sslTotTLSv1RenegSessionsLow,
       "sslTotTLSv1RenegSessionsHigh": sslTotTLSv1RenegSessionsHigh,
       "sslTotSSLv2HandshakesLow": sslTotSSLv2HandshakesLow,
       "sslTotSSLv2HandshakesHigh": sslTotSSLv2HandshakesHigh,
       "sslTotSSLv3HandshakesLow": sslTotSSLv3HandshakesLow,
       "sslTotSSLv3HandshakesHigh": sslTotSSLv3HandshakesHigh,
       "sslTotTLSv1HandshakesLow": sslTotTLSv1HandshakesLow,
       "sslTotTLSv1HandshakesHigh": sslTotTLSv1HandshakesHigh,
       "sslTotSSLv2ClientAuthenticationsLow": sslTotSSLv2ClientAuthenticationsLow,
       "sslTotSSLv2ClientAuthenticationsHigh": sslTotSSLv2ClientAuthenticationsHigh,
       "sslTotSSLv3ClientAuthenticationsLow": sslTotSSLv3ClientAuthenticationsLow,
       "sslTotSSLv3ClientAuthenticationsHigh": sslTotSSLv3ClientAuthenticationsHigh,
       "sslTotTLSv1ClientAuthenticationsLow": sslTotTLSv1ClientAuthenticationsLow,
       "sslTotTLSv1ClientAuthenticationsHigh": sslTotTLSv1ClientAuthenticationsHigh,
       "sslTotRSA512keyExchangesLow": sslTotRSA512keyExchangesLow,
       "sslTotRSA512keyExchangesHigh": sslTotRSA512keyExchangesHigh,
       "sslTotRSA1024keyExchangesLow": sslTotRSA1024keyExchangesLow,
       "sslTotRSA1024keyExchangesHigh": sslTotRSA1024keyExchangesHigh,
       "sslTotRSA2048keyExchangesLow": sslTotRSA2048keyExchangesLow,
       "sslTotRSA2048keyExchangesHigh": sslTotRSA2048keyExchangesHigh,
       "sslTotDH512keyExchangesLow": sslTotDH512keyExchangesLow,
       "sslTotDH512keyExchangesHigh": sslTotDH512keyExchangesHigh,
       "sslTotDH1024keyExchangesLow": sslTotDH1024keyExchangesLow,
       "sslTotDH1024keyExchangesHigh": sslTotDH1024keyExchangesHigh,
       "sslTotDH2048keyExchangesLow": sslTotDH2048keyExchangesLow,
       "sslTotDH2048keyExchangesHigh": sslTotDH2048keyExchangesHigh,
       "sslTotRSAAuthorizationsLow": sslTotRSAAuthorizationsLow,
       "sslTotRSAAuthorizationsHigh": sslTotRSAAuthorizationsHigh,
       "sslTotDHAuthorizationsLow": sslTotDHAuthorizationsLow,
       "sslTotDHAuthorizationsHigh": sslTotDHAuthorizationsHigh,
       "sslTotDSSAuthorizationsLow": sslTotDSSAuthorizationsLow,
       "sslTotDSSAuthorizationsHigh": sslTotDSSAuthorizationsHigh,
       "sslTotNULLAuthorizationsLow": sslTotNULLAuthorizationsLow,
       "sslTotNULLAuthorizationsHigh": sslTotNULLAuthorizationsHigh,
       "sslTot40BitRC4CiphersLow": sslTot40BitRC4CiphersLow,
       "sslTot40BitRC4CiphersHigh": sslTot40BitRC4CiphersHigh,
       "sslTot56BitRC4CiphersLow": sslTot56BitRC4CiphersLow,
       "sslTot56BitRC4CiphersHigh": sslTot56BitRC4CiphersHigh,
       "sslTot64BitRC4CiphersLow": sslTot64BitRC4CiphersLow,
       "sslTot64BitRC4CiphersHigh": sslTot64BitRC4CiphersHigh,
       "sslTot128BitRC4CiphersLow": sslTot128BitRC4CiphersLow,
       "sslTot128BitRC4CiphersHigh": sslTot128BitRC4CiphersHigh,
       "sslTot40BitDESCiphersLow": sslTot40BitDESCiphersLow,
       "sslTot40BitDESCiphersHigh": sslTot40BitDESCiphersHigh,
       "sslTot56BitDESCiphersLow": sslTot56BitDESCiphersLow,
       "sslTot56BitDESCiphersHigh": sslTot56BitDESCiphersHigh,
       "sslTot168Bit3DESCiphersLow": sslTot168Bit3DESCiphersLow,
       "sslTot168Bit3DESCiphersHigh": sslTot168Bit3DESCiphersHigh,
       "sslTot40BitRC2CiphersLow": sslTot40BitRC2CiphersLow,
       "sslTot40BitRC2CiphersHigh": sslTot40BitRC2CiphersHigh,
       "sslTot56BitRC2CiphersLow": sslTot56BitRC2CiphersLow,
       "sslTot56BitRC2CiphersHigh": sslTot56BitRC2CiphersHigh,
       "sslTot128BitRC2CiphersLow": sslTot128BitRC2CiphersLow,
       "sslTot128BitRC2CiphersHigh": sslTot128BitRC2CiphersHigh,
       "sslTot128BitIDEACiphersLow": sslTot128BitIDEACiphersLow,
       "sslTot128BitIDEACiphersHigh": sslTot128BitIDEACiphersHigh,
       "sslTotNULLCiphersLow": sslTotNULLCiphersLow,
       "sslTotNULLCiphersHigh": sslTotNULLCiphersHigh,
       "sslTotMD5MacLow": sslTotMD5MacLow,
       "sslTotMD5MacHigh": sslTotMD5MacHigh,
       "sslTotSHAMacLow": sslTotSHAMacLow,
       "sslTotSHAMacHigh": sslTotSHAMacHigh,
       "sslTotOffloadBulkDESLow": sslTotOffloadBulkDESLow,
       "sslTotOffloadBulkDESHigh": sslTotOffloadBulkDESHigh,
       "sslTotOffloadRSAKeyExchangesLow": sslTotOffloadRSAKeyExchangesLow,
       "sslTotOffloadRSAKeyExchangesHigh": sslTotOffloadRSAKeyExchangesHigh,
       "sslTotOffloadDHKeyExchangesLow": sslTotOffloadDHKeyExchangesLow,
       "sslTotOffloadDHKeyExchangesHigh": sslTotOffloadDHKeyExchangesHigh,
       "sslTotOffloadSignRSALow": sslTotOffloadSignRSALow,
       "sslTotOffloadSignRSAHigh": sslTotOffloadSignRSAHigh,
       "sslBeTotSessionsLow": sslBeTotSessionsLow,
       "sslBeTotSessionsHigh": sslBeTotSessionsHigh,
       "sslBeTotSSLv3SessionsLow": sslBeTotSSLv3SessionsLow,
       "sslBeTotSSLv3SessionsHigh": sslBeTotSSLv3SessionsHigh,
       "sslBeTotTLSv1SessionsLow": sslBeTotTLSv1SessionsLow,
       "sslBeTotTLSv1SessionsHigh": sslBeTotTLSv1SessionsHigh,
       "sslBeExpiredSessionsLow": sslBeExpiredSessionsLow,
       "sslBeTotExpiredSessionsHigh": sslBeTotExpiredSessionsHigh,
       "sslBeTotSessionMultiplexAttemptsLow": sslBeTotSessionMultiplexAttemptsLow,
       "sslBeTotSessionMultiplexAttemptsHigh": sslBeTotSessionMultiplexAttemptsHigh,
       "sslBeTotSessionMultiplexAttemptSuccessLow": sslBeTotSessionMultiplexAttemptSuccessLow,
       "sslBeTotSessionMultiplexAttemptSuccessHigh": sslBeTotSessionMultiplexAttemptSuccessHigh,
       "sslBeTotSessionMultiplexAttemptFailsLow": sslBeTotSessionMultiplexAttemptFailsLow,
       "sslBeTotSessionMultiplexAttemptFailsHigh": sslBeTotSessionMultiplexAttemptFailsHigh,
       "sslBeMaxMultiplexedSessionsLow": sslBeMaxMultiplexedSessionsLow,
       "sslBeMaxMultiplexedSessionsHigh": sslBeMaxMultiplexedSessionsHigh,
       "sslBeSessionsReplacedLow": sslBeSessionsReplacedLow,
       "sslBeSessionsReplacedHigh": sslBeSessionsReplacedHigh,
       "sslBeTotSSLv3HandshakesLow": sslBeTotSSLv3HandshakesLow,
       "sslBeTotSSLv3HandshakesHigh": sslBeTotSSLv3HandshakesHigh,
       "sslBeTotTLSv1HandshakesLow": sslBeTotTLSv1HandshakesLow,
       "sslBeTotTLSv1HandshakesHigh": sslBeTotTLSv1HandshakesHigh,
       "sslBeTotSSLv3ClientAuthenticationsLow": sslBeTotSSLv3ClientAuthenticationsLow,
       "sslBeTotSSLv3ClientAuthenticationsHigh": sslBeTotSSLv3ClientAuthenticationsHigh,
       "sslBeTotTLSv1ClientAuthenticationsLow": sslBeTotTLSv1ClientAuthenticationsLow,
       "sslBeTotTLSv1ClientAuthenticationsHigh": sslBeTotTLSv1ClientAuthenticationsHigh,
       "sslBeTotRSA512keyExchangesLow": sslBeTotRSA512keyExchangesLow,
       "sslBeTotRSA512keyExchangesHigh": sslBeTotRSA512keyExchangesHigh,
       "sslBeTotRSA1024keyExchangesLow": sslBeTotRSA1024keyExchangesLow,
       "sslBeTotRSA1024keyExchangesHigh": sslBeTotRSA1024keyExchangesHigh,
       "sslBeTotRSA2048keyExchangesLow": sslBeTotRSA2048keyExchangesLow,
       "sslBeTotRSA2048keyExchangesHigh": sslBeTotRSA2048keyExchangesHigh,
       "sslBeTotDH512keyExchangesLow": sslBeTotDH512keyExchangesLow,
       "sslBeTotDH512keyExchangesHigh": sslBeTotDH512keyExchangesHigh,
       "sslBeTotDH1024keyExchangesLow": sslBeTotDH1024keyExchangesLow,
       "sslBeTotDH1024keyExchangesHigh": sslBeTotDH1024keyExchangesHigh,
       "sslBeTotDH2048keyExchangesLow": sslBeTotDH2048keyExchangesLow,
       "sslBeTotDH2048keyExchangesHigh": sslBeTotDH2048keyExchangesHigh,
       "sslBeTotRSAAuthorizationsLow": sslBeTotRSAAuthorizationsLow,
       "sslBeTotRSAAuthorizationsHigh": sslBeTotRSAAuthorizationsHigh,
       "sslBeTotDHAuthorizationsLow": sslBeTotDHAuthorizationsLow,
       "sslBeTotDHAuthorizationsHigh": sslBeTotDHAuthorizationsHigh,
       "sslBeTotDSSAuthorizationsLow": sslBeTotDSSAuthorizationsLow,
       "sslBeTotDSSAuthorizationsHigh": sslBeTotDSSAuthorizationsHigh,
       "sslBeTotNULLAuthorizationsLow": sslBeTotNULLAuthorizationsLow,
       "sslBeTotNULLAuthorizationsHigh": sslBeTotNULLAuthorizationsHigh,
       "sslBeTot40BitRC4CiphersLow": sslBeTot40BitRC4CiphersLow,
       "sslBeTot40BitRC4CiphersHigh": sslBeTot40BitRC4CiphersHigh,
       "sslBeTot56BitRC4CiphersLow": sslBeTot56BitRC4CiphersLow,
       "sslBeTot56BitRC4CiphersHigh": sslBeTot56BitRC4CiphersHigh,
       "sslBeTot64BitRC4CiphersLow": sslBeTot64BitRC4CiphersLow,
       "sslBeTot64BitRC4CiphersHigh": sslBeTot64BitRC4CiphersHigh,
       "sslBeTot128BitRC4CiphersLow": sslBeTot128BitRC4CiphersLow,
       "sslBeTot128BitRC4CiphersHigh": sslBeTot128BitRC4CiphersHigh,
       "sslBeTot40BitDESCiphersLow": sslBeTot40BitDESCiphersLow,
       "sslBeTot40BitDESCiphersHigh": sslBeTot40BitDESCiphersHigh,
       "sslBeTot56BitDESCiphersLow": sslBeTot56BitDESCiphersLow,
       "sslBeTot56BitDESCiphersHigh": sslBeTot56BitDESCiphersHigh,
       "sslBeTot168Bit3DESCiphersLow": sslBeTot168Bit3DESCiphersLow,
       "sslBeTot168Bit3DESCiphersHigh": sslBeTot168Bit3DESCiphersHigh,
       "sslBeTot40BitRC2CiphersLow": sslBeTot40BitRC2CiphersLow,
       "sslBeTot40BitRC2CiphersHigh": sslBeTot40BitRC2CiphersHigh,
       "sslBeTot56BitRC2CiphersLow": sslBeTot56BitRC2CiphersLow,
       "sslBeTot56BitRC2CiphersHigh": sslBeTot56BitRC2CiphersHigh,
       "sslBeTot128BitRC2CiphersLow": sslBeTot128BitRC2CiphersLow,
       "sslBeTot128BitRC2CiphersHigh": sslBeTot128BitRC2CiphersHigh,
       "sslBeTot128BitIDEACiphersLow": sslBeTot128BitIDEACiphersLow,
       "sslBeTot128BitIDEACiphersHigh": sslBeTot128BitIDEACiphersHigh,
       "sslBeTotNULLCiphersLow": sslBeTotNULLCiphersLow,
       "sslBeTotNULLCiphersHigh": sslBeTotNULLCiphersHigh,
       "sslBeTotMD5MacLow": sslBeTotMD5MacLow,
       "sslBeTotMD5MacHigh": sslBeTotMD5MacHigh,
       "sslBeTotSHAMacLow": sslBeTotSHAMacLow,
       "sslBeTotSHAMacHigh": sslBeTotSHAMacHigh,
       "sslTotTransactions": sslTotTransactions,
       "sslTotSSLv2Transactions": sslTotSSLv2Transactions,
       "sslTotSSLv3Transactions": sslTotSSLv3Transactions,
       "sslTotTLSv1Transactions": sslTotTLSv1Transactions,
       "sslTotSessions": sslTotSessions,
       "sslTotSSLv2Sessions": sslTotSSLv2Sessions,
       "sslTotSSLv3Sessions": sslTotSSLv3Sessions,
       "sslTotTLSv1Sessions": sslTotTLSv1Sessions,
       "sslTotExpiredSessions": sslTotExpiredSessions,
       "sslTotNewSessions": sslTotNewSessions,
       "sslTotSessionHits": sslTotSessionHits,
       "sslTotSessionMiss": sslTotSessionMiss,
       "sslTotRenegSessions": sslTotRenegSessions,
       "sslTotSSLv3RenegSessions": sslTotSSLv3RenegSessions,
       "sslTotTLSv1RenegSessions": sslTotTLSv1RenegSessions,
       "sslTotSSLv2Handshakes": sslTotSSLv2Handshakes,
       "sslTotSSLv3Handshakes": sslTotSSLv3Handshakes,
       "sslTotTLSv1Handshakes": sslTotTLSv1Handshakes,
       "sslTotSSLv2ClientAuthentications": sslTotSSLv2ClientAuthentications,
       "sslTotSSLv3ClientAuthentications": sslTotSSLv3ClientAuthentications,
       "sslTotTLSv1ClientAuthentications": sslTotTLSv1ClientAuthentications,
       "sslTotRSA512keyExchanges": sslTotRSA512keyExchanges,
       "sslTotRSA1024keyExchanges": sslTotRSA1024keyExchanges,
       "sslTotRSA2048keyExchanges": sslTotRSA2048keyExchanges,
       "sslTotDH512keyExchanges": sslTotDH512keyExchanges,
       "sslTotDH1024keyExchanges": sslTotDH1024keyExchanges,
       "sslTotDH2048keyExchanges": sslTotDH2048keyExchanges,
       "sslTotRSAAuthorizations": sslTotRSAAuthorizations,
       "sslTotDHAuthorizations": sslTotDHAuthorizations,
       "sslTotDSSAuthorizations": sslTotDSSAuthorizations,
       "sslTotNULLAuthorizations": sslTotNULLAuthorizations,
       "sslTot40BitRC4Ciphers": sslTot40BitRC4Ciphers,
       "sslTot56BitRC4Ciphers": sslTot56BitRC4Ciphers,
       "sslTot64BitRC4Ciphers": sslTot64BitRC4Ciphers,
       "sslTot128BitRC4Ciphers": sslTot128BitRC4Ciphers,
       "sslTot40BitDESCiphers": sslTot40BitDESCiphers,
       "sslTot56BitDESCiphers": sslTot56BitDESCiphers,
       "sslTot168Bit3DESCiphers": sslTot168Bit3DESCiphers,
       "sslTot40BitRC2Ciphers": sslTot40BitRC2Ciphers,
       "sslTot56BitRC2Ciphers": sslTot56BitRC2Ciphers,
       "sslTot128BitRC2Ciphers": sslTot128BitRC2Ciphers,
       "sslTot128BitIDEACiphers": sslTot128BitIDEACiphers,
       "sslTotNULLCiphers": sslTotNULLCiphers,
       "sslTotMD5Mac": sslTotMD5Mac,
       "sslTotSHAMac": sslTotSHAMac,
       "sslTotOffloadBulkDES": sslTotOffloadBulkDES,
       "sslTotOffloadRSAKeyExchanges": sslTotOffloadRSAKeyExchanges,
       "sslTotOffloadDHKeyExchanges": sslTotOffloadDHKeyExchanges,
       "sslTotOffloadSignRSA": sslTotOffloadSignRSA,
       "sslBeTotSessions": sslBeTotSessions,
       "sslBeTotSSLv3Sessions": sslBeTotSSLv3Sessions,
       "sslBeTotTLSv1Sessions": sslBeTotTLSv1Sessions,
       "sslBeExpiredSessions": sslBeExpiredSessions,
       "sslBeTotSessionMultiplexAttempts": sslBeTotSessionMultiplexAttempts,
       "sslBeTotSessionMultiplexAttemptSuccess": sslBeTotSessionMultiplexAttemptSuccess,
       "sslBeTotSessionMultiplexAttemptFails": sslBeTotSessionMultiplexAttemptFails,
       "sslBeMaxMultiplexedSessions": sslBeMaxMultiplexedSessions,
       "sslBeTotSSLv3Handshakes": sslBeTotSSLv3Handshakes,
       "sslBeTotTLSv1Handshakes": sslBeTotTLSv1Handshakes,
       "sslBeTotSSLv3ClientAuthentications": sslBeTotSSLv3ClientAuthentications,
       "sslBeTotTLSv1ClientAuthentications": sslBeTotTLSv1ClientAuthentications,
       "sslBeTotRSA512keyExchanges": sslBeTotRSA512keyExchanges,
       "sslBeTotRSA1024keyExchanges": sslBeTotRSA1024keyExchanges,
       "sslBeTotRSA2048keyExchanges": sslBeTotRSA2048keyExchanges,
       "sslBeTotDH512keyExchanges": sslBeTotDH512keyExchanges,
       "sslBeTotDH1024keyExchanges": sslBeTotDH1024keyExchanges,
       "sslBeTotDH2048keyExchanges": sslBeTotDH2048keyExchanges,
       "sslBeTotRSAAuthorizations": sslBeTotRSAAuthorizations,
       "sslBeTotDHAuthorizations": sslBeTotDHAuthorizations,
       "sslBeTotDSSAuthorizations": sslBeTotDSSAuthorizations,
       "sslBeTotNULLAuthorizations": sslBeTotNULLAuthorizations,
       "sslBeTot40BitRC4Ciphers": sslBeTot40BitRC4Ciphers,
       "sslBeTot56BitRC4Ciphers": sslBeTot56BitRC4Ciphers,
       "sslBeTot64BitRC4Ciphers": sslBeTot64BitRC4Ciphers,
       "sslBeTot128BitRC4Ciphers": sslBeTot128BitRC4Ciphers,
       "sslBeTot40BitDESCiphers": sslBeTot40BitDESCiphers,
       "sslBeTot56BitDESCiphers": sslBeTot56BitDESCiphers,
       "sslBeTot168Bit3DESCiphers": sslBeTot168Bit3DESCiphers,
       "sslBeTot40BitRC2Ciphers": sslBeTot40BitRC2Ciphers,
       "sslBeTot56BitRC2Ciphers": sslBeTot56BitRC2Ciphers,
       "sslBeTot128BitRC2Ciphers": sslBeTot128BitRC2Ciphers,
       "sslBeTot128BitIDEACiphers": sslBeTot128BitIDEACiphers,
       "sslBeTotNULLCiphers": sslBeTotNULLCiphers,
       "sslBeTotMD5Mac": sslBeTotMD5Mac,
       "sslBeTotSHAMac": sslBeTotSHAMac,
       "sslCurSessions": sslCurSessions,
       "sslTotOffloadBulkAES": sslTotOffloadBulkAES,
       "sslTotOffloadBulkRC4": sslTotOffloadBulkRC4,
       "sslNumCardsUP": sslNumCardsUP,
       "sslCards": sslCards,
       "sslTotBkendSessionReNegotiate": sslTotBkendSessionReNegotiate,
       "sslTotCipherAES128": sslTotCipherAES128,
       "sslTotBkendSslV3Renego": sslTotBkendSslV3Renego,
       "sslTotBkendTlSvlRenego": sslTotBkendTlSvlRenego,
       "sslTotCipherAES256": sslTotCipherAES256,
       "sslTotBkendCipherAES128": sslTotBkendCipherAES128,
       "sslTotBkendCipherAES256": sslTotBkendCipherAES256,
       "sslTotHwEncBE": sslTotHwEncBE,
       "sslTotDec": sslTotDec,
       "sslTotSwEncFE": sslTotSwEncFE,
       "sslTotEncFE": sslTotEncFE,
       "sslTotEnc": sslTotEnc,
       "sslTotDecHw": sslTotDecHw,
       "sslTotSwDecBE": sslTotSwDecBE,
       "sslTotHwDecFE": sslTotHwDecFE,
       "sslTotEncHw": sslTotEncHw,
       "sslTotDecSw": sslTotDecSw,
       "sslTotSwEncBE": sslTotSwEncBE,
       "sslTotEncSw": sslTotEncSw,
       "sslTotSwDecFE": sslTotSwDecFE,
       "sslTotEncBE": sslTotEncBE,
       "sslTotDecBE": sslTotDecBE,
       "sslTotHwDecBE": sslTotHwDecBE,
       "sslTotDecFE": sslTotDecFE,
       "sslTotHwEncFE": sslTotHwEncFE,
       "sslTotRSA4096keyExchanges": sslTotRSA4096keyExchanges,
       "nsHttpStatsGroup": nsHttpStatsGroup,
       "httpTotGetsLow": httpTotGetsLow,
       "httpTotGetsHigh": httpTotGetsHigh,
       "httpTotPostsLow": httpTotPostsLow,
       "httpTotPostsHigh": httpTotPostsHigh,
       "httpTotOthersLow": httpTotOthersLow,
       "httpTotOthersHigh": httpTotOthersHigh,
       "httpTotRxRequestBytesLow": httpTotRxRequestBytesLow,
       "httpTotRxRequestBytesHigh": httpTotRxRequestBytesHigh,
       "httpTotRxResponseBytesLow": httpTotRxResponseBytesLow,
       "httpTotRxResponseBytesHigh": httpTotRxResponseBytesHigh,
       "httpTotTxRequestBytesLow": httpTotTxRequestBytesLow,
       "httpTotTxRequestBytesHigh": httpTotTxRequestBytesHigh,
       "httpTotTxResponseBytesLow": httpTotTxResponseBytesLow,
       "httpTotTxResponseBytesHigh": httpTotTxResponseBytesHigh,
       "httpTotHTTP10reqLow": httpTotHTTP10reqLow,
       "httpTotHTTP10reqHigh": httpTotHTTP10reqHigh,
       "httpTotResponsesLow": httpTotResponsesLow,
       "httpTotResponsesHigh": httpTotResponsesHigh,
       "httpTot10ResponsesLow": httpTot10ResponsesLow,
       "httpTot10ResponsesHigh": httpTot10ResponsesHigh,
       "httpTotClenResponsesLow": httpTotClenResponsesLow,
       "httpTotClenResponsesHigh": httpTotClenResponsesHigh,
       "httpTotChunkedResponsesLow": httpTotChunkedResponsesLow,
       "httpTotChunkedResponsesHigh": httpTotChunkedResponsesHigh,
       "httpErrIncompleteRequestsLow": httpErrIncompleteRequestsLow,
       "httpErrIncompleteRequestsHigh": httpErrIncompleteRequestsHigh,
       "httpErrIncompleteResponsesLow": httpErrIncompleteResponsesLow,
       "httpErrIncompleteResponsesHigh": httpErrIncompleteResponsesHigh,
       "httpErrPipelinedRequestsLow": httpErrPipelinedRequestsLow,
       "httpErrPipelinedRequestsHigh": httpErrPipelinedRequestsHigh,
       "httpErrIncompleteHeadersLow": httpErrIncompleteHeadersLow,
       "httpErrIncompleteHeadersHigh": httpErrIncompleteHeadersHigh,
       "httpErrServerBusyLow": httpErrServerBusyLow,
       "httpErrServerBusyHigh": httpErrServerBusyHigh,
       "httpTotChunkedReqLow": httpTotChunkedReqLow,
       "httpTotChunkedReqHigh": httpTotChunkedReqHigh,
       "httpTotClenReqLow": httpTotClenReqLow,
       "httpTotClenReqHigh": httpTotClenReqHigh,
       "httpErrLargeContentLow": httpErrLargeContentLow,
       "httpErrLargeContentHigh": httpErrLargeContentHigh,
       "httpErrLargeCtlenLow": httpErrLargeCtlenLow,
       "httpErrLargeCtlenHigh": httpErrLargeCtlenHigh,
       "httpErrLargeChunkLow": httpErrLargeChunkLow,
       "httpErrLargeChunkHigh": httpErrLargeChunkHigh,
       "httpTotGets": httpTotGets,
       "httpTotPosts": httpTotPosts,
       "httpTotOthers": httpTotOthers,
       "httpTotRxRequestBytes": httpTotRxRequestBytes,
       "httpTotRxResponseBytes": httpTotRxResponseBytes,
       "httpTotTxRequestBytes": httpTotTxRequestBytes,
       "httpTotTxResponseBytes": httpTotTxResponseBytes,
       "httpTot10Requests": httpTot10Requests,
       "httpTotResponses": httpTotResponses,
       "httpTot10Responses": httpTot10Responses,
       "httpTotClenResponses": httpTotClenResponses,
       "httpTotChunkedResponses": httpTotChunkedResponses,
       "httpErrIncompleteRequests": httpErrIncompleteRequests,
       "httpErrIncompleteResponses": httpErrIncompleteResponses,
       "httpErrPipelinedRequests": httpErrPipelinedRequests,
       "httpErrIncompleteHeaders": httpErrIncompleteHeaders,
       "httpErrServerBusy": httpErrServerBusy,
       "httpTotChunkedRequests": httpTotChunkedRequests,
       "httpTotClenRequests": httpTotClenRequests,
       "httpErrLargeContent": httpErrLargeContent,
       "httpErrLargeCtlen": httpErrLargeCtlen,
       "httpErrLargeChunk": httpErrLargeChunk,
       "httpTotRequests": httpTotRequests,
       "httpTot11Requests": httpTot11Requests,
       "httpTot11Responses": httpTot11Responses,
       "httpTotNoClenChunkResponses": httpTotNoClenChunkResponses,
       "httpErrNoreuseMultipart": httpErrNoreuseMultipart,
       "nsCacheStatsGroup": nsCacheStatsGroup,
       "cacheMaxMemoryKB": cacheMaxMemoryKB,
       "cacheUtilizedMemoryKB": cacheUtilizedMemoryKB,
       "cacheNumCached": cacheNumCached,
       "cacheErrMemAllocLow": cacheErrMemAllocLow,
       "cacheErrMemAllocHigh": cacheErrMemAllocHigh,
       "cacheTotRequestsLow": cacheTotRequestsLow,
       "cacheTotRequestsHigh": cacheTotRequestsHigh,
       "cacheTotHitsLow": cacheTotHitsLow,
       "cacheTotHitsHigh": cacheTotHitsHigh,
       "cacheTotMissesLow": cacheTotMissesLow,
       "cacheTotMissesHigh": cacheTotMissesHigh,
       "cachePercentHit": cachePercentHit,
       "cacheRecentPercentHit": cacheRecentPercentHit,
       "cacheCurHits": cacheCurHits,
       "cacheCurMisses": cacheCurMisses,
       "cacheTot304HitsLow": cacheTot304HitsLow,
       "cacheTot304HitsHigh": cacheTot304HitsHigh,
       "cacheTotNon304HitsLow": cacheTotNon304HitsLow,
       "cacheTotNon304HitsHigh": cacheTotNon304HitsHigh,
       "cachePercent304Hits": cachePercent304Hits,
       "cacheRecentPercent304Hits": cacheRecentPercent304Hits,
       "cacheTotStoreAbleMissesLow": cacheTotStoreAbleMissesLow,
       "cacheTotStoreAbleMissesHigh": cacheTotStoreAbleMissesHigh,
       "cacheTotNonStoreAbleMissesLow": cacheTotNonStoreAbleMissesLow,
       "cacheTotNonStoreAbleMissesHigh": cacheTotNonStoreAbleMissesHigh,
       "cachePercentStoreAbleMiss": cachePercentStoreAbleMiss,
       "cacheRecentPercentStoreAbleMiss": cacheRecentPercentStoreAbleMiss,
       "cacheTotRevalidationMissLow": cacheTotRevalidationMissLow,
       "cacheTotRevalidationMissHigh": cacheTotRevalidationMissHigh,
       "cacheTotFullToConditionalRequestLow": cacheTotFullToConditionalRequestLow,
       "cacheTotFullToConditionalRequestHigh": cacheTotFullToConditionalRequestHigh,
       "cacheTotSuccessfulRevalidationLow": cacheTotSuccessfulRevalidationLow,
       "cacheTotSuccessfulRevalidationHigh": cacheTotSuccessfulRevalidationHigh,
       "cachePercentSuccessfulRevalidation": cachePercentSuccessfulRevalidation,
       "cacheRecentPercentSuccessfulRevalidation": cacheRecentPercentSuccessfulRevalidation,
       "cacheBytesServedLow": cacheBytesServedLow,
       "cacheBytesServedHigh": cacheBytesServedHigh,
       "cacheCompressedBytesServedLow": cacheCompressedBytesServedLow,
       "cacheCompressedBytesServedHigh": cacheCompressedBytesServedHigh,
       "cachePercentByteHit": cachePercentByteHit,
       "cacheRecentPercentByteHit": cacheRecentPercentByteHit,
       "cachePercentOriginBandwidthSaved": cachePercentOriginBandwidthSaved,
       "cacheRecentPercentOriginBandwidthSaved": cacheRecentPercentOriginBandwidthSaved,
       "cacheErrMemAlloc": cacheErrMemAlloc,
       "cacheTotRequests": cacheTotRequests,
       "cacheTotHits": cacheTotHits,
       "cacheTotMisses": cacheTotMisses,
       "cacheTot304Hits": cacheTot304Hits,
       "cacheTotNon304Hits": cacheTotNon304Hits,
       "cacheTotStoreAbleMisses": cacheTotStoreAbleMisses,
       "cacheTotNonStoreAbleMisses": cacheTotNonStoreAbleMisses,
       "cacheTotRevalidationMiss": cacheTotRevalidationMiss,
       "cacheTotFullToConditionalRequest": cacheTotFullToConditionalRequest,
       "cacheTotSuccessfulRevalidation": cacheTotSuccessfulRevalidation,
       "cacheTotResponseBytes": cacheTotResponseBytes,
       "cacheBytesServed": cacheBytesServed,
       "cacheCompressedBytesServed": cacheCompressedBytesServed,
       "cacheTotPetRequests": cacheTotPetRequests,
       "cacheTotPetHits": cacheTotPetHits,
       "cachePercentPetHits": cachePercentPetHits,
       "cacheTotParameterizedRequests": cacheTotParameterizedRequests,
       "cacheTotParameterizedHits": cacheTotParameterizedHits,
       "cacheTotParameterizedNon304Hits": cacheTotParameterizedNon304Hits,
       "cacheTotParameterized304Hits": cacheTotParameterized304Hits,
       "cachePercentParameterized304Hits": cachePercentParameterized304Hits,
       "cacheRecentPercentParameterizedHits": cacheRecentPercentParameterizedHits,
       "cacheTotInvalidationRequests": cacheTotInvalidationRequests,
       "cacheTotNonParameterizedInvalidationRequests": cacheTotNonParameterizedInvalidationRequests,
       "cacheTotParameterizedInvalidationRequests": cacheTotParameterizedInvalidationRequests,
       "cacheLargestResponseReceived": cacheLargestResponseReceived,
       "cacheTotFlashcacheMisses": cacheTotFlashcacheMisses,
       "cacheTotFlashcacheHits": cacheTotFlashcacheHits,
       "cacheTotExpireAtLastByte": cacheTotExpireAtLastByte,
       "cacheNumMarker": cacheNumMarker,
       "cacheMaxMemoryActiveKB": cacheMaxMemoryActiveKB,
       "cache64MaxMemoryKB": cache64MaxMemoryKB,
       "nsCompressionStatsGroup": nsCompressionStatsGroup,
       "compTotalRequests": compTotalRequests,
       "compTotalTxBytes": compTotalTxBytes,
       "compTotalRxBytes": compTotalRxBytes,
       "compTotalTxPackets": compTotalTxPackets,
       "compTotalRxPackets": compTotalRxPackets,
       "compRatio": compRatio,
       "compTotalDataCompressionRatio": compTotalDataCompressionRatio,
       "compTcpTotalTxBytes": compTcpTotalTxBytes,
       "compTcpTotalRxBytes": compTcpTotalRxBytes,
       "compTcpTotalTxPackets": compTcpTotalTxPackets,
       "compTcpTotalRxPackets": compTcpTotalRxPackets,
       "compTcpTotalQuantum": compTcpTotalQuantum,
       "compTcpTotalPush": compTcpTotalPush,
       "compTcpTotalEoi": compTcpTotalEoi,
       "compTcpTotalTimer": compTcpTotalTimer,
       "compTcpRatio": compTcpRatio,
       "compTcpBandwidthSaving": compTcpBandwidthSaving,
       "deCompTcpRxPackets": deCompTcpRxPackets,
       "deCompTcpTxPackets": deCompTcpTxPackets,
       "deCompTcpRxBytes": deCompTcpRxBytes,
       "deCompTcpTxBytes": deCompTcpTxBytes,
       "deCompTcpErrData": deCompTcpErrData,
       "deCompTcpErrLessData": deCompTcpErrLessData,
       "deCompTcpErrMoreData": deCompTcpErrMoreData,
       "deCompTcpErrMemory": deCompTcpErrMemory,
       "deCompTcpErrUnknown": deCompTcpErrUnknown,
       "deCompTcpRatio": deCompTcpRatio,
       "deCompTcpBandwidthSaving": deCompTcpBandwidthSaving,
       "delCompTotalRequests": delCompTotalRequests,
       "delCompFirstAccess": delCompFirstAccess,
       "delCompDone": delCompDone,
       "delCompTcpRxBytes": delCompTcpRxBytes,
       "delCompTcpTxBytes": delCompTcpTxBytes,
       "delCompTcpRxPackets": delCompTcpRxPackets,
       "delCompTcpTxPackets": delCompTcpTxPackets,
       "delCompBaseServed": delCompBaseServed,
       "delCompBaseTcpTxBytes": delCompBaseTcpTxBytes,
       "delCompErrBypassed": delCompErrBypassed,
       "delCompErrBFileWHdrFailed": delCompErrBFileWHdrFailed,
       "delCompErrNostoreMiss": delCompErrNostoreMiss,
       "delCompErrReqinfoToobig": delCompErrReqinfoToobig,
       "delCompErrReqinfoAllocfail": delCompErrReqinfoAllocfail,
       "delCompErrSessallocFail": delCompErrSessallocFail,
       "delCmpRatio": delCmpRatio,
       "delBwSaving": delBwSaving,
       "compHttpBandwidthSaving": compHttpBandwidthSaving,
       "nsGslbGroup": nsGslbGroup,
       "gslbGlobalStats": gslbGlobalStats,
       "customEntries": customEntries,
       "staticEntries": staticEntries,
       "gslbGlobalInfo": gslbGlobalInfo,
       "gslbSitesTable": gslbSitesTable,
       "gslbSitesEntry": gslbSitesEntry,
       "siteName": siteName,
       "siteIp": siteIp,
       "siteType": siteType,
       "siteMetricExchange": siteMetricExchange,
       "siteMepStatus": siteMepStatus,
       "sitePublicIp": sitePublicIp,
       "siteTotalRequests": siteTotalRequests,
       "siteTotalRequestBytes": siteTotalRequestBytes,
       "siteTotalResponses": siteTotalResponses,
       "siteTotalResponseBytes": siteTotalResponseBytes,
       "siteCurSrvrConnections": siteCurSrvrConnections,
       "siteCurClntConnections": siteCurClntConnections,
       "siteMetricMepStatus": siteMetricMepStatus,
       "nwMetricMepStatus": nwMetricMepStatus,
       "nwMetricExchange": nwMetricExchange,
       "persExchange": persExchange,
       "gslbSiteInetAddressType": gslbSiteInetAddressType,
       "gslbSiteInetAddress": gslbSiteInetAddress,
       "gslbSitePublicInetAddressType": gslbSitePublicInetAddressType,
       "gslbSitePublicInetAddress": gslbSitePublicInetAddress,
       "gslbPoliciesTable": gslbPoliciesTable,
       "gslbPoliciesEntry": gslbPoliciesEntry,
       "gslbPolicyName": gslbPolicyName,
       "totalHits": totalHits,
       "gslbDomainStats": gslbDomainStats,
       "nsDomainTable": nsDomainTable,
       "nsDomainEntry": nsDomainEntry,
       "domainName": domainName,
       "dnsTotalQueries": dnsTotalQueries,
       "nsPolicyEngineGroup": nsPolicyEngineGroup,
       "nsPolicyStatsTable": nsPolicyStatsTable,
       "nsPolicyStatsEntry": nsPolicyStatsEntry,
       "pengPolicyName": pengPolicyName,
       "pengPolicyHits": pengPolicyHits,
       "pengBytesIn": pengBytesIn,
       "pengBytesOut": pengBytesOut,
       "pengPolicyFullName": pengPolicyFullName,
       "nsDomainNameServiceGroup": nsDomainNameServiceGroup,
       "nsDnsServerStatsGroup": nsDnsServerStatsGroup,
       "dnsTotQueries": dnsTotQueries,
       "dnsTotAnswers": dnsTotAnswers,
       "dnsTotArecQueries": dnsTotArecQueries,
       "dnsTotAresponse": dnsTotAresponse,
       "dnsTotNSrecQueries": dnsTotNSrecQueries,
       "dnsTotNSresponse": dnsTotNSresponse,
       "dnsTotMXrecQueries": dnsTotMXrecQueries,
       "dnsTotMXresponse": dnsTotMXresponse,
       "dnsTotSOArecQueries": dnsTotSOArecQueries,
       "dnsTotSOAresponse": dnsTotSOAresponse,
       "dnsTotCNAMErecQueries": dnsTotCNAMErecQueries,
       "dnsTotCNAMEresponse": dnsTotCNAMEresponse,
       "dnsTotUnsupportedResponseClass": dnsTotUnsupportedResponseClass,
       "dnsTotUnsupportedResponseType": dnsTotUnsupportedResponseType,
       "dnsTotUnsupportedQueries": dnsTotUnsupportedQueries,
       "dnsTotUnsupportedQueryClass": dnsTotUnsupportedQueryClass,
       "dnsTotInvalidQueryFormat": dnsTotInvalidQueryFormat,
       "dnsTotNonAuthNoDatas": dnsTotNonAuthNoDatas,
       "dnsTotMultiQuery": dnsTotMultiQuery,
       "dnsTotStrayAnswer": dnsTotStrayAnswer,
       "dnsTotCacheFlush": dnsTotCacheFlush,
       "dnsTotCacheEntriesFlush": dnsTotCacheEntriesFlush,
       "dnsTotServerQuery": dnsTotServerQuery,
       "dnsTotServerResponse": dnsTotServerResponse,
       "dnsTotArecFailed": dnsTotArecFailed,
       "dnsTotNSrecFailed": dnsTotNSrecFailed,
       "dnsTotMXrecFailed": dnsTotMXrecFailed,
       "dnsTotCNAMErecFailed": dnsTotCNAMErecFailed,
       "dnsTotArecUpdate": dnsTotArecUpdate,
       "dnsTotNSrecUpdate": dnsTotNSrecUpdate,
       "dnsTotMXrecUpdate": dnsTotMXrecUpdate,
       "dnsTotSOArecUpdate": dnsTotSOArecUpdate,
       "dnsTotCNAMErecUpdate": dnsTotCNAMErecUpdate,
       "dnsTotRecUpdate": dnsTotRecUpdate,
       "dnsTotMultiQueryDisableError": dnsTotMultiQueryDisableError,
       "dnsCurArecord": dnsCurArecord,
       "dnsCurNSrecord": dnsCurNSrecord,
       "dnsCurMXrecord": dnsCurMXrecord,
       "dnsCurSOArecord": dnsCurSOArecord,
       "dnsCurCNAMErecord": dnsCurCNAMErecord,
       "dnsCurAuthEntries": dnsCurAuthEntries,
       "dnsCurNoAuthEntries": dnsCurNoAuthEntries,
       "dnsTotAuthAns": dnsTotAuthAns,
       "dnsTotAuthNoNames": dnsTotAuthNoNames,
       "dnsTotNoDataResps": dnsTotNoDataResps,
       "dnsTotResponseBadLen": dnsTotResponseBadLen,
       "dnsTotReqRefusals": dnsTotReqRefusals,
       "dnsTotOtherErrors": dnsTotOtherErrors,
       "dnsTotPTRrecQueries": dnsTotPTRrecQueries,
       "dnsTotPTRresponse": dnsTotPTRresponse,
       "dnsTotPTRrecUpdate": dnsTotPTRrecUpdate,
       "dnsTotPTRrecFailed": dnsTotPTRrecFailed,
       "dnsCurPTRrecord": dnsCurPTRrecord,
       "dnsTotSRVrecQueries": dnsTotSRVrecQueries,
       "dnsTotSRVresponse": dnsTotSRVresponse,
       "dnsTotSRVrecUpdate": dnsTotSRVrecUpdate,
       "dnsTotSRVrecFailed": dnsTotSRVrecFailed,
       "dnsCurSRVrecord": dnsCurSRVrecord,
       "dnsTotAAAArecQueries": dnsTotAAAArecQueries,
       "dnsTotAAAAresponse": dnsTotAAAAresponse,
       "dnsTotAAAArecUpdate": dnsTotAAAArecUpdate,
       "dnsTotAAAArecFailed": dnsTotAAAArecFailed,
       "dnsCurAAAArecord": dnsCurAAAArecord,
       "dnsTotANYqueries": dnsTotANYqueries,
       "dnsTotANYresponse": dnsTotANYresponse,
       "dnsTotANYrecFailed": dnsTotANYrecFailed,
       "dnsTotSOArecFailed": dnsTotSOArecFailed,
       "nsIfStatsTable": nsIfStatsTable,
       "nsIfStatsEntry": nsIfStatsEntry,
       "ifName": ifName,
       "ifMedia": ifMedia,
       "ifTotRxBytes": ifTotRxBytes,
       "ifRxAvgBandwidthUsage": ifRxAvgBandwidthUsage,
       "ifTotRxPkts": ifTotRxPkts,
       "ifRxAvgPacketRate": ifRxAvgPacketRate,
       "ifTotTxBytes": ifTotTxBytes,
       "ifTxAvgBandwidthUsage": ifTxAvgBandwidthUsage,
       "ifTotTxPkts": ifTotTxPkts,
       "ifTxAvgPacketRate": ifTxAvgPacketRate,
       "ifRxCRCErrors": ifRxCRCErrors,
       "ifRxFrameErrors": ifRxFrameErrors,
       "ifRxAlignmentErrors": ifRxAlignmentErrors,
       "ifTxCollisions": ifTxCollisions,
       "ifTxExcessCollisions": ifTxExcessCollisions,
       "ifTxLateCollisions": ifTxLateCollisions,
       "ifTxMultiCollisionErrors": ifTxMultiCollisionErrors,
       "ifTxCarrierError": ifTxCarrierError,
       "ifTotRxMbits": ifTotRxMbits,
       "ifTotTxMbits": ifTotTxMbits,
       "ifTotNetScalerPkts": ifTotNetScalerPkts,
       "ifErrDroppedRxPkts": ifErrDroppedRxPkts,
       "ifErrLinkHangs": ifErrLinkHangs,
       "ifLinkReinits": ifLinkReinits,
       "ifErrDuplexMismatch": ifErrDuplexMismatch,
       "ifErrCongestedPktsDrops": ifErrCongestedPktsDrops,
       "ifErrCongestionLimitPktDrops": ifErrCongestionLimitPktDrops,
       "ifErrPktRx": ifErrPktRx,
       "ifErrRxFIFO": ifErrRxFIFO,
       "ifErrRxNoBuffs": ifErrRxNoBuffs,
       "ifErrTxNoNSB": ifErrTxNoNSB,
       "ifErrRxFCS": ifErrRxFCS,
       "ifErrPktTx": ifErrPktTx,
       "ifErrTxFIFO": ifErrTxFIFO,
       "ifErrTxHeartBeat": ifErrTxHeartBeat,
       "ifErrTxOverflow": ifErrTxOverflow,
       "ifErrTxDeferred": ifErrTxDeferred,
       "ifErrDroppedTxPkts": ifErrDroppedTxPkts,
       "ifTotRxXonPause": ifTotRxXonPause,
       "ifTotRxXoffPause": ifTotRxXoffPause,
       "ifTotXoffStateEntered": ifTotXoffStateEntered,
       "ifTotXonSent": ifTotXonSent,
       "ifTotXoffSent": ifTotXoffSent,
       "ifnicStsStalls": ifnicStsStalls,
       "ifnicTxStalls": ifnicTxStalls,
       "ifnicRxStalls": ifnicRxStalls,
       "ifnicErrDisables": ifnicErrDisables,
       "ifThroughput": ifThroughput,
       "ifMinThroughput": ifMinThroughput,
       "nsScPolicyGroup": nsScPolicyGroup,
       "scPolicyStatistics": scPolicyStatistics,
       "scPolicyUrlHits": scPolicyUrlHits,
       "scPopUps": scPopUps,
       "scAltContUrls": scAltContUrls,
       "scSessionReqs": scSessionReqs,
       "scPostReqs": scPostReqs,
       "scThresholdFail": scThresholdFail,
       "scFaultyCookies": scFaultyCookies,
       "scUnSupBrow": scUnSupBrow,
       "scResetStats": scResetStats,
       "scTotCondTriggered": scTotCondTriggered,
       "scTotReissuedRequests": scTotReissuedRequests,
       "scPolicyConfig": scPolicyConfig,
       "scPolicyConfigTable": scPolicyConfigTable,
       "scPolicyConfigEntry": scPolicyConfigEntry,
       "scPolicyName": scPolicyName,
       "scPolUrl": scPolUrl,
       "scDelayThreshold": scDelayThreshold,
       "scMaxConnections": scMaxConnections,
       "scActionType": scActionType,
       "scAlternateContentServiceName": scAlternateContentServiceName,
       "scRuleName": scRuleName,
       "scAlternateContentPath": scAlternateContentPath,
       "nsSslConfigGroup": nsSslConfigGroup,
       "sslCertKeyTable": sslCertKeyTable,
       "sslCertKeyEntry": sslCertKeyEntry,
       "sslCertKeyName": sslCertKeyName,
       "sslCertPath": sslCertPath,
       "sslKeyPath": sslKeyPath,
       "sslInputFormat": sslInputFormat,
       "sslDaysToExpire": sslDaysToExpire,
       "sslCrlTable": sslCrlTable,
       "sslCrlEntry": sslCrlEntry,
       "sslCrlName": sslCrlName,
       "sslCrlPath": sslCrlPath,
       "sslCrlInputFormat": sslCrlInputFormat,
       "sslCipherGroupTable": sslCipherGroupTable,
       "sslCipherGroupEntry": sslCipherGroupEntry,
       "sslCipherGroupName": sslCipherGroupName,
       "sslCipherName": sslCipherName,
       "sslCipherDesc": sslCipherDesc,
       "nsDosPolicyGroup": nsDosPolicyGroup,
       "dosPolicyTable": dosPolicyTable,
       "dosPolicyEntry": dosPolicyEntry,
       "dosPolicyName": dosPolicyName,
       "thresholdValue": thresholdValue,
       "dosPolicyStatistics": dosPolicyStatistics,
       "dosTotConditionTriggered": dosTotConditionTriggered,
       "dosTotValidCookies": dosTotValidCookies,
       "dosTotDosPriorityClients": dosTotDosPriorityClients,
       "dosAvgValidClients": dosAvgValidClients,
       "dosAvgDospriClients": dosAvgDospriClients,
       "nsExpressionTable": nsExpressionTable,
       "nsExpressionEntry": nsExpressionEntry,
       "expressionName": expressionName,
       "expressionTotalHits": expressionTotalHits,
       "nsPqPolicyGroup": nsPqPolicyGroup,
       "pqPolicyConfigTable": pqPolicyConfigTable,
       "pqPolicyConfigEntry": pqPolicyConfigEntry,
       "pqName": pqName,
       "pqRuleName": pqRuleName,
       "pqQdepthThreshold": pqQdepthThreshold,
       "pqPolQdepthThreshold": pqPolQdepthThreshold,
       "pqPriority": pqPriority,
       "pqPolicyWeight": pqPolicyWeight,
       "pqPolicyStatistics": pqPolicyStatistics,
       "pqTotalPolicyMatches": pqTotalPolicyMatches,
       "pqTotalThresholdFailed": pqTotalThresholdFailed,
       "pqPriority1Requests": pqPriority1Requests,
       "pqPriority2Requests": pqPriority2Requests,
       "pqPriority3Requests": pqPriority3Requests,
       "crConfigGroup": crConfigGroup,
       "crPolicyMapConfigTable": crPolicyMapConfigTable,
       "crPolicyMapConfigEntry": crPolicyMapConfigEntry,
       "crMapName": crMapName,
       "crMapSrcName": crMapSrcName,
       "crMapDstName": crMapDstName,
       "crMapSrcUrl": crMapSrcUrl,
       "crMapDstUrl": crMapDstUrl,
       "monitorCount": monitorCount,
       "monitorBindCount": monitorBindCount,
       "htmlInjectionStatsGroup": htmlInjectionStatsGroup,
       "htmlInjectedBytes": htmlInjectedBytes,
       "htmlInjectionSessions": htmlInjectionSessions,
       "htmlInjectionTotalSessions": htmlInjectionTotalSessions,
       "htmlInjectMemAllocFailed": htmlInjectMemAllocFailed,
       "htmlInitFailed": htmlInitFailed,
       "appFirewallGroup": appFirewallGroup,
       "appFirewallStatistics": appFirewallStatistics,
       "appFirewallRequests": appFirewallRequests,
       "appFirewallResponses": appFirewallResponses,
       "appFirewallAborts": appFirewallAborts,
       "appFirewallRedirects": appFirewallRedirects,
       "appFirewallViolStartURL": appFirewallViolStartURL,
       "appFirewallViolDenyURL": appFirewallViolDenyURL,
       "appFirewallViolBufferOverflow": appFirewallViolBufferOverflow,
       "appFirewallViolCookie": appFirewallViolCookie,
       "appFirewallViolXSS": appFirewallViolXSS,
       "appFirewallViolSQL": appFirewallViolSQL,
       "appFirewallViolFieldformat": appFirewallViolFieldformat,
       "appFirewallViolFieldConsistency": appFirewallViolFieldConsistency,
       "appFirewallViolCreditCard": appFirewallViolCreditCard,
       "appFirewallViolSafeObject": appFirewallViolSafeObject,
       "appFirewallTotalViol": appFirewallTotalViol,
       "appFirewallViolWellformednessViolations": appFirewallViolWellformednessViolations,
       "appFirewallViolXdosViolations": appFirewallViolXdosViolations,
       "appFirewallViolMsgValViolations": appFirewallViolMsgValViolations,
       "appFirewallViolWSIViolations": appFirewallViolWSIViolations,
       "appFirewallViolXmlSqlViolations": appFirewallViolXmlSqlViolations,
       "appFirewallViolXmlXssViolations": appFirewallViolXmlXssViolations,
       "appFirewallViolXmlAttachmentViolations": appFirewallViolXmlAttachmentViolations,
       "appFirewallViolCSRFtag": appFirewallViolCSRFtag,
       "appFirewallViolRefererHeader": appFirewallViolRefererHeader,
       "appFirewallViolXmlSoapFaultViolations": appFirewallViolXmlSoapFaultViolations,
       "appFirewallRet4xx": appFirewallRet4xx,
       "appFirewallRet5xx": appFirewallRet5xx,
       "appFirewallReqBytes": appFirewallReqBytes,
       "appFirewallResBytes": appFirewallResBytes,
       "appFirewallLongAvgRespTime": appFirewallLongAvgRespTime,
       "appFirewallShortAvgRespTime": appFirewallShortAvgRespTime,
       "appfwProfileTable": appfwProfileTable,
       "appfwProfileEntry": appfwProfileEntry,
       "appfwprofileName": appfwprofileName,
       "appfwappFirewallRequestsPerProfile": appfwappFirewallRequestsPerProfile,
       "appfwappFirewallResponsesPerProfile": appfwappFirewallResponsesPerProfile,
       "appfwappFirewallAbortsPerProfile": appfwappFirewallAbortsPerProfile,
       "appfwappFirewallRedirectsPerProfile": appfwappFirewallRedirectsPerProfile,
       "appfwappFirewallViolStartURLPerProfile": appfwappFirewallViolStartURLPerProfile,
       "appfwappFirewallViolDenyURLPerProfile": appfwappFirewallViolDenyURLPerProfile,
       "appfwappFirewallViolRefererHeaderPerProfile": appfwappFirewallViolRefererHeaderPerProfile,
       "appfwappFirewallViolBufferOverflowPerProfile": appfwappFirewallViolBufferOverflowPerProfile,
       "appfwappFirewallViolCSRFtagPerProfile": appfwappFirewallViolCSRFtagPerProfile,
       "appfwappFirewallViolCookiePerProfile": appfwappFirewallViolCookiePerProfile,
       "appfwappFirewallViolXSSPerProfile": appfwappFirewallViolXSSPerProfile,
       "appfwappFirewallViolSQLPerProfile": appfwappFirewallViolSQLPerProfile,
       "appfwappFirewallViolFieldformatPerProfile": appfwappFirewallViolFieldformatPerProfile,
       "appfwappFirewallViolFieldConsistencyPerProfile": appfwappFirewallViolFieldConsistencyPerProfile,
       "appfwappFirewallViolCreditCardPerProfile": appfwappFirewallViolCreditCardPerProfile,
       "appfwappFirewallViolSafeObjectPerProfile": appfwappFirewallViolSafeObjectPerProfile,
       "appfwappFirewallViolWellformednessViolationsPerProfile": appfwappFirewallViolWellformednessViolationsPerProfile,
       "appfwappFirewallViolXdosViolationsPerProfile": appfwappFirewallViolXdosViolationsPerProfile,
       "appfwappFirewallViolMsgValViolationsPerProfile": appfwappFirewallViolMsgValViolationsPerProfile,
       "appfwappFirewallViolWSIViolationsPerProfile": appfwappFirewallViolWSIViolationsPerProfile,
       "appfwappFirewallViolXmlSqlViolationsPerProfile": appfwappFirewallViolXmlSqlViolationsPerProfile,
       "appfwappFirewallViolXmlXssViolationsPerProfile": appfwappFirewallViolXmlXssViolationsPerProfile,
       "appfwappFirewallViolXmlAttachmentViolationsPerProfile": appfwappFirewallViolXmlAttachmentViolationsPerProfile,
       "appfwappFirewallTotalViolPerProfile": appfwappFirewallTotalViolPerProfile,
       "appfwappFirewallRet4xxPerProfile": appfwappFirewallRet4xxPerProfile,
       "appfwappFirewallRet5xxPerProfile": appfwappFirewallRet5xxPerProfile,
       "appfwappFirewallViolXmlSoapFaultViolationsPerProfile": appfwappFirewallViolXmlSoapFaultViolationsPerProfile,
       "appfwappFirewallReqBytesPerProfile": appfwappFirewallReqBytesPerProfile,
       "appfwappFirewallResBytesPerProfile": appfwappFirewallResBytesPerProfile,
       "appfwappFirewallLongAvgRespTimePerProfile": appfwappFirewallLongAvgRespTimePerProfile,
       "appfwappFirewallShortAvgRespTimePerProfile": appfwappFirewallShortAvgRespTimePerProfile,
       "nsRnatStatsGroup": nsRnatStatsGroup,
       "nsRnatGlobalStats": nsRnatGlobalStats,
       "rnatTotRxBytes": rnatTotRxBytes,
       "rnatTotTxBytes": rnatTotTxBytes,
       "rnatTotRxPkts": rnatTotRxPkts,
       "rnatTotTxPkts": rnatTotTxPkts,
       "rnatTotTxSyn": rnatTotTxSyn,
       "rnatCurSessions": rnatCurSessions,
       "nsRnatPerIPStatsTable": nsRnatPerIPStatsTable,
       "nsRnatPerIPStatsEntry": nsRnatPerIPStatsEntry,
       "ipRnatTotRxBytes": ipRnatTotRxBytes,
       "ipRnatTotTxBytes": ipRnatTotTxBytes,
       "ipRnatTotRxPkts": ipRnatTotRxPkts,
       "ipRnatTotTxPkts": ipRnatTotTxPkts,
       "ipRnatTotTxSyn": ipRnatTotTxSyn,
       "ipRnatCurSessions": ipRnatCurSessions,
       "nsSslVpnStatsGroup": nsSslVpnStatsGroup,
       "indexHtmlHit": indexHtmlHit,
       "indexHtmlNoServed": indexHtmlNoServed,
       "cfgHtmlServed": cfgHtmlServed,
       "dnsReqHit": dnsReqHit,
       "winsRequestHit": winsRequestHit,
       "csRequestHit": csRequestHit,
       "csNonHttpProbeHit": csNonHttpProbeHit,
       "csHttpProbeHit": csHttpProbeHit,
       "totalCsConnSucc": totalCsConnSucc,
       "totalFsRequest": totalFsRequest,
       "iipDisabledMIPdisabled": iipDisabledMIPdisabled,
       "iipFailedMIPdisabled": iipFailedMIPdisabled,
       "iipDisabledMIPused": iipDisabledMIPused,
       "iipFailedMIPused": iipFailedMIPused,
       "socksMethReqRcvd": socksMethReqRcvd,
       "socksMethReqSent": socksMethReqSent,
       "socksMethRespRcvd": socksMethRespRcvd,
       "socksMethRespSent": socksMethRespSent,
       "socksConnReqRcvd": socksConnReqRcvd,
       "socksConnReqSent": socksConnReqSent,
       "socksConnRespRcvd": socksConnRespRcvd,
       "socksConnRespSent": socksConnRespSent,
       "socksServerError": socksServerError,
       "socksClientError": socksClientError,
       "staConnSuccess": staConnSuccess,
       "staConnFailure": staConnFailure,
       "cpsConnSuccess": cpsConnSuccess,
       "cpsConnFailure": cpsConnFailure,
       "staRequestSent": staRequestSent,
       "staResponseRecvd": staResponseRecvd,
       "icaLicenseFailure": icaLicenseFailure,
       "staRenewSent": staRenewSent,
       "staRenewRecvd": staRenewRecvd,
       "staReassErr": staReassErr,
       "staRnewNoClnt": staRnewNoClnt,
       "staRenewNoRfsh": staRenewNoRfsh,
       "staValidNoClnt": staValidNoClnt,
       "staValidNoEst": staValidNoEst,
       "staMonSent": staMonSent,
       "staMonRcvd": staMonRcvd,
       "staMonSucc": staMonSucc,
       "staMonFail": staMonFail,
       "iipSpilloverMIPused": iipSpilloverMIPused,
       "nsAaaStatsGroup": nsAaaStatsGroup,
       "aaaAuthFail": aaaAuthFail,
       "aaaAuthSuccess": aaaAuthSuccess,
       "aaaAuthNonHttpFail": aaaAuthNonHttpFail,
       "aaaAuthOnlyHttpFail": aaaAuthOnlyHttpFail,
       "aaaAuthNonHttpSuccess": aaaAuthNonHttpSuccess,
       "aaaAuthOnlyHttpSuccess": aaaAuthOnlyHttpSuccess,
       "aaaTotSessions": aaaTotSessions,
       "aaaTotSessionTimeout": aaaTotSessionTimeout,
       "aaaCurSessions": aaaCurSessions,
       "nsGlobalConfigSettings": nsGlobalConfigSettings,
       "webServerHttpPorts": webServerHttpPorts,
       "maxTcpConnections": maxTcpConnections,
       "maxReqPerConnection": maxReqPerConnection,
       "cipInsertionStatus": cipInsertionStatus,
       "cipInsertionHeader": cipInsertionHeader,
       "cookieVersionInserted": cookieVersionInserted,
       "minPathMTU": minPathMTU,
       "mtuEntryTimeoutValue": mtuEntryTimeoutValue,
       "ftpPortRange": ftpPortRange,
       "nsPolicyInfrastructureGroup": nsPolicyInfrastructureGroup,
       "piPolicyTable": piPolicyTable,
       "piPolicyEntry": piPolicyEntry,
       "piPolName": piPolName,
       "piPolicyHits": piPolicyHits,
       "piPolicyUndefHits": piPolicyUndefHits,
       "piPolFullName": piPolFullName,
       "nsSvcGroup": nsSvcGroup,
       "serviceTable": serviceTable,
       "serviceEntry": serviceEntry,
       "svcServiceName": svcServiceName,
       "svcIpAddress": svcIpAddress,
       "svcPort": svcPort,
       "svcServiceType": svcServiceType,
       "svcState": svcState,
       "svcMaxReqPerConn": svcMaxReqPerConn,
       "svcAvgTransactionTime": svcAvgTransactionTime,
       "svcEstablishedConn": svcEstablishedConn,
       "svcActiveConn": svcActiveConn,
       "svcSurgeCount": svcSurgeCount,
       "svcTotalRequestsLow": svcTotalRequestsLow,
       "svcTotalRequestsHigh": svcTotalRequestsHigh,
       "svcTotalRequestBytesLow": svcTotalRequestBytesLow,
       "svcTotalRequestBytesHigh": svcTotalRequestBytesHigh,
       "svcTotalResponsesLow": svcTotalResponsesLow,
       "svcTotalResponsesHigh": svcTotalResponsesHigh,
       "svcTotalResponseBytesLow": svcTotalResponseBytesLow,
       "svcTotalResponseBytesHigh": svcTotalResponseBytesHigh,
       "svcTotalPktsRecvdLow": svcTotalPktsRecvdLow,
       "svcTotalPktsRecvdHigh": svcTotalPktsRecvdHigh,
       "svcTotalPktsSentLow": svcTotalPktsSentLow,
       "svcTotalPktsSentHigh": svcTotalPktsSentHigh,
       "svcTotalSynsRecvdLow": svcTotalSynsRecvdLow,
       "svcTotalSynsRecvdHigh": svcTotalSynsRecvdHigh,
       "svcTotalRequests": svcTotalRequests,
       "svcTotalRequestBytes": svcTotalRequestBytes,
       "svcTotalResponses": svcTotalResponses,
       "svcTotalResponseBytes": svcTotalResponseBytes,
       "svcTotalPktsRecvd": svcTotalPktsRecvd,
       "svcTotalPktsSent": svcTotalPktsSent,
       "svcTotalSynsRecvd": svcTotalSynsRecvd,
       "svcGslbSiteName": svcGslbSiteName,
       "svcAvgSvrTTFB": svcAvgSvrTTFB,
       "svctotalJsTransactions": svctotalJsTransactions,
       "svcdosQDepth": svcdosQDepth,
       "svcCurClntConnections": svcCurClntConnections,
       "svcRequestRate": svcRequestRate,
       "svcRxBytesRate": svcRxBytesRate,
       "svcTxBytesRate": svcTxBytesRate,
       "svcSynfloodRate": svcSynfloodRate,
       "svcTicksSinceLastStateChange": svcTicksSinceLastStateChange,
       "svcTotalClients": svcTotalClients,
       "svcTotalServers": svcTotalServers,
       "svcMaxClients": svcMaxClients,
       "svcActiveTransactions": svcActiveTransactions,
       "svcServiceFullName": svcServiceFullName,
       "svcInetAddressType": svcInetAddressType,
       "svcInetAddress": svcInetAddress,
       "serverTable": serverTable,
       "serverEntry": serverEntry,
       "serverName": serverName,
       "serverIpAddress": serverIpAddress,
       "serverState": serverState,
       "serverDelay": serverDelay,
       "serverFullName": serverFullName,
       "serverInetAddressType": serverInetAddressType,
       "serverInetAddress": serverInetAddress,
       "serviceScpolicyTable": serviceScpolicyTable,
       "serviceScpolicyEntry": serviceScpolicyEntry,
       "svcscpolicyPrimaryIPAddress": svcscpolicyPrimaryIPAddress,
       "svcscpolicyPrimaryPort": svcscpolicyPrimaryPort,
       "svcscpolicyDesIpAddress": svcscpolicyDesIpAddress,
       "svcscpolicyDestPort": svcscpolicyDestPort,
       "svcscpolicyAvgServerTransactionTime": svcscpolicyAvgServerTransactionTime,
       "svcscpolicyTotClientTransaction": svcscpolicyTotClientTransaction,
       "svcscpolicyTotOpenConn": svcscpolicyTotOpenConn,
       "svcscpolicydesIpAddress": svcscpolicydesIpAddress,
       "svcscpolicydestPort": svcscpolicydestPort,
       "svcscpolicyavgServerTransactionTime": svcscpolicyavgServerTransactionTime,
       "svcscpolicytotClientTransaction": svcscpolicytotClientTransaction,
       "svcscpolicytotOpenConn": svcscpolicytotOpenConn,
       "svcscpolicyscPhysicalServiceIP": svcscpolicyscPhysicalServiceIP,
       "svcscpolicyscPhysicalServicePort": svcscpolicyscPhysicalServicePort,
       "svcscpolicyscCurrentWaitingTime": svcscpolicyscCurrentWaitingTime,
       "svcscpolicyscCurrentClientConnections": svcscpolicyscCurrentClientConnections,
       "svcscpolicyscTotalClientConnections": svcscpolicyscTotalClientConnections,
       "svcscpolicyscTotalServerConnections": svcscpolicyscTotalServerConnections,
       "svcscpolicyscTotalRequestsReceived": svcscpolicyscTotalRequestsReceived,
       "svcscpolicyscTotalRequestBytes": svcscpolicyscTotalRequestBytes,
       "svcscpolicyscTotalResponsesReceived": svcscpolicyscTotalResponsesReceived,
       "svcscpolicyscTotalResponseBytes": svcscpolicyscTotalResponseBytes,
       "svcscpolicyscCurrentSurgeQClients": svcscpolicyscCurrentSurgeQClients,
       "svcscpolicyscCurrentWaitingClients": svcscpolicyscCurrentWaitingClients,
       "svcscpolicyscTotalServerTransactions": svcscpolicyscTotalServerTransactions,
       "svcscpolicyscTotalServerTTFBTransactions": svcscpolicyscTotalServerTTFBTransactions,
       "svcscpolicyscTotalServerTTLB": svcscpolicyscTotalServerTTLB,
       "svcscpolicyscTotalClientTTLB": svcscpolicyscTotalClientTTLB,
       "svcscpolicyscTotalServerTTFB": svcscpolicyscTotalServerTTFB,
       "svcscpolicyscAverageClientTTLB": svcscpolicyscAverageClientTTLB,
       "svcscpolicyscAverageServerTTFB": svcscpolicyscAverageServerTTFB,
       "serviceAdvanceSslConfigTable": serviceAdvanceSslConfigTable,
       "serviceAdvanceSslConfigEntry": serviceAdvanceSslConfigEntry,
       "svcSslDH": svcSslDH,
       "svcSslDHCount": svcSslDHCount,
       "svcSslDHFilePath": svcSslDHFilePath,
       "svcSsleRSA": svcSsleRSA,
       "svcSsleRSACount": svcSsleRSACount,
       "svcSslv2Protocol": svcSslv2Protocol,
       "svcSslv3Protocol": svcSslv3Protocol,
       "svcSslTLSv1Protocol": svcSslTLSv1Protocol,
       "svcSslRedirectSupport": svcSslRedirectSupport,
       "svcSslClearTextPort": svcSslClearTextPort,
       "serviceCipherBindingTable": serviceCipherBindingTable,
       "serviceCipherBindingEntry": serviceCipherBindingEntry,
       "svcSslCipherBindName": svcSslCipherBindName,
       "svcSslCipherBindDesc": svcSslCipherBindDesc,
       "serviceGlobalStatsGroup": serviceGlobalStatsGroup,
       "svcCount": svcCount,
       "serverCount": serverCount,
       "svcgroupCount": svcgroupCount,
       "svcgroupmemCount": svcgroupmemCount,
       "serviceGroupMemberTable": serviceGroupMemberTable,
       "serviceGroupMemberEntry": serviceGroupMemberEntry,
       "svcGrpMemberGroupName": svcGrpMemberGroupName,
       "svcGrpMemberName": svcGrpMemberName,
       "svcGrpMemberPrimaryIPAddress": svcGrpMemberPrimaryIPAddress,
       "svcGrpMemberPrimaryPort": svcGrpMemberPrimaryPort,
       "svcGrpMemberServiceType": svcGrpMemberServiceType,
       "svcGrpMemberState": svcGrpMemberState,
       "svcGrpMemberWeight": svcGrpMemberWeight,
       "svcGrpMemberMaxReqPerConn": svcGrpMemberMaxReqPerConn,
       "svcGrpMemberAvgTransactionTime": svcGrpMemberAvgTransactionTime,
       "svcGrpMemberEstablishedConn": svcGrpMemberEstablishedConn,
       "svcGrpMemberActiveConn": svcGrpMemberActiveConn,
       "svcGrpMemberSurgeCount": svcGrpMemberSurgeCount,
       "svcGrpMemberTotalRequests": svcGrpMemberTotalRequests,
       "svcGrpMemberTotalRequestBytes": svcGrpMemberTotalRequestBytes,
       "svcGrpMemberTotalResponses": svcGrpMemberTotalResponses,
       "svcGrpMemberTotalResponseBytes": svcGrpMemberTotalResponseBytes,
       "svcGrpMemberTotalPktsRecvd": svcGrpMemberTotalPktsRecvd,
       "svcGrpMemberTotalPktsSent": svcGrpMemberTotalPktsSent,
       "svcGrpMemberTotalSynsRecvd": svcGrpMemberTotalSynsRecvd,
       "svcGrpMemberGslbSiteName": svcGrpMemberGslbSiteName,
       "svcGrpMemberAvgSvrTTFB": svcGrpMemberAvgSvrTTFB,
       "svcGrpMembertotalJsTransactions": svcGrpMembertotalJsTransactions,
       "svcGrpMemberdosQDepth": svcGrpMemberdosQDepth,
       "svcGrpMemberCurClntConnections": svcGrpMemberCurClntConnections,
       "svcGrpMemberRequestRate": svcGrpMemberRequestRate,
       "svcGrpMemberRxBytesRate": svcGrpMemberRxBytesRate,
       "svcGrpMemberTxBytesRate": svcGrpMemberTxBytesRate,
       "svcGrpMemberSynfloodRate": svcGrpMemberSynfloodRate,
       "svcGrpMemberTicksSinceLastStateChange": svcGrpMemberTicksSinceLastStateChange,
       "svcGrpMemberGroupFullName": svcGrpMemberGroupFullName,
       "svcGrpMemberFullName": svcGrpMemberFullName,
       "svcGrpMemberPrimaryInetAddressType": svcGrpMemberPrimaryInetAddressType,
       "svcGrpMemberPrimaryInetAddress": svcGrpMemberPrimaryInetAddress,
       "serviceDospolicyTable": serviceDospolicyTable,
       "serviceDospolicyEntry": serviceDospolicyEntry,
       "svcdospolicydosTotJSSent": svcdospolicydosTotJSSent,
       "svcdospolicydosTotJSBytesSent": svcdospolicydosTotJSBytesSent,
       "svcdospolicydosTotJSRefused": svcdospolicydosTotJSRefused,
       "svcdospolicydosTotNonGetPostRequests": svcdospolicydosTotNonGetPostRequests,
       "svcdospolicydosPhysicalServiceIP": svcdospolicydosPhysicalServiceIP,
       "svcdospolicydosPhysicalServicePort": svcdospolicydosPhysicalServicePort,
       "svcdospolicydosCurrentQueueSize": svcdospolicydosCurrentQueueSize,
       "svcdospolicydosCurrentJSRate": svcdospolicydosCurrentJSRate,
       "svcdospolicydosTotValidClients": svcdospolicydosTotValidClients,
       "svcdospolicydosCurServerRespRate": svcdospolicydosCurServerRespRate,
       "monitorMemberTable": monitorMemberTable,
       "monitorMemberEntry": monitorMemberEntry,
       "monitorName": monitorName,
       "responseTimeoutThreshold": responseTimeoutThreshold,
       "monitorType": monitorType,
       "monitorInterval": monitorInterval,
       "monitorResponseTimeout": monitorResponseTimeout,
       "monitorDowntime": monitorDowntime,
       "monitorRetrys": monitorRetrys,
       "destinationIP": destinationIP,
       "destinationPort": destinationPort,
       "drtmDeviation": drtmDeviation,
       "drtmActiveMonitors": drtmActiveMonitors,
       "drtmCumResponseTimeout": drtmCumResponseTimeout,
       "alarmProbeFailedRetries": alarmProbeFailedRetries,
       "destinationInetAddressType": destinationInetAddressType,
       "destinationInetAddress": destinationInetAddress,
       "monServiceMemberTable": monServiceMemberTable,
       "monServiceMemberEntry": monServiceMemberEntry,
       "monServiceName": monServiceName,
       "monitorRTO": monitorRTO,
       "monitorState": monitorState,
       "drtmRTO": drtmRTO,
       "drtmLearningProbes": drtmLearningProbes,
       "monitorCurFailedCount": monitorCurFailedCount,
       "monitorWeight": monitorWeight,
       "alarmMonrespto": alarmMonrespto,
       "monitorProbes": monitorProbes,
       "monitorFailed": monitorFailed,
       "monitorMaxClient": monitorMaxClient,
       "monitorFailedCon": monitorFailedCon,
       "monitorFailedCode": monitorFailedCode,
       "monitorFailedStr": monitorFailedStr,
       "monitorFailedTimeout": monitorFailedTimeout,
       "monitorFailedSend": monitorFailedSend,
       "monitorFailedFTP": monitorFailedFTP,
       "monitorFailedPort": monitorFailedPort,
       "monitorFailedResponse": monitorFailedResponse,
       "monitorFailedId": monitorFailedId,
       "monitorProbesNoChange": monitorProbesNoChange,
       "monitorResponseTimeoutThreshExceed": monitorResponseTimeoutThreshExceed,
       "serviceGroupTable": serviceGroupTable,
       "serviceGroupEntry": serviceGroupEntry,
       "svcgrpSvcGroupName": svcgrpSvcGroupName,
       "svcgrpSvcGroupType": svcgrpSvcGroupType,
       "svcgrpSvcGroupState": svcgrpSvcGroupState,
       "svcgrpSvcGroupFullName": svcgrpSvcGroupFullName,
       "nsVserverGroup": nsVserverGroup,
       "vserverTable": vserverTable,
       "vserverEntry": vserverEntry,
       "vsvrName": vsvrName,
       "vsvrIpAddress": vsvrIpAddress,
       "vsvrPort": vsvrPort,
       "vsvrType": vsvrType,
       "vsvrState": vsvrState,
       "vsvrMaxReqPerConn": vsvrMaxReqPerConn,
       "vsvrCurClntConnections": vsvrCurClntConnections,
       "vsvrCurSrvrConnections": vsvrCurSrvrConnections,
       "vsvrAvgTransactionTime": vsvrAvgTransactionTime,
       "vsvrSurgeCount": vsvrSurgeCount,
       "vsvrTotalRequestsLow": vsvrTotalRequestsLow,
       "vsvrTotalRequestsHigh": vsvrTotalRequestsHigh,
       "vsvrTotalRequestBytesLow": vsvrTotalRequestBytesLow,
       "vsvrTotalRequestBytesHigh": vsvrTotalRequestBytesHigh,
       "vsvrTotalResponsesLow": vsvrTotalResponsesLow,
       "vsvrTotalResponsesHigh": vsvrTotalResponsesHigh,
       "vsvrTotalResponseBytesLow": vsvrTotalResponseBytesLow,
       "vsvrTotalResponseBytesHigh": vsvrTotalResponseBytesHigh,
       "vsvrTotalPktsRecvdLow": vsvrTotalPktsRecvdLow,
       "vsvrTotalPktsRecvdHigh": vsvrTotalPktsRecvdHigh,
       "vsvrTotalPktsSentLow": vsvrTotalPktsSentLow,
       "vsvrTotalPktsSentHigh": vsvrTotalPktsSentHigh,
       "vsvrTotalSynsRecvdLow": vsvrTotalSynsRecvdLow,
       "vsvrTotalSynsRecvdHigh": vsvrTotalSynsRecvdHigh,
       "vsvrTotalRequests": vsvrTotalRequests,
       "vsvrTotalRequestBytes": vsvrTotalRequestBytes,
       "vsvrTotalResponses": vsvrTotalResponses,
       "vsvrTotalResponseBytes": vsvrTotalResponseBytes,
       "vsvrTotalPktsRecvd": vsvrTotalPktsRecvd,
       "vsvrTotalPktsSent": vsvrTotalPktsSent,
       "vsvrTotalSynsRecvd": vsvrTotalSynsRecvd,
       "vsvrCurServicesDown": vsvrCurServicesDown,
       "vsvrCurServicesUnKnown": vsvrCurServicesUnKnown,
       "vsvrCurServicesOutOfSvc": vsvrCurServicesOutOfSvc,
       "vsvrCurServicesTransToOutOfSvc": vsvrCurServicesTransToOutOfSvc,
       "vsvrCurServicesUp": vsvrCurServicesUp,
       "vsvrTotMiss": vsvrTotMiss,
       "vsvrRequestRate": vsvrRequestRate,
       "vsvrRxBytesRate": vsvrRxBytesRate,
       "vsvrTxBytesRate": vsvrTxBytesRate,
       "vsvrSynfloodRate": vsvrSynfloodRate,
       "vsvrIp6Address": vsvrIp6Address,
       "vsvrTotHits": vsvrTotHits,
       "vsvrTotSpillOvers": vsvrTotSpillOvers,
       "vsvrTotalClients": vsvrTotalClients,
       "vsvrClientConnOpenRate": vsvrClientConnOpenRate,
       "vsvrFullName": vsvrFullName,
       "vsvrCurSslVpnUsers": vsvrCurSslVpnUsers,
       "vsvrTotalServicesBound": vsvrTotalServicesBound,
       "vsvrHealth": vsvrHealth,
       "vsvrTicksSinceLastStateChange": vsvrTicksSinceLastStateChange,
       "vsvrEntityType": vsvrEntityType,
       "vsvrTotalServers": vsvrTotalServers,
       "vsvrActiveActiveState": vsvrActiveActiveState,
       "vserverServiceTable": vserverServiceTable,
       "vserverServiceEntry": vserverServiceEntry,
       "serviceHitsLow": serviceHitsLow,
       "serviceHitsHigh": serviceHitsHigh,
       "servicePersistentHitsLow": servicePersistentHitsLow,
       "servicePersistentHitsHigh": servicePersistentHitsHigh,
       "vsvrServiceHits": vsvrServiceHits,
       "servicePersistentHits": servicePersistentHits,
       "serviceWeight": serviceWeight,
       "vsvrServiceName": vsvrServiceName,
       "vsvrServiceFullName": vsvrServiceFullName,
       "vserverFullName": vserverFullName,
       "vsvrServiceEntityType": vsvrServiceEntityType,
       "vserverCspolicyTable": vserverCspolicyTable,
       "vserverCspolicyEntry": vserverCspolicyEntry,
       "cspolicyName": cspolicyName,
       "cspolicyDestVserverName": cspolicyDestVserverName,
       "cspolicyHitsLow": cspolicyHitsLow,
       "cspolicyHitsHigh": cspolicyHitsHigh,
       "cspolicyHits": cspolicyHits,
       "csIndexVserverFullName": csIndexVserverFullName,
       "vserverCrpolicyTable": vserverCrpolicyTable,
       "vserverCrpolicyEntry": vserverCrpolicyEntry,
       "crpolicyName": crpolicyName,
       "crpolicyHitsLow": crpolicyHitsLow,
       "crpolicyHitsHigh": crpolicyHitsHigh,
       "crpolicyHits": crpolicyHits,
       "crIndexVserverFullName": crIndexVserverFullName,
       "vserverGlobalStatsGroup": vserverGlobalStatsGroup,
       "curConfigVservers": curConfigVservers,
       "vsvrBindCount": vsvrBindCount,
       "vsvrSvcGrpBindCount": vsvrSvcGrpBindCount,
       "lbvserverTable": lbvserverTable,
       "lbvserverEntry": lbvserverEntry,
       "lbvsvrLBMethod": lbvsvrLBMethod,
       "lbvsvrPersistanceType": lbvsvrPersistanceType,
       "lbvsvrPersistenceTimeOut": lbvsvrPersistenceTimeOut,
       "lbvsvrActiveConn": lbvsvrActiveConn,
       "lbvsvrAvgSvrTTFB": lbvsvrAvgSvrTTFB,
       "vserverPqpolicyTable": vserverPqpolicyTable,
       "vserverPqpolicyEntry": vserverPqpolicyEntry,
       "pqpolicyTotClientTransactionTime": pqpolicyTotClientTransactionTime,
       "pqpolicyTotClientTransactions": pqpolicyTotClientTransactions,
       "pqpolicyDropped": pqpolicyDropped,
       "pqpolicyQdepth": pqpolicyQdepth,
       "pqpolicytotClientTransactionTime": pqpolicytotClientTransactionTime,
       "pqpolicytotClientTransactions": pqpolicytotClientTransactions,
       "pqpolicypqDropped": pqpolicypqDropped,
       "pqpolicypqQdepth": pqpolicypqQdepth,
       "pqpolicypqAvgClientTransactionTime": pqpolicypqAvgClientTransactionTime,
       "pqpolicypqVserverIP": pqpolicypqVserverIP,
       "pqpolicypqVserverPort": pqpolicypqVserverPort,
       "pqpolicypqCurrentClientConnections": pqpolicypqCurrentClientConnections,
       "pqpolicypqTotQueueDepth": pqpolicypqTotQueueDepth,
       "pqpolicypqTotClientConnections": pqpolicypqTotClientConnections,
       "pqpolicypqTotQueueWaitTime": pqpolicypqTotQueueWaitTime,
       "pqpolicypqTotAvgQueueDepth": pqpolicypqTotAvgQueueDepth,
       "pqpolicypqTotAvgQueueWaitTime": pqpolicypqTotAvgQueueWaitTime,
       "pqpolicytotClientTransactionTimems": pqpolicytotClientTransactionTimems,
       "pqpolicypqAvgClientTransactionTimems": pqpolicypqAvgClientTransactionTimems,
       "vserverScpolicyTable": vserverScpolicyTable,
       "vserverScpolicyEntry": vserverScpolicyEntry,
       "vsvrscpolicyPrimaryIPAddress": vsvrscpolicyPrimaryIPAddress,
       "vsvrscpolicyPrimaryPort": vsvrscpolicyPrimaryPort,
       "vsvrscpolicyDesIpAddress": vsvrscpolicyDesIpAddress,
       "vsvrscpolicyDestPort": vsvrscpolicyDestPort,
       "vsvrscpolicyAvgServerTransactionTime": vsvrscpolicyAvgServerTransactionTime,
       "vsvrscpolicyTotClientTransaction": vsvrscpolicyTotClientTransaction,
       "vsvrscpolicyTotOpenConn": vsvrscpolicyTotOpenConn,
       "vsvrscpolicydesIpAddress": vsvrscpolicydesIpAddress,
       "vsvrscpolicydestPort": vsvrscpolicydestPort,
       "vsvrscpolicyavgServerTransactionTime": vsvrscpolicyavgServerTransactionTime,
       "vsvrscpolicytotClientTransaction": vsvrscpolicytotClientTransaction,
       "vsvrscpolicytotOpenConn": vsvrscpolicytotOpenConn,
       "vsvrscpolicyscPhysicalServiceIP": vsvrscpolicyscPhysicalServiceIP,
       "vsvrscpolicyscPhysicalServicePort": vsvrscpolicyscPhysicalServicePort,
       "vsvrscpolicyscCurrentWaitingTime": vsvrscpolicyscCurrentWaitingTime,
       "vsvrscpolicyscCurrentClientConnections": vsvrscpolicyscCurrentClientConnections,
       "vsvrscpolicyscTotalClientConnections": vsvrscpolicyscTotalClientConnections,
       "vsvrscpolicyscTotalServerConnections": vsvrscpolicyscTotalServerConnections,
       "vsvrscpolicyscTotalRequestsReceived": vsvrscpolicyscTotalRequestsReceived,
       "vsvrscpolicyscTotalRequestBytes": vsvrscpolicyscTotalRequestBytes,
       "vsvrscpolicyscTotalResponsesReceived": vsvrscpolicyscTotalResponsesReceived,
       "vsvrscpolicyscTotalResponseBytes": vsvrscpolicyscTotalResponseBytes,
       "vsvrscpolicyscCurrentSurgeQClients": vsvrscpolicyscCurrentSurgeQClients,
       "vsvrscpolicyscCurrentWaitingClients": vsvrscpolicyscCurrentWaitingClients,
       "vsvrscpolicyscTotalServerTransactions": vsvrscpolicyscTotalServerTransactions,
       "vsvrscpolicyscTotalServerTTFBTransactions": vsvrscpolicyscTotalServerTTFBTransactions,
       "vsvrscpolicyscTotalServerTTLB": vsvrscpolicyscTotalServerTTLB,
       "vsvrscpolicyscTotalClientTTLB": vsvrscpolicyscTotalClientTTLB,
       "vsvrscpolicyscTotalServerTTFB": vsvrscpolicyscTotalServerTTFB,
       "vsvrscpolicyscAverageClientTTLB": vsvrscpolicyscAverageClientTTLB,
       "vsvrscpolicyscAverageServerTTFB": vsvrscpolicyscAverageServerTTFB,
       "vserverAdvanceSslConfigTable": vserverAdvanceSslConfigTable,
       "vserverAdvanceSslConfigEntry": vserverAdvanceSslConfigEntry,
       "vsvrSslDH": vsvrSslDH,
       "vsvrSslDHCount": vsvrSslDHCount,
       "vsvrSslDHFilePath": vsvrSslDHFilePath,
       "vsvrSsleRSA": vsvrSsleRSA,
       "vsvrSsleRSACount": vsvrSsleRSACount,
       "vsvrSslv2Protocol": vsvrSslv2Protocol,
       "vsvrSslv3Protocol": vsvrSslv3Protocol,
       "vsvrSslTLSv1Protocol": vsvrSslTLSv1Protocol,
       "vsvrSslRedirectSupport": vsvrSslRedirectSupport,
       "vsvrSslClearTextPort": vsvrSslClearTextPort,
       "vserverCipherBindingTable": vserverCipherBindingTable,
       "vserverCipherBindingEntry": vserverCipherBindingEntry,
       "vsvrSslCipherBindName": vsvrSslCipherBindName,
       "vsvrSslCipherBindDesc": vsvrSslCipherBindDesc,
       "nsSnmpEventsGroup": nsSnmpEventsGroup,
       "snmpTrapVarBindOidsGroup": snmpTrapVarBindOidsGroup,
       "alarmHighThreshold": alarmHighThreshold,
       "alarmNormalThreshold": alarmNormalThreshold,
       "entityName": entityName,
       "nsUserName": nsUserName,
       "configurationCmd": configurationCmd,
       "authorizationStatus": authorizationStatus,
       "commandExecutionStatus": commandExecutionStatus,
       "unackSynCount": unackSynCount,
       "alarmLowThreshold": alarmLowThreshold,
       "alarmProbeFailedErrorString": alarmProbeFailedErrorString,
       "alarmVipRhiIpAddr": alarmVipRhiIpAddr,
       "alarmVipRhiState": alarmVipRhiState,
       "alarmRateLmtThresholdExceeded": alarmRateLmtThresholdExceeded,
       "ipAddressGathered": ipAddressGathered,
       "stringComputed": stringComputed,
       "alarmEntityCurState": alarmEntityCurState,
       "sysHealthPowerSupplyStatus": sysHealthPowerSupplyStatus,
       "alarmCurrentValue": alarmCurrentValue,
       "alarmVipRhiInetAddressType": alarmVipRhiInetAddressType,
       "alarmVipRhiInetAddress": alarmVipRhiInetAddress,
       "alarmVsvrOldName": alarmVsvrOldName,
       "alarmVsvrNewName": alarmVsvrNewName,
       "nsClientIPAddr": nsClientIPAddr,
       "ipConflictAddr": ipConflictAddr,
       "appfwLogMsg": appfwLogMsg}
)
