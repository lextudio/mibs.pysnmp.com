# SNMP MIB module (ALTIGA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTIGA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:03 2024
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

(alMibModule,
 altigaGeneric) = mibBuilder.importSymbols(
    "ALTIGA-GLOBAL-REG",
    "alMibModule",
    "altigaGeneric")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

altigaMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 3, 1)
)
altigaMibModule.setRevisions(
        ("2004-12-30 00:00",
         "2003-10-20 00:00",
         "2003-04-10 00:00",
         "2002-10-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AltigaMib_ObjectIdentity = ObjectIdentity
altigaMib = _AltigaMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1)
)
_AltigaConfs_ObjectIdentity = ObjectIdentity
altigaConfs = _AltigaConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1)
)
_AltigaGroups_ObjectIdentity = ObjectIdentity
altigaGroups = _AltigaGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1)
)
_AlVersionGroup_ObjectIdentity = ObjectIdentity
alVersionGroup = _AlVersionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 1)
)
_AlAccessGroup_ObjectIdentity = ObjectIdentity
alAccessGroup = _AlAccessGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 2)
)
_AlPptpGroup_ObjectIdentity = ObjectIdentity
alPptpGroup = _AlPptpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 3)
)
_AlEventGroup_ObjectIdentity = ObjectIdentity
alEventGroup = _AlEventGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 4)
)
_AlAuthGroup_ObjectIdentity = ObjectIdentity
alAuthGroup = _AlAuthGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 5)
)
_AlPppGroup_ObjectIdentity = ObjectIdentity
alPppGroup = _AlPppGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 6)
)
_AlHttpGroup_ObjectIdentity = ObjectIdentity
alHttpGroup = _AlHttpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 7)
)
_AlIpGroup_ObjectIdentity = ObjectIdentity
alIpGroup = _AlIpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 8)
)
_AlFilterGroup_ObjectIdentity = ObjectIdentity
alFilterGroup = _AlFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 9)
)
_AlUserGroup_ObjectIdentity = ObjectIdentity
alUserGroup = _AlUserGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 10)
)
_AlTelnetGroup_ObjectIdentity = ObjectIdentity
alTelnetGroup = _AlTelnetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 11)
)
_AlFtpGroup_ObjectIdentity = ObjectIdentity
alFtpGroup = _AlFtpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 12)
)
_AlTftpGroup_ObjectIdentity = ObjectIdentity
alTftpGroup = _AlTftpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 13)
)
_AlSnmpGroup_ObjectIdentity = ObjectIdentity
alSnmpGroup = _AlSnmpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 14)
)
_AlIpSecGroup_ObjectIdentity = ObjectIdentity
alIpSecGroup = _AlIpSecGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 15)
)
_AlL2tpGroup_ObjectIdentity = ObjectIdentity
alL2tpGroup = _AlL2tpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 16)
)
_AlSessionGroup_ObjectIdentity = ObjectIdentity
alSessionGroup = _AlSessionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 17)
)
_AlDnsGroup_ObjectIdentity = ObjectIdentity
alDnsGroup = _AlDnsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 18)
)
_AlAddressGroup_ObjectIdentity = ObjectIdentity
alAddressGroup = _AlAddressGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 19)
)
_AlDhcpGroup_ObjectIdentity = ObjectIdentity
alDhcpGroup = _AlDhcpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 20)
)
_AlWatchdogGroup_ObjectIdentity = ObjectIdentity
alWatchdogGroup = _AlWatchdogGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 21)
)
_AlHardwareGroup_ObjectIdentity = ObjectIdentity
alHardwareGroup = _AlHardwareGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 22)
)
_AlNatGroup_ObjectIdentity = ObjectIdentity
alNatGroup = _AlNatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 23)
)
_AlLan2LanGroup_ObjectIdentity = ObjectIdentity
alLan2LanGroup = _AlLan2LanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 24)
)
_AlGeneralGroup_ObjectIdentity = ObjectIdentity
alGeneralGroup = _AlGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 25)
)
_AlSslGroup_ObjectIdentity = ObjectIdentity
alSslGroup = _AlSslGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 26)
)
_AlCertGroup_ObjectIdentity = ObjectIdentity
alCertGroup = _AlCertGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 27)
)
_AlNtpGroup_ObjectIdentity = ObjectIdentity
alNtpGroup = _AlNtpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 28)
)
_AlNetworkListGroup_ObjectIdentity = ObjectIdentity
alNetworkListGroup = _AlNetworkListGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 29)
)
_AlSepGroup_ObjectIdentity = ObjectIdentity
alSepGroup = _AlSepGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 30)
)
_AlIkeGroup_ObjectIdentity = ObjectIdentity
alIkeGroup = _AlIkeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 31)
)
_AlSyncGroup_ObjectIdentity = ObjectIdentity
alSyncGroup = _AlSyncGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 32)
)
_AlT1E1Group_ObjectIdentity = ObjectIdentity
alT1E1Group = _AlT1E1Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 33)
)
_AlMultiLinkGroup_ObjectIdentity = ObjectIdentity
alMultiLinkGroup = _AlMultiLinkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 34)
)
_AlSshGroup_ObjectIdentity = ObjectIdentity
alSshGroup = _AlSshGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 35)
)
_AlLBSSFGroup_ObjectIdentity = ObjectIdentity
alLBSSFGroup = _AlLBSSFGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 36)
)
_AlDhcpServerGroup_ObjectIdentity = ObjectIdentity
alDhcpServerGroup = _AlDhcpServerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 37)
)
_AlAutoUpdateGroup_ObjectIdentity = ObjectIdentity
alAutoUpdateGroup = _AlAutoUpdateGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 38)
)
_AlAdminAuthGroup_ObjectIdentity = ObjectIdentity
alAdminAuthGroup = _AlAdminAuthGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 39)
)
_AlPPPoEGroup_ObjectIdentity = ObjectIdentity
alPPPoEGroup = _AlPPPoEGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 40)
)
_AlXmlGroup_ObjectIdentity = ObjectIdentity
alXmlGroup = _AlXmlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 41)
)
_AlCtcpGroup_ObjectIdentity = ObjectIdentity
alCtcpGroup = _AlCtcpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 42)
)
_AlFwGroup_ObjectIdentity = ObjectIdentity
alFwGroup = _AlFwGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 43)
)
_AlGroupMatchGroup_ObjectIdentity = ObjectIdentity
alGroupMatchGroup = _AlGroupMatchGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 44)
)
_AlACEServerGroup_ObjectIdentity = ObjectIdentity
alACEServerGroup = _AlACEServerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 45)
)
_AlNatTGroup_ObjectIdentity = ObjectIdentity
alNatTGroup = _AlNatTGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 46)
)
_AlBwMgmtGroup_ObjectIdentity = ObjectIdentity
alBwMgmtGroup = _AlBwMgmtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 47)
)
_AlIpSecPreFragGroup_ObjectIdentity = ObjectIdentity
alIpSecPreFragGroup = _AlIpSecPreFragGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 48)
)
_AlFipsGroup_ObjectIdentity = ObjectIdentity
alFipsGroup = _AlFipsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 49)
)
_AlBackupL2LGroup_ObjectIdentity = ObjectIdentity
alBackupL2LGroup = _AlBackupL2LGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 50)
)
_AlNotifyGroup_ObjectIdentity = ObjectIdentity
alNotifyGroup = _AlNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 51)
)
_AlRebootStatusGroup_ObjectIdentity = ObjectIdentity
alRebootStatusGroup = _AlRebootStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 52)
)
_AlAuthorizationGroup_ObjectIdentity = ObjectIdentity
alAuthorizationGroup = _AlAuthorizationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 53)
)
_AlWebPortalGroup_ObjectIdentity = ObjectIdentity
alWebPortalGroup = _AlWebPortalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 54)
)
_AlWebEmailGroup_ObjectIdentity = ObjectIdentity
alWebEmailGroup = _AlWebEmailGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 55)
)
_AlPortForwardGroup_ObjectIdentity = ObjectIdentity
alPortForwardGroup = _AlPortForwardGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 56)
)
_AlRemoteServerGroup_ObjectIdentity = ObjectIdentity
alRemoteServerGroup = _AlRemoteServerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 57)
)
_AlWebvpnAclGroup_ObjectIdentity = ObjectIdentity
alWebvpnAclGroup = _AlWebvpnAclGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 58)
)
_AlNbnsGroup_ObjectIdentity = ObjectIdentity
alNbnsGroup = _AlNbnsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 59)
)
_AlSecureDesktopGroup_ObjectIdentity = ObjectIdentity
alSecureDesktopGroup = _AlSecureDesktopGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 60)
)
_AlSslTunnelClientGroup_ObjectIdentity = ObjectIdentity
alSslTunnelClientGroup = _AlSslTunnelClientGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 61)
)
_AlNacGroup_ObjectIdentity = ObjectIdentity
alNacGroup = _AlNacGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 62)
)
_AltigaCompl_ObjectIdentity = ObjectIdentity
altigaCompl = _AltigaCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 2)
)
_AltigaStats_ObjectIdentity = ObjectIdentity
altigaStats = _AltigaStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2)
)
_AlStatsVersion_ObjectIdentity = ObjectIdentity
alStatsVersion = _AlStatsVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1)
)
_AlStatsAccess_ObjectIdentity = ObjectIdentity
alStatsAccess = _AlStatsAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 2)
)
_AlStatsPptp_ObjectIdentity = ObjectIdentity
alStatsPptp = _AlStatsPptp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3)
)
_AlStatsEvent_ObjectIdentity = ObjectIdentity
alStatsEvent = _AlStatsEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4)
)
_AlStatsAuth_ObjectIdentity = ObjectIdentity
alStatsAuth = _AlStatsAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 5)
)
_AlStatsPpp_ObjectIdentity = ObjectIdentity
alStatsPpp = _AlStatsPpp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 6)
)
_AlStatsHttp_ObjectIdentity = ObjectIdentity
alStatsHttp = _AlStatsHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 7)
)
_AlStatsIp_ObjectIdentity = ObjectIdentity
alStatsIp = _AlStatsIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 8)
)
_AlStatsFilter_ObjectIdentity = ObjectIdentity
alStatsFilter = _AlStatsFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 9)
)
_AlStatsUser_ObjectIdentity = ObjectIdentity
alStatsUser = _AlStatsUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 10)
)
_AlStatsTelnet_ObjectIdentity = ObjectIdentity
alStatsTelnet = _AlStatsTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11)
)
_AlStatsFtp_ObjectIdentity = ObjectIdentity
alStatsFtp = _AlStatsFtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 12)
)
_AlStatsTftp_ObjectIdentity = ObjectIdentity
alStatsTftp = _AlStatsTftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 13)
)
_AlStatsSnmp_ObjectIdentity = ObjectIdentity
alStatsSnmp = _AlStatsSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 14)
)
_AlStatsIpSec_ObjectIdentity = ObjectIdentity
alStatsIpSec = _AlStatsIpSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 15)
)
_AlStatsL2tp_ObjectIdentity = ObjectIdentity
alStatsL2tp = _AlStatsL2tp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16)
)
_AlStatsSession_ObjectIdentity = ObjectIdentity
alStatsSession = _AlStatsSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17)
)
_AlStatsDns_ObjectIdentity = ObjectIdentity
alStatsDns = _AlStatsDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 18)
)
_AlStatsAddress_ObjectIdentity = ObjectIdentity
alStatsAddress = _AlStatsAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19)
)
_AlStatsDhcp_ObjectIdentity = ObjectIdentity
alStatsDhcp = _AlStatsDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 20)
)
_AlStatsWatching_ObjectIdentity = ObjectIdentity
alStatsWatching = _AlStatsWatching_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 21)
)
_AlStatsHardware_ObjectIdentity = ObjectIdentity
alStatsHardware = _AlStatsHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22)
)
_AlStatsNat_ObjectIdentity = ObjectIdentity
alStatsNat = _AlStatsNat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23)
)
_AlStatsLan2Lan_ObjectIdentity = ObjectIdentity
alStatsLan2Lan = _AlStatsLan2Lan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 24)
)
_AlStatsGeneral_ObjectIdentity = ObjectIdentity
alStatsGeneral = _AlStatsGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 25)
)
_AlStatsSsl_ObjectIdentity = ObjectIdentity
alStatsSsl = _AlStatsSsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26)
)
_AlStatsCert_ObjectIdentity = ObjectIdentity
alStatsCert = _AlStatsCert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27)
)
_AlStatsNtp_ObjectIdentity = ObjectIdentity
alStatsNtp = _AlStatsNtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 28)
)
_AlStatsNetworkList_ObjectIdentity = ObjectIdentity
alStatsNetworkList = _AlStatsNetworkList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 29)
)
_AlStatsSep_ObjectIdentity = ObjectIdentity
alStatsSep = _AlStatsSep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30)
)
_AlStatsIke_ObjectIdentity = ObjectIdentity
alStatsIke = _AlStatsIke_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 31)
)
_AlStatsSync_ObjectIdentity = ObjectIdentity
alStatsSync = _AlStatsSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 32)
)
_AlStatsT1E1_ObjectIdentity = ObjectIdentity
alStatsT1E1 = _AlStatsT1E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33)
)
_AlStatsMultiLink_ObjectIdentity = ObjectIdentity
alStatsMultiLink = _AlStatsMultiLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 34)
)
_AlStatsSsh_ObjectIdentity = ObjectIdentity
alStatsSsh = _AlStatsSsh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 35)
)
_AlStatsLBSSF_ObjectIdentity = ObjectIdentity
alStatsLBSSF = _AlStatsLBSSF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 36)
)
_AlStatsDhcpServer_ObjectIdentity = ObjectIdentity
alStatsDhcpServer = _AlStatsDhcpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 37)
)
_AlStatsAutoUpdate_ObjectIdentity = ObjectIdentity
alStatsAutoUpdate = _AlStatsAutoUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 38)
)
_AlAdminAuthStats_ObjectIdentity = ObjectIdentity
alAdminAuthStats = _AlAdminAuthStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 39)
)
_AlStatsPPPoE_ObjectIdentity = ObjectIdentity
alStatsPPPoE = _AlStatsPPPoE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40)
)
_AlXmlStats_ObjectIdentity = ObjectIdentity
alXmlStats = _AlXmlStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 41)
)
_AlCtcpStats_ObjectIdentity = ObjectIdentity
alCtcpStats = _AlCtcpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 42)
)
_AlFwStats_ObjectIdentity = ObjectIdentity
alFwStats = _AlFwStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 43)
)
_AlStatsGroupMatch_ObjectIdentity = ObjectIdentity
alStatsGroupMatch = _AlStatsGroupMatch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 44)
)
_AlACEServerStats_ObjectIdentity = ObjectIdentity
alACEServerStats = _AlACEServerStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 45)
)
_AlNatTStats_ObjectIdentity = ObjectIdentity
alNatTStats = _AlNatTStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 46)
)
_AlStatsBwMgmt_ObjectIdentity = ObjectIdentity
alStatsBwMgmt = _AlStatsBwMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 47)
)
_AlIpSecPreFragStats_ObjectIdentity = ObjectIdentity
alIpSecPreFragStats = _AlIpSecPreFragStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 48)
)
_AlStatsFips_ObjectIdentity = ObjectIdentity
alStatsFips = _AlStatsFips_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 49)
)
_AlStatsBackupL2L_ObjectIdentity = ObjectIdentity
alStatsBackupL2L = _AlStatsBackupL2L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 50)
)
_AlStatsNotify_ObjectIdentity = ObjectIdentity
alStatsNotify = _AlStatsNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 51)
)
_AlStatsRebootStatus_ObjectIdentity = ObjectIdentity
alStatsRebootStatus = _AlStatsRebootStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 52)
)
_AlStatsAuthorization_ObjectIdentity = ObjectIdentity
alStatsAuthorization = _AlStatsAuthorization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 53)
)
_AlStatsWebPortal_ObjectIdentity = ObjectIdentity
alStatsWebPortal = _AlStatsWebPortal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 54)
)
_AlStatsWebEmail_ObjectIdentity = ObjectIdentity
alStatsWebEmail = _AlStatsWebEmail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 55)
)
_AlStatsPortForward_ObjectIdentity = ObjectIdentity
alStatsPortForward = _AlStatsPortForward_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 56)
)
_AlStatsRemoteServer_ObjectIdentity = ObjectIdentity
alStatsRemoteServer = _AlStatsRemoteServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 57)
)
_AlStatsWebvpnAcl_ObjectIdentity = ObjectIdentity
alStatsWebvpnAcl = _AlStatsWebvpnAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 58)
)
_AlStatsNbns_ObjectIdentity = ObjectIdentity
alStatsNbns = _AlStatsNbns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 59)
)
_AlStatsSecureDesktop_ObjectIdentity = ObjectIdentity
alStatsSecureDesktop = _AlStatsSecureDesktop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 60)
)
_AlStatsSslTunnelClient_ObjectIdentity = ObjectIdentity
alStatsSslTunnelClient = _AlStatsSslTunnelClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 61)
)
_AlStatsNac_ObjectIdentity = ObjectIdentity
alStatsNac = _AlStatsNac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 62)
)
_AltigaConfig_ObjectIdentity = ObjectIdentity
altigaConfig = _AltigaConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3)
)
_AlCfgVersion_ObjectIdentity = ObjectIdentity
alCfgVersion = _AlCfgVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 1)
)
_AlCfgAccess_ObjectIdentity = ObjectIdentity
alCfgAccess = _AlCfgAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 2)
)
_AlCfgPptp_ObjectIdentity = ObjectIdentity
alCfgPptp = _AlCfgPptp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 3)
)
_AlCfgEvent_ObjectIdentity = ObjectIdentity
alCfgEvent = _AlCfgEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 4)
)
_AlCfgAuth_ObjectIdentity = ObjectIdentity
alCfgAuth = _AlCfgAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 5)
)
_AlCfgPpp_ObjectIdentity = ObjectIdentity
alCfgPpp = _AlCfgPpp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 6)
)
_AlCfgHttp_ObjectIdentity = ObjectIdentity
alCfgHttp = _AlCfgHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 7)
)
_AlCfgIp_ObjectIdentity = ObjectIdentity
alCfgIp = _AlCfgIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 8)
)
_AlCfgFilter_ObjectIdentity = ObjectIdentity
alCfgFilter = _AlCfgFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 9)
)
_AlCfgUser_ObjectIdentity = ObjectIdentity
alCfgUser = _AlCfgUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 10)
)
_AlCfgTelnet_ObjectIdentity = ObjectIdentity
alCfgTelnet = _AlCfgTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 11)
)
_AlCfgFtp_ObjectIdentity = ObjectIdentity
alCfgFtp = _AlCfgFtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 12)
)
_AlCfgTftp_ObjectIdentity = ObjectIdentity
alCfgTftp = _AlCfgTftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 13)
)
_AlCfgSnmp_ObjectIdentity = ObjectIdentity
alCfgSnmp = _AlCfgSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 14)
)
_AlCfgIpSec_ObjectIdentity = ObjectIdentity
alCfgIpSec = _AlCfgIpSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 15)
)
_AlCfgL2tp_ObjectIdentity = ObjectIdentity
alCfgL2tp = _AlCfgL2tp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 16)
)
_AlCfgSession_ObjectIdentity = ObjectIdentity
alCfgSession = _AlCfgSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 17)
)
_AlCfgDns_ObjectIdentity = ObjectIdentity
alCfgDns = _AlCfgDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 18)
)
_AlCfgAddress_ObjectIdentity = ObjectIdentity
alCfgAddress = _AlCfgAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 19)
)
_AlCfgDhcp_ObjectIdentity = ObjectIdentity
alCfgDhcp = _AlCfgDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 20)
)
_AlCfgWatchdog_ObjectIdentity = ObjectIdentity
alCfgWatchdog = _AlCfgWatchdog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 21)
)
_AlCfgHardware_ObjectIdentity = ObjectIdentity
alCfgHardware = _AlCfgHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 22)
)
_AlCfgNat_ObjectIdentity = ObjectIdentity
alCfgNat = _AlCfgNat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 23)
)
_AlCfgLan2Lan_ObjectIdentity = ObjectIdentity
alCfgLan2Lan = _AlCfgLan2Lan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 24)
)
_AlCfgGeneral_ObjectIdentity = ObjectIdentity
alCfgGeneral = _AlCfgGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 25)
)
_AlCfgSsl_ObjectIdentity = ObjectIdentity
alCfgSsl = _AlCfgSsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 26)
)
_AlCfgCert_ObjectIdentity = ObjectIdentity
alCfgCert = _AlCfgCert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 27)
)
_AlCfgNtp_ObjectIdentity = ObjectIdentity
alCfgNtp = _AlCfgNtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 28)
)
_AlCfgNetworkList_ObjectIdentity = ObjectIdentity
alCfgNetworkList = _AlCfgNetworkList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 29)
)
_AlCfgSep_ObjectIdentity = ObjectIdentity
alCfgSep = _AlCfgSep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 30)
)
_AlCfgIke_ObjectIdentity = ObjectIdentity
alCfgIke = _AlCfgIke_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 31)
)
_AlCfgSync_ObjectIdentity = ObjectIdentity
alCfgSync = _AlCfgSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 32)
)
_AlCfgT1E1_ObjectIdentity = ObjectIdentity
alCfgT1E1 = _AlCfgT1E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 33)
)
_AlCfgMultiLink_ObjectIdentity = ObjectIdentity
alCfgMultiLink = _AlCfgMultiLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 34)
)
_AlCfgSsh_ObjectIdentity = ObjectIdentity
alCfgSsh = _AlCfgSsh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 35)
)
_AlCfgLBSSF_ObjectIdentity = ObjectIdentity
alCfgLBSSF = _AlCfgLBSSF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 36)
)
_AlCfgDhcpServer_ObjectIdentity = ObjectIdentity
alCfgDhcpServer = _AlCfgDhcpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 37)
)
_AlCfgAutoUpdate_ObjectIdentity = ObjectIdentity
alCfgAutoUpdate = _AlCfgAutoUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 38)
)
_AlCfgAdminAuth_ObjectIdentity = ObjectIdentity
alCfgAdminAuth = _AlCfgAdminAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 39)
)
_AlCfgPPPoE_ObjectIdentity = ObjectIdentity
alCfgPPPoE = _AlCfgPPPoE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 40)
)
_AlCfgXml_ObjectIdentity = ObjectIdentity
alCfgXml = _AlCfgXml_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 41)
)
_AlCfgCtcp_ObjectIdentity = ObjectIdentity
alCfgCtcp = _AlCfgCtcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 42)
)
_AlCfgFw_ObjectIdentity = ObjectIdentity
alCfgFw = _AlCfgFw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 43)
)
_AlCfgGroupMatch_ObjectIdentity = ObjectIdentity
alCfgGroupMatch = _AlCfgGroupMatch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 44)
)
_AlCfgACE_ObjectIdentity = ObjectIdentity
alCfgACE = _AlCfgACE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 45)
)
_AlCfgNatT_ObjectIdentity = ObjectIdentity
alCfgNatT = _AlCfgNatT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 46)
)
_AlCfgBwMgmt_ObjectIdentity = ObjectIdentity
alCfgBwMgmt = _AlCfgBwMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 47)
)
_AlCfgIpSecPreFrag_ObjectIdentity = ObjectIdentity
alCfgIpSecPreFrag = _AlCfgIpSecPreFrag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 48)
)
_AlCfgFips_ObjectIdentity = ObjectIdentity
alCfgFips = _AlCfgFips_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 49)
)
_AlCfgBackupL2L_ObjectIdentity = ObjectIdentity
alCfgBackupL2L = _AlCfgBackupL2L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 50)
)
_AlCfgNotify_ObjectIdentity = ObjectIdentity
alCfgNotify = _AlCfgNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 51)
)
_AlCfgRebootStatus_ObjectIdentity = ObjectIdentity
alCfgRebootStatus = _AlCfgRebootStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 52)
)
_AlCfgAuthorization_ObjectIdentity = ObjectIdentity
alCfgAuthorization = _AlCfgAuthorization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 53)
)
_AlCfgWebPortal_ObjectIdentity = ObjectIdentity
alCfgWebPortal = _AlCfgWebPortal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 54)
)
_AlCfgWebEmail_ObjectIdentity = ObjectIdentity
alCfgWebEmail = _AlCfgWebEmail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 55)
)
_AlCfgPortForward_ObjectIdentity = ObjectIdentity
alCfgPortForward = _AlCfgPortForward_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 56)
)
_AlCfgRemoteServer_ObjectIdentity = ObjectIdentity
alCfgRemoteServer = _AlCfgRemoteServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 57)
)
_AlCfgWebvpnAcl_ObjectIdentity = ObjectIdentity
alCfgWebvpnAcl = _AlCfgWebvpnAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 58)
)
_AlCfgNbns_ObjectIdentity = ObjectIdentity
alCfgNbns = _AlCfgNbns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 59)
)
_AlCfgSecureDesktop_ObjectIdentity = ObjectIdentity
alCfgSecureDesktop = _AlCfgSecureDesktop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 60)
)
_AlCfgSslTunnelClient_ObjectIdentity = ObjectIdentity
alCfgSslTunnelClient = _AlCfgSslTunnelClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 61)
)
_AlCfgNac_ObjectIdentity = ObjectIdentity
alCfgNac = _AlCfgNac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 3, 62)
)
_AltigaEvents_ObjectIdentity = ObjectIdentity
altigaEvents = _AltigaEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4)
)
_AlEventsVersion_ObjectIdentity = ObjectIdentity
alEventsVersion = _AlEventsVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 1)
)
_AlEventsAccess_ObjectIdentity = ObjectIdentity
alEventsAccess = _AlEventsAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 2)
)
_AlEventsPptp_ObjectIdentity = ObjectIdentity
alEventsPptp = _AlEventsPptp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 3)
)
_AlEventsEvent_ObjectIdentity = ObjectIdentity
alEventsEvent = _AlEventsEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 4)
)
_AlEventsAuth_ObjectIdentity = ObjectIdentity
alEventsAuth = _AlEventsAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 5)
)
_AlEventsPpp_ObjectIdentity = ObjectIdentity
alEventsPpp = _AlEventsPpp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 6)
)
_AlEventsHttp_ObjectIdentity = ObjectIdentity
alEventsHttp = _AlEventsHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 7)
)
_AlEventsIp_ObjectIdentity = ObjectIdentity
alEventsIp = _AlEventsIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 8)
)
_AlEventsFilter_ObjectIdentity = ObjectIdentity
alEventsFilter = _AlEventsFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 9)
)
_AlEventsUser_ObjectIdentity = ObjectIdentity
alEventsUser = _AlEventsUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 10)
)
_AlEventsTelnet_ObjectIdentity = ObjectIdentity
alEventsTelnet = _AlEventsTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 11)
)
_AlEventsFtp_ObjectIdentity = ObjectIdentity
alEventsFtp = _AlEventsFtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 12)
)
_AlEventsTftp_ObjectIdentity = ObjectIdentity
alEventsTftp = _AlEventsTftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 13)
)
_AlEventsSnmp_ObjectIdentity = ObjectIdentity
alEventsSnmp = _AlEventsSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 14)
)
_AlEventsIpSec_ObjectIdentity = ObjectIdentity
alEventsIpSec = _AlEventsIpSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 15)
)
_AlEventsL2tp_ObjectIdentity = ObjectIdentity
alEventsL2tp = _AlEventsL2tp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 16)
)
_AlEventsSession_ObjectIdentity = ObjectIdentity
alEventsSession = _AlEventsSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 17)
)
_AlEventsDns_ObjectIdentity = ObjectIdentity
alEventsDns = _AlEventsDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 18)
)
_AlEventsAddress_ObjectIdentity = ObjectIdentity
alEventsAddress = _AlEventsAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 19)
)
_AlEventsDhcp_ObjectIdentity = ObjectIdentity
alEventsDhcp = _AlEventsDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 20)
)
_AlEventsWatchdog_ObjectIdentity = ObjectIdentity
alEventsWatchdog = _AlEventsWatchdog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 21)
)
_AlEventsHardware_ObjectIdentity = ObjectIdentity
alEventsHardware = _AlEventsHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 22)
)
_AlEventsNat_ObjectIdentity = ObjectIdentity
alEventsNat = _AlEventsNat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 23)
)
_AlEventsLan2Lan_ObjectIdentity = ObjectIdentity
alEventsLan2Lan = _AlEventsLan2Lan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 24)
)
_AlEventsGeneral_ObjectIdentity = ObjectIdentity
alEventsGeneral = _AlEventsGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 25)
)
_AlEventsSsl_ObjectIdentity = ObjectIdentity
alEventsSsl = _AlEventsSsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 26)
)
_AlEventsCert_ObjectIdentity = ObjectIdentity
alEventsCert = _AlEventsCert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 27)
)
_AlEventsNtp_ObjectIdentity = ObjectIdentity
alEventsNtp = _AlEventsNtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 28)
)
_AlEventsNetworkList_ObjectIdentity = ObjectIdentity
alEventsNetworkList = _AlEventsNetworkList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 29)
)
_AlEventsSep_ObjectIdentity = ObjectIdentity
alEventsSep = _AlEventsSep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 30)
)
_AlEventsIke_ObjectIdentity = ObjectIdentity
alEventsIke = _AlEventsIke_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 31)
)
_AlEventsSync_ObjectIdentity = ObjectIdentity
alEventsSync = _AlEventsSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 32)
)
_AlEventsT1E1_ObjectIdentity = ObjectIdentity
alEventsT1E1 = _AlEventsT1E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 33)
)
_AlEventsMultiLink_ObjectIdentity = ObjectIdentity
alEventsMultiLink = _AlEventsMultiLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 34)
)
_AlEventsSsh_ObjectIdentity = ObjectIdentity
alEventsSsh = _AlEventsSsh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 35)
)
_AlEventsLBSSF_ObjectIdentity = ObjectIdentity
alEventsLBSSF = _AlEventsLBSSF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 36)
)
_AlEventsAutoUpdate_ObjectIdentity = ObjectIdentity
alEventsAutoUpdate = _AlEventsAutoUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 38)
)
_AlEventsAdminAuth_ObjectIdentity = ObjectIdentity
alEventsAdminAuth = _AlEventsAdminAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 39)
)
_AlEventsPPPoE_ObjectIdentity = ObjectIdentity
alEventsPPPoE = _AlEventsPPPoE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 40)
)
_AlEventXml_ObjectIdentity = ObjectIdentity
alEventXml = _AlEventXml_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 41)
)
_AlEventCtcp_ObjectIdentity = ObjectIdentity
alEventCtcp = _AlEventCtcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 42)
)
_AlEventFw_ObjectIdentity = ObjectIdentity
alEventFw = _AlEventFw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 43)
)
_AlEventGroupMatch_ObjectIdentity = ObjectIdentity
alEventGroupMatch = _AlEventGroupMatch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 44)
)
_AlEventACE_ObjectIdentity = ObjectIdentity
alEventACE = _AlEventACE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 45)
)
_AlEventNatT_ObjectIdentity = ObjectIdentity
alEventNatT = _AlEventNatT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 46)
)
_AlEventBwMgmt_ObjectIdentity = ObjectIdentity
alEventBwMgmt = _AlEventBwMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 47)
)
_AlEventIpSecPreFrag_ObjectIdentity = ObjectIdentity
alEventIpSecPreFrag = _AlEventIpSecPreFrag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 48)
)
_AlEventFips_ObjectIdentity = ObjectIdentity
alEventFips = _AlEventFips_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 49)
)
_AlEventBackupL2L_ObjectIdentity = ObjectIdentity
alEventBackupL2L = _AlEventBackupL2L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 50)
)
_AlEventsNotify_ObjectIdentity = ObjectIdentity
alEventsNotify = _AlEventsNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 51)
)
_AlEventsRebootStatus_ObjectIdentity = ObjectIdentity
alEventsRebootStatus = _AlEventsRebootStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 52)
)
_AlEventAuthorization_ObjectIdentity = ObjectIdentity
alEventAuthorization = _AlEventAuthorization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 53)
)
_AlEventWebPortal_ObjectIdentity = ObjectIdentity
alEventWebPortal = _AlEventWebPortal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 54)
)
_AlEventWebEmail_ObjectIdentity = ObjectIdentity
alEventWebEmail = _AlEventWebEmail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 55)
)
_AlEventPortForward_ObjectIdentity = ObjectIdentity
alEventPortForward = _AlEventPortForward_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 56)
)
_AlEventRemoteServer_ObjectIdentity = ObjectIdentity
alEventRemoteServer = _AlEventRemoteServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 57)
)
_AlEventWebvpnAcl_ObjectIdentity = ObjectIdentity
alEventWebvpnAcl = _AlEventWebvpnAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 58)
)
_AlEventNbns_ObjectIdentity = ObjectIdentity
alEventNbns = _AlEventNbns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 59)
)
_AlEventSecureDesktop_ObjectIdentity = ObjectIdentity
alEventSecureDesktop = _AlEventSecureDesktop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 60)
)
_AlEventSslTunnelClient_ObjectIdentity = ObjectIdentity
alEventSslTunnelClient = _AlEventSslTunnelClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 61)
)
_AlEventNac_ObjectIdentity = ObjectIdentity
alEventNac = _AlEventNac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 4, 62)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTIGA-MIB",
    **{"altigaMibModule": altigaMibModule,
       "altigaMib": altigaMib,
       "altigaConfs": altigaConfs,
       "altigaGroups": altigaGroups,
       "alVersionGroup": alVersionGroup,
       "alAccessGroup": alAccessGroup,
       "alPptpGroup": alPptpGroup,
       "alEventGroup": alEventGroup,
       "alAuthGroup": alAuthGroup,
       "alPppGroup": alPppGroup,
       "alHttpGroup": alHttpGroup,
       "alIpGroup": alIpGroup,
       "alFilterGroup": alFilterGroup,
       "alUserGroup": alUserGroup,
       "alTelnetGroup": alTelnetGroup,
       "alFtpGroup": alFtpGroup,
       "alTftpGroup": alTftpGroup,
       "alSnmpGroup": alSnmpGroup,
       "alIpSecGroup": alIpSecGroup,
       "alL2tpGroup": alL2tpGroup,
       "alSessionGroup": alSessionGroup,
       "alDnsGroup": alDnsGroup,
       "alAddressGroup": alAddressGroup,
       "alDhcpGroup": alDhcpGroup,
       "alWatchdogGroup": alWatchdogGroup,
       "alHardwareGroup": alHardwareGroup,
       "alNatGroup": alNatGroup,
       "alLan2LanGroup": alLan2LanGroup,
       "alGeneralGroup": alGeneralGroup,
       "alSslGroup": alSslGroup,
       "alCertGroup": alCertGroup,
       "alNtpGroup": alNtpGroup,
       "alNetworkListGroup": alNetworkListGroup,
       "alSepGroup": alSepGroup,
       "alIkeGroup": alIkeGroup,
       "alSyncGroup": alSyncGroup,
       "alT1E1Group": alT1E1Group,
       "alMultiLinkGroup": alMultiLinkGroup,
       "alSshGroup": alSshGroup,
       "alLBSSFGroup": alLBSSFGroup,
       "alDhcpServerGroup": alDhcpServerGroup,
       "alAutoUpdateGroup": alAutoUpdateGroup,
       "alAdminAuthGroup": alAdminAuthGroup,
       "alPPPoEGroup": alPPPoEGroup,
       "alXmlGroup": alXmlGroup,
       "alCtcpGroup": alCtcpGroup,
       "alFwGroup": alFwGroup,
       "alGroupMatchGroup": alGroupMatchGroup,
       "alACEServerGroup": alACEServerGroup,
       "alNatTGroup": alNatTGroup,
       "alBwMgmtGroup": alBwMgmtGroup,
       "alIpSecPreFragGroup": alIpSecPreFragGroup,
       "alFipsGroup": alFipsGroup,
       "alBackupL2LGroup": alBackupL2LGroup,
       "alNotifyGroup": alNotifyGroup,
       "alRebootStatusGroup": alRebootStatusGroup,
       "alAuthorizationGroup": alAuthorizationGroup,
       "alWebPortalGroup": alWebPortalGroup,
       "alWebEmailGroup": alWebEmailGroup,
       "alPortForwardGroup": alPortForwardGroup,
       "alRemoteServerGroup": alRemoteServerGroup,
       "alWebvpnAclGroup": alWebvpnAclGroup,
       "alNbnsGroup": alNbnsGroup,
       "alSecureDesktopGroup": alSecureDesktopGroup,
       "alSslTunnelClientGroup": alSslTunnelClientGroup,
       "alNacGroup": alNacGroup,
       "altigaCompl": altigaCompl,
       "altigaStats": altigaStats,
       "alStatsVersion": alStatsVersion,
       "alStatsAccess": alStatsAccess,
       "alStatsPptp": alStatsPptp,
       "alStatsEvent": alStatsEvent,
       "alStatsAuth": alStatsAuth,
       "alStatsPpp": alStatsPpp,
       "alStatsHttp": alStatsHttp,
       "alStatsIp": alStatsIp,
       "alStatsFilter": alStatsFilter,
       "alStatsUser": alStatsUser,
       "alStatsTelnet": alStatsTelnet,
       "alStatsFtp": alStatsFtp,
       "alStatsTftp": alStatsTftp,
       "alStatsSnmp": alStatsSnmp,
       "alStatsIpSec": alStatsIpSec,
       "alStatsL2tp": alStatsL2tp,
       "alStatsSession": alStatsSession,
       "alStatsDns": alStatsDns,
       "alStatsAddress": alStatsAddress,
       "alStatsDhcp": alStatsDhcp,
       "alStatsWatching": alStatsWatching,
       "alStatsHardware": alStatsHardware,
       "alStatsNat": alStatsNat,
       "alStatsLan2Lan": alStatsLan2Lan,
       "alStatsGeneral": alStatsGeneral,
       "alStatsSsl": alStatsSsl,
       "alStatsCert": alStatsCert,
       "alStatsNtp": alStatsNtp,
       "alStatsNetworkList": alStatsNetworkList,
       "alStatsSep": alStatsSep,
       "alStatsIke": alStatsIke,
       "alStatsSync": alStatsSync,
       "alStatsT1E1": alStatsT1E1,
       "alStatsMultiLink": alStatsMultiLink,
       "alStatsSsh": alStatsSsh,
       "alStatsLBSSF": alStatsLBSSF,
       "alStatsDhcpServer": alStatsDhcpServer,
       "alStatsAutoUpdate": alStatsAutoUpdate,
       "alAdminAuthStats": alAdminAuthStats,
       "alStatsPPPoE": alStatsPPPoE,
       "alXmlStats": alXmlStats,
       "alCtcpStats": alCtcpStats,
       "alFwStats": alFwStats,
       "alStatsGroupMatch": alStatsGroupMatch,
       "alACEServerStats": alACEServerStats,
       "alNatTStats": alNatTStats,
       "alStatsBwMgmt": alStatsBwMgmt,
       "alIpSecPreFragStats": alIpSecPreFragStats,
       "alStatsFips": alStatsFips,
       "alStatsBackupL2L": alStatsBackupL2L,
       "alStatsNotify": alStatsNotify,
       "alStatsRebootStatus": alStatsRebootStatus,
       "alStatsAuthorization": alStatsAuthorization,
       "alStatsWebPortal": alStatsWebPortal,
       "alStatsWebEmail": alStatsWebEmail,
       "alStatsPortForward": alStatsPortForward,
       "alStatsRemoteServer": alStatsRemoteServer,
       "alStatsWebvpnAcl": alStatsWebvpnAcl,
       "alStatsNbns": alStatsNbns,
       "alStatsSecureDesktop": alStatsSecureDesktop,
       "alStatsSslTunnelClient": alStatsSslTunnelClient,
       "alStatsNac": alStatsNac,
       "altigaConfig": altigaConfig,
       "alCfgVersion": alCfgVersion,
       "alCfgAccess": alCfgAccess,
       "alCfgPptp": alCfgPptp,
       "alCfgEvent": alCfgEvent,
       "alCfgAuth": alCfgAuth,
       "alCfgPpp": alCfgPpp,
       "alCfgHttp": alCfgHttp,
       "alCfgIp": alCfgIp,
       "alCfgFilter": alCfgFilter,
       "alCfgUser": alCfgUser,
       "alCfgTelnet": alCfgTelnet,
       "alCfgFtp": alCfgFtp,
       "alCfgTftp": alCfgTftp,
       "alCfgSnmp": alCfgSnmp,
       "alCfgIpSec": alCfgIpSec,
       "alCfgL2tp": alCfgL2tp,
       "alCfgSession": alCfgSession,
       "alCfgDns": alCfgDns,
       "alCfgAddress": alCfgAddress,
       "alCfgDhcp": alCfgDhcp,
       "alCfgWatchdog": alCfgWatchdog,
       "alCfgHardware": alCfgHardware,
       "alCfgNat": alCfgNat,
       "alCfgLan2Lan": alCfgLan2Lan,
       "alCfgGeneral": alCfgGeneral,
       "alCfgSsl": alCfgSsl,
       "alCfgCert": alCfgCert,
       "alCfgNtp": alCfgNtp,
       "alCfgNetworkList": alCfgNetworkList,
       "alCfgSep": alCfgSep,
       "alCfgIke": alCfgIke,
       "alCfgSync": alCfgSync,
       "alCfgT1E1": alCfgT1E1,
       "alCfgMultiLink": alCfgMultiLink,
       "alCfgSsh": alCfgSsh,
       "alCfgLBSSF": alCfgLBSSF,
       "alCfgDhcpServer": alCfgDhcpServer,
       "alCfgAutoUpdate": alCfgAutoUpdate,
       "alCfgAdminAuth": alCfgAdminAuth,
       "alCfgPPPoE": alCfgPPPoE,
       "alCfgXml": alCfgXml,
       "alCfgCtcp": alCfgCtcp,
       "alCfgFw": alCfgFw,
       "alCfgGroupMatch": alCfgGroupMatch,
       "alCfgACE": alCfgACE,
       "alCfgNatT": alCfgNatT,
       "alCfgBwMgmt": alCfgBwMgmt,
       "alCfgIpSecPreFrag": alCfgIpSecPreFrag,
       "alCfgFips": alCfgFips,
       "alCfgBackupL2L": alCfgBackupL2L,
       "alCfgNotify": alCfgNotify,
       "alCfgRebootStatus": alCfgRebootStatus,
       "alCfgAuthorization": alCfgAuthorization,
       "alCfgWebPortal": alCfgWebPortal,
       "alCfgWebEmail": alCfgWebEmail,
       "alCfgPortForward": alCfgPortForward,
       "alCfgRemoteServer": alCfgRemoteServer,
       "alCfgWebvpnAcl": alCfgWebvpnAcl,
       "alCfgNbns": alCfgNbns,
       "alCfgSecureDesktop": alCfgSecureDesktop,
       "alCfgSslTunnelClient": alCfgSslTunnelClient,
       "alCfgNac": alCfgNac,
       "altigaEvents": altigaEvents,
       "alEventsVersion": alEventsVersion,
       "alEventsAccess": alEventsAccess,
       "alEventsPptp": alEventsPptp,
       "alEventsEvent": alEventsEvent,
       "alEventsAuth": alEventsAuth,
       "alEventsPpp": alEventsPpp,
       "alEventsHttp": alEventsHttp,
       "alEventsIp": alEventsIp,
       "alEventsFilter": alEventsFilter,
       "alEventsUser": alEventsUser,
       "alEventsTelnet": alEventsTelnet,
       "alEventsFtp": alEventsFtp,
       "alEventsTftp": alEventsTftp,
       "alEventsSnmp": alEventsSnmp,
       "alEventsIpSec": alEventsIpSec,
       "alEventsL2tp": alEventsL2tp,
       "alEventsSession": alEventsSession,
       "alEventsDns": alEventsDns,
       "alEventsAddress": alEventsAddress,
       "alEventsDhcp": alEventsDhcp,
       "alEventsWatchdog": alEventsWatchdog,
       "alEventsHardware": alEventsHardware,
       "alEventsNat": alEventsNat,
       "alEventsLan2Lan": alEventsLan2Lan,
       "alEventsGeneral": alEventsGeneral,
       "alEventsSsl": alEventsSsl,
       "alEventsCert": alEventsCert,
       "alEventsNtp": alEventsNtp,
       "alEventsNetworkList": alEventsNetworkList,
       "alEventsSep": alEventsSep,
       "alEventsIke": alEventsIke,
       "alEventsSync": alEventsSync,
       "alEventsT1E1": alEventsT1E1,
       "alEventsMultiLink": alEventsMultiLink,
       "alEventsSsh": alEventsSsh,
       "alEventsLBSSF": alEventsLBSSF,
       "alEventsAutoUpdate": alEventsAutoUpdate,
       "alEventsAdminAuth": alEventsAdminAuth,
       "alEventsPPPoE": alEventsPPPoE,
       "alEventXml": alEventXml,
       "alEventCtcp": alEventCtcp,
       "alEventFw": alEventFw,
       "alEventGroupMatch": alEventGroupMatch,
       "alEventACE": alEventACE,
       "alEventNatT": alEventNatT,
       "alEventBwMgmt": alEventBwMgmt,
       "alEventIpSecPreFrag": alEventIpSecPreFrag,
       "alEventFips": alEventFips,
       "alEventBackupL2L": alEventBackupL2L,
       "alEventsNotify": alEventsNotify,
       "alEventsRebootStatus": alEventsRebootStatus,
       "alEventAuthorization": alEventAuthorization,
       "alEventWebPortal": alEventWebPortal,
       "alEventWebEmail": alEventWebEmail,
       "alEventPortForward": alEventPortForward,
       "alEventRemoteServer": alEventRemoteServer,
       "alEventWebvpnAcl": alEventWebvpnAcl,
       "alEventNbns": alEventNbns,
       "alEventSecureDesktop": alEventSecureDesktop,
       "alEventSslTunnelClient": alEventSslTunnelClient,
       "alEventNac": alEventNac}
)
