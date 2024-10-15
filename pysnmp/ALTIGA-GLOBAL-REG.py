# SNMP MIB module (ALTIGA-GLOBAL-REG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTIGA-GLOBAL-REG
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

altigaGlobalRegModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 1, 1)
)
altigaGlobalRegModule.setRevisions(
        ("2005-01-05 00:00",
         "2003-10-20 00:00",
         "2003-04-25 00:00",
         "2002-07-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AltigaRoot_ObjectIdentity = ObjectIdentity
altigaRoot = _AltigaRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076)
)
_AltigaReg_ObjectIdentity = ObjectIdentity
altigaReg = _AltigaReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1)
)
_AltigaModules_ObjectIdentity = ObjectIdentity
altigaModules = _AltigaModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1)
)
_AlGlobalRegModule_ObjectIdentity = ObjectIdentity
alGlobalRegModule = _AlGlobalRegModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 1)
)
_AlCapModule_ObjectIdentity = ObjectIdentity
alCapModule = _AlCapModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 2)
)
_AlMibModule_ObjectIdentity = ObjectIdentity
alMibModule = _AlMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 3)
)
_AlComplModule_ObjectIdentity = ObjectIdentity
alComplModule = _AlComplModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 4)
)
_AlVersionMibModule_ObjectIdentity = ObjectIdentity
alVersionMibModule = _AlVersionMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 6)
)
_AlAccessMibModule_ObjectIdentity = ObjectIdentity
alAccessMibModule = _AlAccessMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 7)
)
_AlEventMibModule_ObjectIdentity = ObjectIdentity
alEventMibModule = _AlEventMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 8)
)
_AlAuthMibModule_ObjectIdentity = ObjectIdentity
alAuthMibModule = _AlAuthMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 9)
)
_AlPptpMibModule_ObjectIdentity = ObjectIdentity
alPptpMibModule = _AlPptpMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 10)
)
_AlPppMibModule_ObjectIdentity = ObjectIdentity
alPppMibModule = _AlPppMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 11)
)
_AlHttpMibModule_ObjectIdentity = ObjectIdentity
alHttpMibModule = _AlHttpMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 12)
)
_AlIpMibModule_ObjectIdentity = ObjectIdentity
alIpMibModule = _AlIpMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 13)
)
_AlFilterMibModule_ObjectIdentity = ObjectIdentity
alFilterMibModule = _AlFilterMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 14)
)
_AlUserMibModule_ObjectIdentity = ObjectIdentity
alUserMibModule = _AlUserMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 15)
)
_AlTelnetMibModule_ObjectIdentity = ObjectIdentity
alTelnetMibModule = _AlTelnetMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 16)
)
_AlFtpMibModule_ObjectIdentity = ObjectIdentity
alFtpMibModule = _AlFtpMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 17)
)
_AlTftpMibModule_ObjectIdentity = ObjectIdentity
alTftpMibModule = _AlTftpMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 18)
)
_AlSnmpMibModule_ObjectIdentity = ObjectIdentity
alSnmpMibModule = _AlSnmpMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 19)
)
_AlIpSecMibModule_ObjectIdentity = ObjectIdentity
alIpSecMibModule = _AlIpSecMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 20)
)
_AlL2tpMibModule_ObjectIdentity = ObjectIdentity
alL2tpMibModule = _AlL2tpMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 21)
)
_AlSessionMibModule_ObjectIdentity = ObjectIdentity
alSessionMibModule = _AlSessionMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 22)
)
_AlDnsMibModule_ObjectIdentity = ObjectIdentity
alDnsMibModule = _AlDnsMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 23)
)
_AlAddressMibModule_ObjectIdentity = ObjectIdentity
alAddressMibModule = _AlAddressMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 24)
)
_AlDhcpMibModule_ObjectIdentity = ObjectIdentity
alDhcpMibModule = _AlDhcpMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 25)
)
_AlWatchdogMibModule_ObjectIdentity = ObjectIdentity
alWatchdogMibModule = _AlWatchdogMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 26)
)
_AlHardwareMibModule_ObjectIdentity = ObjectIdentity
alHardwareMibModule = _AlHardwareMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 27)
)
_AlNatMibModule_ObjectIdentity = ObjectIdentity
alNatMibModule = _AlNatMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 28)
)
_AlLan2LanMibModule_ObjectIdentity = ObjectIdentity
alLan2LanMibModule = _AlLan2LanMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 29)
)
_AlGeneralMibModule_ObjectIdentity = ObjectIdentity
alGeneralMibModule = _AlGeneralMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 30)
)
_AlSslMibModule_ObjectIdentity = ObjectIdentity
alSslMibModule = _AlSslMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 31)
)
_AlCertMibModule_ObjectIdentity = ObjectIdentity
alCertMibModule = _AlCertMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 32)
)
_AlNtpMibModule_ObjectIdentity = ObjectIdentity
alNtpMibModule = _AlNtpMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 33)
)
_AlNetworkListMibModule_ObjectIdentity = ObjectIdentity
alNetworkListMibModule = _AlNetworkListMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 34)
)
_AlSepMibModule_ObjectIdentity = ObjectIdentity
alSepMibModule = _AlSepMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 35)
)
_AlIkeMibModule_ObjectIdentity = ObjectIdentity
alIkeMibModule = _AlIkeMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 36)
)
_AlSyncMibModule_ObjectIdentity = ObjectIdentity
alSyncMibModule = _AlSyncMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 37)
)
_AlT1E1MibModule_ObjectIdentity = ObjectIdentity
alT1E1MibModule = _AlT1E1MibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 38)
)
_AlMultiLinkMibModule_ObjectIdentity = ObjectIdentity
alMultiLinkMibModule = _AlMultiLinkMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 39)
)
_AlSshMibModule_ObjectIdentity = ObjectIdentity
alSshMibModule = _AlSshMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 40)
)
_AlLBSSFMibModule_ObjectIdentity = ObjectIdentity
alLBSSFMibModule = _AlLBSSFMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 41)
)
_AlDhcpServerMibModule_ObjectIdentity = ObjectIdentity
alDhcpServerMibModule = _AlDhcpServerMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 42)
)
_AlAutoUpdateMibModule_ObjectIdentity = ObjectIdentity
alAutoUpdateMibModule = _AlAutoUpdateMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 43)
)
_AlAdminAuthMibModule_ObjectIdentity = ObjectIdentity
alAdminAuthMibModule = _AlAdminAuthMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 44)
)
_AlPPPoEMibModule_ObjectIdentity = ObjectIdentity
alPPPoEMibModule = _AlPPPoEMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 45)
)
_AlXmlMibModule_ObjectIdentity = ObjectIdentity
alXmlMibModule = _AlXmlMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 46)
)
_AlCtcpMibModule_ObjectIdentity = ObjectIdentity
alCtcpMibModule = _AlCtcpMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 47)
)
_AlFwMibModule_ObjectIdentity = ObjectIdentity
alFwMibModule = _AlFwMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 48)
)
_AlGroupMatchMibModule_ObjectIdentity = ObjectIdentity
alGroupMatchMibModule = _AlGroupMatchMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 49)
)
_AlACEServerMibModule_ObjectIdentity = ObjectIdentity
alACEServerMibModule = _AlACEServerMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 50)
)
_AlNatTMibModule_ObjectIdentity = ObjectIdentity
alNatTMibModule = _AlNatTMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 51)
)
_AlBwMgmtMibModule_ObjectIdentity = ObjectIdentity
alBwMgmtMibModule = _AlBwMgmtMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 52)
)
_AlIpSecPreFragMibModule_ObjectIdentity = ObjectIdentity
alIpSecPreFragMibModule = _AlIpSecPreFragMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 53)
)
_AlFipsMibModule_ObjectIdentity = ObjectIdentity
alFipsMibModule = _AlFipsMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 54)
)
_AlBackupL2LMibModule_ObjectIdentity = ObjectIdentity
alBackupL2LMibModule = _AlBackupL2LMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 55)
)
_AlNotifyMibModule_ObjectIdentity = ObjectIdentity
alNotifyMibModule = _AlNotifyMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 56)
)
_AlRebootStatusMibModule_ObjectIdentity = ObjectIdentity
alRebootStatusMibModule = _AlRebootStatusMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 57)
)
_AlAuthorizationModule_ObjectIdentity = ObjectIdentity
alAuthorizationModule = _AlAuthorizationModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 58)
)
_AlWebPortalMibModule_ObjectIdentity = ObjectIdentity
alWebPortalMibModule = _AlWebPortalMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 59)
)
_AlWebEmailMibModule_ObjectIdentity = ObjectIdentity
alWebEmailMibModule = _AlWebEmailMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 60)
)
_AlPortForwardMibModule_ObjectIdentity = ObjectIdentity
alPortForwardMibModule = _AlPortForwardMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 61)
)
_AlRemoteServerMibModule_ObjectIdentity = ObjectIdentity
alRemoteServerMibModule = _AlRemoteServerMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 62)
)
_AlWebvpnAclMibModule_ObjectIdentity = ObjectIdentity
alWebvpnAclMibModule = _AlWebvpnAclMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 63)
)
_AlNbnsMibModule_ObjectIdentity = ObjectIdentity
alNbnsMibModule = _AlNbnsMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 64)
)
_AlSecureDesktopMibModule_ObjectIdentity = ObjectIdentity
alSecureDesktopMibModule = _AlSecureDesktopMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 65)
)
_AlSslTunnelClientMibModule_ObjectIdentity = ObjectIdentity
alSslTunnelClientMibModule = _AlSslTunnelClientMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 66)
)
_AlNacMibModule_ObjectIdentity = ObjectIdentity
alNacMibModule = _AlNacMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 67)
)
_AltigaHw_ObjectIdentity = ObjectIdentity
altigaHw = _AltigaHw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 2)
)
_AltigaVpnHw_ObjectIdentity = ObjectIdentity
altigaVpnHw = _AltigaVpnHw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 2, 1)
)
_AltigaVpnChassis_ObjectIdentity = ObjectIdentity
altigaVpnChassis = _AltigaVpnChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 2, 1, 1)
)
_VpnConcentrator_ObjectIdentity = ObjectIdentity
vpnConcentrator = _VpnConcentrator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 2, 1, 1, 1)
)
_VpnConcentratorRev1_ObjectIdentity = ObjectIdentity
vpnConcentratorRev1 = _VpnConcentratorRev1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    vpnConcentratorRev1.setStatus("current")
_VpnConcentratorRev2_ObjectIdentity = ObjectIdentity
vpnConcentratorRev2 = _VpnConcentratorRev2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 2, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    vpnConcentratorRev2.setStatus("current")
_VpnRemote_ObjectIdentity = ObjectIdentity
vpnRemote = _VpnRemote_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 2, 1, 1, 2)
)
_VpnRemoteRev1_ObjectIdentity = ObjectIdentity
vpnRemoteRev1 = _VpnRemoteRev1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    vpnRemoteRev1.setStatus("current")
_VpnClient_ObjectIdentity = ObjectIdentity
vpnClient = _VpnClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 2, 1, 1, 3)
)
_VpnClientRev1_ObjectIdentity = ObjectIdentity
vpnClientRev1 = _VpnClientRev1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 2, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    vpnClientRev1.setStatus("current")
_AltigaVpnIntf_ObjectIdentity = ObjectIdentity
altigaVpnIntf = _AltigaVpnIntf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 2, 1, 2)
)
_AltigaVpnEncrypt_ObjectIdentity = ObjectIdentity
altigaVpnEncrypt = _AltigaVpnEncrypt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 2, 1, 3)
)
_AltigaGeneric_ObjectIdentity = ObjectIdentity
altigaGeneric = _AltigaGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2)
)
_AltigaProducts_ObjectIdentity = ObjectIdentity
altigaProducts = _AltigaProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 3)
)
_AltigaCaps_ObjectIdentity = ObjectIdentity
altigaCaps = _AltigaCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 4)
)
_AltigaReqs_ObjectIdentity = ObjectIdentity
altigaReqs = _AltigaReqs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 5)
)
_AltigaExpr_ObjectIdentity = ObjectIdentity
altigaExpr = _AltigaExpr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTIGA-GLOBAL-REG",
    **{"altigaRoot": altigaRoot,
       "altigaReg": altigaReg,
       "altigaModules": altigaModules,
       "alGlobalRegModule": alGlobalRegModule,
       "altigaGlobalRegModule": altigaGlobalRegModule,
       "alCapModule": alCapModule,
       "alMibModule": alMibModule,
       "alComplModule": alComplModule,
       "alVersionMibModule": alVersionMibModule,
       "alAccessMibModule": alAccessMibModule,
       "alEventMibModule": alEventMibModule,
       "alAuthMibModule": alAuthMibModule,
       "alPptpMibModule": alPptpMibModule,
       "alPppMibModule": alPppMibModule,
       "alHttpMibModule": alHttpMibModule,
       "alIpMibModule": alIpMibModule,
       "alFilterMibModule": alFilterMibModule,
       "alUserMibModule": alUserMibModule,
       "alTelnetMibModule": alTelnetMibModule,
       "alFtpMibModule": alFtpMibModule,
       "alTftpMibModule": alTftpMibModule,
       "alSnmpMibModule": alSnmpMibModule,
       "alIpSecMibModule": alIpSecMibModule,
       "alL2tpMibModule": alL2tpMibModule,
       "alSessionMibModule": alSessionMibModule,
       "alDnsMibModule": alDnsMibModule,
       "alAddressMibModule": alAddressMibModule,
       "alDhcpMibModule": alDhcpMibModule,
       "alWatchdogMibModule": alWatchdogMibModule,
       "alHardwareMibModule": alHardwareMibModule,
       "alNatMibModule": alNatMibModule,
       "alLan2LanMibModule": alLan2LanMibModule,
       "alGeneralMibModule": alGeneralMibModule,
       "alSslMibModule": alSslMibModule,
       "alCertMibModule": alCertMibModule,
       "alNtpMibModule": alNtpMibModule,
       "alNetworkListMibModule": alNetworkListMibModule,
       "alSepMibModule": alSepMibModule,
       "alIkeMibModule": alIkeMibModule,
       "alSyncMibModule": alSyncMibModule,
       "alT1E1MibModule": alT1E1MibModule,
       "alMultiLinkMibModule": alMultiLinkMibModule,
       "alSshMibModule": alSshMibModule,
       "alLBSSFMibModule": alLBSSFMibModule,
       "alDhcpServerMibModule": alDhcpServerMibModule,
       "alAutoUpdateMibModule": alAutoUpdateMibModule,
       "alAdminAuthMibModule": alAdminAuthMibModule,
       "alPPPoEMibModule": alPPPoEMibModule,
       "alXmlMibModule": alXmlMibModule,
       "alCtcpMibModule": alCtcpMibModule,
       "alFwMibModule": alFwMibModule,
       "alGroupMatchMibModule": alGroupMatchMibModule,
       "alACEServerMibModule": alACEServerMibModule,
       "alNatTMibModule": alNatTMibModule,
       "alBwMgmtMibModule": alBwMgmtMibModule,
       "alIpSecPreFragMibModule": alIpSecPreFragMibModule,
       "alFipsMibModule": alFipsMibModule,
       "alBackupL2LMibModule": alBackupL2LMibModule,
       "alNotifyMibModule": alNotifyMibModule,
       "alRebootStatusMibModule": alRebootStatusMibModule,
       "alAuthorizationModule": alAuthorizationModule,
       "alWebPortalMibModule": alWebPortalMibModule,
       "alWebEmailMibModule": alWebEmailMibModule,
       "alPortForwardMibModule": alPortForwardMibModule,
       "alRemoteServerMibModule": alRemoteServerMibModule,
       "alWebvpnAclMibModule": alWebvpnAclMibModule,
       "alNbnsMibModule": alNbnsMibModule,
       "alSecureDesktopMibModule": alSecureDesktopMibModule,
       "alSslTunnelClientMibModule": alSslTunnelClientMibModule,
       "alNacMibModule": alNacMibModule,
       "altigaHw": altigaHw,
       "altigaVpnHw": altigaVpnHw,
       "altigaVpnChassis": altigaVpnChassis,
       "vpnConcentrator": vpnConcentrator,
       "vpnConcentratorRev1": vpnConcentratorRev1,
       "vpnConcentratorRev2": vpnConcentratorRev2,
       "vpnRemote": vpnRemote,
       "vpnRemoteRev1": vpnRemoteRev1,
       "vpnClient": vpnClient,
       "vpnClientRev1": vpnClientRev1,
       "altigaVpnIntf": altigaVpnIntf,
       "altigaVpnEncrypt": altigaVpnEncrypt,
       "altigaGeneric": altigaGeneric,
       "altigaProducts": altigaProducts,
       "altigaCaps": altigaCaps,
       "altigaReqs": altigaReqs,
       "altigaExpr": altigaExpr}
)
