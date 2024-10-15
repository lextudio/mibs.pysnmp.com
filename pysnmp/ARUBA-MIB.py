# SNMP MIB module (ARUBA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ARUBA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:45 2024
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
 enterprises,
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aruba_ObjectIdentity = ObjectIdentity
aruba = _Aruba_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1)
)
_SwitchProducts_ObjectIdentity = ObjectIdentity
switchProducts = _SwitchProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1)
)
_A5000_ObjectIdentity = ObjectIdentity
a5000 = _A5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 1)
)
_A2400_ObjectIdentity = ObjectIdentity
a2400 = _A2400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 2)
)
_A800_ObjectIdentity = ObjectIdentity
a800 = _A800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 3)
)
_A6000_ObjectIdentity = ObjectIdentity
a6000 = _A6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 4)
)
_A2400E_ObjectIdentity = ObjectIdentity
a2400E = _A2400E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 7)
)
_A800E_ObjectIdentity = ObjectIdentity
a800E = _A800E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 8)
)
_A804_ObjectIdentity = ObjectIdentity
a804 = _A804_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 9)
)
_A200_ObjectIdentity = ObjectIdentity
a200 = _A200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 10)
)
_A2424_ObjectIdentity = ObjectIdentity
a2424 = _A2424_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 11)
)
_A6000_SC3_ObjectIdentity = ObjectIdentity
a6000_SC3 = _A6000_SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 12)
)
_A3200_ObjectIdentity = ObjectIdentity
a3200 = _A3200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 13)
)
_A3200_8_ObjectIdentity = ObjectIdentity
a3200_8 = _A3200_8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 14)
)
_A3400_ObjectIdentity = ObjectIdentity
a3400 = _A3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 15)
)
_A3400_32_ObjectIdentity = ObjectIdentity
a3400_32 = _A3400_32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 16)
)
_A3600_ObjectIdentity = ObjectIdentity
a3600 = _A3600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 17)
)
_A3600_64_ObjectIdentity = ObjectIdentity
a3600_64 = _A3600_64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 18)
)
_A650_ObjectIdentity = ObjectIdentity
a650 = _A650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 19)
)
_A651_ObjectIdentity = ObjectIdentity
a651 = _A651_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 20)
)
_Reserved1_ObjectIdentity = ObjectIdentity
reserved1 = _Reserved1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 21)
)
_Reserved2_ObjectIdentity = ObjectIdentity
reserved2 = _Reserved2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 22)
)
_A620_ObjectIdentity = ObjectIdentity
a620 = _A620_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 23)
)
_S3500_24P_ObjectIdentity = ObjectIdentity
s3500_24P = _S3500_24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 24)
)
_S3500_24T_ObjectIdentity = ObjectIdentity
s3500_24T = _S3500_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 25)
)
_S3500_48P_ObjectIdentity = ObjectIdentity
s3500_48P = _S3500_48P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 26)
)
_S3500_48T_ObjectIdentity = ObjectIdentity
s3500_48T = _S3500_48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 27)
)
_S2500_24P_ObjectIdentity = ObjectIdentity
s2500_24P = _S2500_24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 28)
)
_S2500_24T_ObjectIdentity = ObjectIdentity
s2500_24T = _S2500_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 29)
)
_S2500_48P_ObjectIdentity = ObjectIdentity
s2500_48P = _S2500_48P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 30)
)
_S2500_48T_ObjectIdentity = ObjectIdentity
s2500_48T = _S2500_48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 31)
)
_A7210_ObjectIdentity = ObjectIdentity
a7210 = _A7210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 32)
)
_A7220_ObjectIdentity = ObjectIdentity
a7220 = _A7220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 33)
)
_A7240_ObjectIdentity = ObjectIdentity
a7240 = _A7240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 34)
)
_S3500_24F_ObjectIdentity = ObjectIdentity
s3500_24F = _S3500_24F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 35)
)
_AUndefined_ObjectIdentity = ObjectIdentity
aUndefined = _AUndefined_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 9999)
)
_ApProducts_ObjectIdentity = ObjectIdentity
apProducts = _ApProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2)
)
_A50_ObjectIdentity = ObjectIdentity
a50 = _A50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 1)
)
_A52_ObjectIdentity = ObjectIdentity
a52 = _A52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 2)
)
_Ap60_ObjectIdentity = ObjectIdentity
ap60 = _Ap60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 3)
)
_Ap61_ObjectIdentity = ObjectIdentity
ap61 = _Ap61_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 4)
)
_Ap70_ObjectIdentity = ObjectIdentity
ap70 = _Ap70_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 5)
)
_WalljackAp61_ObjectIdentity = ObjectIdentity
walljackAp61 = _WalljackAp61_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 6)
)
_A2E_ObjectIdentity = ObjectIdentity
a2E = _A2E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 7)
)
_Ap1200_ObjectIdentity = ObjectIdentity
ap1200 = _Ap1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 8)
)
_Ap80s_ObjectIdentity = ObjectIdentity
ap80s = _Ap80s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 9)
)
_Ap80m_ObjectIdentity = ObjectIdentity
ap80m = _Ap80m_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 10)
)
_Wg102_ObjectIdentity = ObjectIdentity
wg102 = _Wg102_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 11)
)
_Ap40_ObjectIdentity = ObjectIdentity
ap40 = _Ap40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 12)
)
_Ap41_ObjectIdentity = ObjectIdentity
ap41 = _Ap41_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 13)
)
_Ap65_ObjectIdentity = ObjectIdentity
ap65 = _Ap65_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 14)
)
_ApMw1700_ObjectIdentity = ObjectIdentity
apMw1700 = _ApMw1700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 15)
)
_ApDuowj_ObjectIdentity = ObjectIdentity
apDuowj = _ApDuowj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 16)
)
_ApDuo_ObjectIdentity = ObjectIdentity
apDuo = _ApDuo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 17)
)
_Ap80MB_ObjectIdentity = ObjectIdentity
ap80MB = _Ap80MB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 18)
)
_Ap80SB_ObjectIdentity = ObjectIdentity
ap80SB = _Ap80SB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 19)
)
_Ap85_ObjectIdentity = ObjectIdentity
ap85 = _Ap85_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 20)
)
_Ap124_ObjectIdentity = ObjectIdentity
ap124 = _Ap124_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 21)
)
_Ap125_ObjectIdentity = ObjectIdentity
ap125 = _Ap125_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 22)
)
_Ap120_ObjectIdentity = ObjectIdentity
ap120 = _Ap120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 23)
)
_Ap121_ObjectIdentity = ObjectIdentity
ap121 = _Ap121_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 24)
)
_Ap1250_ObjectIdentity = ObjectIdentity
ap1250 = _Ap1250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 25)
)
_Ap120abg_ObjectIdentity = ObjectIdentity
ap120abg = _Ap120abg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 26)
)
_Ap121abg_ObjectIdentity = ObjectIdentity
ap121abg = _Ap121abg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 27)
)
_Ap124abg_ObjectIdentity = ObjectIdentity
ap124abg = _Ap124abg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 28)
)
_Ap125abg_ObjectIdentity = ObjectIdentity
ap125abg = _Ap125abg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 29)
)
_Rap5wn_ObjectIdentity = ObjectIdentity
rap5wn = _Rap5wn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 30)
)
_Rap5_ObjectIdentity = ObjectIdentity
rap5 = _Rap5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 31)
)
_Rap2wg_ObjectIdentity = ObjectIdentity
rap2wg = _Rap2wg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 32)
)
_Reserved4_ObjectIdentity = ObjectIdentity
reserved4 = _Reserved4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 33)
)
_Ap105_ObjectIdentity = ObjectIdentity
ap105 = _Ap105_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 34)
)
_Ap65wb_ObjectIdentity = ObjectIdentity
ap65wb = _Ap65wb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 35)
)
_Ap651_ObjectIdentity = ObjectIdentity
ap651 = _Ap651_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 36)
)
_Reserved6_ObjectIdentity = ObjectIdentity
reserved6 = _Reserved6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 37)
)
_Ap60p_ObjectIdentity = ObjectIdentity
ap60p = _Ap60p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 38)
)
_Reserved7_ObjectIdentity = ObjectIdentity
reserved7 = _Reserved7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 39)
)
_Ap92_ObjectIdentity = ObjectIdentity
ap92 = _Ap92_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 40)
)
_Ap93_ObjectIdentity = ObjectIdentity
ap93 = _Ap93_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 41)
)
_Ap68_ObjectIdentity = ObjectIdentity
ap68 = _Ap68_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 42)
)
_Ap68p_ObjectIdentity = ObjectIdentity
ap68p = _Ap68p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 43)
)
_Ap175p_ObjectIdentity = ObjectIdentity
ap175p = _Ap175p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 44)
)
_Ap175ac_ObjectIdentity = ObjectIdentity
ap175ac = _Ap175ac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 45)
)
_Ap175dc_ObjectIdentity = ObjectIdentity
ap175dc = _Ap175dc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 46)
)
_Ap134_ObjectIdentity = ObjectIdentity
ap134 = _Ap134_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 47)
)
_Ap135_ObjectIdentity = ObjectIdentity
ap135 = _Ap135_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 48)
)
_Reserved8_ObjectIdentity = ObjectIdentity
reserved8 = _Reserved8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 49)
)
_Ap93h_ObjectIdentity = ObjectIdentity
ap93h = _Ap93h_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 50)
)
_Iap23_ObjectIdentity = ObjectIdentity
iap23 = _Iap23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 51)
)
_Iap23p_ObjectIdentity = ObjectIdentity
iap23p = _Iap23p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 52)
)
_Ap104_ObjectIdentity = ObjectIdentity
ap104 = _Ap104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 53)
)
_ApUndefined_ObjectIdentity = ObjectIdentity
apUndefined = _ApUndefined_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 9999)
)
_EmsProducts_ObjectIdentity = ObjectIdentity
emsProducts = _EmsProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 3)
)
_PartnerProducts_ObjectIdentity = ObjectIdentity
partnerProducts = _PartnerProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 4)
)
_EcsE50_ObjectIdentity = ObjectIdentity
ecsE50 = _EcsE50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 4, 1)
)
_EcsE100C_ObjectIdentity = ObjectIdentity
ecsE100C = _EcsE100C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 4, 2)
)
_EcsE100A_ObjectIdentity = ObjectIdentity
ecsE100A = _EcsE100A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 4, 3)
)
_EcsENSM_ObjectIdentity = ObjectIdentity
ecsENSM = _EcsENSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 4, 4)
)
_AmigopodProducts_ObjectIdentity = ObjectIdentity
amigopodProducts = _AmigopodProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 5)
)
_ArubaEnterpriseMibModules_ObjectIdentity = ObjectIdentity
arubaEnterpriseMibModules = _ArubaEnterpriseMibModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2)
)
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 1)
)
_ArubaMIBModules_ObjectIdentity = ObjectIdentity
arubaMIBModules = _ArubaMIBModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 1, 1)
)
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2)
)
_WlsxEnterpriseMibModules_ObjectIdentity = ObjectIdentity
wlsxEnterpriseMibModules = _WlsxEnterpriseMibModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1)
)
_ArubaAp_ObjectIdentity = ObjectIdentity
arubaAp = _ArubaAp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3)
)
_WlsrEnterpriseMibModules_ObjectIdentity = ObjectIdentity
wlsrEnterpriseMibModules = _WlsrEnterpriseMibModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1)
)
_WlsrOutDoorApMibModules_ObjectIdentity = ObjectIdentity
wlsrOutDoorApMibModules = _WlsrOutDoorApMibModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2)
)
_ArubaEcs_ObjectIdentity = ObjectIdentity
arubaEcs = _ArubaEcs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 4)
)
_ArubaMgmt_ObjectIdentity = ObjectIdentity
arubaMgmt = _ArubaMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBA-MIB",
    **{"aruba": aruba,
       "products": products,
       "switchProducts": switchProducts,
       "a5000": a5000,
       "a2400": a2400,
       "a800": a800,
       "a6000": a6000,
       "a2400E": a2400E,
       "a800E": a800E,
       "a804": a804,
       "a200": a200,
       "a2424": a2424,
       "a6000-SC3": a6000_SC3,
       "a3200": a3200,
       "a3200-8": a3200_8,
       "a3400": a3400,
       "a3400-32": a3400_32,
       "a3600": a3600,
       "a3600-64": a3600_64,
       "a650": a650,
       "a651": a651,
       "reserved1": reserved1,
       "reserved2": reserved2,
       "a620": a620,
       "s3500-24P": s3500_24P,
       "s3500-24T": s3500_24T,
       "s3500-48P": s3500_48P,
       "s3500-48T": s3500_48T,
       "s2500-24P": s2500_24P,
       "s2500-24T": s2500_24T,
       "s2500-48P": s2500_48P,
       "s2500-48T": s2500_48T,
       "a7210": a7210,
       "a7220": a7220,
       "a7240": a7240,
       "s3500-24F": s3500_24F,
       "aUndefined": aUndefined,
       "apProducts": apProducts,
       "a50": a50,
       "a52": a52,
       "ap60": ap60,
       "ap61": ap61,
       "ap70": ap70,
       "walljackAp61": walljackAp61,
       "a2E": a2E,
       "ap1200": ap1200,
       "ap80s": ap80s,
       "ap80m": ap80m,
       "wg102": wg102,
       "ap40": ap40,
       "ap41": ap41,
       "ap65": ap65,
       "apMw1700": apMw1700,
       "apDuowj": apDuowj,
       "apDuo": apDuo,
       "ap80MB": ap80MB,
       "ap80SB": ap80SB,
       "ap85": ap85,
       "ap124": ap124,
       "ap125": ap125,
       "ap120": ap120,
       "ap121": ap121,
       "ap1250": ap1250,
       "ap120abg": ap120abg,
       "ap121abg": ap121abg,
       "ap124abg": ap124abg,
       "ap125abg": ap125abg,
       "rap5wn": rap5wn,
       "rap5": rap5,
       "rap2wg": rap2wg,
       "reserved4": reserved4,
       "ap105": ap105,
       "ap65wb": ap65wb,
       "ap651": ap651,
       "reserved6": reserved6,
       "ap60p": ap60p,
       "reserved7": reserved7,
       "ap92": ap92,
       "ap93": ap93,
       "ap68": ap68,
       "ap68p": ap68p,
       "ap175p": ap175p,
       "ap175ac": ap175ac,
       "ap175dc": ap175dc,
       "ap134": ap134,
       "ap135": ap135,
       "reserved8": reserved8,
       "ap93h": ap93h,
       "iap23": iap23,
       "iap23p": iap23p,
       "ap104": ap104,
       "apUndefined": apUndefined,
       "emsProducts": emsProducts,
       "partnerProducts": partnerProducts,
       "ecsE50": ecsE50,
       "ecsE100C": ecsE100C,
       "ecsE100A": ecsE100A,
       "ecsENSM": ecsENSM,
       "amigopodProducts": amigopodProducts,
       "arubaEnterpriseMibModules": arubaEnterpriseMibModules,
       "common": common,
       "arubaMIBModules": arubaMIBModules,
       "switch": switch,
       "wlsxEnterpriseMibModules": wlsxEnterpriseMibModules,
       "arubaAp": arubaAp,
       "wlsrEnterpriseMibModules": wlsrEnterpriseMibModules,
       "wlsrOutDoorApMibModules": wlsrOutDoorApMibModules,
       "arubaEcs": arubaEcs,
       "arubaMgmt": arubaMgmt}
)
