# SNMP MIB module (APENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:31 2024
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

arrowPoint = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApMgmt_ObjectIdentity = ObjectIdentity
apMgmt = _ApMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1)
)
_PppExt_ObjectIdentity = ObjectIdentity
pppExt = _PppExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 1)
)
_FrExt_ObjectIdentity = ObjectIdentity
frExt = _FrExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 2)
)
_IsdnExt_ObjectIdentity = ObjectIdentity
isdnExt = _IsdnExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 3)
)
_Firewall_ObjectIdentity = ObjectIdentity
firewall = _Firewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 4)
)
_Qos_ObjectIdentity = ObjectIdentity
qos = _Qos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 5)
)
_LocalBalance_ObjectIdentity = ObjectIdentity
localBalance = _LocalBalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 6)
)
_RemoteBalance_ObjectIdentity = ObjectIdentity
remoteBalance = _RemoteBalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 7)
)
_TunnelExt_ObjectIdentity = ObjectIdentity
tunnelExt = _TunnelExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 8)
)
_Ipv4Ext_ObjectIdentity = ObjectIdentity
ipv4Ext = _Ipv4Ext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9)
)
_ApIpv4_ObjectIdentity = ObjectIdentity
apIpv4 = _ApIpv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1)
)
_ApIpv4Interface_ObjectIdentity = ObjectIdentity
apIpv4Interface = _ApIpv4Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 2)
)
_ApIpv4RoutingProtocols_ObjectIdentity = ObjectIdentity
apIpv4RoutingProtocols = _ApIpv4RoutingProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3)
)
_ApIpv4Rip_ObjectIdentity = ObjectIdentity
apIpv4Rip = _ApIpv4Rip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1)
)
_ApIpv4Ospf_ObjectIdentity = ObjectIdentity
apIpv4Ospf = _ApIpv4Ospf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2)
)
_ApIpv4Arp_ObjectIdentity = ObjectIdentity
apIpv4Arp = _ApIpv4Arp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 4)
)
_ApIpv4StaticRoutes_ObjectIdentity = ObjectIdentity
apIpv4StaticRoutes = _ApIpv4StaticRoutes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 5)
)
_ApIpv4Host_ObjectIdentity = ObjectIdentity
apIpv4Host = _ApIpv4Host_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 6)
)
_ApIpv4Dns_ObjectIdentity = ObjectIdentity
apIpv4Dns = _ApIpv4Dns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 7)
)
_ApIpv4Redundancy_ObjectIdentity = ObjectIdentity
apIpv4Redundancy = _ApIpv4Redundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 8)
)
_ConnMgmt_ObjectIdentity = ObjectIdentity
connMgmt = _ConnMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 10)
)
_TerminalMgmt_ObjectIdentity = ObjectIdentity
terminalMgmt = _TerminalMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 11)
)
_RadiusClientExt_ObjectIdentity = ObjectIdentity
radiusClientExt = _RadiusClientExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12)
)
_SecurityMgrExt_ObjectIdentity = ObjectIdentity
securityMgrExt = _SecurityMgrExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 13)
)
_BridgeExt_ObjectIdentity = ObjectIdentity
bridgeExt = _BridgeExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 14)
)
_SvcExt_ObjectIdentity = ObjectIdentity
svcExt = _SvcExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15)
)
_CntExt_ObjectIdentity = ObjectIdentity
cntExt = _CntExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16)
)
_GrpExt_ObjectIdentity = ObjectIdentity
grpExt = _GrpExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 17)
)
_CntsvcExt_ObjectIdentity = ObjectIdentity
cntsvcExt = _CntsvcExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 18)
)
_GrpsvcExt_ObjectIdentity = ObjectIdentity
grpsvcExt = _GrpsvcExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 19)
)
_LogExt_ObjectIdentity = ObjectIdentity
logExt = _LogExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 20)
)
_Ds1Ext_ObjectIdentity = ObjectIdentity
ds1Ext = _Ds1Ext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 21)
)
_SnmpExt_ObjectIdentity = ObjectIdentity
snmpExt = _SnmpExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22)
)
_AclExt_ObjectIdentity = ObjectIdentity
aclExt = _AclExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23)
)
_IfExt_ObjectIdentity = ObjectIdentity
ifExt = _IfExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 24)
)
_OwnExt_ObjectIdentity = ObjectIdentity
ownExt = _OwnExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 25)
)
_BwdthExt_ObjectIdentity = ObjectIdentity
bwdthExt = _BwdthExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 26)
)
_IspgrpExt_ObjectIdentity = ObjectIdentity
ispgrpExt = _IspgrpExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 27)
)
_QosExt_ObjectIdentity = ObjectIdentity
qosExt = _QosExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 28)
)
_CctExt_ObjectIdentity = ObjectIdentity
cctExt = _CctExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 29)
)
_FtpExt_ObjectIdentity = ObjectIdentity
ftpExt = _FtpExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 30)
)
_BootExt_ObjectIdentity = ObjectIdentity
bootExt = _BootExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 31)
)
_AppExt_ObjectIdentity = ObjectIdentity
appExt = _AppExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 32)
)
_HssiExt_ObjectIdentity = ObjectIdentity
hssiExt = _HssiExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 33)
)
_ChassisMgrExt_ObjectIdentity = ObjectIdentity
chassisMgrExt = _ChassisMgrExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34)
)
_CnthotExt_ObjectIdentity = ObjectIdentity
cnthotExt = _CnthotExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 35)
)
_FlowMgrExt_ObjectIdentity = ObjectIdentity
flowMgrExt = _FlowMgrExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36)
)
_WebMgmtExt_ObjectIdentity = ObjectIdentity
webMgmtExt = _WebMgmtExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 37)
)
_CsrpExt_ObjectIdentity = ObjectIdentity
csrpExt = _CsrpExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 38)
)
_EnetExt_ObjectIdentity = ObjectIdentity
enetExt = _EnetExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 39)
)
_DnsServerExt_ObjectIdentity = ObjectIdentity
dnsServerExt = _DnsServerExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 40)
)
_CntdnsExt_ObjectIdentity = ObjectIdentity
cntdnsExt = _CntdnsExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 41)
)
_EqlExt_ObjectIdentity = ObjectIdentity
eqlExt = _EqlExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 42)
)
_SshdExt_ObjectIdentity = ObjectIdentity
sshdExt = _SshdExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 43)
)
_Ap64Stats_ObjectIdentity = ObjectIdentity
ap64Stats = _Ap64Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44)
)
_SchedExt_ObjectIdentity = ObjectIdentity
schedExt = _SchedExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 45)
)
_KalExt_ObjectIdentity = ObjectIdentity
kalExt = _KalExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 46)
)
_HttpExt_ObjectIdentity = ObjectIdentity
httpExt = _HttpExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 47)
)
_DnshotExt_ObjectIdentity = ObjectIdentity
dnshotExt = _DnshotExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 48)
)
_UrqlExt_ObjectIdentity = ObjectIdentity
urqlExt = _UrqlExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 49)
)
_NqlExt_ObjectIdentity = ObjectIdentity
nqlExt = _NqlExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 50)
)
_DqlExt_ObjectIdentity = ObjectIdentity
dqlExt = _DqlExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 51)
)
_CappUdpExt_ObjectIdentity = ObjectIdentity
cappUdpExt = _CappUdpExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 52)
)
_TagExt_ObjectIdentity = ObjectIdentity
tagExt = _TagExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 53)
)
_ProxDbExt_ObjectIdentity = ObjectIdentity
proxDbExt = _ProxDbExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54)
)
_ProbeRttExt_ObjectIdentity = ObjectIdentity
probeRttExt = _ProbeRttExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 55)
)
_PlucExt_ObjectIdentity = ObjectIdentity
plucExt = _PlucExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 56)
)
_PublishExt_ObjectIdentity = ObjectIdentity
publishExt = _PublishExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 57)
)
_SubscribeExt_ObjectIdentity = ObjectIdentity
subscribeExt = _SubscribeExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 58)
)
_ApLocal_ObjectIdentity = ObjectIdentity
apLocal = _ApLocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 2)
)
_Chassis_ObjectIdentity = ObjectIdentity
chassis = _Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 2, 1)
)
_Flash_ObjectIdentity = ObjectIdentity
flash = _Flash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 2, 2)
)
_ApTemp_ObjectIdentity = ObjectIdentity
apTemp = _ApTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 3)
)
_LayerDepend_ObjectIdentity = ObjectIdentity
layerDepend = _LayerDepend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 3, 1)
)
_ApProducts_ObjectIdentity = ObjectIdentity
apProducts = _ApProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 4)
)
_ApCS100_ObjectIdentity = ObjectIdentity
apCS100 = _ApCS100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 4, 1)
)
_ApCS800_ObjectIdentity = ObjectIdentity
apCS800 = _ApCS800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 4, 2)
)
_ApCS150_ObjectIdentity = ObjectIdentity
apCS150 = _ApCS150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 4, 3)
)
_ApCS50_ObjectIdentity = ObjectIdentity
apCS50 = _ApCS50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 4, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APENT-MIB",
    **{"arrowPoint": arrowPoint,
       "apMgmt": apMgmt,
       "pppExt": pppExt,
       "frExt": frExt,
       "isdnExt": isdnExt,
       "firewall": firewall,
       "qos": qos,
       "localBalance": localBalance,
       "remoteBalance": remoteBalance,
       "tunnelExt": tunnelExt,
       "ipv4Ext": ipv4Ext,
       "apIpv4": apIpv4,
       "apIpv4Interface": apIpv4Interface,
       "apIpv4RoutingProtocols": apIpv4RoutingProtocols,
       "apIpv4Rip": apIpv4Rip,
       "apIpv4Ospf": apIpv4Ospf,
       "apIpv4Arp": apIpv4Arp,
       "apIpv4StaticRoutes": apIpv4StaticRoutes,
       "apIpv4Host": apIpv4Host,
       "apIpv4Dns": apIpv4Dns,
       "apIpv4Redundancy": apIpv4Redundancy,
       "connMgmt": connMgmt,
       "terminalMgmt": terminalMgmt,
       "radiusClientExt": radiusClientExt,
       "securityMgrExt": securityMgrExt,
       "bridgeExt": bridgeExt,
       "svcExt": svcExt,
       "cntExt": cntExt,
       "grpExt": grpExt,
       "cntsvcExt": cntsvcExt,
       "grpsvcExt": grpsvcExt,
       "logExt": logExt,
       "ds1Ext": ds1Ext,
       "snmpExt": snmpExt,
       "aclExt": aclExt,
       "ifExt": ifExt,
       "ownExt": ownExt,
       "bwdthExt": bwdthExt,
       "ispgrpExt": ispgrpExt,
       "qosExt": qosExt,
       "cctExt": cctExt,
       "ftpExt": ftpExt,
       "bootExt": bootExt,
       "appExt": appExt,
       "hssiExt": hssiExt,
       "chassisMgrExt": chassisMgrExt,
       "cnthotExt": cnthotExt,
       "flowMgrExt": flowMgrExt,
       "webMgmtExt": webMgmtExt,
       "csrpExt": csrpExt,
       "enetExt": enetExt,
       "dnsServerExt": dnsServerExt,
       "cntdnsExt": cntdnsExt,
       "eqlExt": eqlExt,
       "sshdExt": sshdExt,
       "ap64Stats": ap64Stats,
       "schedExt": schedExt,
       "kalExt": kalExt,
       "httpExt": httpExt,
       "dnshotExt": dnshotExt,
       "urqlExt": urqlExt,
       "nqlExt": nqlExt,
       "dqlExt": dqlExt,
       "cappUdpExt": cappUdpExt,
       "tagExt": tagExt,
       "proxDbExt": proxDbExt,
       "probeRttExt": probeRttExt,
       "plucExt": plucExt,
       "publishExt": publishExt,
       "subscribeExt": subscribeExt,
       "apLocal": apLocal,
       "chassis": chassis,
       "flash": flash,
       "apTemp": apTemp,
       "layerDepend": layerDepend,
       "apProducts": apProducts,
       "apCS100": apCS100,
       "apCS800": apCS800,
       "apCS150": apCS150,
       "apCS50": apCS50}
)
