# SNMP MIB module (HPN-ICF-OID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-OID-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:22 2024
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_Icf_ObjectIdentity = ObjectIdentity
icf = _Icf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14)
)
_HpicfObjects_ObjectIdentity = ObjectIdentity
hpicfObjects = _HpicfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11)
)
_Hpnicf_ObjectIdentity = ObjectIdentity
hpnicf = _Hpnicf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15)
)
_HpnicfCommon_ObjectIdentity = ObjectIdentity
hpnicfCommon = _HpnicfCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2)
)
_HpnicfFtm_ObjectIdentity = ObjectIdentity
hpnicfFtm = _HpnicfFtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 1)
)
_HpnicfUIMgt_ObjectIdentity = ObjectIdentity
hpnicfUIMgt = _HpnicfUIMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2)
)
_HpnicfSystemMan_ObjectIdentity = ObjectIdentity
hpnicfSystemMan = _HpnicfSystemMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3)
)
_HpnicfConfig_ObjectIdentity = ObjectIdentity
hpnicfConfig = _HpnicfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4)
)
_HpnicfFlash_ObjectIdentity = ObjectIdentity
hpnicfFlash = _HpnicfFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5)
)
_HpnicfEntityExtend_ObjectIdentity = ObjectIdentity
hpnicfEntityExtend = _HpnicfEntityExtend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6)
)
_HpnicfIPSecMonitor_ObjectIdentity = ObjectIdentity
hpnicfIPSecMonitor = _HpnicfIPSecMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7)
)
_HpnicfAcl_ObjectIdentity = ObjectIdentity
hpnicfAcl = _HpnicfAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8)
)
_HpnicfVoiceVlan_ObjectIdentity = ObjectIdentity
hpnicfVoiceVlan = _HpnicfVoiceVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 9)
)
_HpnicfL4Redirect_ObjectIdentity = ObjectIdentity
hpnicfL4Redirect = _HpnicfL4Redirect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 10)
)
_HpnicfIpPBX_ObjectIdentity = ObjectIdentity
hpnicfIpPBX = _HpnicfIpPBX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 11)
)
_HpnicfUser_ObjectIdentity = ObjectIdentity
hpnicfUser = _HpnicfUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12)
)
_HpnicfRadius_ObjectIdentity = ObjectIdentity
hpnicfRadius = _HpnicfRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13)
)
_HpnicfPowerEthernetExt_ObjectIdentity = ObjectIdentity
hpnicfPowerEthernetExt = _HpnicfPowerEthernetExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14)
)
_HpnicfEntityRelation_ObjectIdentity = ObjectIdentity
hpnicfEntityRelation = _HpnicfEntityRelation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15)
)
_HpnicfProtocolVlan_ObjectIdentity = ObjectIdentity
hpnicfProtocolVlan = _HpnicfProtocolVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16)
)
_HpnicfQosProfile_ObjectIdentity = ObjectIdentity
hpnicfQosProfile = _HpnicfQosProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17)
)
_HpnicfNat_ObjectIdentity = ObjectIdentity
hpnicfNat = _HpnicfNat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18)
)
_HpnicfPos_ObjectIdentity = ObjectIdentity
hpnicfPos = _HpnicfPos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19)
)
_HpnicfNS_ObjectIdentity = ObjectIdentity
hpnicfNS = _HpnicfNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20)
)
_HpnicfAAL5_ObjectIdentity = ObjectIdentity
hpnicfAAL5 = _HpnicfAAL5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 21)
)
_HpnicfSSH_ObjectIdentity = ObjectIdentity
hpnicfSSH = _HpnicfSSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22)
)
_HpnicfRSA_ObjectIdentity = ObjectIdentity
hpnicfRSA = _HpnicfRSA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 23)
)
_HpnicfVrrpExt_ObjectIdentity = ObjectIdentity
hpnicfVrrpExt = _HpnicfVrrpExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 24)
)
_HpnicfIpa_ObjectIdentity = ObjectIdentity
hpnicfIpa = _HpnicfIpa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25)
)
_HpnicfPortSecurity_ObjectIdentity = ObjectIdentity
hpnicfPortSecurity = _HpnicfPortSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26)
)
_HpnicfVpls_ObjectIdentity = ObjectIdentity
hpnicfVpls = _HpnicfVpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 27)
)
_HpnicfE1_ObjectIdentity = ObjectIdentity
hpnicfE1 = _HpnicfE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28)
)
_HpnicfT1_ObjectIdentity = ObjectIdentity
hpnicfT1 = _HpnicfT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29)
)
_HpnicfIKEMonitor_ObjectIdentity = ObjectIdentity
hpnicfIKEMonitor = _HpnicfIKEMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30)
)
_HpnicfWebSwitch_ObjectIdentity = ObjectIdentity
hpnicfWebSwitch = _HpnicfWebSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 31)
)
_HpnicfAutoDetect_ObjectIdentity = ObjectIdentity
hpnicfAutoDetect = _HpnicfAutoDetect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 32)
)
_HpnicfIpBroadcast_ObjectIdentity = ObjectIdentity
hpnicfIpBroadcast = _HpnicfIpBroadcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 33)
)
_HpnicfIpx_ObjectIdentity = ObjectIdentity
hpnicfIpx = _HpnicfIpx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34)
)
_HpnicfIPS_ObjectIdentity = ObjectIdentity
hpnicfIPS = _HpnicfIPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 35)
)
_HpnicfDhcpSnoop_ObjectIdentity = ObjectIdentity
hpnicfDhcpSnoop = _HpnicfDhcpSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 36)
)
_HpnicfProtocolPriority_ObjectIdentity = ObjectIdentity
hpnicfProtocolPriority = _HpnicfProtocolPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 37)
)
_HpnicfTrap_ObjectIdentity = ObjectIdentity
hpnicfTrap = _HpnicfTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38)
)
_HpnicfVoice_ObjectIdentity = ObjectIdentity
hpnicfVoice = _HpnicfVoice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39)
)
_HpnicfIfExt_ObjectIdentity = ObjectIdentity
hpnicfIfExt = _HpnicfIfExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40)
)
_HpnicfCfCard_ObjectIdentity = ObjectIdentity
hpnicfCfCard = _HpnicfCfCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 41)
)
_HpnicfEpon_ObjectIdentity = ObjectIdentity
hpnicfEpon = _HpnicfEpon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42)
)
_HpnicfDldp_ObjectIdentity = ObjectIdentity
hpnicfDldp = _HpnicfDldp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 43)
)
_HpnicfUnicast_ObjectIdentity = ObjectIdentity
hpnicfUnicast = _HpnicfUnicast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 44)
)
_HpnicfRrpp_ObjectIdentity = ObjectIdentity
hpnicfRrpp = _HpnicfRrpp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45)
)
_HpnicfDomain_ObjectIdentity = ObjectIdentity
hpnicfDomain = _HpnicfDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46)
)
_HpnicfIds_ObjectIdentity = ObjectIdentity
hpnicfIds = _HpnicfIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47)
)
_HpnicfRcr_ObjectIdentity = ObjectIdentity
hpnicfRcr = _HpnicfRcr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48)
)
_HpnicfAtmDxi_ObjectIdentity = ObjectIdentity
hpnicfAtmDxi = _HpnicfAtmDxi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 49)
)
_HpnicfMulticast_ObjectIdentity = ObjectIdentity
hpnicfMulticast = _HpnicfMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 50)
)
_HpnicfMpm_ObjectIdentity = ObjectIdentity
hpnicfMpm = _HpnicfMpm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51)
)
_HpnicfOadp_ObjectIdentity = ObjectIdentity
hpnicfOadp = _HpnicfOadp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 52)
)
_HpnicfTunnel_ObjectIdentity = ObjectIdentity
hpnicfTunnel = _HpnicfTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53)
)
_HpnicfGre_ObjectIdentity = ObjectIdentity
hpnicfGre = _HpnicfGre_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 54)
)
_HpnicfObjectInfo_ObjectIdentity = ObjectIdentity
hpnicfObjectInfo = _HpnicfObjectInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55)
)
_HpnicfStorage_ObjectIdentity = ObjectIdentity
hpnicfStorage = _HpnicfStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 56)
)
_HpnicfDvpn_ObjectIdentity = ObjectIdentity
hpnicfDvpn = _HpnicfDvpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57)
)
_HpnicfDhcpRelay_ObjectIdentity = ObjectIdentity
hpnicfDhcpRelay = _HpnicfDhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58)
)
_HpnicfIsis_ObjectIdentity = ObjectIdentity
hpnicfIsis = _HpnicfIsis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 59)
)
_HpnicfRpr_ObjectIdentity = ObjectIdentity
hpnicfRpr = _HpnicfRpr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 60)
)
_HpnicfSubnetVlan_ObjectIdentity = ObjectIdentity
hpnicfSubnetVlan = _HpnicfSubnetVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 61)
)
_HpnicfDlswExt_ObjectIdentity = ObjectIdentity
hpnicfDlswExt = _HpnicfDlswExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62)
)
_HpnicfSyslog_ObjectIdentity = ObjectIdentity
hpnicfSyslog = _HpnicfSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63)
)
_HpnicfFlowTemplate_ObjectIdentity = ObjectIdentity
hpnicfFlowTemplate = _HpnicfFlowTemplate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64)
)
_HpnicfQos2_ObjectIdentity = ObjectIdentity
hpnicfQos2 = _HpnicfQos2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65)
)
_HpnicfIfQos2_ObjectIdentity = ObjectIdentity
hpnicfIfQos2 = _HpnicfIfQos2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1)
)
_HpnicfCBQos2_ObjectIdentity = ObjectIdentity
hpnicfCBQos2 = _HpnicfCBQos2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2)
)
_HpnicfStormConstrain_ObjectIdentity = ObjectIdentity
hpnicfStormConstrain = _HpnicfStormConstrain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 66)
)
_HpnicfIpAddrMIB_ObjectIdentity = ObjectIdentity
hpnicfIpAddrMIB = _HpnicfIpAddrMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67)
)
_HpnicfMirrGroup_ObjectIdentity = ObjectIdentity
hpnicfMirrGroup = _HpnicfMirrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68)
)
_HpnicfQINQ_ObjectIdentity = ObjectIdentity
hpnicfQINQ = _HpnicfQINQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69)
)
_HpnicfTransceiver_ObjectIdentity = ObjectIdentity
hpnicfTransceiver = _HpnicfTransceiver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70)
)
_HpnicfIpv6AddrMIB_ObjectIdentity = ObjectIdentity
hpnicfIpv6AddrMIB = _HpnicfIpv6AddrMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 71)
)
_HpnicfBfdMIB_ObjectIdentity = ObjectIdentity
hpnicfBfdMIB = _HpnicfBfdMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72)
)
_HpnicfRCP_ObjectIdentity = ObjectIdentity
hpnicfRCP = _HpnicfRCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73)
)
_HpnicfAcfp_ObjectIdentity = ObjectIdentity
hpnicfAcfp = _HpnicfAcfp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74)
)
_HpnicfDot11_ObjectIdentity = ObjectIdentity
hpnicfDot11 = _HpnicfDot11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75)
)
_HpnicfE1T1VI_ObjectIdentity = ObjectIdentity
hpnicfE1T1VI = _HpnicfE1T1VI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 76)
)
_HpnicfL2VpnPwe3_ObjectIdentity = ObjectIdentity
hpnicfL2VpnPwe3 = _HpnicfL2VpnPwe3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 78)
)
_HpnicfMplsOam_ObjectIdentity = ObjectIdentity
hpnicfMplsOam = _HpnicfMplsOam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79)
)
_HpnicfMplsOamPs_ObjectIdentity = ObjectIdentity
hpnicfMplsOamPs = _HpnicfMplsOamPs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 80)
)
_HpnicfSiemMib_ObjectIdentity = ObjectIdentity
hpnicfSiemMib = _HpnicfSiemMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 81)
)
_HpnicfUps_ObjectIdentity = ObjectIdentity
hpnicfUps = _HpnicfUps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82)
)
_HpnicfEOCCommon_ObjectIdentity = ObjectIdentity
hpnicfEOCCommon = _HpnicfEOCCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 83)
)
_HpnicfHPEOC_ObjectIdentity = ObjectIdentity
hpnicfHPEOC = _HpnicfHPEOC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 84)
)
_HpnicfAFC_ObjectIdentity = ObjectIdentity
hpnicfAFC = _HpnicfAFC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 85)
)
_HpnicfMultCDR_ObjectIdentity = ObjectIdentity
hpnicfMultCDR = _HpnicfMultCDR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86)
)
_HpnicfMACInformation_ObjectIdentity = ObjectIdentity
hpnicfMACInformation = _HpnicfMACInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87)
)
_HpnicfFireWall_ObjectIdentity = ObjectIdentity
hpnicfFireWall = _HpnicfFireWall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 88)
)
_HpnicfDSP_ObjectIdentity = ObjectIdentity
hpnicfDSP = _HpnicfDSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89)
)
_HpnicfNetMan_ObjectIdentity = ObjectIdentity
hpnicfNetMan = _HpnicfNetMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90)
)
_HpnicfStack_ObjectIdentity = ObjectIdentity
hpnicfStack = _HpnicfStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91)
)
_HpnicfPosa_ObjectIdentity = ObjectIdentity
hpnicfPosa = _HpnicfPosa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92)
)
_HpnicfWebAuthentication_ObjectIdentity = ObjectIdentity
hpnicfWebAuthentication = _HpnicfWebAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 93)
)
_HpnicfCATVTransceiver_ObjectIdentity = ObjectIdentity
hpnicfCATVTransceiver = _HpnicfCATVTransceiver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 94)
)
_HpnicfLpbkdt_ObjectIdentity = ObjectIdentity
hpnicfLpbkdt = _HpnicfLpbkdt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 95)
)
_HpnicfMultiMedia_ObjectIdentity = ObjectIdentity
hpnicfMultiMedia = _HpnicfMultiMedia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 96)
)
_HpnicfDns_ObjectIdentity = ObjectIdentity
hpnicfDns = _HpnicfDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 97)
)
_Hpnicf3GModem_ObjectIdentity = ObjectIdentity
hpnicf3GModem = _Hpnicf3GModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98)
)
_HpnicfPortal_ObjectIdentity = ObjectIdentity
hpnicfPortal = _HpnicfPortal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99)
)
_Hpnicflldp_ObjectIdentity = ObjectIdentity
hpnicflldp = _Hpnicflldp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 100)
)
_HpnicfDHCPServer_ObjectIdentity = ObjectIdentity
hpnicfDHCPServer = _HpnicfDHCPServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101)
)
_HpnicfPPPoEServer_ObjectIdentity = ObjectIdentity
hpnicfPPPoEServer = _HpnicfPPPoEServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102)
)
_HpnicfL2Isolate_ObjectIdentity = ObjectIdentity
hpnicfL2Isolate = _HpnicfL2Isolate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 103)
)
_HpnicfSnmpExt_ObjectIdentity = ObjectIdentity
hpnicfSnmpExt = _HpnicfSnmpExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104)
)
_HpnicfVsi_ObjectIdentity = ObjectIdentity
hpnicfVsi = _HpnicfVsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105)
)
_HpnicfEvc_ObjectIdentity = ObjectIdentity
hpnicfEvc = _HpnicfEvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 106)
)
_HpnicfMinm_ObjectIdentity = ObjectIdentity
hpnicfMinm = _HpnicfMinm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107)
)
_HpnicfBlg_ObjectIdentity = ObjectIdentity
hpnicfBlg = _HpnicfBlg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108)
)
_HpnicfRS485_ObjectIdentity = ObjectIdentity
hpnicfRS485 = _HpnicfRS485_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109)
)
_HpnicfARPRatelimit_ObjectIdentity = ObjectIdentity
hpnicfARPRatelimit = _HpnicfARPRatelimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 110)
)
_HpnicfLI_ObjectIdentity = ObjectIdentity
hpnicfLI = _HpnicfLI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111)
)
_HpnicfDar_ObjectIdentity = ObjectIdentity
hpnicfDar = _HpnicfDar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112)
)
_HpnicfPBR_ObjectIdentity = ObjectIdentity
hpnicfPBR = _HpnicfPBR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113)
)
_HpnicfAAANasId_ObjectIdentity = ObjectIdentity
hpnicfAAANasId = _HpnicfAAANasId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 114)
)
_HpnicfTeTunnel_ObjectIdentity = ObjectIdentity
hpnicfTeTunnel = _HpnicfTeTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115)
)
_HpnicfLB_ObjectIdentity = ObjectIdentity
hpnicfLB = _HpnicfLB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 116)
)
_HpnicfDldp2_ObjectIdentity = ObjectIdentity
hpnicfDldp2 = _HpnicfDldp2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117)
)
_HpnicfWIPS_ObjectIdentity = ObjectIdentity
hpnicfWIPS = _HpnicfWIPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118)
)
_HpnicfInfoCenter_ObjectIdentity = ObjectIdentity
hpnicfInfoCenter = _HpnicfInfoCenter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119)
)
_HpnicfFCoE_ObjectIdentity = ObjectIdentity
hpnicfFCoE = _HpnicfFCoE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120)
)
_HpnicfTRNG2_ObjectIdentity = ObjectIdentity
hpnicfTRNG2 = _HpnicfTRNG2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 121)
)
_HpnicfDhcp4_ObjectIdentity = ObjectIdentity
hpnicfDhcp4 = _HpnicfDhcp4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122)
)
_HpnicfDhcpSnoop2_ObjectIdentity = ObjectIdentity
hpnicfDhcpSnoop2 = _HpnicfDhcpSnoop2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124)
)
_HpnicfRmonExt_ObjectIdentity = ObjectIdentity
hpnicfRmonExt = _HpnicfRmonExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125)
)
_HpnicfIPsecMonitorV2_ObjectIdentity = ObjectIdentity
hpnicfIPsecMonitorV2 = _HpnicfIPsecMonitorV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126)
)
_HpnicfSan_ObjectIdentity = ObjectIdentity
hpnicfSan = _HpnicfSan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127)
)
_HpnicfSpb_ObjectIdentity = ObjectIdentity
hpnicfSpb = _HpnicfSpb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 128)
)
_HpnicfPex_ObjectIdentity = ObjectIdentity
hpnicfPex = _HpnicfPex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129)
)
_HpnicfSlbg_ObjectIdentity = ObjectIdentity
hpnicfSlbg = _HpnicfSlbg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 130)
)
_HpnicfEvi_ObjectIdentity = ObjectIdentity
hpnicfEvi = _HpnicfEvi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132)
)
_HpnicfIssuUpgrade_ObjectIdentity = ObjectIdentity
hpnicfIssuUpgrade = _HpnicfIssuUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133)
)
_HpnicfEvb_ObjectIdentity = ObjectIdentity
hpnicfEvb = _HpnicfEvb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134)
)
_HpnicfFcoeMode_ObjectIdentity = ObjectIdentity
hpnicfFcoeMode = _HpnicfFcoeMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 135)
)
_HpnicfMDC_ObjectIdentity = ObjectIdentity
hpnicfMDC = _HpnicfMDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136)
)
_HpnicfQinQv2_ObjectIdentity = ObjectIdentity
hpnicfQinQv2 = _HpnicfQinQv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 137)
)
_HpnicfVmap_ObjectIdentity = ObjectIdentity
hpnicfVmap = _HpnicfVmap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138)
)
_HpnicfL2tp_ObjectIdentity = ObjectIdentity
hpnicfL2tp = _HpnicfL2tp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 139)
)
_HpnicfMultilinkPPPV2_ObjectIdentity = ObjectIdentity
hpnicfMultilinkPPPV2 = _HpnicfMultilinkPPPV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140)
)
_HpnicfLocAAASrv_ObjectIdentity = ObjectIdentity
hpnicfLocAAASrv = _HpnicfLocAAASrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 141)
)
_HpnicfMplsExt_ObjectIdentity = ObjectIdentity
hpnicfMplsExt = _HpnicfMplsExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 142)
)
_HpnicfMplsTe_ObjectIdentity = ObjectIdentity
hpnicfMplsTe = _HpnicfMplsTe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143)
)
_HpnicfBpa_ObjectIdentity = ObjectIdentity
hpnicfBpa = _HpnicfBpa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144)
)
_HpnicfLicense_ObjectIdentity = ObjectIdentity
hpnicfLicense = _HpnicfLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145)
)
_HpnicfARPSourceSuppression_ObjectIdentity = ObjectIdentity
hpnicfARPSourceSuppression = _HpnicfARPSourceSuppression_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 146)
)
_HpnicfLBv2_ObjectIdentity = ObjectIdentity
hpnicfLBv2 = _HpnicfLBv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148)
)
_HpnicfSession_ObjectIdentity = ObjectIdentity
hpnicfSession = _HpnicfSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 149)
)
_HpnicfVxlan_ObjectIdentity = ObjectIdentity
hpnicfVxlan = _HpnicfVxlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150)
)
_HpnicfRddc_ObjectIdentity = ObjectIdentity
hpnicfRddc = _HpnicfRddc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 151)
)
_HpnicfIpRanDcn_ObjectIdentity = ObjectIdentity
hpnicfIpRanDcn = _HpnicfIpRanDcn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 152)
)
_HpnicfContext_ObjectIdentity = ObjectIdentity
hpnicfContext = _HpnicfContext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 154)
)
_HpnicfEntityVendorTypeOID_ObjectIdentity = ObjectIdentity
hpnicfEntityVendorTypeOID = _HpnicfEntityVendorTypeOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3)
)
_HpnicfNM_ObjectIdentity = ObjectIdentity
hpnicfNM = _HpnicfNM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 4)
)
_HpnicfSystem_ObjectIdentity = ObjectIdentity
hpnicfSystem = _HpnicfSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6)
)
_HpnicfSNMPAgCpb_ObjectIdentity = ObjectIdentity
hpnicfSNMPAgCpb = _HpnicfSNMPAgCpb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 7)
)
_HpnicfQosCapability_ObjectIdentity = ObjectIdentity
hpnicfQosCapability = _HpnicfQosCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 7, 1)
)
_HpnicfRhw_ObjectIdentity = ObjectIdentity
hpnicfRhw = _HpnicfRhw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8)
)
_HpnicfDHCPRelayMib_ObjectIdentity = ObjectIdentity
hpnicfDHCPRelayMib = _HpnicfDHCPRelayMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1)
)
_HpnicfDHCPServerMib_ObjectIdentity = ObjectIdentity
hpnicfDHCPServerMib = _HpnicfDHCPServerMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2)
)
_HpnicfNqa_ObjectIdentity = ObjectIdentity
hpnicfNqa = _HpnicfNqa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3)
)
_HpnicfrmonExtend_ObjectIdentity = ObjectIdentity
hpnicfrmonExtend = _HpnicfrmonExtend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 4)
)
_HpnicfpaeExtMib_ObjectIdentity = ObjectIdentity
hpnicfpaeExtMib = _HpnicfpaeExtMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 6)
)
_HpnicfHgmp_ObjectIdentity = ObjectIdentity
hpnicfHgmp = _HpnicfHgmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7)
)
_HpnicfDevice_ObjectIdentity = ObjectIdentity
hpnicfDevice = _HpnicfDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 8)
)
_HpnicfMpls_ObjectIdentity = ObjectIdentity
hpnicfMpls = _HpnicfMpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12)
)
_HpnicfMplsLsr_ObjectIdentity = ObjectIdentity
hpnicfMplsLsr = _HpnicfMplsLsr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1)
)
_HpnicfMplsLdp_ObjectIdentity = ObjectIdentity
hpnicfMplsLdp = _HpnicfMplsLdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2)
)
_HpnicfMplsVpn_ObjectIdentity = ObjectIdentity
hpnicfMplsVpn = _HpnicfMplsVpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3)
)
_HpnicfTRNG_ObjectIdentity = ObjectIdentity
hpnicfTRNG = _HpnicfTRNG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 13)
)
_HpnicfUserLogMIB_ObjectIdentity = ObjectIdentity
hpnicfUserLogMIB = _HpnicfUserLogMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18)
)
_HpnicfNTP_ObjectIdentity = ObjectIdentity
hpnicfNTP = _HpnicfNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22)
)
_HpnicfLAG_ObjectIdentity = ObjectIdentity
hpnicfLAG = _HpnicfLAG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25)
)
_HpnicfSmonExtend_ObjectIdentity = ObjectIdentity
hpnicfSmonExtend = _HpnicfSmonExtend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 26)
)
_HpnicfQoS_ObjectIdentity = ObjectIdentity
hpnicfQoS = _HpnicfQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32)
)
_HpnicfMultilinkPPP_ObjectIdentity = ObjectIdentity
hpnicfMultilinkPPP = _HpnicfMultilinkPPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 33)
)
_HpnicflswCommon_ObjectIdentity = ObjectIdentity
hpnicflswCommon = _HpnicflswCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35)
)
_HpnicfLswExtInterface_ObjectIdentity = ObjectIdentity
hpnicfLswExtInterface = _HpnicfLswExtInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1)
)
_HpnicfLswVlan_ObjectIdentity = ObjectIdentity
hpnicfLswVlan = _HpnicfLswVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2)
)
_HpnicfLswMacPort_ObjectIdentity = ObjectIdentity
hpnicfLswMacPort = _HpnicfLswMacPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3)
)
_HpnicfLswArpMib_ObjectIdentity = ObjectIdentity
hpnicfLswArpMib = _HpnicfLswArpMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 4)
)
_HpnicfLswL2InfMib_ObjectIdentity = ObjectIdentity
hpnicfLswL2InfMib = _HpnicfLswL2InfMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5)
)
_HpnicfLswRstpMib_ObjectIdentity = ObjectIdentity
hpnicfLswRstpMib = _HpnicfLswRstpMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6)
)
_HpnicfLswIgmpsnoopingMib_ObjectIdentity = ObjectIdentity
hpnicfLswIgmpsnoopingMib = _HpnicfLswIgmpsnoopingMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7)
)
_HpnicfLswDhcpMib_ObjectIdentity = ObjectIdentity
hpnicfLswDhcpMib = _HpnicfLswDhcpMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8)
)
_HpnicfLswdevMMib_ObjectIdentity = ObjectIdentity
hpnicfLswdevMMib = _HpnicfLswdevMMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 9)
)
_HpnicfLswTrapMib_ObjectIdentity = ObjectIdentity
hpnicfLswTrapMib = _HpnicfLswTrapMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12)
)
_Hpnicfdot1sMstp_ObjectIdentity = ObjectIdentity
hpnicfdot1sMstp = _Hpnicfdot1sMstp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14)
)
_HpnicfLswQosAclMib_ObjectIdentity = ObjectIdentity
hpnicfLswQosAclMib = _HpnicfLswQosAclMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16)
)
_HpnicfLswMix_ObjectIdentity = ObjectIdentity
hpnicfLswMix = _HpnicfLswMix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 17)
)
_HpnicfLswDeviceAdmin_ObjectIdentity = ObjectIdentity
hpnicfLswDeviceAdmin = _HpnicfLswDeviceAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 18)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-OID-MIB",
    **{"hp": hp,
       "nm": nm,
       "icf": icf,
       "hpicfObjects": hpicfObjects,
       "hpnicf": hpnicf,
       "hpnicfCommon": hpnicfCommon,
       "hpnicfFtm": hpnicfFtm,
       "hpnicfUIMgt": hpnicfUIMgt,
       "hpnicfSystemMan": hpnicfSystemMan,
       "hpnicfConfig": hpnicfConfig,
       "hpnicfFlash": hpnicfFlash,
       "hpnicfEntityExtend": hpnicfEntityExtend,
       "hpnicfIPSecMonitor": hpnicfIPSecMonitor,
       "hpnicfAcl": hpnicfAcl,
       "hpnicfVoiceVlan": hpnicfVoiceVlan,
       "hpnicfL4Redirect": hpnicfL4Redirect,
       "hpnicfIpPBX": hpnicfIpPBX,
       "hpnicfUser": hpnicfUser,
       "hpnicfRadius": hpnicfRadius,
       "hpnicfPowerEthernetExt": hpnicfPowerEthernetExt,
       "hpnicfEntityRelation": hpnicfEntityRelation,
       "hpnicfProtocolVlan": hpnicfProtocolVlan,
       "hpnicfQosProfile": hpnicfQosProfile,
       "hpnicfNat": hpnicfNat,
       "hpnicfPos": hpnicfPos,
       "hpnicfNS": hpnicfNS,
       "hpnicfAAL5": hpnicfAAL5,
       "hpnicfSSH": hpnicfSSH,
       "hpnicfRSA": hpnicfRSA,
       "hpnicfVrrpExt": hpnicfVrrpExt,
       "hpnicfIpa": hpnicfIpa,
       "hpnicfPortSecurity": hpnicfPortSecurity,
       "hpnicfVpls": hpnicfVpls,
       "hpnicfE1": hpnicfE1,
       "hpnicfT1": hpnicfT1,
       "hpnicfIKEMonitor": hpnicfIKEMonitor,
       "hpnicfWebSwitch": hpnicfWebSwitch,
       "hpnicfAutoDetect": hpnicfAutoDetect,
       "hpnicfIpBroadcast": hpnicfIpBroadcast,
       "hpnicfIpx": hpnicfIpx,
       "hpnicfIPS": hpnicfIPS,
       "hpnicfDhcpSnoop": hpnicfDhcpSnoop,
       "hpnicfProtocolPriority": hpnicfProtocolPriority,
       "hpnicfTrap": hpnicfTrap,
       "hpnicfVoice": hpnicfVoice,
       "hpnicfIfExt": hpnicfIfExt,
       "hpnicfCfCard": hpnicfCfCard,
       "hpnicfEpon": hpnicfEpon,
       "hpnicfDldp": hpnicfDldp,
       "hpnicfUnicast": hpnicfUnicast,
       "hpnicfRrpp": hpnicfRrpp,
       "hpnicfDomain": hpnicfDomain,
       "hpnicfIds": hpnicfIds,
       "hpnicfRcr": hpnicfRcr,
       "hpnicfAtmDxi": hpnicfAtmDxi,
       "hpnicfMulticast": hpnicfMulticast,
       "hpnicfMpm": hpnicfMpm,
       "hpnicfOadp": hpnicfOadp,
       "hpnicfTunnel": hpnicfTunnel,
       "hpnicfGre": hpnicfGre,
       "hpnicfObjectInfo": hpnicfObjectInfo,
       "hpnicfStorage": hpnicfStorage,
       "hpnicfDvpn": hpnicfDvpn,
       "hpnicfDhcpRelay": hpnicfDhcpRelay,
       "hpnicfIsis": hpnicfIsis,
       "hpnicfRpr": hpnicfRpr,
       "hpnicfSubnetVlan": hpnicfSubnetVlan,
       "hpnicfDlswExt": hpnicfDlswExt,
       "hpnicfSyslog": hpnicfSyslog,
       "hpnicfFlowTemplate": hpnicfFlowTemplate,
       "hpnicfQos2": hpnicfQos2,
       "hpnicfIfQos2": hpnicfIfQos2,
       "hpnicfCBQos2": hpnicfCBQos2,
       "hpnicfStormConstrain": hpnicfStormConstrain,
       "hpnicfIpAddrMIB": hpnicfIpAddrMIB,
       "hpnicfMirrGroup": hpnicfMirrGroup,
       "hpnicfQINQ": hpnicfQINQ,
       "hpnicfTransceiver": hpnicfTransceiver,
       "hpnicfIpv6AddrMIB": hpnicfIpv6AddrMIB,
       "hpnicfBfdMIB": hpnicfBfdMIB,
       "hpnicfRCP": hpnicfRCP,
       "hpnicfAcfp": hpnicfAcfp,
       "hpnicfDot11": hpnicfDot11,
       "hpnicfE1T1VI": hpnicfE1T1VI,
       "hpnicfL2VpnPwe3": hpnicfL2VpnPwe3,
       "hpnicfMplsOam": hpnicfMplsOam,
       "hpnicfMplsOamPs": hpnicfMplsOamPs,
       "hpnicfSiemMib": hpnicfSiemMib,
       "hpnicfUps": hpnicfUps,
       "hpnicfEOCCommon": hpnicfEOCCommon,
       "hpnicfHPEOC": hpnicfHPEOC,
       "hpnicfAFC": hpnicfAFC,
       "hpnicfMultCDR": hpnicfMultCDR,
       "hpnicfMACInformation": hpnicfMACInformation,
       "hpnicfFireWall": hpnicfFireWall,
       "hpnicfDSP": hpnicfDSP,
       "hpnicfNetMan": hpnicfNetMan,
       "hpnicfStack": hpnicfStack,
       "hpnicfPosa": hpnicfPosa,
       "hpnicfWebAuthentication": hpnicfWebAuthentication,
       "hpnicfCATVTransceiver": hpnicfCATVTransceiver,
       "hpnicfLpbkdt": hpnicfLpbkdt,
       "hpnicfMultiMedia": hpnicfMultiMedia,
       "hpnicfDns": hpnicfDns,
       "hpnicf3GModem": hpnicf3GModem,
       "hpnicfPortal": hpnicfPortal,
       "hpnicflldp": hpnicflldp,
       "hpnicfDHCPServer": hpnicfDHCPServer,
       "hpnicfPPPoEServer": hpnicfPPPoEServer,
       "hpnicfL2Isolate": hpnicfL2Isolate,
       "hpnicfSnmpExt": hpnicfSnmpExt,
       "hpnicfVsi": hpnicfVsi,
       "hpnicfEvc": hpnicfEvc,
       "hpnicfMinm": hpnicfMinm,
       "hpnicfBlg": hpnicfBlg,
       "hpnicfRS485": hpnicfRS485,
       "hpnicfARPRatelimit": hpnicfARPRatelimit,
       "hpnicfLI": hpnicfLI,
       "hpnicfDar": hpnicfDar,
       "hpnicfPBR": hpnicfPBR,
       "hpnicfAAANasId": hpnicfAAANasId,
       "hpnicfTeTunnel": hpnicfTeTunnel,
       "hpnicfLB": hpnicfLB,
       "hpnicfDldp2": hpnicfDldp2,
       "hpnicfWIPS": hpnicfWIPS,
       "hpnicfInfoCenter": hpnicfInfoCenter,
       "hpnicfFCoE": hpnicfFCoE,
       "hpnicfTRNG2": hpnicfTRNG2,
       "hpnicfDhcp4": hpnicfDhcp4,
       "hpnicfDhcpSnoop2": hpnicfDhcpSnoop2,
       "hpnicfRmonExt": hpnicfRmonExt,
       "hpnicfIPsecMonitorV2": hpnicfIPsecMonitorV2,
       "hpnicfSan": hpnicfSan,
       "hpnicfSpb": hpnicfSpb,
       "hpnicfPex": hpnicfPex,
       "hpnicfSlbg": hpnicfSlbg,
       "hpnicfEvi": hpnicfEvi,
       "hpnicfIssuUpgrade": hpnicfIssuUpgrade,
       "hpnicfEvb": hpnicfEvb,
       "hpnicfFcoeMode": hpnicfFcoeMode,
       "hpnicfMDC": hpnicfMDC,
       "hpnicfQinQv2": hpnicfQinQv2,
       "hpnicfVmap": hpnicfVmap,
       "hpnicfL2tp": hpnicfL2tp,
       "hpnicfMultilinkPPPV2": hpnicfMultilinkPPPV2,
       "hpnicfLocAAASrv": hpnicfLocAAASrv,
       "hpnicfMplsExt": hpnicfMplsExt,
       "hpnicfMplsTe": hpnicfMplsTe,
       "hpnicfBpa": hpnicfBpa,
       "hpnicfLicense": hpnicfLicense,
       "hpnicfARPSourceSuppression": hpnicfARPSourceSuppression,
       "hpnicfLBv2": hpnicfLBv2,
       "hpnicfSession": hpnicfSession,
       "hpnicfVxlan": hpnicfVxlan,
       "hpnicfRddc": hpnicfRddc,
       "hpnicfIpRanDcn": hpnicfIpRanDcn,
       "hpnicfContext": hpnicfContext,
       "hpnicfEntityVendorTypeOID": hpnicfEntityVendorTypeOID,
       "hpnicfNM": hpnicfNM,
       "hpnicfSystem": hpnicfSystem,
       "hpnicfSNMPAgCpb": hpnicfSNMPAgCpb,
       "hpnicfQosCapability": hpnicfQosCapability,
       "hpnicfRhw": hpnicfRhw,
       "hpnicfDHCPRelayMib": hpnicfDHCPRelayMib,
       "hpnicfDHCPServerMib": hpnicfDHCPServerMib,
       "hpnicfNqa": hpnicfNqa,
       "hpnicfrmonExtend": hpnicfrmonExtend,
       "hpnicfpaeExtMib": hpnicfpaeExtMib,
       "hpnicfHgmp": hpnicfHgmp,
       "hpnicfDevice": hpnicfDevice,
       "hpnicfMpls": hpnicfMpls,
       "hpnicfMplsLsr": hpnicfMplsLsr,
       "hpnicfMplsLdp": hpnicfMplsLdp,
       "hpnicfMplsVpn": hpnicfMplsVpn,
       "hpnicfTRNG": hpnicfTRNG,
       "hpnicfUserLogMIB": hpnicfUserLogMIB,
       "hpnicfNTP": hpnicfNTP,
       "hpnicfLAG": hpnicfLAG,
       "hpnicfSmonExtend": hpnicfSmonExtend,
       "hpnicfQoS": hpnicfQoS,
       "hpnicfMultilinkPPP": hpnicfMultilinkPPP,
       "hpnicflswCommon": hpnicflswCommon,
       "hpnicfLswExtInterface": hpnicfLswExtInterface,
       "hpnicfLswVlan": hpnicfLswVlan,
       "hpnicfLswMacPort": hpnicfLswMacPort,
       "hpnicfLswArpMib": hpnicfLswArpMib,
       "hpnicfLswL2InfMib": hpnicfLswL2InfMib,
       "hpnicfLswRstpMib": hpnicfLswRstpMib,
       "hpnicfLswIgmpsnoopingMib": hpnicfLswIgmpsnoopingMib,
       "hpnicfLswDhcpMib": hpnicfLswDhcpMib,
       "hpnicfLswdevMMib": hpnicfLswdevMMib,
       "hpnicfLswTrapMib": hpnicfLswTrapMib,
       "hpnicfdot1sMstp": hpnicfdot1sMstp,
       "hpnicfLswQosAclMib": hpnicfLswQosAclMib,
       "hpnicfLswMix": hpnicfLswMix,
       "hpnicfLswDeviceAdmin": hpnicfLswDeviceAdmin}
)
