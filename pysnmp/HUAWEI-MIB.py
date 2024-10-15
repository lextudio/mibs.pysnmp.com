# SNMP MIB module (HUAWEI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:42 2024
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

huawei = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwLocal_ObjectIdentity = ObjectIdentity
hwLocal = _HwLocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1)
)
_Quidway_ObjectIdentity = ObjectIdentity
quidway = _Quidway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1)
)
_HwTrans_ObjectIdentity = ObjectIdentity
hwTrans = _HwTrans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 2)
)
_HwInternetProtocol_ObjectIdentity = ObjectIdentity
hwInternetProtocol = _HwInternetProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3)
)
_RmonExtend_ObjectIdentity = ObjectIdentity
rmonExtend = _RmonExtend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 4)
)
_Performance_ObjectIdentity = ObjectIdentity
performance = _Performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 4, 4)
)
_HwNovellProtocol_ObjectIdentity = ObjectIdentity
hwNovellProtocol = _HwNovellProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 4)
)
_HwProducts_ObjectIdentity = ObjectIdentity
hwProducts = _HwProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2)
)
_Atm_ObjectIdentity = ObjectIdentity
atm = _Atm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 1)
)
_AtmAccess_ObjectIdentity = ObjectIdentity
atmAccess = _AtmAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 1, 1)
)
_AtmBone_ObjectIdentity = ObjectIdentity
atmBone = _AtmBone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 1, 2)
)
_R8750_ObjectIdentity = ObjectIdentity
r8750 = _R8750_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 1, 2, 1)
)
_Router_ObjectIdentity = ObjectIdentity
router = _Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2)
)
_RouterGeneral_ObjectIdentity = ObjectIdentity
routerGeneral = _RouterGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 1)
)
_Attr_ObjectIdentity = ObjectIdentity
attr = _Attr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 1, 1)
)
_Ne08_ObjectIdentity = ObjectIdentity
ne08 = _Ne08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 1, 7508)
)
_Ne16_ObjectIdentity = ObjectIdentity
ne16 = _Ne16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 1, 7516)
)
_Module_ObjectIdentity = ObjectIdentity
module = _Module_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 2)
)
_Flash_ObjectIdentity = ObjectIdentity
flash = _Flash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 3)
)
_Mixinfo_ObjectIdentity = ObjectIdentity
mixinfo = _Mixinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 4)
)
_HuaweiMemoryPool_ObjectIdentity = ObjectIdentity
huaweiMemoryPool = _HuaweiMemoryPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5)
)
_ConfigFile_ObjectIdentity = ObjectIdentity
configFile = _ConfigFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 6)
)
_NetEngine_ObjectIdentity = ObjectIdentity
netEngine = _NetEngine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 8070)
)
_Access_server_ObjectIdentity = ObjectIdentity
access_server = _Access_server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 3)
)
_As8010_ObjectIdentity = ObjectIdentity
as8010 = _As8010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 3, 1)
)
_Lan_switch_ObjectIdentity = ObjectIdentity
lan_switch = _Lan_switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 4)
)
_Switch2403_ObjectIdentity = ObjectIdentity
switch2403 = _Switch2403_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 4, 1)
)
_Switch2403F_ObjectIdentity = ObjectIdentity
switch2403F = _Switch2403F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 4, 1, 0)
)
_Switch3008_ObjectIdentity = ObjectIdentity
switch3008 = _Switch3008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 4, 2)
)
_Switch3016_ObjectIdentity = ObjectIdentity
switch3016 = _Switch3016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 4, 3)
)
_Switch2024_M_ObjectIdentity = ObjectIdentity
switch2024_M = _Switch2024_M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 4, 4)
)
_Switch3025_M_ObjectIdentity = ObjectIdentity
switch3025_M = _Switch3025_M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 4, 5)
)
_Xdsl_ObjectIdentity = ObjectIdentity
xdsl = _Xdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 5)
)
_Adsl_ObjectIdentity = ObjectIdentity
adsl = _Adsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 5, 1)
)
_Musa_ObjectIdentity = ObjectIdentity
musa = _Musa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6)
)
_HwMusaV100R001Mib_ObjectIdentity = ObjectIdentity
hwMusaV100R001Mib = _HwMusaV100R001Mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 1)
)
_HwMA5200Mib_ObjectIdentity = ObjectIdentity
hwMA5200Mib = _HwMA5200Mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2)
)
_HwMusaV100R002Mib_ObjectIdentity = ObjectIdentity
hwMusaV100R002Mib = _HwMusaV100R002Mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 3)
)
_HwMd5500Mib_ObjectIdentity = ObjectIdentity
hwMd5500Mib = _HwMd5500Mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 4)
)
_HwMa5100Mib_ObjectIdentity = ObjectIdentity
hwMa5100Mib = _HwMa5100Mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5)
)
_HwMa5300Mib_ObjectIdentity = ObjectIdentity
hwMa5300Mib = _HwMa5300Mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 6)
)
_Ias_ObjectIdentity = ObjectIdentity
ias = _Ias_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 7)
)
_Mpeg_2_ObjectIdentity = ObjectIdentity
mpeg_2 = _Mpeg_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 7)
)
_Gprs_ObjectIdentity = ObjectIdentity
gprs = _Gprs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 8)
)
_Honet_ObjectIdentity = ObjectIdentity
honet = _Honet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 9)
)
_Cc08_ObjectIdentity = ObjectIdentity
cc08 = _Cc08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 10)
)
_Sbs_ObjectIdentity = ObjectIdentity
sbs = _Sbs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 11)
)
_Ip_phone_ObjectIdentity = ObjectIdentity
ip_phone = _Ip_phone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 12)
)
_Ups_ObjectIdentity = ObjectIdentity
ups = _Ups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 13)
)
_Viewpoint_ObjectIdentity = ObjectIdentity
viewpoint = _Viewpoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 14)
)
_NetManager_ObjectIdentity = ObjectIdentity
netManager = _NetManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15)
)
_INet_ObjectIdentity = ObjectIdentity
iNet = _INet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 16)
)
_Ne80_ObjectIdentity = ObjectIdentity
ne80 = _Ne80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 17)
)
_WireIn_ObjectIdentity = ObjectIdentity
wireIn = _WireIn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 18)
)
_WireInScp_ObjectIdentity = ObjectIdentity
wireInScp = _WireInScp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 18, 1)
)
_WireInSdp_ObjectIdentity = ObjectIdentity
wireInSdp = _WireInSdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 18, 2)
)
_WireInSmp_ObjectIdentity = ObjectIdentity
wireInSmp = _WireInSmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 18, 3)
)
_WireInSsp_ObjectIdentity = ObjectIdentity
wireInSsp = _WireInSsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 18, 4)
)
_WireInIP_ObjectIdentity = ObjectIdentity
wireInIP = _WireInIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 18, 5)
)
_MobileIn_ObjectIdentity = ObjectIdentity
mobileIn = _MobileIn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 19)
)
_MobileInScp_ObjectIdentity = ObjectIdentity
mobileInScp = _MobileInScp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 19, 1)
)
_MobileInSdp_ObjectIdentity = ObjectIdentity
mobileInSdp = _MobileInSdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 19, 2)
)
_MobileInSmp_ObjectIdentity = ObjectIdentity
mobileInSmp = _MobileInSmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 19, 3)
)
_MobileInSsp_ObjectIdentity = ObjectIdentity
mobileInSsp = _MobileInSsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 19, 4)
)
_MobileInIP_ObjectIdentity = ObjectIdentity
mobileInIP = _MobileInIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 19, 5)
)
_CdmaIn_ObjectIdentity = ObjectIdentity
cdmaIn = _CdmaIn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 20)
)
_CdmaInScp_ObjectIdentity = ObjectIdentity
cdmaInScp = _CdmaInScp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 20, 1)
)
_CdmaInSdp_ObjectIdentity = ObjectIdentity
cdmaInSdp = _CdmaInSdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 20, 2)
)
_CdmaInSmp_ObjectIdentity = ObjectIdentity
cdmaInSmp = _CdmaInSmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 20, 3)
)
_CdmaInSsp_ObjectIdentity = ObjectIdentity
cdmaInSsp = _CdmaInSsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 20, 4)
)
_CdmaInIP_ObjectIdentity = ObjectIdentity
cdmaInIP = _CdmaInIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 20, 5)
)
_AcdIn_ObjectIdentity = ObjectIdentity
acdIn = _AcdIn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 21)
)
_Esr_ObjectIdentity = ObjectIdentity
esr = _Esr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 22)
)
_Radium8750_ObjectIdentity = ObjectIdentity
radium8750 = _Radium8750_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 22, 2)
)
_Isn8850_ObjectIdentity = ObjectIdentity
isn8850 = _Isn8850_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 22, 3)
)
_Esr8825_ObjectIdentity = ObjectIdentity
esr8825 = _Esr8825_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 22, 5)
)
_EsrV5R3_ObjectIdentity = ObjectIdentity
esrV5R3 = _EsrV5R3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 22, 6)
)
_EsrV5R58850_ObjectIdentity = ObjectIdentity
esrV5R58850 = _EsrV5R58850_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 22, 7)
)
_EsrV5R58825_ObjectIdentity = ObjectIdentity
esrV5R58825 = _EsrV5R58825_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 22, 8)
)
_LanSw_ObjectIdentity = ObjectIdentity
lanSw = _LanSw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23)
)
_LswCommon_ObjectIdentity = ObjectIdentity
lswCommon = _LswCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1)
)
_S8016_ObjectIdentity = ObjectIdentity
s8016 = _S8016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 11)
)
_S8016Common_ObjectIdentity = ObjectIdentity
s8016Common = _S8016Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 11, 1)
)
_S8016A_ObjectIdentity = ObjectIdentity
s8016A = _S8016A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 11, 2)
)
_S8016B_ObjectIdentity = ObjectIdentity
s8016B = _S8016B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 11, 3)
)
_S3526_ObjectIdentity = ObjectIdentity
s3526 = _S3526_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 12)
)
_S3026_ObjectIdentity = ObjectIdentity
s3026 = _S3026_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 13)
)
_S3026V_ObjectIdentity = ObjectIdentity
s3026V = _S3026V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 14)
)
_S2008_ObjectIdentity = ObjectIdentity
s2008 = _S2008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 15)
)
_S2016_ObjectIdentity = ObjectIdentity
s2016 = _S2016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 16)
)
_S3526F_ObjectIdentity = ObjectIdentity
s3526F = _S3526F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 17)
)
_S5516_ObjectIdentity = ObjectIdentity
s5516 = _S5516_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 18)
)
_S6506_ObjectIdentity = ObjectIdentity
s6506 = _S6506_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 19)
)
_S3026F_ObjectIdentity = ObjectIdentity
s3026F = _S3026F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 20)
)
_S3526E_ObjectIdentity = ObjectIdentity
s3526E = _S3526E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 21)
)
_S2026_ObjectIdentity = ObjectIdentity
s2026 = _S2026_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 22)
)
_S2403H_ObjectIdentity = ObjectIdentity
s2403H = _S2403H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 23)
)
_S3026E_ObjectIdentity = ObjectIdentity
s3026E = _S3026E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 24)
)
_S3050C_ObjectIdentity = ObjectIdentity
s3050C = _S3050C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 29)
)
_S6503_ObjectIdentity = ObjectIdentity
s6503 = _S6503_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 30)
)
_S8512_ObjectIdentity = ObjectIdentity
s8512 = _S8512_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 31)
)
_S8505_ObjectIdentity = ObjectIdentity
s8505 = _S8505_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 32)
)
_S6506R_ObjectIdentity = ObjectIdentity
s6506R = _S6506R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 33)
)
_S3026c_ObjectIdentity = ObjectIdentity
s3026c = _S3026c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 34)
)
_S3026g_ObjectIdentity = ObjectIdentity
s3026g = _S3026g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 35)
)
_S3026t_ObjectIdentity = ObjectIdentity
s3026t = _S3026t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 36)
)
_S3552G_ObjectIdentity = ObjectIdentity
s3552G = _S3552G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 37)
)
_S3552P_ObjectIdentity = ObjectIdentity
s3552P = _S3552P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 38)
)
_S3528G_ObjectIdentity = ObjectIdentity
s3528G = _S3528G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 39)
)
_S3528P_ObjectIdentity = ObjectIdentity
s3528P = _S3528P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 40)
)
_S3526c_ObjectIdentity = ObjectIdentity
s3526c = _S3526c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 41)
)
_S3026c_24_12fs_ObjectIdentity = ObjectIdentity
s3026c_24_12fs = _S3026c_24_12fs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 42)
)
_S3026c_24_12fm_ObjectIdentity = ObjectIdentity
s3026c_24_12fm = _S3026c_24_12fm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 43)
)
_S3526c_24_12fs_ObjectIdentity = ObjectIdentity
s3526c_24_12fs = _S3526c_24_12fs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 44)
)
_S3526c_24_12fm_ObjectIdentity = ObjectIdentity
s3526c_24_12fm = _S3526c_24_12fm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 45)
)
_S5012G_ObjectIdentity = ObjectIdentity
s5012G = _S5012G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 46)
)
_S5012G_DC_ObjectIdentity = ObjectIdentity
s5012G_DC = _S5012G_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 47)
)
_S5012T_12_10GBC_ObjectIdentity = ObjectIdentity
s5012T_12_10GBC = _S5012T_12_10GBC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 48)
)
_S5012T_12_10GBC_DC_ObjectIdentity = ObjectIdentity
s5012T_12_10GBC_DC = _S5012T_12_10GBC_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 49)
)
_S5024G_24_20TP_ObjectIdentity = ObjectIdentity
s5024G_24_20TP = _S5024G_24_20TP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 50)
)
_S5024G_24_20TP_DC_ObjectIdentity = ObjectIdentity
s5024G_24_20TP_DC = _S5024G_24_20TP_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 51)
)
_S2026Z_ObjectIdentity = ObjectIdentity
s2026Z = _S2026Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 52)
)
_S2026C_ObjectIdentity = ObjectIdentity
s2026C = _S2026C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 53)
)
_S3026G_SI_ObjectIdentity = ObjectIdentity
s3026G_SI = _S3026G_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 54)
)
_S3026C_SI_ObjectIdentity = ObjectIdentity
s3026C_SI = _S3026C_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 55)
)
_S3026S_SI_ObjectIdentity = ObjectIdentity
s3026S_SI = _S3026S_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 56)
)
_S8505e_ObjectIdentity = ObjectIdentity
s8505e = _S8505e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 57)
)
_S3552F_SI_ObjectIdentity = ObjectIdentity
s3552F_SI = _S3552F_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 67)
)
_S3552F_EI_ObjectIdentity = ObjectIdentity
s3552F_EI = _S3552F_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 68)
)
_E026_ObjectIdentity = ObjectIdentity
e026 = _E026_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 69)
)
_E026_SI_ObjectIdentity = ObjectIdentity
e026_SI = _E026_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 70)
)
_E050_ObjectIdentity = ObjectIdentity
e050 = _E050_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 71)
)
_S2326P_SI_ObjectIdentity = ObjectIdentity
s2326P_SI = _S2326P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 72)
)
_S2326P_EI_ObjectIdentity = ObjectIdentity
s2326P_EI = _S2326P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 73)
)
_S2318P_SI_ObjectIdentity = ObjectIdentity
s2318P_SI = _S2318P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 74)
)
_S2318P_EI_ObjectIdentity = ObjectIdentity
s2318P_EI = _S2318P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 75)
)
_S2309P_SI_ObjectIdentity = ObjectIdentity
s2309P_SI = _S2309P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 76)
)
_S2309P_EI_ObjectIdentity = ObjectIdentity
s2309P_EI = _S2309P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 77)
)
_S3352P_SI_ObjectIdentity = ObjectIdentity
s3352P_SI = _S3352P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 78)
)
_S3352P_EI_ObjectIdentity = ObjectIdentity
s3352P_EI = _S3352P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 79)
)
_S3328TP_SI_ObjectIdentity = ObjectIdentity
s3328TP_SI = _S3328TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 80)
)
_S3328TP_EI_ObjectIdentity = ObjectIdentity
s3328TP_EI = _S3328TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 81)
)
_S3328TP_EI_24S_ObjectIdentity = ObjectIdentity
s3328TP_EI_24S = _S3328TP_EI_24S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 82)
)
_S3328TP_SI_24S_ObjectIdentity = ObjectIdentity
s3328TP_SI_24S = _S3328TP_SI_24S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 83)
)
_S3352P_EI_24S_ObjectIdentity = ObjectIdentity
s3352P_EI_24S = _S3352P_EI_24S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 84)
)
_S3352P_EI_48S_ObjectIdentity = ObjectIdentity
s3352P_EI_48S = _S3352P_EI_48S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 85)
)
_S3352P_SI_48S_ObjectIdentity = ObjectIdentity
s3352P_SI_48S = _S3352P_SI_48S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 86)
)
_S2309TP_SI_ObjectIdentity = ObjectIdentity
s2309TP_SI = _S2309TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 87)
)
_S2309TP_EI_ObjectIdentity = ObjectIdentity
s2309TP_EI = _S2309TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 88)
)
_S2318TP_SI_ObjectIdentity = ObjectIdentity
s2318TP_SI = _S2318TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 89)
)
_S2318TP_EI_ObjectIdentity = ObjectIdentity
s2318TP_EI = _S2318TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 90)
)
_S2326TP_SI_ObjectIdentity = ObjectIdentity
s2326TP_SI = _S2326TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 91)
)
_S2326TP_EI_ObjectIdentity = ObjectIdentity
s2326TP_EI = _S2326TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 92)
)
_S2352P_SI_ObjectIdentity = ObjectIdentity
s2352P_SI = _S2352P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 93)
)
_S2352P_EI_ObjectIdentity = ObjectIdentity
s2352P_EI = _S2352P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 94)
)
_S5328C_EI_ObjectIdentity = ObjectIdentity
s5328C_EI = _S5328C_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 95)
)
_S5328C_EI_24S_ObjectIdentity = ObjectIdentity
s5328C_EI_24S = _S5328C_EI_24S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 96)
)
_S5352C_EI_ObjectIdentity = ObjectIdentity
s5352C_EI = _S5352C_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 97)
)
_S5324TP_SI_ObjectIdentity = ObjectIdentity
s5324TP_SI = _S5324TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 98)
)
_S5348TP_SI_ObjectIdentity = ObjectIdentity
s5348TP_SI = _S5348TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 99)
)
_S5324TP_PWR_SI_ObjectIdentity = ObjectIdentity
s5324TP_PWR_SI = _S5324TP_PWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 100)
)
_S5348TP_PWR_SI_ObjectIdentity = ObjectIdentity
s5348TP_PWR_SI = _S5348TP_PWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 101)
)
_S5328C_SI_ObjectIdentity = ObjectIdentity
s5328C_SI = _S5328C_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 102)
)
_S5352C_SI_ObjectIdentity = ObjectIdentity
s5352C_SI = _S5352C_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 103)
)
_S5328C_PWR_SI_ObjectIdentity = ObjectIdentity
s5328C_PWR_SI = _S5328C_PWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 104)
)
_S5352C_PWR_SI_ObjectIdentity = ObjectIdentity
s5352C_PWR_SI = _S5352C_PWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 105)
)
_S5328C_PWR_EI_ObjectIdentity = ObjectIdentity
s5328C_PWR_EI = _S5328C_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 106)
)
_S5352C_PWR_EI_ObjectIdentity = ObjectIdentity
s5352C_PWR_EI = _S5352C_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 107)
)
_S2309TP_PWR_EI_ObjectIdentity = ObjectIdentity
s2309TP_PWR_EI = _S2309TP_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 108)
)
_S2326TP_PWR_EI_ObjectIdentity = ObjectIdentity
s2326TP_PWR_EI = _S2326TP_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 109)
)
_S3328TP_PWR_EI_ObjectIdentity = ObjectIdentity
s3328TP_PWR_EI = _S3328TP_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 110)
)
_S3352P_PWR_EI_ObjectIdentity = ObjectIdentity
s3352P_PWR_EI = _S3352P_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 111)
)
_S3328TP_EI_MC_ObjectIdentity = ObjectIdentity
s3328TP_EI_MC = _S3328TP_EI_MC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 112)
)
_S3318TP_EI_MC_ObjectIdentity = ObjectIdentity
s3318TP_EI_MC = _S3318TP_EI_MC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 113)
)
_S2700_9TP_EI_AC_ObjectIdentity = ObjectIdentity
s2700_9TP_EI_AC = _S2700_9TP_EI_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 114)
)
_S2700_9TP_EI_DC_ObjectIdentity = ObjectIdentity
s2700_9TP_EI_DC = _S2700_9TP_EI_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 115)
)
_S2700_18TP_EI_AC_ObjectIdentity = ObjectIdentity
s2700_18TP_EI_AC = _S2700_18TP_EI_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 116)
)
_S2700_26TP_EI_AC_ObjectIdentity = ObjectIdentity
s2700_26TP_EI_AC = _S2700_26TP_EI_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 117)
)
_S2700_26TP_EI_DC_ObjectIdentity = ObjectIdentity
s2700_26TP_EI_DC = _S2700_26TP_EI_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 118)
)
_S2700_52TP_EI_AC_ObjectIdentity = ObjectIdentity
s2700_52TP_EI_AC = _S2700_52TP_EI_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 119)
)
_S2700_9TP_SI_AC_ObjectIdentity = ObjectIdentity
s2700_9TP_SI_AC = _S2700_9TP_SI_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 120)
)
_S2700_18TP_SI_AC_ObjectIdentity = ObjectIdentity
s2700_18TP_SI_AC = _S2700_18TP_SI_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 121)
)
_S2700_26TP_SI_AC_ObjectIdentity = ObjectIdentity
s2700_26TP_SI_AC = _S2700_26TP_SI_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 122)
)
_S2700_9TP_PWR_EI_ObjectIdentity = ObjectIdentity
s2700_9TP_PWR_EI = _S2700_9TP_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 123)
)
_S2700_26TP_PWR_EI_ObjectIdentity = ObjectIdentity
s2700_26TP_PWR_EI = _S2700_26TP_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 124)
)
_S3700_28TP_EI_AC_ObjectIdentity = ObjectIdentity
s3700_28TP_EI_AC = _S3700_28TP_EI_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 125)
)
_S3700_28TP_EI_DC_ObjectIdentity = ObjectIdentity
s3700_28TP_EI_DC = _S3700_28TP_EI_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 126)
)
_S3700_28TP_EI_24S_AC_ObjectIdentity = ObjectIdentity
s3700_28TP_EI_24S_AC = _S3700_28TP_EI_24S_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 127)
)
_S3700_52TP_EI_AC_ObjectIdentity = ObjectIdentity
s3700_52TP_EI_AC = _S3700_52TP_EI_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 128)
)
_S3700_52TP_EI_DC_ObjectIdentity = ObjectIdentity
s3700_52TP_EI_DC = _S3700_52TP_EI_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 129)
)
_S3700_52TP_EI_24S_AC_ObjectIdentity = ObjectIdentity
s3700_52TP_EI_24S_AC = _S3700_52TP_EI_24S_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 130)
)
_S3700_52TP_EI_24S_DC_ObjectIdentity = ObjectIdentity
s3700_52TP_EI_24S_DC = _S3700_52TP_EI_24S_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 131)
)
_S3700_52TP_EI_48S_AC_ObjectIdentity = ObjectIdentity
s3700_52TP_EI_48S_AC = _S3700_52TP_EI_48S_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 132)
)
_S3700_52TP_EI_48S_DC_ObjectIdentity = ObjectIdentity
s3700_52TP_EI_48S_DC = _S3700_52TP_EI_48S_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 133)
)
_S3700_28TP_SI_AC_ObjectIdentity = ObjectIdentity
s3700_28TP_SI_AC = _S3700_28TP_SI_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 134)
)
_S3700_28TP_SI_DC_ObjectIdentity = ObjectIdentity
s3700_28TP_SI_DC = _S3700_28TP_SI_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 135)
)
_S3700_52TP_SI_AC_ObjectIdentity = ObjectIdentity
s3700_52TP_SI_AC = _S3700_52TP_SI_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 136)
)
_S3700_28TP_PWR_EI_ObjectIdentity = ObjectIdentity
s3700_28TP_PWR_EI = _S3700_28TP_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 137)
)
_S3700_52TP_PWR_EI_ObjectIdentity = ObjectIdentity
s3700_52TP_PWR_EI = _S3700_52TP_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 138)
)
_S3700_28TP_EI_MC_AC_ObjectIdentity = ObjectIdentity
s3700_28TP_EI_MC_AC = _S3700_28TP_EI_MC_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 139)
)
_S5700_28C_EI_ObjectIdentity = ObjectIdentity
s5700_28C_EI = _S5700_28C_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 140)
)
_S5700_28C_SI_ObjectIdentity = ObjectIdentity
s5700_28C_SI = _S5700_28C_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 141)
)
_S5700_28C_EI_24S_ObjectIdentity = ObjectIdentity
s5700_28C_EI_24S = _S5700_28C_EI_24S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 142)
)
_S5700_52C_EI_ObjectIdentity = ObjectIdentity
s5700_52C_EI = _S5700_52C_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 143)
)
_S5700_52C_SI_ObjectIdentity = ObjectIdentity
s5700_52C_SI = _S5700_52C_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 144)
)
_S5700_24TP_SI_AC_ObjectIdentity = ObjectIdentity
s5700_24TP_SI_AC = _S5700_24TP_SI_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 145)
)
_S5700_24TP_SI_DC_ObjectIdentity = ObjectIdentity
s5700_24TP_SI_DC = _S5700_24TP_SI_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 146)
)
_S5700_48TP_SI_AC_ObjectIdentity = ObjectIdentity
s5700_48TP_SI_AC = _S5700_48TP_SI_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 147)
)
_S5700_48TP_SI_DC_ObjectIdentity = ObjectIdentity
s5700_48TP_SI_DC = _S5700_48TP_SI_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 148)
)
_S5700_28C_PWR_EI_ObjectIdentity = ObjectIdentity
s5700_28C_PWR_EI = _S5700_28C_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 149)
)
_S5700_52C_PWR_EI_ObjectIdentity = ObjectIdentity
s5700_52C_PWR_EI = _S5700_52C_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 150)
)
_S5700_24TP_PWR_SI_ObjectIdentity = ObjectIdentity
s5700_24TP_PWR_SI = _S5700_24TP_PWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 151)
)
_S5700_48TP_PWR_SI_ObjectIdentity = ObjectIdentity
s5700_48TP_PWR_SI = _S5700_48TP_PWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 152)
)
_S6324C_ObjectIdentity = ObjectIdentity
s6324C = _S6324C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 153)
)
_S6348C_ObjectIdentity = ObjectIdentity
s6348C = _S6348C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 154)
)
_S5328C_HI_ObjectIdentity = ObjectIdentity
s5328C_HI = _S5328C_HI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 155)
)
_S5328C_HI_24S_ObjectIdentity = ObjectIdentity
s5328C_HI_24S = _S5328C_HI_24S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 156)
)
_S5306TP_SI_ObjectIdentity = ObjectIdentity
s5306TP_SI = _S5306TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 157)
)
_S3326C_HI_ObjectIdentity = ObjectIdentity
s3326C_HI = _S3326C_HI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 158)
)
_S5328C_HI_24SA_ObjectIdentity = ObjectIdentity
s5328C_HI_24SA = _S5328C_HI_24SA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 159)
)
_S6700_24_EI_ObjectIdentity = ObjectIdentity
s6700_24_EI = _S6700_24_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 160)
)
_S6700_48_EI_ObjectIdentity = ObjectIdentity
s6700_48_EI = _S6700_48_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 161)
)
_S1728_GWR_4P_ObjectIdentity = ObjectIdentity
s1728_GWR_4P = _S1728_GWR_4P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 162)
)
_S5700_28P_LI_ObjectIdentity = ObjectIdentity
s5700_28P_LI = _S5700_28P_LI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 163)
)
_S5700_28P_PWR_LI_AC_ObjectIdentity = ObjectIdentity
s5700_28P_PWR_LI_AC = _S5700_28P_PWR_LI_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 164)
)
_S5700_52P_LI_ObjectIdentity = ObjectIdentity
s5700_52P_LI = _S5700_52P_LI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 165)
)
_S5700_52P_PWR_LI_AC_ObjectIdentity = ObjectIdentity
s5700_52P_PWR_LI_AC = _S5700_52P_PWR_LI_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 166)
)
_S5700_28X_EI_ObjectIdentity = ObjectIdentity
s5700_28X_EI = _S5700_28X_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 167)
)
_S5700_52X_EI_ObjectIdentity = ObjectIdentity
s5700_52X_EI = _S5700_52X_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 168)
)
_S5700_28C_HI_ObjectIdentity = ObjectIdentity
s5700_28C_HI = _S5700_28C_HI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 169)
)
_S5700_28C_HI_24S_ObjectIdentity = ObjectIdentity
s5700_28C_HI_24S = _S5700_28C_HI_24S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 170)
)
_S5700_6TP_LI_AC_ObjectIdentity = ObjectIdentity
s5700_6TP_LI_AC = _S5700_6TP_LI_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 171)
)
_S3700_26C_HI_ObjectIdentity = ObjectIdentity
s3700_26C_HI = _S3700_26C_HI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 172)
)
_S5300_28C_PWR_EI_ObjectIdentity = ObjectIdentity
s5300_28C_PWR_EI = _S5300_28C_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 173)
)
_S5300_52C_PWR_EI_ObjectIdentity = ObjectIdentity
s5300_52C_PWR_EI = _S5300_52C_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 174)
)
_S5310_28P_LI_ObjectIdentity = ObjectIdentity
s5310_28P_LI = _S5310_28P_LI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 175)
)
_S5310_52P_LI_ObjectIdentity = ObjectIdentity
s5310_52P_LI = _S5310_52P_LI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 176)
)
_S5700_28P_LI_DC_ObjectIdentity = ObjectIdentity
s5700_28P_LI_DC = _S5700_28P_LI_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 177)
)
_S5700_52P_LI_DC_ObjectIdentity = ObjectIdentity
s5700_52P_LI_DC = _S5700_52P_LI_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 178)
)
_S5310_28P_LI_DC_ObjectIdentity = ObjectIdentity
s5310_28P_LI_DC = _S5310_28P_LI_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 179)
)
_S5310_52P_LI_DC_ObjectIdentity = ObjectIdentity
s5310_52P_LI_DC = _S5310_52P_LI_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 180)
)
_S5700S_28P_LI_AC_ObjectIdentity = ObjectIdentity
s5700S_28P_LI_AC = _S5700S_28P_LI_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 181)
)
_S5700S_52P_LI_AC_ObjectIdentity = ObjectIdentity
s5700S_52P_LI_AC = _S5700S_52P_LI_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 182)
)
_S1700_28GFR_4P_AC_ObjectIdentity = ObjectIdentity
s1700_28GFR_4P_AC = _S1700_28GFR_4P_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 183)
)
_S1700_52GFR_4P_AC_ObjectIdentity = ObjectIdentity
s1700_52GFR_4P_AC = _S1700_52GFR_4P_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 184)
)
_S1700_28FR_2T2P_AC_ObjectIdentity = ObjectIdentity
s1700_28FR_2T2P_AC = _S1700_28FR_2T2P_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 185)
)
_S1700_52FR_2T2P_AC_ObjectIdentity = ObjectIdentity
s1700_52FR_2T2P_AC = _S1700_52FR_2T2P_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 186)
)
_S5700_28C_PWR_SI_ObjectIdentity = ObjectIdentity
s5700_28C_PWR_SI = _S5700_28C_PWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 187)
)
_S5700_52C_PWR_SI_ObjectIdentity = ObjectIdentity
s5700_52C_PWR_SI = _S5700_52C_PWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 188)
)
_S5710_28C_PWR_LI_ObjectIdentity = ObjectIdentity
s5710_28C_PWR_LI = _S5710_28C_PWR_LI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 189)
)
_S5710_52C_PWR_LI_ObjectIdentity = ObjectIdentity
s5710_52C_PWR_LI = _S5710_52C_PWR_LI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 190)
)
_S5710_28C_LI_ObjectIdentity = ObjectIdentity
s5710_28C_LI = _S5710_28C_LI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 191)
)
_S5710_52C_LI_ObjectIdentity = ObjectIdentity
s5710_52C_LI = _S5710_52C_LI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 192)
)
_E6000_ObjectIdentity = ObjectIdentity
e6000 = _E6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 193)
)
_S5710_28C_PWR_EI_ObjectIdentity = ObjectIdentity
s5710_28C_PWR_EI = _S5710_28C_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 194)
)
_S5710_52C_PWR_EI_ObjectIdentity = ObjectIdentity
s5710_52C_PWR_EI = _S5710_52C_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 195)
)
_S2710_26TP_PWR_SI_ObjectIdentity = ObjectIdentity
s2710_26TP_PWR_SI = _S2710_26TP_PWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 196)
)
_S2710_52P_SI_AC_ObjectIdentity = ObjectIdentity
s2710_52P_SI_AC = _S2710_52P_SI_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 197)
)
_S2710_52P_PWR_SI_ObjectIdentity = ObjectIdentity
s2710_52P_PWR_SI = _S2710_52P_PWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 198)
)
_S2700_52P_PWR_EI_ObjectIdentity = ObjectIdentity
s2700_52P_PWR_EI = _S2700_52P_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 199)
)
_S3700_52P_PWR_SI_ObjectIdentity = ObjectIdentity
s3700_52P_PWR_SI = _S3700_52P_PWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 200)
)
_S3700_28TP_PWR_SI_ObjectIdentity = ObjectIdentity
s3700_28TP_PWR_SI = _S3700_28TP_PWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 201)
)
_S5710_108C_PWR_HI_ObjectIdentity = ObjectIdentity
s5710_108C_PWR_HI = _S5710_108C_PWR_HI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 202)
)
_S5700_10P_LI_AC_ObjectIdentity = ObjectIdentity
s5700_10P_LI_AC = _S5700_10P_LI_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 203)
)
_S5700_10P_PWR_LI_AC_ObjectIdentity = ObjectIdentity
s5700_10P_PWR_LI_AC = _S5700_10P_PWR_LI_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 204)
)
_S5700_26X_SI_12S_AC_ObjectIdentity = ObjectIdentity
s5700_26X_SI_12S_AC = _S5700_26X_SI_12S_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 205)
)
_S5700_28X_LI_AC_ObjectIdentity = ObjectIdentity
s5700_28X_LI_AC = _S5700_28X_LI_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 206)
)
_S5700_28X_LI_DC_ObjectIdentity = ObjectIdentity
s5700_28X_LI_DC = _S5700_28X_LI_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 207)
)
_S5700_52X_LI_AC_ObjectIdentity = ObjectIdentity
s5700_52X_LI_AC = _S5700_52X_LI_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 208)
)
_S5700_52X_LI_DC_ObjectIdentity = ObjectIdentity
s5700_52X_LI_DC = _S5700_52X_LI_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 209)
)
_S5700_28X_PWR_LI_AC_ObjectIdentity = ObjectIdentity
s5700_28X_PWR_LI_AC = _S5700_28X_PWR_LI_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 210)
)
_S5700_52X_PWR_LI_AC_ObjectIdentity = ObjectIdentity
s5700_52X_PWR_LI_AC = _S5700_52X_PWR_LI_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 211)
)
_Apon_ObjectIdentity = ObjectIdentity
apon = _Apon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 24)
)
_Ma5101_ObjectIdentity = ObjectIdentity
ma5101 = _Ma5101_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 24, 1)
)
_Ma5102_ObjectIdentity = ObjectIdentity
ma5102 = _Ma5102_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 24, 2)
)
_Transmission_ObjectIdentity = ObjectIdentity
transmission = _Transmission_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25)
)
_Optix155622H_ObjectIdentity = ObjectIdentity
optix155622H = _Optix155622H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 1)
)
_Optix10Gv2_ObjectIdentity = ObjectIdentity
optix10Gv2 = _Optix10Gv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 2)
)
_Hsr_ObjectIdentity = ObjectIdentity
hsr = _Hsr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 26)
)
_Ne16E_ObjectIdentity = ObjectIdentity
ne16E = _Ne16E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 26, 1)
)
_Ne08E_ObjectIdentity = ObjectIdentity
ne08E = _Ne08E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 26, 2)
)
_Ne05_ObjectIdentity = ObjectIdentity
ne05 = _Ne05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 26, 3)
)
_Amg5000_ObjectIdentity = ObjectIdentity
amg5000 = _Amg5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 27)
)
_Umg8900_ObjectIdentity = ObjectIdentity
umg8900 = _Umg8900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 28)
)
_Ne20_ObjectIdentity = ObjectIdentity
ne20 = _Ne20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 29)
)
_Ne20s_ObjectIdentity = ObjectIdentity
ne20s = _Ne20s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 30)
)
_Ne40_ObjectIdentity = ObjectIdentity
ne40 = _Ne40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 31)
)
_Wcdma_ObjectIdentity = ObjectIdentity
wcdma = _Wcdma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 32)
)
_Sgsn_ObjectIdentity = ObjectIdentity
sgsn = _Sgsn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 32, 1)
)
_Mlsr_ObjectIdentity = ObjectIdentity
mlsr = _Mlsr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33)
)
_Dslw_ObjectIdentity = ObjectIdentity
dslw = _Dslw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 34)
)
_DlswNode_ObjectIdentity = ObjectIdentity
dlswNode = _DlswNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 34, 1)
)
_DlswTConn_ObjectIdentity = ObjectIdentity
dlswTConn = _DlswTConn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 34, 2)
)
_DlswInterface_ObjectIdentity = ObjectIdentity
dlswInterface = _DlswInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 34, 3)
)
_DlswDirectory_ObjectIdentity = ObjectIdentity
dlswDirectory = _DlswDirectory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 34, 4)
)
_DlswCircuit_ObjectIdentity = ObjectIdentity
dlswCircuit = _DlswCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 34, 5)
)
_DlswSdlc_ObjectIdentity = ObjectIdentity
dlswSdlc = _DlswSdlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 34, 6)
)
_DlswLlc2_ObjectIdentity = ObjectIdentity
dlswLlc2 = _DlswLlc2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 34, 7)
)
_Sm_ObjectIdentity = ObjectIdentity
sm = _Sm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 35)
)
_Mmsc_ObjectIdentity = ObjectIdentity
mmsc = _Mmsc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 35, 1)
)
__pysmi_as_ObjectIdentity = ObjectIdentity
_pysmi_as = __pysmi_as_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 36)
)
_P3_ObjectIdentity = ObjectIdentity
p3 = _P3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 37)
)
_Iad_ObjectIdentity = ObjectIdentity
iad = _Iad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 38)
)
_Iad132_ObjectIdentity = ObjectIdentity
iad132 = _Iad132_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 38, 1)
)
_WlanAp_ObjectIdentity = ObjectIdentity
wlanAp = _WlanAp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 39)
)
_WlanApCommon_ObjectIdentity = ObjectIdentity
wlanApCommon = _WlanApCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 39, 1)
)
_WlanApWA1003_ObjectIdentity = ObjectIdentity
wlanApWA1003 = _WlanApWA1003_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 39, 2)
)
_WlanApWA1003A_ObjectIdentity = ObjectIdentity
wlanApWA1003A = _WlanApWA1003A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 39, 3)
)
_WlanApWA1005_ObjectIdentity = ObjectIdentity
wlanApWA1005 = _WlanApWA1005_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 39, 4)
)
_WlanApWA1008_ObjectIdentity = ObjectIdentity
wlanApWA1008 = _WlanApWA1008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 39, 5)
)
_WlanApWA1208_ObjectIdentity = ObjectIdentity
wlanApWA1208 = _WlanApWA1208_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 39, 6)
)
_WlanApWA1208H_ObjectIdentity = ObjectIdentity
wlanApWA1208H = _WlanApWA1208H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 39, 7)
)
_WlanApWA1006E_ObjectIdentity = ObjectIdentity
wlanApWA1006E = _WlanApWA1006E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 39, 8)
)
_WlanBridgeWB2010_ObjectIdentity = ObjectIdentity
wlanBridgeWB2010 = _WlanBridgeWB2010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 39, 9)
)
_WlanBridgeWB2011_ObjectIdentity = ObjectIdentity
wlanBridgeWB2011 = _WlanBridgeWB2011_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 39, 10)
)
_Wa1208E_ObjectIdentity = ObjectIdentity
wa1208E = _Wa1208E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 39, 11)
)
_HwinfoX_ObjectIdentity = ObjectIdentity
hwinfoX = _HwinfoX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 40)
)
_WlanApWA1006_ObjectIdentity = ObjectIdentity
wlanApWA1006 = _WlanApWA1006_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 43)
)
_Ar46_20_ObjectIdentity = ObjectIdentity
ar46_20 = _Ar46_20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 44)
)
_Ar46_40_ObjectIdentity = ObjectIdentity
ar46_40 = _Ar46_40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 45)
)
_Ar46_80_ObjectIdentity = ObjectIdentity
ar46_80 = _Ar46_80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 46)
)
_Ne20_2_ObjectIdentity = ObjectIdentity
ne20_2 = _Ne20_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 47)
)
_Ne20_4_ObjectIdentity = ObjectIdentity
ne20_4 = _Ne20_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 48)
)
_Ne20_8_ObjectIdentity = ObjectIdentity
ne20_8 = _Ne20_8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 49)
)
_Eudemon200_ObjectIdentity = ObjectIdentity
eudemon200 = _Eudemon200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 50)
)
_Eudemon1000_ObjectIdentity = ObjectIdentity
eudemon1000 = _Eudemon1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 51)
)
_Vdg10_40_ObjectIdentity = ObjectIdentity
vdg10_40 = _Vdg10_40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 52)
)
_Vdg10_41_ObjectIdentity = ObjectIdentity
vdg10_41 = _Vdg10_41_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 53)
)
_HwSps_ObjectIdentity = ObjectIdentity
hwSps = _HwSps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 54)
)
_Ar18_18_ObjectIdentity = ObjectIdentity
ar18_18 = _Ar18_18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 55)
)
_Ar18_20_ObjectIdentity = ObjectIdentity
ar18_20 = _Ar18_20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 56)
)
_Ar18_30_ObjectIdentity = ObjectIdentity
ar18_30 = _Ar18_30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 57)
)
_Ar18_31_ObjectIdentity = ObjectIdentity
ar18_31 = _Ar18_31_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 58)
)
_Ar18_32_ObjectIdentity = ObjectIdentity
ar18_32 = _Ar18_32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 59)
)
_Ar18_33_ObjectIdentity = ObjectIdentity
ar18_33 = _Ar18_33_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 60)
)
_Ar18_34_ObjectIdentity = ObjectIdentity
ar18_34 = _Ar18_34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 61)
)
_Ne5000_ObjectIdentity = ObjectIdentity
ne5000 = _Ne5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 62)
)
_Ne5000SysOid_ObjectIdentity = ObjectIdentity
ne5000SysOid = _Ne5000SysOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 62, 2)
)
_Ne5000oem_ObjectIdentity = ObjectIdentity
ne5000oem = _Ne5000oem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 1)
)
_Ne80E_ObjectIdentity = ObjectIdentity
ne80E = _Ne80E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 2)
)
_Ne5000E_ObjectIdentity = ObjectIdentity
ne5000E = _Ne5000E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 3)
)
_Ne5000EMulti_ObjectIdentity = ObjectIdentity
ne5000EMulti = _Ne5000EMulti_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 4)
)
_Ne40E_ObjectIdentity = ObjectIdentity
ne40E = _Ne40E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 5)
)
_Ne5000E_BTB_ObjectIdentity = ObjectIdentity
ne5000E_BTB = _Ne5000E_BTB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 6)
)
_Ne40E_4_ObjectIdentity = ObjectIdentity
ne40E_4 = _Ne40E_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 7)
)
_Ne40E_X3_ObjectIdentity = ObjectIdentity
ne40E_X3 = _Ne40E_X3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 8)
)
_Ne40E_X8_ObjectIdentity = ObjectIdentity
ne40E_X8 = _Ne40E_X8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 9)
)
_Ne40E_X16_ObjectIdentity = ObjectIdentity
ne40E_X16 = _Ne40E_X16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 10)
)
_Ne5000E_X16_ObjectIdentity = ObjectIdentity
ne5000E_X16 = _Ne5000E_X16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 11)
)
_Ne40E_X1_ObjectIdentity = ObjectIdentity
ne40E_X1 = _Ne40E_X1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 12)
)
_Ne40E_X2_ObjectIdentity = ObjectIdentity
ne40E_X2 = _Ne40E_X2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 13)
)
_Ne40E_X1_M4_ObjectIdentity = ObjectIdentity
ne40E_X1_M4 = _Ne40E_X1_M4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 14)
)
_Ne40E_X2_M8_ObjectIdentity = ObjectIdentity
ne40E_X2_M8 = _Ne40E_X2_M8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 15)
)
_Ne40E_X2_M16_ObjectIdentity = ObjectIdentity
ne40E_X2_M16 = _Ne40E_X2_M16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 16)
)
_Ggsn9811_ObjectIdentity = ObjectIdentity
ggsn9811 = _Ggsn9811_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 63)
)
_Pdsn9660_ObjectIdentity = ObjectIdentity
pdsn9660 = _Pdsn9660_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 64)
)
_Eudemon2100_ObjectIdentity = ObjectIdentity
eudemon2100 = _Eudemon2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 65)
)
_Eudemon2200_ObjectIdentity = ObjectIdentity
eudemon2200 = _Eudemon2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 66)
)
_Ua5000ipm_ObjectIdentity = ObjectIdentity
ua5000ipm = _Ua5000ipm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 72)
)
_Rm9000_ObjectIdentity = ObjectIdentity
rm9000 = _Rm9000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 73)
)
_HwIMAPNorthbound_ObjectIdentity = ObjectIdentity
hwIMAPNorthbound = _HwIMAPNorthbound_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 74)
)
_HwBITS_ObjectIdentity = ObjectIdentity
hwBITS = _HwBITS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 75)
)
_HwPv8_ObjectIdentity = ObjectIdentity
hwPv8 = _HwPv8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 76)
)
_Eudemon500_ObjectIdentity = ObjectIdentity
eudemon500 = _Eudemon500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 77)
)
_Ua5000IpmB_ObjectIdentity = ObjectIdentity
ua5000IpmB = _Ua5000IpmB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 78)
)
_Ua5000ApmB_ObjectIdentity = ObjectIdentity
ua5000ApmB = _Ua5000ApmB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 79)
)
_Ma5600_ObjectIdentity = ObjectIdentity
ma5600 = _Ma5600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 80)
)
_Softx3000UC_ObjectIdentity = ObjectIdentity
softx3000UC = _Softx3000UC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 81)
)
_HwOSTA_ObjectIdentity = ObjectIdentity
hwOSTA = _HwOSTA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 82)
)
_Secpath1800F_ObjectIdentity = ObjectIdentity
secpath1800F = _Secpath1800F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 83)
)
_Eudemon2300_ObjectIdentity = ObjectIdentity
eudemon2300 = _Eudemon2300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 84)
)
_Ma5100V600_ObjectIdentity = ObjectIdentity
ma5100V600 = _Ma5100V600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 85)
)
_Ma5605_ObjectIdentity = ObjectIdentity
ma5605 = _Ma5605_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 86)
)
_Msp_ObjectIdentity = ObjectIdentity
msp = _Msp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 87)
)
_CX200A_ObjectIdentity = ObjectIdentity
cX200A = _CX200A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 87, 1)
)
_CX200B_ObjectIdentity = ObjectIdentity
cX200B = _CX200B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 87, 2)
)
_CX300A_ObjectIdentity = ObjectIdentity
cX300A = _CX300A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 87, 3)
)
_CX300B_ObjectIdentity = ObjectIdentity
cX300B = _CX300B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 87, 4)
)
_CX500A_ObjectIdentity = ObjectIdentity
cX500A = _CX500A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 87, 5)
)
_CX380_ObjectIdentity = ObjectIdentity
cX380 = _CX380_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 87, 6)
)
_CX600_8_ObjectIdentity = ObjectIdentity
cX600_8 = _CX600_8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 87, 7)
)
_CX600_16_ObjectIdentity = ObjectIdentity
cX600_16 = _CX600_16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 87, 8)
)
_CX200C_ObjectIdentity = ObjectIdentity
cX200C = _CX200C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 87, 9)
)
_CX200D_ObjectIdentity = ObjectIdentity
cX200D = _CX200D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 87, 10)
)
_CX200D_EA_ObjectIdentity = ObjectIdentity
cX200D_EA = _CX200D_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 87, 11)
)
_CX200D_MC_ObjectIdentity = ObjectIdentity
cX200D_MC = _CX200D_MC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 87, 12)
)
_CX600_4_ObjectIdentity = ObjectIdentity
cX600_4 = _CX600_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 87, 13)
)
_CX380_PBT_ObjectIdentity = ObjectIdentity
cX380_PBT = _CX380_PBT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 87, 14)
)
_CX380_ME_ObjectIdentity = ObjectIdentity
cX380_ME = _CX380_ME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 87, 15)
)
_CX200D_EA_MC_ObjectIdentity = ObjectIdentity
cX200D_EA_MC = _CX200D_EA_MC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 87, 16)
)
_CX600_X3_ObjectIdentity = ObjectIdentity
cX600_X3 = _CX600_X3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 87, 17)
)
_CX600_X8_ObjectIdentity = ObjectIdentity
cX600_X8 = _CX600_X8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 87, 18)
)
_CX600_X16_ObjectIdentity = ObjectIdentity
cX600_X16 = _CX600_X16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 87, 19)
)
_CX600_X1_ObjectIdentity = ObjectIdentity
cX600_X1 = _CX600_X1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 87, 20)
)
_CX600_X2_ObjectIdentity = ObjectIdentity
cX600_X2 = _CX600_X2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 87, 21)
)
_CX600_X1DO_ObjectIdentity = ObjectIdentity
cX600_X1DO = _CX600_X1DO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 87, 22)
)
_CX600_X2DO_ObjectIdentity = ObjectIdentity
cX600_X2DO = _CX600_X2DO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 87, 23)
)
_CX600_X3DO_ObjectIdentity = ObjectIdentity
cX600_X3DO = _CX600_X3DO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 87, 24)
)
_CX600_X8DO_ObjectIdentity = ObjectIdentity
cX600_X8DO = _CX600_X8DO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 87, 25)
)
_CX600_X16DO_ObjectIdentity = ObjectIdentity
cX600_X16DO = _CX600_X16DO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 87, 26)
)
_CX600_X1_M4_ObjectIdentity = ObjectIdentity
cX600_X1_M4 = _CX600_X1_M4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 87, 27)
)
_CX600_X2_M8_ObjectIdentity = ObjectIdentity
cX600_X2_M8 = _CX600_X2_M8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 87, 28)
)
_CX600_X2_M16_ObjectIdentity = ObjectIdentity
cX600_X2_M16 = _CX600_X2_M16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 87, 29)
)
_Ne20E_ObjectIdentity = ObjectIdentity
ne20E = _Ne20E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 88)
)
_Ne20E_4_ObjectIdentity = ObjectIdentity
ne20E_4 = _Ne20E_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 88, 1)
)
_Ne20E_8_ObjectIdentity = ObjectIdentity
ne20E_8 = _Ne20E_8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 88, 2)
)
_Ne20E_X6_ObjectIdentity = ObjectIdentity
ne20E_X6 = _Ne20E_X6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 88, 3)
)
_Me60_ObjectIdentity = ObjectIdentity
me60 = _Me60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 89)
)
_Me60_16_ObjectIdentity = ObjectIdentity
me60_16 = _Me60_16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 89, 1)
)
_Me60_8_ObjectIdentity = ObjectIdentity
me60_8 = _Me60_8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 89, 2)
)
_Me60_4_ObjectIdentity = ObjectIdentity
me60_4 = _Me60_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 89, 3)
)
_Me60_X3_ObjectIdentity = ObjectIdentity
me60_X3 = _Me60_X3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 89, 4)
)
_Me60_X8_ObjectIdentity = ObjectIdentity
me60_X8 = _Me60_X8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 89, 5)
)
_Me60_X16_ObjectIdentity = ObjectIdentity
me60_X16 = _Me60_X16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 89, 6)
)
_Eudemon300_ObjectIdentity = ObjectIdentity
eudemon300 = _Eudemon300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 113)
)
_EudemonVPN3900_ObjectIdentity = ObjectIdentity
eudemonVPN3900 = _EudemonVPN3900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 114)
)
_EudemonEVPN5900_ObjectIdentity = ObjectIdentity
eudemonEVPN5900 = _EudemonEVPN5900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 115)
)
_Eudemon100E_ObjectIdentity = ObjectIdentity
eudemon100E = _Eudemon100E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 116)
)
_Eudemon200E_ObjectIdentity = ObjectIdentity
eudemon200E = _Eudemon200E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 117)
)
_Eudemon200S_ObjectIdentity = ObjectIdentity
eudemon200S = _Eudemon200S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 118)
)
_Svn3000_ObjectIdentity = ObjectIdentity
svn3000 = _Svn3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 124)
)
_Usg5000_ObjectIdentity = ObjectIdentity
usg5000 = _Usg5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 125)
)
_Usg9000_ObjectIdentity = ObjectIdentity
usg9000 = _Usg9000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 126)
)
_Eudemon200s_ObjectIdentity = ObjectIdentity
eudemon200s = _Eudemon200s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 127)
)
_Sig1000_ObjectIdentity = ObjectIdentity
sig1000 = _Sig1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 129)
)
_Sig9280_ObjectIdentity = ObjectIdentity
sig9280 = _Sig9280_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 130)
)
_Sig2000_ObjectIdentity = ObjectIdentity
sig2000 = _Sig2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 131)
)
_S9300_ObjectIdentity = ObjectIdentity
s9300 = _S9300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 170)
)
_S9303_ObjectIdentity = ObjectIdentity
s9303 = _S9303_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 170, 1)
)
_S9306_ObjectIdentity = ObjectIdentity
s9306 = _S9306_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 170, 2)
)
_S9312_ObjectIdentity = ObjectIdentity
s9312 = _S9312_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 170, 3)
)
_Vasp_ObjectIdentity = ObjectIdentity
vasp = _Vasp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 170, 4)
)
_S9303E_ObjectIdentity = ObjectIdentity
s9303E = _S9303E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 170, 5)
)
_S9306E_ObjectIdentity = ObjectIdentity
s9306E = _S9306E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 170, 6)
)
_S9312E_ObjectIdentity = ObjectIdentity
s9312E = _S9312E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 170, 7)
)
_Ptn_ObjectIdentity = ObjectIdentity
ptn = _Ptn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 182)
)
_Ptn2900_ObjectIdentity = ObjectIdentity
ptn2900 = _Ptn2900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 182, 1)
)
_Ptn6900_ObjectIdentity = ObjectIdentity
ptn6900 = _Ptn6900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 182, 2)
)
_Ptn6900_16_ObjectIdentity = ObjectIdentity
ptn6900_16 = _Ptn6900_16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 182, 5)
)
_Ptn6900_8_ObjectIdentity = ObjectIdentity
ptn6900_8 = _Ptn6900_8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 182, 6)
)
_Ptn6900_3_ObjectIdentity = ObjectIdentity
ptn6900_3 = _Ptn6900_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 182, 7)
)
_Ptn6900_2_ObjectIdentity = ObjectIdentity
ptn6900_2 = _Ptn6900_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 182, 8)
)
_Ptn6900_1_ObjectIdentity = ObjectIdentity
ptn6900_1 = _Ptn6900_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 182, 9)
)
_Nse_ObjectIdentity = ObjectIdentity
nse = _Nse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 187)
)
_Ssp1000_ObjectIdentity = ObjectIdentity
ssp1000 = _Ssp1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 187, 1)
)
_Ssp2000_ObjectIdentity = ObjectIdentity
ssp2000 = _Ssp2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 187, 2)
)
_Ssp3000_ObjectIdentity = ObjectIdentity
ssp3000 = _Ssp3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 187, 3)
)
_Ssp1000_4_ObjectIdentity = ObjectIdentity
ssp1000_4 = _Ssp1000_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 187, 4)
)
_Nse1000_4_ObjectIdentity = ObjectIdentity
nse1000_4 = _Nse1000_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 187, 5)
)
_Nse1000_8_ObjectIdentity = ObjectIdentity
nse1000_8 = _Nse1000_8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 187, 6)
)
_Nse1000_X3_ObjectIdentity = ObjectIdentity
nse1000_X3 = _Nse1000_X3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 187, 7)
)
_Ssp5000_X3_ObjectIdentity = ObjectIdentity
ssp5000_X3 = _Ssp5000_X3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 187, 8)
)
_Ssp5000_X8_ObjectIdentity = ObjectIdentity
ssp5000_X8 = _Ssp5000_X8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 187, 9)
)
_Ssp5000_X16_ObjectIdentity = ObjectIdentity
ssp5000_X16 = _Ssp5000_X16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 187, 10)
)
_Atn_ObjectIdentity = ObjectIdentity
atn = _Atn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 220)
)
_Atn980_ObjectIdentity = ObjectIdentity
atn980 = _Atn980_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 220, 1)
)
_Atn990_ObjectIdentity = ObjectIdentity
atn990 = _Atn990_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 220, 2)
)
_Atn910_ObjectIdentity = ObjectIdentity
atn910 = _Atn910_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 220, 3)
)
_Atn950_ObjectIdentity = ObjectIdentity
atn950 = _Atn950_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 220, 4)
)
_Atn950B_ObjectIdentity = ObjectIdentity
atn950B = _Atn950B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 220, 5)
)
_S7700_ObjectIdentity = ObjectIdentity
s7700 = _S7700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 223)
)
_S7703_ObjectIdentity = ObjectIdentity
s7703 = _S7703_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 223, 1)
)
_S7706_ObjectIdentity = ObjectIdentity
s7706 = _S7706_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 223, 2)
)
_S7712_ObjectIdentity = ObjectIdentity
s7712 = _S7712_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 223, 3)
)
_Ar_ObjectIdentity = ObjectIdentity
ar = _Ar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 224)
)
_Ar1220_ObjectIdentity = ObjectIdentity
ar1220 = _Ar1220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 224, 1)
)
_Ar1220w_ObjectIdentity = ObjectIdentity
ar1220w = _Ar1220w_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 224, 2)
)
_Ar1240_ObjectIdentity = ObjectIdentity
ar1240 = _Ar1240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 224, 3)
)
_Ar1240w_ObjectIdentity = ObjectIdentity
ar1240w = _Ar1240w_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 224, 4)
)
_Ar2220_ObjectIdentity = ObjectIdentity
ar2220 = _Ar2220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 224, 5)
)
_Ar2240_ObjectIdentity = ObjectIdentity
ar2240 = _Ar2240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 224, 6)
)
_Ar3260_ObjectIdentity = ObjectIdentity
ar3260 = _Ar3260_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 224, 7)
)
_Ar1220v_ObjectIdentity = ObjectIdentity
ar1220v = _Ar1220v_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 224, 8)
)
_Ar201_ObjectIdentity = ObjectIdentity
ar201 = _Ar201_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 224, 9)
)
_Ar206_ObjectIdentity = ObjectIdentity
ar206 = _Ar206_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 224, 10)
)
_Ar207_ObjectIdentity = ObjectIdentity
ar207 = _Ar207_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 224, 11)
)
_Ar207v_ObjectIdentity = ObjectIdentity
ar207v = _Ar207v_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 224, 12)
)
_Ar208_ObjectIdentity = ObjectIdentity
ar208 = _Ar208_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 224, 13)
)
_Ar1220vw_ObjectIdentity = ObjectIdentity
ar1220vw = _Ar1220vw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 224, 14)
)
_Ar1220s_ObjectIdentity = ObjectIdentity
ar1220s = _Ar1220s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 224, 15)
)
_Ar1220ws_ObjectIdentity = ObjectIdentity
ar1220ws = _Ar1220ws_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 224, 16)
)
_S12700_ObjectIdentity = ObjectIdentity
s12700 = _S12700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 225)
)
_S12708_ObjectIdentity = ObjectIdentity
s12708 = _S12708_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 225, 1)
)
_S12716_ObjectIdentity = ObjectIdentity
s12716 = _S12716_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 225, 2)
)
_VRGW_ObjectIdentity = ObjectIdentity
vRGW = _VRGW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 227)
)
_S9700_ObjectIdentity = ObjectIdentity
s9700 = _S9700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 236)
)
_S9703_ObjectIdentity = ObjectIdentity
s9703 = _S9703_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 236, 1)
)
_S9706_ObjectIdentity = ObjectIdentity
s9706 = _S9706_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 236, 2)
)
_S9712_ObjectIdentity = ObjectIdentity
s9712 = _S9712_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 236, 3)
)
_Dcswitch_ObjectIdentity = ObjectIdentity
dcswitch = _Dcswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 239)
)
_Ce12804_ObjectIdentity = ObjectIdentity
ce12804 = _Ce12804_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 239, 1)
)
_Ce12808_ObjectIdentity = ObjectIdentity
ce12808 = _Ce12808_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 239, 2)
)
_Ce12812_ObjectIdentity = ObjectIdentity
ce12812 = _Ce12812_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 239, 3)
)
_Ce5850_54Q_EI_48T_ObjectIdentity = ObjectIdentity
ce5850_54Q_EI_48T = _Ce5850_54Q_EI_48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 239, 4)
)
_Ce6850_52Q_EI_48S_ObjectIdentity = ObjectIdentity
ce6850_52Q_EI_48S = _Ce6850_52Q_EI_48S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 239, 5)
)
_Ce6850_52Q_EI_48T_ObjectIdentity = ObjectIdentity
ce6850_52Q_EI_48T = _Ce6850_52Q_EI_48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 239, 6)
)
_Wlan_ObjectIdentity = ObjectIdentity
wlan = _Wlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 240)
)
_Acu_ObjectIdentity = ObjectIdentity
acu = _Acu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 240, 1)
)
_Ac6605_lsw_ObjectIdentity = ObjectIdentity
ac6605_lsw = _Ac6605_lsw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 240, 2)
)
_Ac6605_ac_ObjectIdentity = ObjectIdentity
ac6605_ac = _Ac6605_ac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 240, 3)
)
_HuaweiExperimental_ObjectIdentity = ObjectIdentity
huaweiExperimental = _HuaweiExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 4)
)
_HuaweiMgmt_ObjectIdentity = ObjectIdentity
huaweiMgmt = _HuaweiMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5)
)
_HwAcl_ObjectIdentity = ObjectIdentity
hwAcl = _HwAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1)
)
_HwAaa_ObjectIdentity = ObjectIdentity
hwAaa = _HwAaa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2)
)
_HwLam_ObjectIdentity = ObjectIdentity
hwLam = _HwLam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 3)
)
_HwPortal_ObjectIdentity = ObjectIdentity
hwPortal = _HwPortal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4)
)
_HwRadius_ObjectIdentity = ObjectIdentity
hwRadius = _HwRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 5)
)
_HwVlan_ObjectIdentity = ObjectIdentity
hwVlan = _HwVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6)
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
_HwVprn_ObjectIdentity = ObjectIdentity
hwVprn = _HwVprn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 8)
)
_HwFr_ObjectIdentity = ObjectIdentity
hwFr = _HwFr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 9)
)
_HwAtmCmRm_ObjectIdentity = ObjectIdentity
hwAtmCmRm = _HwAtmCmRm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 10)
)
_HwCes_ObjectIdentity = ObjectIdentity
hwCes = _HwCes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 11)
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
_HwMplsFtn_ObjectIdentity = ObjectIdentity
hwMplsFtn = _HwMplsFtn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 4)
)
_HwMplsVpls_ObjectIdentity = ObjectIdentity
hwMplsVpls = _HwMplsVpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 5)
)
_HwMplsLsp_ObjectIdentity = ObjectIdentity
hwMplsLsp = _HwMplsLsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 6)
)
_HwMplsOam_ObjectIdentity = ObjectIdentity
hwMplsOam = _HwMplsOam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7)
)
_HwPw_ObjectIdentity = ObjectIdentity
hwPw = _HwPw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 8)
)
_HwRouteManagement_ObjectIdentity = ObjectIdentity
hwRouteManagement = _HwRouteManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 13)
)
_HwRouteManagementUrm_ObjectIdentity = ObjectIdentity
hwRouteManagementUrm = _HwRouteManagementUrm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 13, 1)
)
_HwRouteManagementMrm_ObjectIdentity = ObjectIdentity
hwRouteManagementMrm = _HwRouteManagementMrm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 13, 2)
)
_HwRouteManagementRpm_ObjectIdentity = ObjectIdentity
hwRouteManagementRpm = _HwRouteManagementRpm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 13, 3)
)
_HwEthernetPort_ObjectIdentity = ObjectIdentity
hwEthernetPort = _HwEthernetPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 14)
)
_HwVTP_ObjectIdentity = ObjectIdentity
hwVTP = _HwVTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 15)
)
_HwMam_ObjectIdentity = ObjectIdentity
hwMam = _HwMam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 16)
)
_HwArpProxy_ObjectIdentity = ObjectIdentity
hwArpProxy = _HwArpProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 17)
)
_HwDhcpProxy_ObjectIdentity = ObjectIdentity
hwDhcpProxy = _HwDhcpProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 18)
)
_HwIgspSnooping_ObjectIdentity = ObjectIdentity
hwIgspSnooping = _HwIgspSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 19)
)
_HwGarpExt_ObjectIdentity = ObjectIdentity
hwGarpExt = _HwGarpExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 20)
)
_HwRstpExt_ObjectIdentity = ObjectIdentity
hwRstpExt = _HwRstpExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 21)
)
_HwPae8021xExt_ObjectIdentity = ObjectIdentity
hwPae8021xExt = _HwPae8021xExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 22)
)
_HwNat_ObjectIdentity = ObjectIdentity
hwNat = _HwNat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 23)
)
_HwVlanProtocol_ObjectIdentity = ObjectIdentity
hwVlanProtocol = _HwVlanProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 24)
)
_HwDatacomm_ObjectIdentity = ObjectIdentity
hwDatacomm = _HwDatacomm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25)
)
_HwBRASMib_ObjectIdentity = ObjectIdentity
hwBRASMib = _HwBRASMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40)
)
_HwImps_ObjectIdentity = ObjectIdentity
hwImps = _HwImps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 26)
)
_HuaweiUtility_ObjectIdentity = ObjectIdentity
huaweiUtility = _HuaweiUtility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6)
)
_HwEnvironment_ObjectIdentity = ObjectIdentity
hwEnvironment = _HwEnvironment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 1)
)
_HwPower_ObjectIdentity = ObjectIdentity
hwPower = _HwPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 2)
)
_HwDev_ObjectIdentity = ObjectIdentity
hwDev = _HwDev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3)
)
_HwNtp_ObjectIdentity = ObjectIdentity
hwNtp = _HwNtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 4)
)
_HwMem_ObjectIdentity = ObjectIdentity
hwMem = _HwMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 5)
)
_HwLoadBackup_ObjectIdentity = ObjectIdentity
hwLoadBackup = _HwLoadBackup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6)
)
_HwHgmp_ObjectIdentity = ObjectIdentity
hwHgmp = _HwHgmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7)
)
_HwIppool_ObjectIdentity = ObjectIdentity
hwIppool = _HwIppool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8)
)
_HwFlash_ObjectIdentity = ObjectIdentity
hwFlash = _HwFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 9)
)
_HwConfig_ObjectIdentity = ObjectIdentity
hwConfig = _HwConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10)
)
_HwAtmOam_ObjectIdentity = ObjectIdentity
hwAtmOam = _HwAtmOam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 11)
)
_HwAtmPos_ObjectIdentity = ObjectIdentity
hwAtmPos = _HwAtmPos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 12)
)
_HwHSL_ObjectIdentity = ObjectIdentity
hwHSL = _HwHSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 13)
)
_HwMTA_ObjectIdentity = ObjectIdentity
hwMTA = _HwMTA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 14)
)
_HwSPC_ObjectIdentity = ObjectIdentity
hwSPC = _HwSPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 15)
)
_HwV5_ObjectIdentity = ObjectIdentity
hwV5 = _HwV5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 16)
)
_HwIma_ObjectIdentity = ObjectIdentity
hwIma = _HwIma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 17)
)
_HwUcl_ObjectIdentity = ObjectIdentity
hwUcl = _HwUcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 18)
)
_HwAtmSvc_ObjectIdentity = ObjectIdentity
hwAtmSvc = _HwAtmSvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 19)
)
_HwVPRing_ObjectIdentity = ObjectIdentity
hwVPRing = _HwVPRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 20)
)
_HwTest_ObjectIdentity = ObjectIdentity
hwTest = _HwTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 21)
)
_HwTestCommon_ObjectIdentity = ObjectIdentity
hwTestCommon = _HwTestCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 21, 1)
)
_HwNTest_ObjectIdentity = ObjectIdentity
hwNTest = _HwNTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 21, 2)
)
_HwBtest_ObjectIdentity = ObjectIdentity
hwBtest = _HwBtest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 21, 3)
)
_HwSwitchOver_ObjectIdentity = ObjectIdentity
hwSwitchOver = _HwSwitchOver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 22)
)
_HwVfb_ObjectIdentity = ObjectIdentity
hwVfb = _HwVfb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 23)
)
_HwClk_ObjectIdentity = ObjectIdentity
hwClk = _HwClk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 25)
)
_HwCdi_ObjectIdentity = ObjectIdentity
hwCdi = _HwCdi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 26)
)
_HwAti_ObjectIdentity = ObjectIdentity
hwAti = _HwAti_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 27)
)
_HwDslamNtv_ObjectIdentity = ObjectIdentity
hwDslamNtv = _HwDslamNtv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 28)
)
_HwServerMon_ObjectIdentity = ObjectIdentity
hwServerMon = _HwServerMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 29)
)
_HwSyntrap_ObjectIdentity = ObjectIdentity
hwSyntrap = _HwSyntrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 30)
)
_HwAdsl_ObjectIdentity = ObjectIdentity
hwAdsl = _HwAdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 31)
)
_HwVdsl_ObjectIdentity = ObjectIdentity
hwVdsl = _HwVdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 32)
)
_HwHdsl_ObjectIdentity = ObjectIdentity
hwHdsl = _HwHdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 33)
)
_HwDeha_ObjectIdentity = ObjectIdentity
hwDeha = _HwDeha_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 34)
)
_HwSyslog_ObjectIdentity = ObjectIdentity
hwSyslog = _HwSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 35)
)
_HwVoip_ObjectIdentity = ObjectIdentity
hwVoip = _HwVoip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 36)
)
_HwVrp_ObjectIdentity = ObjectIdentity
hwVrp = _HwVrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 37)
)
_HwMus_ObjectIdentity = ObjectIdentity
hwMus = _HwMus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 38)
)
_HwDns_ObjectIdentity = ObjectIdentity
hwDns = _HwDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 39)
)
_HwNetTest_ObjectIdentity = ObjectIdentity
hwNetTest = _HwNetTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 40)
)
_HwMs_ObjectIdentity = ObjectIdentity
hwMs = _HwMs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 41)
)
_HwPITP_ObjectIdentity = ObjectIdentity
hwPITP = _HwPITP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 42)
)
_HwDslamMacPool_ObjectIdentity = ObjectIdentity
hwDslamMacPool = _HwDslamMacPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 43)
)
_HwDslamPPPoA_ObjectIdentity = ObjectIdentity
hwDslamPPPoA = _HwDslamPPPoA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 44)
)
_HwDslamPvcProtocol_ObjectIdentity = ObjectIdentity
hwDslamPvcProtocol = _HwDslamPvcProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 45)
)
_HwDslamIpoa_ObjectIdentity = ObjectIdentity
hwDslamIpoa = _HwDslamIpoa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 46)
)
_HwLicense_ObjectIdentity = ObjectIdentity
hwLicense = _HwLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 47)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-MIB",
    **{"huawei": huawei,
       "hwLocal": hwLocal,
       "quidway": quidway,
       "hwTrans": hwTrans,
       "hwInternetProtocol": hwInternetProtocol,
       "rmonExtend": rmonExtend,
       "performance": performance,
       "hwNovellProtocol": hwNovellProtocol,
       "hwProducts": hwProducts,
       "atm": atm,
       "atmAccess": atmAccess,
       "atmBone": atmBone,
       "r8750": r8750,
       "router": router,
       "routerGeneral": routerGeneral,
       "attr": attr,
       "ne08": ne08,
       "ne16": ne16,
       "module": module,
       "flash": flash,
       "mixinfo": mixinfo,
       "huaweiMemoryPool": huaweiMemoryPool,
       "configFile": configFile,
       "netEngine": netEngine,
       "access-server": access_server,
       "as8010": as8010,
       "lan-switch": lan_switch,
       "switch2403": switch2403,
       "switch2403F": switch2403F,
       "switch3008": switch3008,
       "switch3016": switch3016,
       "switch2024-M": switch2024_M,
       "switch3025-M": switch3025_M,
       "xdsl": xdsl,
       "adsl": adsl,
       "musa": musa,
       "hwMusaV100R001Mib": hwMusaV100R001Mib,
       "hwMA5200Mib": hwMA5200Mib,
       "hwMusaV100R002Mib": hwMusaV100R002Mib,
       "hwMd5500Mib": hwMd5500Mib,
       "hwMa5100Mib": hwMa5100Mib,
       "hwMa5300Mib": hwMa5300Mib,
       "ias": ias,
       "mpeg-2": mpeg_2,
       "gprs": gprs,
       "honet": honet,
       "cc08": cc08,
       "sbs": sbs,
       "ip-phone": ip_phone,
       "ups": ups,
       "viewpoint": viewpoint,
       "netManager": netManager,
       "iNet": iNet,
       "ne80": ne80,
       "wireIn": wireIn,
       "wireInScp": wireInScp,
       "wireInSdp": wireInSdp,
       "wireInSmp": wireInSmp,
       "wireInSsp": wireInSsp,
       "wireInIP": wireInIP,
       "mobileIn": mobileIn,
       "mobileInScp": mobileInScp,
       "mobileInSdp": mobileInSdp,
       "mobileInSmp": mobileInSmp,
       "mobileInSsp": mobileInSsp,
       "mobileInIP": mobileInIP,
       "cdmaIn": cdmaIn,
       "cdmaInScp": cdmaInScp,
       "cdmaInSdp": cdmaInSdp,
       "cdmaInSmp": cdmaInSmp,
       "cdmaInSsp": cdmaInSsp,
       "cdmaInIP": cdmaInIP,
       "acdIn": acdIn,
       "esr": esr,
       "radium8750": radium8750,
       "isn8850": isn8850,
       "esr8825": esr8825,
       "esrV5R3": esrV5R3,
       "esrV5R58850": esrV5R58850,
       "esrV5R58825": esrV5R58825,
       "lanSw": lanSw,
       "lswCommon": lswCommon,
       "s8016": s8016,
       "s8016Common": s8016Common,
       "s8016A": s8016A,
       "s8016B": s8016B,
       "s3526": s3526,
       "s3026": s3026,
       "s3026V": s3026V,
       "s2008": s2008,
       "s2016": s2016,
       "s3526F": s3526F,
       "s5516": s5516,
       "s6506": s6506,
       "s3026F": s3026F,
       "s3526E": s3526E,
       "s2026": s2026,
       "s2403H": s2403H,
       "s3026E": s3026E,
       "s3050C": s3050C,
       "s6503": s6503,
       "s8512": s8512,
       "s8505": s8505,
       "s6506R": s6506R,
       "s3026c": s3026c,
       "s3026g": s3026g,
       "s3026t": s3026t,
       "s3552G": s3552G,
       "s3552P": s3552P,
       "s3528G": s3528G,
       "s3528P": s3528P,
       "s3526c": s3526c,
       "s3026c-24-12fs": s3026c_24_12fs,
       "s3026c-24-12fm": s3026c_24_12fm,
       "s3526c-24-12fs": s3526c_24_12fs,
       "s3526c-24-12fm": s3526c_24_12fm,
       "s5012G": s5012G,
       "s5012G-DC": s5012G_DC,
       "s5012T-12-10GBC": s5012T_12_10GBC,
       "s5012T-12-10GBC-DC": s5012T_12_10GBC_DC,
       "s5024G-24-20TP": s5024G_24_20TP,
       "s5024G-24-20TP-DC": s5024G_24_20TP_DC,
       "s2026Z": s2026Z,
       "s2026C": s2026C,
       "s3026G-SI": s3026G_SI,
       "s3026C-SI": s3026C_SI,
       "s3026S-SI": s3026S_SI,
       "s8505e": s8505e,
       "s3552F-SI": s3552F_SI,
       "s3552F-EI": s3552F_EI,
       "e026": e026,
       "e026-SI": e026_SI,
       "e050": e050,
       "s2326P-SI": s2326P_SI,
       "s2326P-EI": s2326P_EI,
       "s2318P-SI": s2318P_SI,
       "s2318P-EI": s2318P_EI,
       "s2309P-SI": s2309P_SI,
       "s2309P-EI": s2309P_EI,
       "s3352P-SI": s3352P_SI,
       "s3352P-EI": s3352P_EI,
       "s3328TP-SI": s3328TP_SI,
       "s3328TP-EI": s3328TP_EI,
       "s3328TP-EI-24S": s3328TP_EI_24S,
       "s3328TP-SI-24S": s3328TP_SI_24S,
       "s3352P-EI-24S": s3352P_EI_24S,
       "s3352P-EI-48S": s3352P_EI_48S,
       "s3352P-SI-48S": s3352P_SI_48S,
       "s2309TP-SI": s2309TP_SI,
       "s2309TP-EI": s2309TP_EI,
       "s2318TP-SI": s2318TP_SI,
       "s2318TP-EI": s2318TP_EI,
       "s2326TP-SI": s2326TP_SI,
       "s2326TP-EI": s2326TP_EI,
       "s2352P-SI": s2352P_SI,
       "s2352P-EI": s2352P_EI,
       "s5328C-EI": s5328C_EI,
       "s5328C-EI-24S": s5328C_EI_24S,
       "s5352C-EI": s5352C_EI,
       "s5324TP-SI": s5324TP_SI,
       "s5348TP-SI": s5348TP_SI,
       "s5324TP-PWR-SI": s5324TP_PWR_SI,
       "s5348TP-PWR-SI": s5348TP_PWR_SI,
       "s5328C-SI": s5328C_SI,
       "s5352C-SI": s5352C_SI,
       "s5328C-PWR-SI": s5328C_PWR_SI,
       "s5352C-PWR-SI": s5352C_PWR_SI,
       "s5328C-PWR-EI": s5328C_PWR_EI,
       "s5352C-PWR-EI": s5352C_PWR_EI,
       "s2309TP-PWR-EI": s2309TP_PWR_EI,
       "s2326TP-PWR-EI": s2326TP_PWR_EI,
       "s3328TP-PWR-EI": s3328TP_PWR_EI,
       "s3352P-PWR-EI": s3352P_PWR_EI,
       "s3328TP-EI-MC": s3328TP_EI_MC,
       "s3318TP-EI-MC": s3318TP_EI_MC,
       "s2700-9TP-EI-AC": s2700_9TP_EI_AC,
       "s2700-9TP-EI-DC": s2700_9TP_EI_DC,
       "s2700-18TP-EI-AC": s2700_18TP_EI_AC,
       "s2700-26TP-EI-AC": s2700_26TP_EI_AC,
       "s2700-26TP-EI-DC": s2700_26TP_EI_DC,
       "s2700-52TP-EI-AC": s2700_52TP_EI_AC,
       "s2700-9TP-SI-AC": s2700_9TP_SI_AC,
       "s2700-18TP-SI-AC": s2700_18TP_SI_AC,
       "s2700-26TP-SI-AC": s2700_26TP_SI_AC,
       "s2700-9TP-PWR-EI": s2700_9TP_PWR_EI,
       "s2700-26TP-PWR-EI": s2700_26TP_PWR_EI,
       "s3700-28TP-EI-AC": s3700_28TP_EI_AC,
       "s3700-28TP-EI-DC": s3700_28TP_EI_DC,
       "s3700-28TP-EI-24S-AC": s3700_28TP_EI_24S_AC,
       "s3700-52TP-EI-AC": s3700_52TP_EI_AC,
       "s3700-52TP-EI-DC": s3700_52TP_EI_DC,
       "s3700-52TP-EI-24S-AC": s3700_52TP_EI_24S_AC,
       "s3700-52TP-EI-24S-DC": s3700_52TP_EI_24S_DC,
       "s3700-52TP-EI-48S-AC": s3700_52TP_EI_48S_AC,
       "s3700-52TP-EI-48S-DC": s3700_52TP_EI_48S_DC,
       "s3700-28TP-SI-AC": s3700_28TP_SI_AC,
       "s3700-28TP-SI-DC": s3700_28TP_SI_DC,
       "s3700-52TP-SI-AC": s3700_52TP_SI_AC,
       "s3700-28TP-PWR-EI": s3700_28TP_PWR_EI,
       "s3700-52TP-PWR-EI": s3700_52TP_PWR_EI,
       "s3700-28TP-EI-MC-AC": s3700_28TP_EI_MC_AC,
       "s5700-28C-EI": s5700_28C_EI,
       "s5700-28C-SI": s5700_28C_SI,
       "s5700-28C-EI-24S": s5700_28C_EI_24S,
       "s5700-52C-EI": s5700_52C_EI,
       "s5700-52C-SI": s5700_52C_SI,
       "s5700-24TP-SI-AC": s5700_24TP_SI_AC,
       "s5700-24TP-SI-DC": s5700_24TP_SI_DC,
       "s5700-48TP-SI-AC": s5700_48TP_SI_AC,
       "s5700-48TP-SI-DC": s5700_48TP_SI_DC,
       "s5700-28C-PWR-EI": s5700_28C_PWR_EI,
       "s5700-52C-PWR-EI": s5700_52C_PWR_EI,
       "s5700-24TP-PWR-SI": s5700_24TP_PWR_SI,
       "s5700-48TP-PWR-SI": s5700_48TP_PWR_SI,
       "s6324C": s6324C,
       "s6348C": s6348C,
       "s5328C-HI": s5328C_HI,
       "s5328C-HI-24S": s5328C_HI_24S,
       "s5306TP-SI": s5306TP_SI,
       "s3326C-HI": s3326C_HI,
       "s5328C-HI-24SA": s5328C_HI_24SA,
       "s6700-24-EI": s6700_24_EI,
       "s6700-48-EI": s6700_48_EI,
       "s1728-GWR-4P": s1728_GWR_4P,
       "s5700-28P-LI": s5700_28P_LI,
       "s5700-28P-PWR-LI-AC": s5700_28P_PWR_LI_AC,
       "s5700-52P-LI": s5700_52P_LI,
       "s5700-52P-PWR-LI-AC": s5700_52P_PWR_LI_AC,
       "s5700-28X-EI": s5700_28X_EI,
       "s5700-52X-EI": s5700_52X_EI,
       "s5700-28C-HI": s5700_28C_HI,
       "s5700-28C-HI-24S": s5700_28C_HI_24S,
       "s5700-6TP-LI-AC": s5700_6TP_LI_AC,
       "s3700-26C-HI": s3700_26C_HI,
       "s5300-28C-PWR-EI": s5300_28C_PWR_EI,
       "s5300-52C-PWR-EI": s5300_52C_PWR_EI,
       "s5310-28P-LI": s5310_28P_LI,
       "s5310-52P-LI": s5310_52P_LI,
       "s5700-28P-LI-DC": s5700_28P_LI_DC,
       "s5700-52P-LI-DC": s5700_52P_LI_DC,
       "s5310-28P-LI-DC": s5310_28P_LI_DC,
       "s5310-52P-LI-DC": s5310_52P_LI_DC,
       "s5700S-28P-LI-AC": s5700S_28P_LI_AC,
       "s5700S-52P-LI-AC": s5700S_52P_LI_AC,
       "s1700-28GFR-4P-AC": s1700_28GFR_4P_AC,
       "s1700-52GFR-4P-AC": s1700_52GFR_4P_AC,
       "s1700-28FR-2T2P-AC": s1700_28FR_2T2P_AC,
       "s1700-52FR-2T2P-AC": s1700_52FR_2T2P_AC,
       "s5700-28C-PWR-SI": s5700_28C_PWR_SI,
       "s5700-52C-PWR-SI": s5700_52C_PWR_SI,
       "s5710-28C-PWR-LI": s5710_28C_PWR_LI,
       "s5710-52C-PWR-LI": s5710_52C_PWR_LI,
       "s5710-28C-LI": s5710_28C_LI,
       "s5710-52C-LI": s5710_52C_LI,
       "e6000": e6000,
       "s5710-28C-PWR-EI": s5710_28C_PWR_EI,
       "s5710-52C-PWR-EI": s5710_52C_PWR_EI,
       "s2710-26TP-PWR-SI": s2710_26TP_PWR_SI,
       "s2710-52P-SI-AC": s2710_52P_SI_AC,
       "s2710-52P-PWR-SI": s2710_52P_PWR_SI,
       "s2700-52P-PWR-EI": s2700_52P_PWR_EI,
       "s3700-52P-PWR-SI": s3700_52P_PWR_SI,
       "s3700-28TP-PWR-SI": s3700_28TP_PWR_SI,
       "s5710-108C-PWR-HI": s5710_108C_PWR_HI,
       "s5700-10P-LI-AC": s5700_10P_LI_AC,
       "s5700-10P-PWR-LI-AC": s5700_10P_PWR_LI_AC,
       "s5700-26X-SI-12S-AC": s5700_26X_SI_12S_AC,
       "s5700-28X-LI-AC": s5700_28X_LI_AC,
       "s5700-28X-LI-DC": s5700_28X_LI_DC,
       "s5700-52X-LI-AC": s5700_52X_LI_AC,
       "s5700-52X-LI-DC": s5700_52X_LI_DC,
       "s5700-28X-PWR-LI-AC": s5700_28X_PWR_LI_AC,
       "s5700-52X-PWR-LI-AC": s5700_52X_PWR_LI_AC,
       "apon": apon,
       "ma5101": ma5101,
       "ma5102": ma5102,
       "transmission": transmission,
       "optix155622H": optix155622H,
       "optix10Gv2": optix10Gv2,
       "hsr": hsr,
       "ne16E": ne16E,
       "ne08E": ne08E,
       "ne05": ne05,
       "amg5000": amg5000,
       "umg8900": umg8900,
       "ne20": ne20,
       "ne20s": ne20s,
       "ne40": ne40,
       "wcdma": wcdma,
       "sgsn": sgsn,
       "mlsr": mlsr,
       "dslw": dslw,
       "dlswNode": dlswNode,
       "dlswTConn": dlswTConn,
       "dlswInterface": dlswInterface,
       "dlswDirectory": dlswDirectory,
       "dlswCircuit": dlswCircuit,
       "dlswSdlc": dlswSdlc,
       "dlswLlc2": dlswLlc2,
       "sm": sm,
       "mmsc": mmsc,
       "as": _pysmi_as,
       "p3": p3,
       "iad": iad,
       "iad132": iad132,
       "wlanAp": wlanAp,
       "wlanApCommon": wlanApCommon,
       "wlanApWA1003": wlanApWA1003,
       "wlanApWA1003A": wlanApWA1003A,
       "wlanApWA1005": wlanApWA1005,
       "wlanApWA1008": wlanApWA1008,
       "wlanApWA1208": wlanApWA1208,
       "wlanApWA1208H": wlanApWA1208H,
       "wlanApWA1006E": wlanApWA1006E,
       "wlanBridgeWB2010": wlanBridgeWB2010,
       "wlanBridgeWB2011": wlanBridgeWB2011,
       "wa1208E": wa1208E,
       "hwinfoX": hwinfoX,
       "wlanApWA1006": wlanApWA1006,
       "ar46-20": ar46_20,
       "ar46-40": ar46_40,
       "ar46-80": ar46_80,
       "ne20-2": ne20_2,
       "ne20-4": ne20_4,
       "ne20-8": ne20_8,
       "eudemon200": eudemon200,
       "eudemon1000": eudemon1000,
       "vdg10-40": vdg10_40,
       "vdg10-41": vdg10_41,
       "hwSps": hwSps,
       "ar18-18": ar18_18,
       "ar18-20": ar18_20,
       "ar18-30": ar18_30,
       "ar18-31": ar18_31,
       "ar18-32": ar18_32,
       "ar18-33": ar18_33,
       "ar18-34": ar18_34,
       "ne5000": ne5000,
       "ne5000SysOid": ne5000SysOid,
       "ne5000oem": ne5000oem,
       "ne80E": ne80E,
       "ne5000E": ne5000E,
       "ne5000EMulti": ne5000EMulti,
       "ne40E": ne40E,
       "ne5000E-BTB": ne5000E_BTB,
       "ne40E-4": ne40E_4,
       "ne40E-X3": ne40E_X3,
       "ne40E-X8": ne40E_X8,
       "ne40E-X16": ne40E_X16,
       "ne5000E-X16": ne5000E_X16,
       "ne40E-X1": ne40E_X1,
       "ne40E-X2": ne40E_X2,
       "ne40E-X1-M4": ne40E_X1_M4,
       "ne40E-X2-M8": ne40E_X2_M8,
       "ne40E-X2-M16": ne40E_X2_M16,
       "ggsn9811": ggsn9811,
       "pdsn9660": pdsn9660,
       "eudemon2100": eudemon2100,
       "eudemon2200": eudemon2200,
       "ua5000ipm": ua5000ipm,
       "rm9000": rm9000,
       "hwIMAPNorthbound": hwIMAPNorthbound,
       "hwBITS": hwBITS,
       "hwPv8": hwPv8,
       "eudemon500": eudemon500,
       "ua5000IpmB": ua5000IpmB,
       "ua5000ApmB": ua5000ApmB,
       "ma5600": ma5600,
       "softx3000UC": softx3000UC,
       "hwOSTA": hwOSTA,
       "secpath1800F": secpath1800F,
       "eudemon2300": eudemon2300,
       "ma5100V600": ma5100V600,
       "ma5605": ma5605,
       "msp": msp,
       "cX200A": cX200A,
       "cX200B": cX200B,
       "cX300A": cX300A,
       "cX300B": cX300B,
       "cX500A": cX500A,
       "cX380": cX380,
       "cX600-8": cX600_8,
       "cX600-16": cX600_16,
       "cX200C": cX200C,
       "cX200D": cX200D,
       "cX200D-EA": cX200D_EA,
       "cX200D-MC": cX200D_MC,
       "cX600-4": cX600_4,
       "cX380-PBT": cX380_PBT,
       "cX380-ME": cX380_ME,
       "cX200D-EA-MC": cX200D_EA_MC,
       "cX600-X3": cX600_X3,
       "cX600-X8": cX600_X8,
       "cX600-X16": cX600_X16,
       "cX600-X1": cX600_X1,
       "cX600-X2": cX600_X2,
       "cX600-X1DO": cX600_X1DO,
       "cX600-X2DO": cX600_X2DO,
       "cX600-X3DO": cX600_X3DO,
       "cX600-X8DO": cX600_X8DO,
       "cX600-X16DO": cX600_X16DO,
       "cX600-X1-M4": cX600_X1_M4,
       "cX600-X2-M8": cX600_X2_M8,
       "cX600-X2-M16": cX600_X2_M16,
       "ne20E": ne20E,
       "ne20E-4": ne20E_4,
       "ne20E-8": ne20E_8,
       "ne20E-X6": ne20E_X6,
       "me60": me60,
       "me60-16": me60_16,
       "me60-8": me60_8,
       "me60-4": me60_4,
       "me60-X3": me60_X3,
       "me60-X8": me60_X8,
       "me60-X16": me60_X16,
       "eudemon300": eudemon300,
       "eudemonVPN3900": eudemonVPN3900,
       "eudemonEVPN5900": eudemonEVPN5900,
       "eudemon100E": eudemon100E,
       "eudemon200E": eudemon200E,
       "eudemon200S": eudemon200S,
       "svn3000": svn3000,
       "usg5000": usg5000,
       "usg9000": usg9000,
       "eudemon200s": eudemon200s,
       "sig1000": sig1000,
       "sig9280": sig9280,
       "sig2000": sig2000,
       "s9300": s9300,
       "s9303": s9303,
       "s9306": s9306,
       "s9312": s9312,
       "vasp": vasp,
       "s9303E": s9303E,
       "s9306E": s9306E,
       "s9312E": s9312E,
       "ptn": ptn,
       "ptn2900": ptn2900,
       "ptn6900": ptn6900,
       "ptn6900-16": ptn6900_16,
       "ptn6900-8": ptn6900_8,
       "ptn6900-3": ptn6900_3,
       "ptn6900-2": ptn6900_2,
       "ptn6900-1": ptn6900_1,
       "nse": nse,
       "ssp1000": ssp1000,
       "ssp2000": ssp2000,
       "ssp3000": ssp3000,
       "ssp1000-4": ssp1000_4,
       "nse1000-4": nse1000_4,
       "nse1000-8": nse1000_8,
       "nse1000-X3": nse1000_X3,
       "ssp5000-X3": ssp5000_X3,
       "ssp5000-X8": ssp5000_X8,
       "ssp5000-X16": ssp5000_X16,
       "atn": atn,
       "atn980": atn980,
       "atn990": atn990,
       "atn910": atn910,
       "atn950": atn950,
       "atn950B": atn950B,
       "s7700": s7700,
       "s7703": s7703,
       "s7706": s7706,
       "s7712": s7712,
       "ar": ar,
       "ar1220": ar1220,
       "ar1220w": ar1220w,
       "ar1240": ar1240,
       "ar1240w": ar1240w,
       "ar2220": ar2220,
       "ar2240": ar2240,
       "ar3260": ar3260,
       "ar1220v": ar1220v,
       "ar201": ar201,
       "ar206": ar206,
       "ar207": ar207,
       "ar207v": ar207v,
       "ar208": ar208,
       "ar1220vw": ar1220vw,
       "ar1220s": ar1220s,
       "ar1220ws": ar1220ws,
       "s12700": s12700,
       "s12708": s12708,
       "s12716": s12716,
       "vRGW": vRGW,
       "s9700": s9700,
       "s9703": s9703,
       "s9706": s9706,
       "s9712": s9712,
       "dcswitch": dcswitch,
       "ce12804": ce12804,
       "ce12808": ce12808,
       "ce12812": ce12812,
       "ce5850-54Q-EI-48T": ce5850_54Q_EI_48T,
       "ce6850-52Q-EI-48S": ce6850_52Q_EI_48S,
       "ce6850-52Q-EI-48T": ce6850_52Q_EI_48T,
       "wlan": wlan,
       "acu": acu,
       "ac6605-lsw": ac6605_lsw,
       "ac6605-ac": ac6605_ac,
       "huaweiExperimental": huaweiExperimental,
       "huaweiMgmt": huaweiMgmt,
       "hwAcl": hwAcl,
       "hwAaa": hwAaa,
       "hwLam": hwLam,
       "hwPortal": hwPortal,
       "hwRadius": hwRadius,
       "hwVlan": hwVlan,
       "hwDhcp": hwDhcp,
       "hwDHCPRelayMib": hwDHCPRelayMib,
       "hwDHCPServerMib": hwDHCPServerMib,
       "hwVprn": hwVprn,
       "hwFr": hwFr,
       "hwAtmCmRm": hwAtmCmRm,
       "hwCes": hwCes,
       "hwMpls": hwMpls,
       "hwMplsLsr": hwMplsLsr,
       "hwMplsLdp": hwMplsLdp,
       "hwMplsVpn": hwMplsVpn,
       "hwMplsFtn": hwMplsFtn,
       "hwMplsVpls": hwMplsVpls,
       "hwMplsLsp": hwMplsLsp,
       "hwMplsOam": hwMplsOam,
       "hwPw": hwPw,
       "hwRouteManagement": hwRouteManagement,
       "hwRouteManagementUrm": hwRouteManagementUrm,
       "hwRouteManagementMrm": hwRouteManagementMrm,
       "hwRouteManagementRpm": hwRouteManagementRpm,
       "hwEthernetPort": hwEthernetPort,
       "hwVTP": hwVTP,
       "hwMam": hwMam,
       "hwArpProxy": hwArpProxy,
       "hwDhcpProxy": hwDhcpProxy,
       "hwIgspSnooping": hwIgspSnooping,
       "hwGarpExt": hwGarpExt,
       "hwRstpExt": hwRstpExt,
       "hwPae8021xExt": hwPae8021xExt,
       "hwNat": hwNat,
       "hwVlanProtocol": hwVlanProtocol,
       "hwDatacomm": hwDatacomm,
       "hwBRASMib": hwBRASMib,
       "hwImps": hwImps,
       "huaweiUtility": huaweiUtility,
       "hwEnvironment": hwEnvironment,
       "hwPower": hwPower,
       "hwDev": hwDev,
       "hwNtp": hwNtp,
       "hwMem": hwMem,
       "hwLoadBackup": hwLoadBackup,
       "hwHgmp": hwHgmp,
       "hwIppool": hwIppool,
       "hwFlash": hwFlash,
       "hwConfig": hwConfig,
       "hwAtmOam": hwAtmOam,
       "hwAtmPos": hwAtmPos,
       "hwHSL": hwHSL,
       "hwMTA": hwMTA,
       "hwSPC": hwSPC,
       "hwV5": hwV5,
       "hwIma": hwIma,
       "hwUcl": hwUcl,
       "hwAtmSvc": hwAtmSvc,
       "hwVPRing": hwVPRing,
       "hwTest": hwTest,
       "hwTestCommon": hwTestCommon,
       "hwNTest": hwNTest,
       "hwBtest": hwBtest,
       "hwSwitchOver": hwSwitchOver,
       "hwVfb": hwVfb,
       "hwClk": hwClk,
       "hwCdi": hwCdi,
       "hwAti": hwAti,
       "hwDslamNtv": hwDslamNtv,
       "hwServerMon": hwServerMon,
       "hwSyntrap": hwSyntrap,
       "hwAdsl": hwAdsl,
       "hwVdsl": hwVdsl,
       "hwHdsl": hwHdsl,
       "hwDeha": hwDeha,
       "hwSyslog": hwSyslog,
       "hwVoip": hwVoip,
       "hwVrp": hwVrp,
       "hwMus": hwMus,
       "hwDns": hwDns,
       "hwNetTest": hwNetTest,
       "hwMs": hwMs,
       "hwPITP": hwPITP,
       "hwDslamMacPool": hwDslamMacPool,
       "hwDslamPPPoA": hwDslamPPPoA,
       "hwDslamPvcProtocol": hwDslamPvcProtocol,
       "hwDslamIpoa": hwDslamIpoa,
       "hwLicense": hwLicense}
)
