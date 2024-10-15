# SNMP MIB module (HUAWEI-3COM-OID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-3COM-OID-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:49 2024
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

_Huawei_ObjectIdentity = ObjectIdentity
huawei = _Huawei_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011)
)
_HwLocal_ObjectIdentity = ObjectIdentity
hwLocal = _HwLocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1)
)
_Quidway_ObjectIdentity = ObjectIdentity
quidway = _Quidway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1)
)
_HwInternetProtocol_ObjectIdentity = ObjectIdentity
hwInternetProtocol = _HwInternetProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3)
)
_RIp_ObjectIdentity = ObjectIdentity
rIp = _RIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 1)
)
_RIcmp_ObjectIdentity = ObjectIdentity
rIcmp = _RIcmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 2)
)
_VrpProtocol_ObjectIdentity = ObjectIdentity
vrpProtocol = _VrpProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 3)
)
_Huawei_qos_ObjectIdentity = ObjectIdentity
huawei_qos = _Huawei_qos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 3, 2)
)
_Huawei_vlan_ObjectIdentity = ObjectIdentity
huawei_vlan = _Huawei_vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 3, 3)
)
_RmonExtend_ObjectIdentity = ObjectIdentity
rmonExtend = _RmonExtend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 4)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2)
)
_Router_ObjectIdentity = ObjectIdentity
router = _Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2)
)
_LanSw_ObjectIdentity = ObjectIdentity
lanSw = _LanSw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23)
)
_LswCommon_ObjectIdentity = ObjectIdentity
lswCommon = _LswCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1)
)
_HwLswExtInterface_ObjectIdentity = ObjectIdentity
hwLswExtInterface = _HwLswExtInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1)
)
_HwLswVlan_ObjectIdentity = ObjectIdentity
hwLswVlan = _HwLswVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2)
)
_HwLswMacPort_ObjectIdentity = ObjectIdentity
hwLswMacPort = _HwLswMacPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3)
)
_HwLswArpMib_ObjectIdentity = ObjectIdentity
hwLswArpMib = _HwLswArpMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 4)
)
_HwLswL2InfMib_ObjectIdentity = ObjectIdentity
hwLswL2InfMib = _HwLswL2InfMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5)
)
_HwLswRstpMib_ObjectIdentity = ObjectIdentity
hwLswRstpMib = _HwLswRstpMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6)
)
_HwLswIgmpsnoopingMib_ObjectIdentity = ObjectIdentity
hwLswIgmpsnoopingMib = _HwLswIgmpsnoopingMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7)
)
_HwLswDhcpMib_ObjectIdentity = ObjectIdentity
hwLswDhcpMib = _HwLswDhcpMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 8)
)
_HwLswdevMMib_ObjectIdentity = ObjectIdentity
hwLswdevMMib = _HwLswdevMMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 9)
)
_HwsLswTrapMib_ObjectIdentity = ObjectIdentity
hwsLswTrapMib = _HwsLswTrapMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12)
)
_Hwdot1sMstp_ObjectIdentity = ObjectIdentity
hwdot1sMstp = _Hwdot1sMstp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 14)
)
_HwLswQosAclMib_ObjectIdentity = ObjectIdentity
hwLswQosAclMib = _HwLswQosAclMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16)
)
_HwLswMix_ObjectIdentity = ObjectIdentity
hwLswMix = _HwLswMix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 17)
)
_HwLswDeviceAdmin_ObjectIdentity = ObjectIdentity
hwLswDeviceAdmin = _HwLswDeviceAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 18)
)
_Mlsr_ObjectIdentity = ObjectIdentity
mlsr = _Mlsr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33)
)
_TerminalServer_ObjectIdentity = ObjectIdentity
terminalServer = _TerminalServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1)
)
_HuaweiNDEC_ObjectIdentity = ObjectIdentity
huaweiNDEC = _HuaweiNDEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 2)
)
_RedundancyPower_ObjectIdentity = ObjectIdentity
redundancyPower = _RedundancyPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 4)
)
_RedundancyFan_ObjectIdentity = ObjectIdentity
redundancyFan = _RedundancyFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 5)
)
_HwmSystem_ObjectIdentity = ObjectIdentity
hwmSystem = _HwmSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 6)
)
_Hw8040If_ObjectIdentity = ObjectIdentity
hw8040If = _Hw8040If_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 7)
)
_Pos_ObjectIdentity = ObjectIdentity
pos = _Pos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8)
)
_HwIsdnMib_ObjectIdentity = ObjectIdentity
hwIsdnMib = _HwIsdnMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 9)
)
_AR46_E200_ObjectIdentity = ObjectIdentity
aR46_E200 = _AR46_E200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 20)
)
_Dlsw_ObjectIdentity = ObjectIdentity
dlsw = _Dlsw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 34)
)
_HuaweiMgmt_ObjectIdentity = ObjectIdentity
huaweiMgmt = _HuaweiMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5)
)
_HwDhcp_ObjectIdentity = ObjectIdentity
hwDhcp = _HwDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 7)
)
_HwDHCPRelayMib_ObjectIdentity = ObjectIdentity
hwDHCPRelayMib = _HwDHCPRelayMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 7, 1)
)
_HwDHCPServerMib_ObjectIdentity = ObjectIdentity
hwDHCPServerMib = _HwDHCPServerMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 7, 2)
)
_HwMpls_ObjectIdentity = ObjectIdentity
hwMpls = _HwMpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12)
)
_HwMplsLsr_ObjectIdentity = ObjectIdentity
hwMplsLsr = _HwMplsLsr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 1)
)
_HwMplsLdp_ObjectIdentity = ObjectIdentity
hwMplsLdp = _HwMplsLdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2)
)
_HwMplsVpn_ObjectIdentity = ObjectIdentity
hwMplsVpn = _HwMplsVpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3)
)
_HwpaeExtMib_ObjectIdentity = ObjectIdentity
hwpaeExtMib = _HwpaeExtMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 22)
)
_HuaweiDatacomm_ObjectIdentity = ObjectIdentity
huaweiDatacomm = _HuaweiDatacomm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25)
)
_Voice_ObjectIdentity = ObjectIdentity
voice = _Voice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1)
)
_HwVoiceGeneralMIB_ObjectIdentity = ObjectIdentity
hwVoiceGeneralMIB = _HwVoiceGeneralMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1)
)
_HwVoiceIfMIB_ObjectIdentity = ObjectIdentity
hwVoiceIfMIB = _HwVoiceIfMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 2)
)
_HwVoiceAnalogInterfaceMIB_ObjectIdentity = ObjectIdentity
hwVoiceAnalogInterfaceMIB = _HwVoiceAnalogInterfaceMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3)
)
_HwVoiceDigitalInterfaceMIB_ObjectIdentity = ObjectIdentity
hwVoiceDigitalInterfaceMIB = _HwVoiceDigitalInterfaceMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 4)
)
_HwVoiceDialControlMIB_ObjectIdentity = ObjectIdentity
hwVoiceDialControlMIB = _HwVoiceDialControlMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5)
)
_HwVoiceCallActiveMIB_ObjectIdentity = ObjectIdentity
hwVoiceCallActiveMIB = _HwVoiceCallActiveMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 6)
)
_HwVoiceCallHistoryMIB_ObjectIdentity = ObjectIdentity
hwVoiceCallHistoryMIB = _HwVoiceCallHistoryMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7)
)
_HwVoiceGKClientMIB_ObjectIdentity = ObjectIdentity
hwVoiceGKClientMIB = _HwVoiceGKClientMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 8)
)
_HwVoiceAAAClientMIB_ObjectIdentity = ObjectIdentity
hwVoiceAAAClientMIB = _HwVoiceAAAClientMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 9)
)
_HwVoiceH323CallStatMIB_ObjectIdentity = ObjectIdentity
hwVoiceH323CallStatMIB = _HwVoiceH323CallStatMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11)
)
_HwSIPMIB_ObjectIdentity = ObjectIdentity
hwSIPMIB = _HwSIPMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12)
)
_HwIPX_ObjectIdentity = ObjectIdentity
hwIPX = _HwIPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 2)
)
_HwFWTP_ObjectIdentity = ObjectIdentity
hwFWTP = _HwFWTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 3)
)
_HwHIIP_ObjectIdentity = ObjectIdentity
hwHIIP = _HwHIIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 4)
)
_HwHRP_ObjectIdentity = ObjectIdentity
hwHRP = _HwHRP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 5)
)
_HwASPF_ObjectIdentity = ObjectIdentity
hwASPF = _HwASPF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 6)
)
_HwNAT_ObjectIdentity = ObjectIdentity
hwNAT = _HwNAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7)
)
_HwBLS_ObjectIdentity = ObjectIdentity
hwBLS = _HwBLS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 8)
)
_HwMACBIND_ObjectIdentity = ObjectIdentity
hwMACBIND = _HwMACBIND_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 9)
)
_HwATK_ObjectIdentity = ObjectIdentity
hwATK = _HwATK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10)
)
_HwSECSTAT_ObjectIdentity = ObjectIdentity
hwSECSTAT = _HwSECSTAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11)
)
_HwPFLT_ObjectIdentity = ObjectIdentity
hwPFLT = _HwPFLT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 12)
)
_HwTRNG_ObjectIdentity = ObjectIdentity
hwTRNG = _HwTRNG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 13)
)
_HwSMAP_ObjectIdentity = ObjectIdentity
hwSMAP = _HwSMAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 14)
)
_HwSZONE_ObjectIdentity = ObjectIdentity
hwSZONE = _HwSZONE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 15)
)
_HwSLOG_ObjectIdentity = ObjectIdentity
hwSLOG = _HwSLOG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 16)
)
_HwSSHMIB_ObjectIdentity = ObjectIdentity
hwSSHMIB = _HwSSHMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 17)
)
_HwUserLogMIB_ObjectIdentity = ObjectIdentity
hwUserLogMIB = _HwUserLogMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 18)
)
_HwSystemMan_ObjectIdentity = ObjectIdentity
hwSystemMan = _HwSystemMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19)
)
_HwTACACS_ObjectIdentity = ObjectIdentity
hwTACACS = _HwTACACS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20)
)
_HwNBPortalMIB_ObjectIdentity = ObjectIdentity
hwNBPortalMIB = _HwNBPortalMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 21)
)
_HwNTP_ObjectIdentity = ObjectIdentity
hwNTP = _HwNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 22)
)
_HwCmdOverSnmpMib_ObjectIdentity = ObjectIdentity
hwCmdOverSnmpMib = _HwCmdOverSnmpMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 23)
)
_HwISIS_ObjectIdentity = ObjectIdentity
hwISIS = _HwISIS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24)
)
_HwLAG_ObjectIdentity = ObjectIdentity
hwLAG = _HwLAG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 25)
)
_HwSmonExtend_ObjectIdentity = ObjectIdentity
hwSmonExtend = _HwSmonExtend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 26)
)
_HwTask_ObjectIdentity = ObjectIdentity
hwTask = _HwTask_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 27)
)
_HwDismanPing_ObjectIdentity = ObjectIdentity
hwDismanPing = _HwDismanPing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28)
)
_HwVlan_ObjectIdentity = ObjectIdentity
hwVlan = _HwVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 29)
)
_HwAddrMgmt_ObjectIdentity = ObjectIdentity
hwAddrMgmt = _HwAddrMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 30)
)
_HwEntityExtentMIB_ObjectIdentity = ObjectIdentity
hwEntityExtentMIB = _HwEntityExtentMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31)
)
_HwQoS_ObjectIdentity = ObjectIdentity
hwQoS = _HwQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32)
)
_HwMultilinkPPP_ObjectIdentity = ObjectIdentity
hwMultilinkPPP = _HwMultilinkPPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33)
)
_HwTCPMib_ObjectIdentity = ObjectIdentity
hwTCPMib = _HwTCPMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 34)
)
_HwBGPMib_ObjectIdentity = ObjectIdentity
hwBGPMib = _HwBGPMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 35)
)
_HuaweiUtility_ObjectIdentity = ObjectIdentity
huaweiUtility = _HuaweiUtility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6)
)
_HwDevice_ObjectIdentity = ObjectIdentity
hwDevice = _HwDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 1)
)
_HwCluster_ObjectIdentity = ObjectIdentity
hwCluster = _HwCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7)
)
_H3c_ObjectIdentity = ObjectIdentity
h3c = _H3c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10)
)
_H3cProductId_ObjectIdentity = ObjectIdentity
h3cProductId = _H3cProductId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1)
)
_H3cCommon_ObjectIdentity = ObjectIdentity
h3cCommon = _H3cCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2)
)
_H3cFtm_ObjectIdentity = ObjectIdentity
h3cFtm = _H3cFtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 1)
)
_H3cUIMgt_ObjectIdentity = ObjectIdentity
h3cUIMgt = _H3cUIMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2)
)
_H3cSystemMan_ObjectIdentity = ObjectIdentity
h3cSystemMan = _H3cSystemMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3)
)
_H3cConfig_ObjectIdentity = ObjectIdentity
h3cConfig = _H3cConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 4)
)
_H3cFlash_ObjectIdentity = ObjectIdentity
h3cFlash = _H3cFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 5)
)
_H3cEntityExtend_ObjectIdentity = ObjectIdentity
h3cEntityExtend = _H3cEntityExtend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6)
)
_H3cIPSecMonitor_ObjectIdentity = ObjectIdentity
h3cIPSecMonitor = _H3cIPSecMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 7)
)
_H3cAcl_ObjectIdentity = ObjectIdentity
h3cAcl = _H3cAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8)
)
_H3cVoiceVlan_ObjectIdentity = ObjectIdentity
h3cVoiceVlan = _H3cVoiceVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 9)
)
_H3cL4Redirect_ObjectIdentity = ObjectIdentity
h3cL4Redirect = _H3cL4Redirect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 10)
)
_H3cIpPBX_ObjectIdentity = ObjectIdentity
h3cIpPBX = _H3cIpPBX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 11)
)
_H3cUser_ObjectIdentity = ObjectIdentity
h3cUser = _H3cUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12)
)
_H3cRadius_ObjectIdentity = ObjectIdentity
h3cRadius = _H3cRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 13)
)
_H3cPowerEthernetExt_ObjectIdentity = ObjectIdentity
h3cPowerEthernetExt = _H3cPowerEthernetExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14)
)
_H3cEntityRelation_ObjectIdentity = ObjectIdentity
h3cEntityRelation = _H3cEntityRelation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 15)
)
_H3cProtocolVlan_ObjectIdentity = ObjectIdentity
h3cProtocolVlan = _H3cProtocolVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 16)
)
_H3cQosProfile_ObjectIdentity = ObjectIdentity
h3cQosProfile = _H3cQosProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 17)
)
_H3cNat_ObjectIdentity = ObjectIdentity
h3cNat = _H3cNat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18)
)
_H3cPos_ObjectIdentity = ObjectIdentity
h3cPos = _H3cPos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19)
)
_H3cNS_ObjectIdentity = ObjectIdentity
h3cNS = _H3cNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20)
)
_H3cAAL5_ObjectIdentity = ObjectIdentity
h3cAAL5 = _H3cAAL5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 21)
)
_H3cSSH_ObjectIdentity = ObjectIdentity
h3cSSH = _H3cSSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 22)
)
_H3cRSA_ObjectIdentity = ObjectIdentity
h3cRSA = _H3cRSA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 23)
)
_H3cVrrpExt_ObjectIdentity = ObjectIdentity
h3cVrrpExt = _H3cVrrpExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 24)
)
_H3cIpa_ObjectIdentity = ObjectIdentity
h3cIpa = _H3cIpa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 25)
)
_H3cPortSecurity_ObjectIdentity = ObjectIdentity
h3cPortSecurity = _H3cPortSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26)
)
_H3cVpls_ObjectIdentity = ObjectIdentity
h3cVpls = _H3cVpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 27)
)
_H3cE1_ObjectIdentity = ObjectIdentity
h3cE1 = _H3cE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 28)
)
_H3cT1_ObjectIdentity = ObjectIdentity
h3cT1 = _H3cT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 29)
)
_H3cIKEMonitor_ObjectIdentity = ObjectIdentity
h3cIKEMonitor = _H3cIKEMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30)
)
_H3cWebSwitch_ObjectIdentity = ObjectIdentity
h3cWebSwitch = _H3cWebSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 31)
)
_H3cAutoDetect_ObjectIdentity = ObjectIdentity
h3cAutoDetect = _H3cAutoDetect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 32)
)
_H3cIpBroadcast_ObjectIdentity = ObjectIdentity
h3cIpBroadcast = _H3cIpBroadcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 33)
)
_H3cIpx_ObjectIdentity = ObjectIdentity
h3cIpx = _H3cIpx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 34)
)
_H3cIPS_ObjectIdentity = ObjectIdentity
h3cIPS = _H3cIPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 35)
)
_H3cDhcpSnoop_ObjectIdentity = ObjectIdentity
h3cDhcpSnoop = _H3cDhcpSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 36)
)
_H3cProtocolPriority_ObjectIdentity = ObjectIdentity
h3cProtocolPriority = _H3cProtocolPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 37)
)
_H3cTrap_ObjectIdentity = ObjectIdentity
h3cTrap = _H3cTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38)
)
_H3cVoice_ObjectIdentity = ObjectIdentity
h3cVoice = _H3cVoice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39)
)
_H3cIfExt_ObjectIdentity = ObjectIdentity
h3cIfExt = _H3cIfExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40)
)
_H3cCfCard_ObjectIdentity = ObjectIdentity
h3cCfCard = _H3cCfCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 41)
)
_H3cEpon_ObjectIdentity = ObjectIdentity
h3cEpon = _H3cEpon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42)
)
_H3cDldp_ObjectIdentity = ObjectIdentity
h3cDldp = _H3cDldp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 43)
)
_H3cUnicast_ObjectIdentity = ObjectIdentity
h3cUnicast = _H3cUnicast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 44)
)
_H3cRrpp_ObjectIdentity = ObjectIdentity
h3cRrpp = _H3cRrpp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 45)
)
_H3cDomain_ObjectIdentity = ObjectIdentity
h3cDomain = _H3cDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46)
)
_H3cIds_ObjectIdentity = ObjectIdentity
h3cIds = _H3cIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 47)
)
_H3cRcr_ObjectIdentity = ObjectIdentity
h3cRcr = _H3cRcr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 48)
)
_H3cAtmDxi_ObjectIdentity = ObjectIdentity
h3cAtmDxi = _H3cAtmDxi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 49)
)
_H3cMulticast_ObjectIdentity = ObjectIdentity
h3cMulticast = _H3cMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 50)
)
_H3cMpm_ObjectIdentity = ObjectIdentity
h3cMpm = _H3cMpm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 51)
)
_H3cOadp_ObjectIdentity = ObjectIdentity
h3cOadp = _H3cOadp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 52)
)
_H3cTunnel_ObjectIdentity = ObjectIdentity
h3cTunnel = _H3cTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53)
)
_H3cGre_ObjectIdentity = ObjectIdentity
h3cGre = _H3cGre_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 54)
)
_H3cObjectInfo_ObjectIdentity = ObjectIdentity
h3cObjectInfo = _H3cObjectInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 55)
)
_H3cStorage_ObjectIdentity = ObjectIdentity
h3cStorage = _H3cStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 56)
)
_H3cDvpn_ObjectIdentity = ObjectIdentity
h3cDvpn = _H3cDvpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 57)
)
_H3cDhcpRelay_ObjectIdentity = ObjectIdentity
h3cDhcpRelay = _H3cDhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 58)
)
_H3cIsis_ObjectIdentity = ObjectIdentity
h3cIsis = _H3cIsis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 59)
)
_H3cRpr_ObjectIdentity = ObjectIdentity
h3cRpr = _H3cRpr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 60)
)
_H3cSubnetVlan_ObjectIdentity = ObjectIdentity
h3cSubnetVlan = _H3cSubnetVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 61)
)
_H3cDlswExt_ObjectIdentity = ObjectIdentity
h3cDlswExt = _H3cDlswExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 62)
)
_H3cSyslog_ObjectIdentity = ObjectIdentity
h3cSyslog = _H3cSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63)
)
_H3cFlowTemplate_ObjectIdentity = ObjectIdentity
h3cFlowTemplate = _H3cFlowTemplate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 64)
)
_H3cQos2_ObjectIdentity = ObjectIdentity
h3cQos2 = _H3cQos2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 65)
)
_H3cIfQos2_ObjectIdentity = ObjectIdentity
h3cIfQos2 = _H3cIfQos2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 65, 1)
)
_H3cCBQos2_ObjectIdentity = ObjectIdentity
h3cCBQos2 = _H3cCBQos2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 65, 2)
)
_H3cStormConstrain_ObjectIdentity = ObjectIdentity
h3cStormConstrain = _H3cStormConstrain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 66)
)
_H3cIpAddrMIB_ObjectIdentity = ObjectIdentity
h3cIpAddrMIB = _H3cIpAddrMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 67)
)
_H3cMirrGroup_ObjectIdentity = ObjectIdentity
h3cMirrGroup = _H3cMirrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 68)
)
_H3cQINQ_ObjectIdentity = ObjectIdentity
h3cQINQ = _H3cQINQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 69)
)
_H3cTransceiver_ObjectIdentity = ObjectIdentity
h3cTransceiver = _H3cTransceiver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 70)
)
_H3cIpv6AddrMIB_ObjectIdentity = ObjectIdentity
h3cIpv6AddrMIB = _H3cIpv6AddrMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 71)
)
_H3cBfdMIB_ObjectIdentity = ObjectIdentity
h3cBfdMIB = _H3cBfdMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72)
)
_H3cRCP_ObjectIdentity = ObjectIdentity
h3cRCP = _H3cRCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 73)
)
_H3cAcfp_ObjectIdentity = ObjectIdentity
h3cAcfp = _H3cAcfp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 74)
)
_H3cDot11_ObjectIdentity = ObjectIdentity
h3cDot11 = _H3cDot11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75)
)
_H3cE1T1VI_ObjectIdentity = ObjectIdentity
h3cE1T1VI = _H3cE1T1VI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 76)
)
_H3cwapiMIB_ObjectIdentity = ObjectIdentity
h3cwapiMIB = _H3cwapiMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77)
)
_H3cL2VpnPwe3_ObjectIdentity = ObjectIdentity
h3cL2VpnPwe3 = _H3cL2VpnPwe3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 78)
)
_H3cMplsOam_ObjectIdentity = ObjectIdentity
h3cMplsOam = _H3cMplsOam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79)
)
_H3cMplsOamPs_ObjectIdentity = ObjectIdentity
h3cMplsOamPs = _H3cMplsOamPs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 80)
)
_H3cSiemMib_ObjectIdentity = ObjectIdentity
h3cSiemMib = _H3cSiemMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 81)
)
_H3cUps_ObjectIdentity = ObjectIdentity
h3cUps = _H3cUps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 82)
)
_H3cEOCCommon_ObjectIdentity = ObjectIdentity
h3cEOCCommon = _H3cEOCCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83)
)
_H3cHPEOC_ObjectIdentity = ObjectIdentity
h3cHPEOC = _H3cHPEOC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84)
)
_H3cAFC_ObjectIdentity = ObjectIdentity
h3cAFC = _H3cAFC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 85)
)
_H3cMultCDR_ObjectIdentity = ObjectIdentity
h3cMultCDR = _H3cMultCDR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 86)
)
_H3cMACInformation_ObjectIdentity = ObjectIdentity
h3cMACInformation = _H3cMACInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 87)
)
_H3cFireWall_ObjectIdentity = ObjectIdentity
h3cFireWall = _H3cFireWall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 88)
)
_H3cDSP_ObjectIdentity = ObjectIdentity
h3cDSP = _H3cDSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 89)
)
_H3cNetMan_ObjectIdentity = ObjectIdentity
h3cNetMan = _H3cNetMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 90)
)
_H3cStack_ObjectIdentity = ObjectIdentity
h3cStack = _H3cStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 91)
)
_H3cPosa_ObjectIdentity = ObjectIdentity
h3cPosa = _H3cPosa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92)
)
_H3cWebAuthentication_ObjectIdentity = ObjectIdentity
h3cWebAuthentication = _H3cWebAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 93)
)
_H3cCATVTransceiver_ObjectIdentity = ObjectIdentity
h3cCATVTransceiver = _H3cCATVTransceiver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 94)
)
_H3cLpbkdt_ObjectIdentity = ObjectIdentity
h3cLpbkdt = _H3cLpbkdt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 95)
)
_H3cMultiMedia_ObjectIdentity = ObjectIdentity
h3cMultiMedia = _H3cMultiMedia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 96)
)
_H3cDns_ObjectIdentity = ObjectIdentity
h3cDns = _H3cDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 97)
)
_H3c3GModem_ObjectIdentity = ObjectIdentity
h3c3GModem = _H3c3GModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98)
)
_H3cPortal_ObjectIdentity = ObjectIdentity
h3cPortal = _H3cPortal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99)
)
_H3clldp_ObjectIdentity = ObjectIdentity
h3clldp = _H3clldp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 100)
)
_H3cDHCPServer_ObjectIdentity = ObjectIdentity
h3cDHCPServer = _H3cDHCPServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101)
)
_H3cPPPoEServer_ObjectIdentity = ObjectIdentity
h3cPPPoEServer = _H3cPPPoEServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 102)
)
_H3cL2Isolate_ObjectIdentity = ObjectIdentity
h3cL2Isolate = _H3cL2Isolate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 103)
)
_H3cSnmpExt_ObjectIdentity = ObjectIdentity
h3cSnmpExt = _H3cSnmpExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 104)
)
_H3cVsi_ObjectIdentity = ObjectIdentity
h3cVsi = _H3cVsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105)
)
_H3cEvc_ObjectIdentity = ObjectIdentity
h3cEvc = _H3cEvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 106)
)
_H3cMinm_ObjectIdentity = ObjectIdentity
h3cMinm = _H3cMinm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 107)
)
_H3cBlg_ObjectIdentity = ObjectIdentity
h3cBlg = _H3cBlg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 108)
)
_H3cRS485_ObjectIdentity = ObjectIdentity
h3cRS485 = _H3cRS485_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 109)
)
_H3cARPRatelimit_ObjectIdentity = ObjectIdentity
h3cARPRatelimit = _H3cARPRatelimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 110)
)
_H3cLI_ObjectIdentity = ObjectIdentity
h3cLI = _H3cLI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 111)
)
_H3cDar_ObjectIdentity = ObjectIdentity
h3cDar = _H3cDar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 112)
)
_H3cPBR_ObjectIdentity = ObjectIdentity
h3cPBR = _H3cPBR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 113)
)
_H3cAAANasId_ObjectIdentity = ObjectIdentity
h3cAAANasId = _H3cAAANasId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 114)
)
_H3cTeTunnel_ObjectIdentity = ObjectIdentity
h3cTeTunnel = _H3cTeTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 115)
)
_H3cLB_ObjectIdentity = ObjectIdentity
h3cLB = _H3cLB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 116)
)
_H3cDldp2_ObjectIdentity = ObjectIdentity
h3cDldp2 = _H3cDldp2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 117)
)
_H3cWIPS_ObjectIdentity = ObjectIdentity
h3cWIPS = _H3cWIPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 118)
)
_H3cFCoE_ObjectIdentity = ObjectIdentity
h3cFCoE = _H3cFCoE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120)
)
_H3cEntityVendorTypeOID_ObjectIdentity = ObjectIdentity
h3cEntityVendorTypeOID = _H3cEntityVendorTypeOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3)
)
_H3cNM_ObjectIdentity = ObjectIdentity
h3cNM = _H3cNM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 4)
)
_HwSystem_ObjectIdentity = ObjectIdentity
hwSystem = _HwSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 6)
)
_H3cSNMPAgCpb_ObjectIdentity = ObjectIdentity
h3cSNMPAgCpb = _H3cSNMPAgCpb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 7)
)
_H3cQosCapability_ObjectIdentity = ObjectIdentity
h3cQosCapability = _H3cQosCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 7, 1)
)
_H3cRhw_ObjectIdentity = ObjectIdentity
h3cRhw = _H3cRhw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 8)
)
_H3cNqa_ObjectIdentity = ObjectIdentity
h3cNqa = _H3cNqa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 8, 3)
)
_H3cHgmp_ObjectIdentity = ObjectIdentity
h3cHgmp = _H3cHgmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 8, 7)
)
_H3cNTP_ObjectIdentity = ObjectIdentity
h3cNTP = _H3cNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 8, 19)
)
_H3cSurveillanceMIB_ObjectIdentity = ObjectIdentity
h3cSurveillanceMIB = _H3cSurveillanceMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9)
)
_H3cVMMan_ObjectIdentity = ObjectIdentity
h3cVMMan = _H3cVMMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1)
)
_H3cPUMan_ObjectIdentity = ObjectIdentity
h3cPUMan = _H3cPUMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2)
)
_H3cMSMan_ObjectIdentity = ObjectIdentity
h3cMSMan = _H3cMSMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3)
)
_H3cStorageRef_ObjectIdentity = ObjectIdentity
h3cStorageRef = _H3cStorageRef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10)
)
_H3cStorageMIB_ObjectIdentity = ObjectIdentity
h3cStorageMIB = _H3cStorageMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1)
)
_H3cStorageSnap_ObjectIdentity = ObjectIdentity
h3cStorageSnap = _H3cStorageSnap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2)
)
_H3cDisk_ObjectIdentity = ObjectIdentity
h3cDisk = _H3cDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 3)
)
_H3cRaid_ObjectIdentity = ObjectIdentity
h3cRaid = _H3cRaid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 4)
)
_H3cLogicVolume_ObjectIdentity = ObjectIdentity
h3cLogicVolume = _H3cLogicVolume_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5)
)
_HuaweiTCMIB_ObjectIdentity = ObjectIdentity
huaweiTCMIB = _HuaweiTCMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 20021210)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-3COM-OID-MIB",
    **{"huawei": huawei,
       "hwLocal": hwLocal,
       "quidway": quidway,
       "hwInternetProtocol": hwInternetProtocol,
       "rIp": rIp,
       "rIcmp": rIcmp,
       "vrpProtocol": vrpProtocol,
       "huawei-qos": huawei_qos,
       "huawei-vlan": huawei_vlan,
       "rmonExtend": rmonExtend,
       "products": products,
       "router": router,
       "lanSw": lanSw,
       "lswCommon": lswCommon,
       "hwLswExtInterface": hwLswExtInterface,
       "hwLswVlan": hwLswVlan,
       "hwLswMacPort": hwLswMacPort,
       "hwLswArpMib": hwLswArpMib,
       "hwLswL2InfMib": hwLswL2InfMib,
       "hwLswRstpMib": hwLswRstpMib,
       "hwLswIgmpsnoopingMib": hwLswIgmpsnoopingMib,
       "hwLswDhcpMib": hwLswDhcpMib,
       "hwLswdevMMib": hwLswdevMMib,
       "hwsLswTrapMib": hwsLswTrapMib,
       "hwdot1sMstp": hwdot1sMstp,
       "hwLswQosAclMib": hwLswQosAclMib,
       "hwLswMix": hwLswMix,
       "hwLswDeviceAdmin": hwLswDeviceAdmin,
       "mlsr": mlsr,
       "terminalServer": terminalServer,
       "huaweiNDEC": huaweiNDEC,
       "redundancyPower": redundancyPower,
       "redundancyFan": redundancyFan,
       "hwmSystem": hwmSystem,
       "hw8040If": hw8040If,
       "pos": pos,
       "hwIsdnMib": hwIsdnMib,
       "aR46-E200": aR46_E200,
       "dlsw": dlsw,
       "huaweiMgmt": huaweiMgmt,
       "hwDhcp": hwDhcp,
       "hwDHCPRelayMib": hwDHCPRelayMib,
       "hwDHCPServerMib": hwDHCPServerMib,
       "hwMpls": hwMpls,
       "hwMplsLsr": hwMplsLsr,
       "hwMplsLdp": hwMplsLdp,
       "hwMplsVpn": hwMplsVpn,
       "hwpaeExtMib": hwpaeExtMib,
       "huaweiDatacomm": huaweiDatacomm,
       "voice": voice,
       "hwVoiceGeneralMIB": hwVoiceGeneralMIB,
       "hwVoiceIfMIB": hwVoiceIfMIB,
       "hwVoiceAnalogInterfaceMIB": hwVoiceAnalogInterfaceMIB,
       "hwVoiceDigitalInterfaceMIB": hwVoiceDigitalInterfaceMIB,
       "hwVoiceDialControlMIB": hwVoiceDialControlMIB,
       "hwVoiceCallActiveMIB": hwVoiceCallActiveMIB,
       "hwVoiceCallHistoryMIB": hwVoiceCallHistoryMIB,
       "hwVoiceGKClientMIB": hwVoiceGKClientMIB,
       "hwVoiceAAAClientMIB": hwVoiceAAAClientMIB,
       "hwVoiceH323CallStatMIB": hwVoiceH323CallStatMIB,
       "hwSIPMIB": hwSIPMIB,
       "hwIPX": hwIPX,
       "hwFWTP": hwFWTP,
       "hwHIIP": hwHIIP,
       "hwHRP": hwHRP,
       "hwASPF": hwASPF,
       "hwNAT": hwNAT,
       "hwBLS": hwBLS,
       "hwMACBIND": hwMACBIND,
       "hwATK": hwATK,
       "hwSECSTAT": hwSECSTAT,
       "hwPFLT": hwPFLT,
       "hwTRNG": hwTRNG,
       "hwSMAP": hwSMAP,
       "hwSZONE": hwSZONE,
       "hwSLOG": hwSLOG,
       "hwSSHMIB": hwSSHMIB,
       "hwUserLogMIB": hwUserLogMIB,
       "hwSystemMan": hwSystemMan,
       "hwTACACS": hwTACACS,
       "hwNBPortalMIB": hwNBPortalMIB,
       "hwNTP": hwNTP,
       "hwCmdOverSnmpMib": hwCmdOverSnmpMib,
       "hwISIS": hwISIS,
       "hwLAG": hwLAG,
       "hwSmonExtend": hwSmonExtend,
       "hwTask": hwTask,
       "hwDismanPing": hwDismanPing,
       "hwVlan": hwVlan,
       "hwAddrMgmt": hwAddrMgmt,
       "hwEntityExtentMIB": hwEntityExtentMIB,
       "hwQoS": hwQoS,
       "hwMultilinkPPP": hwMultilinkPPP,
       "hwTCPMib": hwTCPMib,
       "hwBGPMib": hwBGPMib,
       "huaweiUtility": huaweiUtility,
       "hwDevice": hwDevice,
       "hwCluster": hwCluster,
       "h3c": h3c,
       "h3cProductId": h3cProductId,
       "h3cCommon": h3cCommon,
       "h3cFtm": h3cFtm,
       "h3cUIMgt": h3cUIMgt,
       "h3cSystemMan": h3cSystemMan,
       "h3cConfig": h3cConfig,
       "h3cFlash": h3cFlash,
       "h3cEntityExtend": h3cEntityExtend,
       "h3cIPSecMonitor": h3cIPSecMonitor,
       "h3cAcl": h3cAcl,
       "h3cVoiceVlan": h3cVoiceVlan,
       "h3cL4Redirect": h3cL4Redirect,
       "h3cIpPBX": h3cIpPBX,
       "h3cUser": h3cUser,
       "h3cRadius": h3cRadius,
       "h3cPowerEthernetExt": h3cPowerEthernetExt,
       "h3cEntityRelation": h3cEntityRelation,
       "h3cProtocolVlan": h3cProtocolVlan,
       "h3cQosProfile": h3cQosProfile,
       "h3cNat": h3cNat,
       "h3cPos": h3cPos,
       "h3cNS": h3cNS,
       "h3cAAL5": h3cAAL5,
       "h3cSSH": h3cSSH,
       "h3cRSA": h3cRSA,
       "h3cVrrpExt": h3cVrrpExt,
       "h3cIpa": h3cIpa,
       "h3cPortSecurity": h3cPortSecurity,
       "h3cVpls": h3cVpls,
       "h3cE1": h3cE1,
       "h3cT1": h3cT1,
       "h3cIKEMonitor": h3cIKEMonitor,
       "h3cWebSwitch": h3cWebSwitch,
       "h3cAutoDetect": h3cAutoDetect,
       "h3cIpBroadcast": h3cIpBroadcast,
       "h3cIpx": h3cIpx,
       "h3cIPS": h3cIPS,
       "h3cDhcpSnoop": h3cDhcpSnoop,
       "h3cProtocolPriority": h3cProtocolPriority,
       "h3cTrap": h3cTrap,
       "h3cVoice": h3cVoice,
       "h3cIfExt": h3cIfExt,
       "h3cCfCard": h3cCfCard,
       "h3cEpon": h3cEpon,
       "h3cDldp": h3cDldp,
       "h3cUnicast": h3cUnicast,
       "h3cRrpp": h3cRrpp,
       "h3cDomain": h3cDomain,
       "h3cIds": h3cIds,
       "h3cRcr": h3cRcr,
       "h3cAtmDxi": h3cAtmDxi,
       "h3cMulticast": h3cMulticast,
       "h3cMpm": h3cMpm,
       "h3cOadp": h3cOadp,
       "h3cTunnel": h3cTunnel,
       "h3cGre": h3cGre,
       "h3cObjectInfo": h3cObjectInfo,
       "h3cStorage": h3cStorage,
       "h3cDvpn": h3cDvpn,
       "h3cDhcpRelay": h3cDhcpRelay,
       "h3cIsis": h3cIsis,
       "h3cRpr": h3cRpr,
       "h3cSubnetVlan": h3cSubnetVlan,
       "h3cDlswExt": h3cDlswExt,
       "h3cSyslog": h3cSyslog,
       "h3cFlowTemplate": h3cFlowTemplate,
       "h3cQos2": h3cQos2,
       "h3cIfQos2": h3cIfQos2,
       "h3cCBQos2": h3cCBQos2,
       "h3cStormConstrain": h3cStormConstrain,
       "h3cIpAddrMIB": h3cIpAddrMIB,
       "h3cMirrGroup": h3cMirrGroup,
       "h3cQINQ": h3cQINQ,
       "h3cTransceiver": h3cTransceiver,
       "h3cIpv6AddrMIB": h3cIpv6AddrMIB,
       "h3cBfdMIB": h3cBfdMIB,
       "h3cRCP": h3cRCP,
       "h3cAcfp": h3cAcfp,
       "h3cDot11": h3cDot11,
       "h3cE1T1VI": h3cE1T1VI,
       "h3cwapiMIB": h3cwapiMIB,
       "h3cL2VpnPwe3": h3cL2VpnPwe3,
       "h3cMplsOam": h3cMplsOam,
       "h3cMplsOamPs": h3cMplsOamPs,
       "h3cSiemMib": h3cSiemMib,
       "h3cUps": h3cUps,
       "h3cEOCCommon": h3cEOCCommon,
       "h3cHPEOC": h3cHPEOC,
       "h3cAFC": h3cAFC,
       "h3cMultCDR": h3cMultCDR,
       "h3cMACInformation": h3cMACInformation,
       "h3cFireWall": h3cFireWall,
       "h3cDSP": h3cDSP,
       "h3cNetMan": h3cNetMan,
       "h3cStack": h3cStack,
       "h3cPosa": h3cPosa,
       "h3cWebAuthentication": h3cWebAuthentication,
       "h3cCATVTransceiver": h3cCATVTransceiver,
       "h3cLpbkdt": h3cLpbkdt,
       "h3cMultiMedia": h3cMultiMedia,
       "h3cDns": h3cDns,
       "h3c3GModem": h3c3GModem,
       "h3cPortal": h3cPortal,
       "h3clldp": h3clldp,
       "h3cDHCPServer": h3cDHCPServer,
       "h3cPPPoEServer": h3cPPPoEServer,
       "h3cL2Isolate": h3cL2Isolate,
       "h3cSnmpExt": h3cSnmpExt,
       "h3cVsi": h3cVsi,
       "h3cEvc": h3cEvc,
       "h3cMinm": h3cMinm,
       "h3cBlg": h3cBlg,
       "h3cRS485": h3cRS485,
       "h3cARPRatelimit": h3cARPRatelimit,
       "h3cLI": h3cLI,
       "h3cDar": h3cDar,
       "h3cPBR": h3cPBR,
       "h3cAAANasId": h3cAAANasId,
       "h3cTeTunnel": h3cTeTunnel,
       "h3cLB": h3cLB,
       "h3cDldp2": h3cDldp2,
       "h3cWIPS": h3cWIPS,
       "h3cFCoE": h3cFCoE,
       "h3cEntityVendorTypeOID": h3cEntityVendorTypeOID,
       "h3cNM": h3cNM,
       "hwSystem": hwSystem,
       "h3cSNMPAgCpb": h3cSNMPAgCpb,
       "h3cQosCapability": h3cQosCapability,
       "h3cRhw": h3cRhw,
       "h3cNqa": h3cNqa,
       "h3cHgmp": h3cHgmp,
       "h3cNTP": h3cNTP,
       "h3cSurveillanceMIB": h3cSurveillanceMIB,
       "h3cVMMan": h3cVMMan,
       "h3cPUMan": h3cPUMan,
       "h3cMSMan": h3cMSMan,
       "h3cStorageRef": h3cStorageRef,
       "h3cStorageMIB": h3cStorageMIB,
       "h3cStorageSnap": h3cStorageSnap,
       "h3cDisk": h3cDisk,
       "h3cRaid": h3cRaid,
       "h3cLogicVolume": h3cLogicVolume,
       "huaweiTCMIB": huaweiTCMIB}
)
