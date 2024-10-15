# SNMP MIB module (TELTREND-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TELTREND-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:07 2024
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

teltrend = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 293)
)
teltrend.setRevisions(
        ("1970-01-01 00:00",
         "1970-01-01 00:00",
         "1970-01-01 00:00",
         "1970-01-01 00:00",
         "1970-01-01 00:00",
         "1970-01-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class InterfaceIndexOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1)
)
_NiqRouter_ObjectIdentity = ObjectIdentity
niqRouter = _NiqRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1)
)
_Niq_4820_2wan_ObjectIdentity = ObjectIdentity
niq_4820_2wan = _Niq_4820_2wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 1)
)
_Niq_2830_bri_ObjectIdentity = ObjectIdentity
niq_2830_bri = _Niq_2830_bri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 9)
)
_Niq_2820_2wan_ObjectIdentity = ObjectIdentity
niq_2820_2wan = _Niq_2820_2wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 10)
)
_Niq_2810_1wan_ObjectIdentity = ObjectIdentity
niq_2810_1wan = _Niq_2810_1wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 11)
)
_Niq_3830_bri_ObjectIdentity = ObjectIdentity
niq_3830_bri = _Niq_3830_bri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 12)
)
_Niq_3820_2wan_ObjectIdentity = ObjectIdentity
niq_3820_2wan = _Niq_3820_2wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 13)
)
_Niq_3810_1wan_ObjectIdentity = ObjectIdentity
niq_3810_1wan = _Niq_3810_1wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 14)
)
_Niq_1870_bri_wan_ObjectIdentity = ObjectIdentity
niq_1870_bri_wan = _Niq_1870_bri_wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 15)
)
_Niq_1830_bri_ObjectIdentity = ObjectIdentity
niq_1830_bri = _Niq_1830_bri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 16)
)
_Niq_1810_wan_ObjectIdentity = ObjectIdentity
niq_1810_wan = _Niq_1810_wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 18)
)
_Niq_1100_bri_wan_ObjectIdentity = ObjectIdentity
niq_1100_bri_wan = _Niq_1100_bri_wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 35)
)
_Niq_1100_bri_bay_ObjectIdentity = ObjectIdentity
niq_1100_bri_bay = _Niq_1100_bri_bay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 36)
)
_Niq_1100_wan_bay_ObjectIdentity = ObjectIdentity
niq_1100_wan_bay = _Niq_1100_wan_bay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 37)
)
_Niq_1100_bay_bay_ObjectIdentity = ObjectIdentity
niq_1100_bay_bay = _Niq_1100_bay_bay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 38)
)
_Niq_1900_bay_bay_ObjectIdentity = ObjectIdentity
niq_1900_bay_bay = _Niq_1900_bay_bay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 47)
)
_Niq_3100_ObjectIdentity = ObjectIdentity
niq_3100 = _Niq_3100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 48)
)
_Niq_800_2_pots_ObjectIdentity = ObjectIdentity
niq_800_2_pots = _Niq_800_2_pots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 49)
)
_Niq_800_no_pots_ObjectIdentity = ObjectIdentity
niq_800_no_pots = _Niq_800_no_pots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 52)
)
_Niq_800_4_pots_ObjectIdentity = ObjectIdentity
niq_800_4_pots = _Niq_800_4_pots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 53)
)
_Niq_5200_ObjectIdentity = ObjectIdentity
niq_5200 = _Niq_5200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 54)
)
_Niq_800u_no_pots_ObjectIdentity = ObjectIdentity
niq_800u_no_pots = _Niq_800u_no_pots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 55)
)
_Niq_800u_2_pots_ObjectIdentity = ObjectIdentity
niq_800u_2_pots = _Niq_800u_2_pots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 56)
)
_Niq_800u_4_pots_ObjectIdentity = ObjectIdentity
niq_800u_4_pots = _Niq_800u_4_pots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 57)
)
_Niq_800_syn_ObjectIdentity = ObjectIdentity
niq_800_syn = _Niq_800_syn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 58)
)
_Niq_nac_wan_ObjectIdentity = ObjectIdentity
niq_nac_wan = _Niq_nac_wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 60)
)
_Niq_pr2000_ObjectIdentity = ObjectIdentity
niq_pr2000 = _Niq_pr2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 62)
)
_Niq_pr2000_50_ObjectIdentity = ObjectIdentity
niq_pr2000_50 = _Niq_pr2000_50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 63)
)
_Niq_pr3000_ObjectIdentity = ObjectIdentity
niq_pr3000 = _Niq_pr3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 64)
)
_Niq_alpha_ObjectIdentity = ObjectIdentity
niq_alpha = _Niq_alpha_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 65)
)
_Niq_nac_g703_ObjectIdentity = ObjectIdentity
niq_nac_g703 = _Niq_nac_g703_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 66)
)
_Niq_800_syn_bri_ObjectIdentity = ObjectIdentity
niq_800_syn_bri = _Niq_800_syn_bri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 70)
)
_Niq_800_2_eth_syn_ObjectIdentity = ObjectIdentity
niq_800_2_eth_syn = _Niq_800_2_eth_syn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 71)
)
_Niq_800_pri_ObjectIdentity = ObjectIdentity
niq_800_pri = _Niq_800_pri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 72)
)
_Niq_800_g703_ObjectIdentity = ObjectIdentity
niq_800_g703 = _Niq_800_g703_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 73)
)
_Niq_nac_60_ObjectIdentity = ObjectIdentity
niq_nac_60 = _Niq_nac_60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 74)
)
_Niq_800_syn_briu_ObjectIdentity = ObjectIdentity
niq_800_syn_briu = _Niq_800_syn_briu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 1, 1, 75)
)
_Niq_ObjectIdentity = ObjectIdentity
niq = _Niq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2)
)
_Objects_ObjectIdentity = ObjectIdentity
objects = _Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1)
)
_Boards_ObjectIdentity = ObjectIdentity
boards = _Boards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1)
)
_Ppr_mpr_base_ObjectIdentity = ObjectIdentity
ppr_mpr_base = _Ppr_mpr_base_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 1)
)
_Ppr_mpr_sync4_ObjectIdentity = ObjectIdentity
ppr_mpr_sync4 = _Ppr_mpr_sync4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 2)
)
_Ppr_mpr_lan4_ObjectIdentity = ObjectIdentity
ppr_mpr_lan4 = _Ppr_mpr_lan4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 3)
)
_Ppr_mpr_async12_ObjectIdentity = ObjectIdentity
ppr_mpr_async12 = _Ppr_mpr_async12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 4)
)
_Ppr_mpr_bri1_ObjectIdentity = ObjectIdentity
ppr_mpr_bri1 = _Ppr_mpr_bri1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 5)
)
_Ppr_mpr_async16_ObjectIdentity = ObjectIdentity
ppr_mpr_async16 = _Ppr_mpr_async16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 6)
)
_Ppr_mpr_comp_ObjectIdentity = ObjectIdentity
ppr_mpr_comp = _Ppr_mpr_comp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 7)
)
_Ppr_mpr_pri2_ObjectIdentity = ObjectIdentity
ppr_mpr_pri2 = _Ppr_mpr_pri2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 8)
)
_Ppr_2830_bri_ObjectIdentity = ObjectIdentity
ppr_2830_bri = _Ppr_2830_bri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 9)
)
_Ppr_2820_wan_ww_ObjectIdentity = ObjectIdentity
ppr_2820_wan_ww = _Ppr_2820_wan_ww_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 10)
)
_Ppr_2810_wan_w_ObjectIdentity = ObjectIdentity
ppr_2810_wan_w = _Ppr_2810_wan_w_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 11)
)
_Ppr_3830_bri_ObjectIdentity = ObjectIdentity
ppr_3830_bri = _Ppr_3830_bri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 12)
)
_Ppr_3820_wan_ww_ObjectIdentity = ObjectIdentity
ppr_3820_wan_ww = _Ppr_3820_wan_ww_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 13)
)
_Ppr_3810_wan_w_ObjectIdentity = ObjectIdentity
ppr_3810_wan_w = _Ppr_3810_wan_w_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 14)
)
_Ppr_1870_ext_bri_wan_ObjectIdentity = ObjectIdentity
ppr_1870_ext_bri_wan = _Ppr_1870_ext_bri_wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 15)
)
_Ppr_1830_ext_bri_ObjectIdentity = ObjectIdentity
ppr_1830_ext_bri = _Ppr_1830_ext_bri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 16)
)
_Ppr_1850_pc_bri_ObjectIdentity = ObjectIdentity
ppr_1850_pc_bri = _Ppr_1850_pc_bri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 17)
)
_Ppr_1810_ext_wan_ObjectIdentity = ObjectIdentity
ppr_1810_ext_wan = _Ppr_1810_ext_wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 18)
)
_Ppr_1810_pc_wan_ObjectIdentity = ObjectIdentity
ppr_1810_pc_wan = _Ppr_1810_pc_wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 19)
)
_Ppr_mpr_sync2_ObjectIdentity = ObjectIdentity
ppr_mpr_sync2 = _Ppr_mpr_sync2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 20)
)
_Ppr_mpr_pri1_ObjectIdentity = ObjectIdentity
ppr_mpr_pri1 = _Ppr_mpr_pri1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 21)
)
_Ppr_mpr_bri2_ObjectIdentity = ObjectIdentity
ppr_mpr_bri2 = _Ppr_mpr_bri2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 22)
)
_Ppr_mpr_bri4_ObjectIdentity = ObjectIdentity
ppr_mpr_bri4 = _Ppr_mpr_bri4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 23)
)
_Ppr_mpr_enco_us_ObjectIdentity = ObjectIdentity
ppr_mpr_enco_us = _Ppr_mpr_enco_us_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 24)
)
_Ppr_mpr_enco_hs_ObjectIdentity = ObjectIdentity
ppr_mpr_enco_hs = _Ppr_mpr_enco_hs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 25)
)
_Ppr_mpr_cryp_us_ObjectIdentity = ObjectIdentity
ppr_mpr_cryp_us = _Ppr_mpr_cryp_us_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 26)
)
_Ppr_mpr_cryp_hs_ObjectIdentity = ObjectIdentity
ppr_mpr_cryp_hs = _Ppr_mpr_cryp_hs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 27)
)
_Ppr_mpr_comp_2_ObjectIdentity = ObjectIdentity
ppr_mpr_comp_2 = _Ppr_mpr_comp_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 28)
)
_Ppr_mpr_gio_ObjectIdentity = ObjectIdentity
ppr_mpr_gio = _Ppr_mpr_gio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 29)
)
_Ppr_iom_asyn4_ObjectIdentity = ObjectIdentity
ppr_iom_asyn4 = _Ppr_iom_asyn4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 30)
)
_Ppr_iom_bri1_ObjectIdentity = ObjectIdentity
ppr_iom_bri1 = _Ppr_iom_bri1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 31)
)
_Ppr_iom_eth1_ObjectIdentity = ObjectIdentity
ppr_iom_eth1 = _Ppr_iom_eth1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 32)
)
_Ppr_iom_pri1_ObjectIdentity = ObjectIdentity
ppr_iom_pri1 = _Ppr_iom_pri1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 33)
)
_Ppr_iom_syn2_ObjectIdentity = ObjectIdentity
ppr_iom_syn2 = _Ppr_iom_syn2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 34)
)
_Ppr_1000_bri_wan_ObjectIdentity = ObjectIdentity
ppr_1000_bri_wan = _Ppr_1000_bri_wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 35)
)
_Ppr_1000_bri_bay_ObjectIdentity = ObjectIdentity
ppr_1000_bri_bay = _Ppr_1000_bri_bay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 36)
)
_Ppr_1000_wan_bay_ObjectIdentity = ObjectIdentity
ppr_1000_wan_bay = _Ppr_1000_wan_bay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 37)
)
_Ppr_1000_bay_bay_ObjectIdentity = ObjectIdentity
ppr_1000_bay_bay = _Ppr_1000_bay_bay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 38)
)
_Ppr_icm_syn1_ObjectIdentity = ObjectIdentity
ppr_icm_syn1 = _Ppr_icm_syn1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 39)
)
_Ppr_icm_bri1_ObjectIdentity = ObjectIdentity
ppr_icm_bri1 = _Ppr_icm_bri1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 40)
)
_Ppr_icm_eth1_ObjectIdentity = ObjectIdentity
ppr_icm_eth1 = _Ppr_icm_eth1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 41)
)
_Ppr_icm_pots1_ObjectIdentity = ObjectIdentity
ppr_icm_pots1 = _Ppr_icm_pots1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 42)
)
_Ppr_icm_pots2_ObjectIdentity = ObjectIdentity
ppr_icm_pots2 = _Ppr_icm_pots2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 43)
)
_Ppr_icm_pots4_ObjectIdentity = ObjectIdentity
ppr_icm_pots4 = _Ppr_icm_pots4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 44)
)
_Ppr_icm_pri1_ObjectIdentity = ObjectIdentity
ppr_icm_pri1 = _Ppr_icm_pri1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 45)
)
_Ppr_icm_asyn4_ObjectIdentity = ObjectIdentity
ppr_icm_asyn4 = _Ppr_icm_asyn4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 46)
)
_Ppr_1900_bay_bay_ObjectIdentity = ObjectIdentity
ppr_1900_bay_bay = _Ppr_1900_bay_bay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 47)
)
_Ppr_3100_ObjectIdentity = ObjectIdentity
ppr_3100 = _Ppr_3100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 48)
)
_Ppr_840_ObjectIdentity = ObjectIdentity
ppr_840 = _Ppr_840_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 49)
)
_Ppr_iom_g703tdm_ObjectIdentity = ObjectIdentity
ppr_iom_g703tdm = _Ppr_iom_g703tdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 50)
)
_Ppr_icm_g703tdm_ObjectIdentity = ObjectIdentity
ppr_icm_g703tdm = _Ppr_icm_g703tdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 51)
)
_Ppr_820_ObjectIdentity = ObjectIdentity
ppr_820 = _Ppr_820_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 52)
)
_Ppr_860_ObjectIdentity = ObjectIdentity
ppr_860 = _Ppr_860_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 53)
)
_Ppr_5200_ObjectIdentity = ObjectIdentity
ppr_5200 = _Ppr_5200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 54)
)
_Ppr_820U_ObjectIdentity = ObjectIdentity
ppr_820U = _Ppr_820U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 55)
)
_Ppr_840U_ObjectIdentity = ObjectIdentity
ppr_840U = _Ppr_840U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 56)
)
_Ppr_860U_ObjectIdentity = ObjectIdentity
ppr_860U = _Ppr_860U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 57)
)
_Ppr_800SYN_ObjectIdentity = ObjectIdentity
ppr_800SYN = _Ppr_800SYN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 58)
)
_Ppr_ICM_BRI1U_ObjectIdentity = ObjectIdentity
ppr_ICM_BRI1U = _Ppr_ICM_BRI1U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 59)
)
_Ppr_NAS_ObjectIdentity = ObjectIdentity
ppr_NAS = _Ppr_NAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 60)
)
_Ppr_GIO_3100_ObjectIdentity = ObjectIdentity
ppr_GIO_3100 = _Ppr_GIO_3100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 61)
)
_Ppr_PR2000_ObjectIdentity = ObjectIdentity
ppr_PR2000 = _Ppr_PR2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 62)
)
_Ppr_beta_cpu_ObjectIdentity = ObjectIdentity
ppr_beta_cpu = _Ppr_beta_cpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 63)
)
_Ppr_PR3000_ObjectIdentity = ObjectIdentity
ppr_PR3000 = _Ppr_PR3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 64)
)
_Ppr_alpha_cpu_ObjectIdentity = ObjectIdentity
ppr_alpha_cpu = _Ppr_alpha_cpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 65)
)
_Ppr_NAC_G703_ObjectIdentity = ObjectIdentity
ppr_NAC_G703 = _Ppr_NAC_G703_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 66)
)
_Ppr_EMAC_ObjectIdentity = ObjectIdentity
ppr_EMAC = _Ppr_EMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 67)
)
_Ppr_CMAC_ObjectIdentity = ObjectIdentity
ppr_CMAC = _Ppr_CMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 68)
)
_Ppr_CEMAC_ObjectIdentity = ObjectIdentity
ppr_CEMAC = _Ppr_CEMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 69)
)
_Ppr_800DUAL_ObjectIdentity = ObjectIdentity
ppr_800DUAL = _Ppr_800DUAL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 70)
)
_Ppr_800SYNDUALETH_ObjectIdentity = ObjectIdentity
ppr_800SYNDUALETH = _Ppr_800SYNDUALETH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 71)
)
_Ppr_800PRI_ObjectIdentity = ObjectIdentity
ppr_800PRI = _Ppr_800PRI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 72)
)
_Ppr_800PRITDMONLY_ObjectIdentity = ObjectIdentity
ppr_800PRITDMONLY = _Ppr_800PRITDMONLY_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 73)
)
_Ppr_NAC_60_ObjectIdentity = ObjectIdentity
ppr_NAC_60 = _Ppr_NAC_60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 74)
)
_Ppr_800DUAL_U_ObjectIdentity = ObjectIdentity
ppr_800DUAL_U = _Ppr_800DUAL_U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 75)
)
_Ppr_icm_e1t1_ObjectIdentity = ObjectIdentity
ppr_icm_e1t1 = _Ppr_icm_e1t1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 76)
)
_Ppr_icm_e1t1tdmonly_ObjectIdentity = ObjectIdentity
ppr_icm_e1t1tdmonly = _Ppr_icm_e1t1tdmonly_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 1, 77)
)
_Release_ObjectIdentity = ObjectIdentity
release = _Release_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 2)
)
_Iftypes_ObjectIdentity = ObjectIdentity
iftypes = _Iftypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 3)
)
_Iface_eth_ObjectIdentity = ObjectIdentity
iface_eth = _Iface_eth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 3, 1)
)
_Iface_syn_ObjectIdentity = ObjectIdentity
iface_syn = _Iface_syn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 3, 2)
)
_Iface_asyn_ObjectIdentity = ObjectIdentity
iface_asyn = _Iface_asyn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 3, 3)
)
_Iface_bri_ObjectIdentity = ObjectIdentity
iface_bri = _Iface_bri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 3, 4)
)
_Iface_pri_ObjectIdentity = ObjectIdentity
iface_pri = _Iface_pri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 3, 5)
)
_Iface_pots_ObjectIdentity = ObjectIdentity
iface_pots = _Iface_pots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 3, 6)
)
_Chips_ObjectIdentity = ObjectIdentity
chips = _Chips_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 4)
)
_Chip_68020_cpu_ObjectIdentity = ObjectIdentity
chip_68020_cpu = _Chip_68020_cpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 4, 1)
)
_Chip_68340_cpu_ObjectIdentity = ObjectIdentity
chip_68340_cpu = _Chip_68340_cpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 4, 2)
)
_Chip_68302_cpu_ObjectIdentity = ObjectIdentity
chip_68302_cpu = _Chip_68302_cpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 4, 3)
)
_Chip_68360_cpu_ObjectIdentity = ObjectIdentity
chip_68360_cpu = _Chip_68360_cpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 4, 4)
)
_Chip_rtc1_ObjectIdentity = ObjectIdentity
chip_rtc1 = _Chip_rtc1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 4, 21)
)
_Chip_rtc2_ObjectIdentity = ObjectIdentity
chip_rtc2 = _Chip_rtc2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 4, 22)
)
_Chip_rtc3_ObjectIdentity = ObjectIdentity
chip_rtc3 = _Chip_rtc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 4, 23)
)
_Chip_rtc4_ObjectIdentity = ObjectIdentity
chip_rtc4 = _Chip_rtc4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 4, 24)
)
_Chip_ram_1mb_ObjectIdentity = ObjectIdentity
chip_ram_1mb = _Chip_ram_1mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 4, 31)
)
_Chip_ram_2mb_ObjectIdentity = ObjectIdentity
chip_ram_2mb = _Chip_ram_2mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 4, 32)
)
_Chip_ram_3mb_ObjectIdentity = ObjectIdentity
chip_ram_3mb = _Chip_ram_3mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 4, 33)
)
_Chip_ram_4mb_ObjectIdentity = ObjectIdentity
chip_ram_4mb = _Chip_ram_4mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 4, 34)
)
_Chip_ram_6mb_ObjectIdentity = ObjectIdentity
chip_ram_6mb = _Chip_ram_6mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 4, 36)
)
_Chip_ram_8mb_ObjectIdentity = ObjectIdentity
chip_ram_8mb = _Chip_ram_8mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 4, 38)
)
_Chip_ram_12mb_ObjectIdentity = ObjectIdentity
chip_ram_12mb = _Chip_ram_12mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 4, 42)
)
_Chip_ram_16mb_ObjectIdentity = ObjectIdentity
chip_ram_16mb = _Chip_ram_16mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 4, 46)
)
_Chip_ram_20mb_ObjectIdentity = ObjectIdentity
chip_ram_20mb = _Chip_ram_20mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 4, 50)
)
_Chip_ram_32mb_ObjectIdentity = ObjectIdentity
chip_ram_32mb = _Chip_ram_32mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 4, 62)
)
_Chip_flash_1mb_ObjectIdentity = ObjectIdentity
chip_flash_1mb = _Chip_flash_1mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 4, 71)
)
_Chip_flash_2mb_ObjectIdentity = ObjectIdentity
chip_flash_2mb = _Chip_flash_2mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 4, 72)
)
_Chip_flash_3mb_ObjectIdentity = ObjectIdentity
chip_flash_3mb = _Chip_flash_3mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 4, 73)
)
_Chip_flash_4mb_ObjectIdentity = ObjectIdentity
chip_flash_4mb = _Chip_flash_4mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 4, 74)
)
_Chip_flash_6mb_ObjectIdentity = ObjectIdentity
chip_flash_6mb = _Chip_flash_6mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 4, 76)
)
_Chip_flash_8mb_ObjectIdentity = ObjectIdentity
chip_flash_8mb = _Chip_flash_8mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 4, 78)
)
_Chip_pem_ObjectIdentity = ObjectIdentity
chip_pem = _Chip_pem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 1, 4, 120)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 2)
)
_Sysinfo_ObjectIdentity = ObjectIdentity
sysinfo = _Sysinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 3)
)
_Modules_ObjectIdentity = ObjectIdentity
modules = _Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 4)
)
_Cc_ObjectIdentity = ObjectIdentity
cc = _Cc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37)
)
_CcDetailsTable_Object = MibTable
ccDetailsTable = _CcDetailsTable_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1)
)
if mibBuilder.loadTexts:
    ccDetailsTable.setStatus("mandatory")
_CcDetailsEntry_Object = MibTableRow
ccDetailsEntry = _CcDetailsEntry_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1)
)
ccDetailsEntry.setIndexNames(
    (0, "TELTREND-MIB", "ccDetailsIndex"),
)
if mibBuilder.loadTexts:
    ccDetailsEntry.setStatus("mandatory")


class _CcDetailsIndex_Type(Integer32):
    """Custom type ccDetailsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CcDetailsIndex_Type.__name__ = "Integer32"
_CcDetailsIndex_Object = MibTableColumn
ccDetailsIndex = _CcDetailsIndex_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 1),
    _CcDetailsIndex_Type()
)
ccDetailsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDetailsIndex.setStatus("mandatory")


class _CcDetailsName_Type(OctetString):
    """Custom type ccDetailsName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CcDetailsName_Type.__name__ = "OctetString"
_CcDetailsName_Object = MibTableColumn
ccDetailsName = _CcDetailsName_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 2),
    _CcDetailsName_Type()
)
ccDetailsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsName.setStatus("mandatory")


class _CcDetailsRemoteName_Type(OctetString):
    """Custom type ccDetailsRemoteName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CcDetailsRemoteName_Type.__name__ = "OctetString"
_CcDetailsRemoteName_Object = MibTableColumn
ccDetailsRemoteName = _CcDetailsRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 3),
    _CcDetailsRemoteName_Type()
)
ccDetailsRemoteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsRemoteName.setStatus("mandatory")


class _CcDetailsCalledNumber_Type(OctetString):
    """Custom type ccDetailsCalledNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CcDetailsCalledNumber_Type.__name__ = "OctetString"
_CcDetailsCalledNumber_Object = MibTableColumn
ccDetailsCalledNumber = _CcDetailsCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 4),
    _CcDetailsCalledNumber_Type()
)
ccDetailsCalledNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsCalledNumber.setStatus("mandatory")


class _CcDetailsCallingNumber_Type(OctetString):
    """Custom type ccDetailsCallingNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CcDetailsCallingNumber_Type.__name__ = "OctetString"
_CcDetailsCallingNumber_Object = MibTableColumn
ccDetailsCallingNumber = _CcDetailsCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 5),
    _CcDetailsCallingNumber_Type()
)
ccDetailsCallingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsCallingNumber.setStatus("mandatory")


class _CcDetailsAlternateNumber_Type(OctetString):
    """Custom type ccDetailsAlternateNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CcDetailsAlternateNumber_Type.__name__ = "OctetString"
_CcDetailsAlternateNumber_Object = MibTableColumn
ccDetailsAlternateNumber = _CcDetailsAlternateNumber_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 6),
    _CcDetailsAlternateNumber_Type()
)
ccDetailsAlternateNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsAlternateNumber.setStatus("mandatory")


class _CcDetailsEnabled_Type(Integer32):
    """Custom type ccDetailsEnabled based on Integer32"""
    defaultValue = 2

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


_CcDetailsEnabled_Type.__name__ = "Integer32"
_CcDetailsEnabled_Object = MibTableColumn
ccDetailsEnabled = _CcDetailsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 7),
    _CcDetailsEnabled_Type()
)
ccDetailsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsEnabled.setStatus("mandatory")


class _CcDetailsDirection_Type(Integer32):
    """Custom type ccDetailsDirection based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("in-only", 1),
          ("out-only", 2))
    )


_CcDetailsDirection_Type.__name__ = "Integer32"
_CcDetailsDirection_Object = MibTableColumn
ccDetailsDirection = _CcDetailsDirection_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 8),
    _CcDetailsDirection_Type()
)
ccDetailsDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsDirection.setStatus("mandatory")


class _CcDetailsPrecedence_Type(Integer32):
    """Custom type ccDetailsPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_CcDetailsPrecedence_Type.__name__ = "Integer32"
_CcDetailsPrecedence_Object = MibTableColumn
ccDetailsPrecedence = _CcDetailsPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 9),
    _CcDetailsPrecedence_Type()
)
ccDetailsPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsPrecedence.setStatus("mandatory")


class _CcDetailsHoldupTime_Type(Integer32):
    """Custom type ccDetailsHoldupTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7200),
    )


_CcDetailsHoldupTime_Type.__name__ = "Integer32"
_CcDetailsHoldupTime_Object = MibTableColumn
ccDetailsHoldupTime = _CcDetailsHoldupTime_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 10),
    _CcDetailsHoldupTime_Type()
)
ccDetailsHoldupTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsHoldupTime.setStatus("mandatory")


class _CcDetailsPreferredIfIndex_Type(InterfaceIndexOrZero):
    """Custom type ccDetailsPreferredIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_CcDetailsPreferredIfIndex_Object = MibTableColumn
ccDetailsPreferredIfIndex = _CcDetailsPreferredIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 11),
    _CcDetailsPreferredIfIndex_Type()
)
ccDetailsPreferredIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsPreferredIfIndex.setStatus("mandatory")


class _CcDetailsRequiredIfIndex_Type(InterfaceIndexOrZero):
    """Custom type ccDetailsRequiredIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_CcDetailsRequiredIfIndex_Object = MibTableColumn
ccDetailsRequiredIfIndex = _CcDetailsRequiredIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 12),
    _CcDetailsRequiredIfIndex_Type()
)
ccDetailsRequiredIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsRequiredIfIndex.setStatus("mandatory")


class _CcDetailsPriority_Type(Integer32):
    """Custom type ccDetailsPriority based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_CcDetailsPriority_Type.__name__ = "Integer32"
_CcDetailsPriority_Object = MibTableColumn
ccDetailsPriority = _CcDetailsPriority_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 13),
    _CcDetailsPriority_Type()
)
ccDetailsPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsPriority.setStatus("mandatory")


class _CcDetailsRetryT1_Type(Integer32):
    """Custom type ccDetailsRetryT1 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 120),
    )


_CcDetailsRetryT1_Type.__name__ = "Integer32"
_CcDetailsRetryT1_Object = MibTableColumn
ccDetailsRetryT1 = _CcDetailsRetryT1_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 14),
    _CcDetailsRetryT1_Type()
)
ccDetailsRetryT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsRetryT1.setStatus("mandatory")


class _CcDetailsRetryN1_Type(Integer32):
    """Custom type ccDetailsRetryN1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CcDetailsRetryN1_Type.__name__ = "Integer32"
_CcDetailsRetryN1_Object = MibTableColumn
ccDetailsRetryN1 = _CcDetailsRetryN1_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 15),
    _CcDetailsRetryN1_Type()
)
ccDetailsRetryN1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsRetryN1.setStatus("mandatory")


class _CcDetailsRetryT2_Type(Integer32):
    """Custom type ccDetailsRetryT2 based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1200),
    )


_CcDetailsRetryT2_Type.__name__ = "Integer32"
_CcDetailsRetryT2_Object = MibTableColumn
ccDetailsRetryT2 = _CcDetailsRetryT2_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 16),
    _CcDetailsRetryT2_Type()
)
ccDetailsRetryT2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsRetryT2.setStatus("mandatory")


class _CcDetailsRetryN2_Type(Integer32):
    """Custom type ccDetailsRetryN2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_CcDetailsRetryN2_Type.__name__ = "Integer32"
_CcDetailsRetryN2_Object = MibTableColumn
ccDetailsRetryN2 = _CcDetailsRetryN2_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 17),
    _CcDetailsRetryN2_Type()
)
ccDetailsRetryN2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsRetryN2.setStatus("mandatory")


class _CcDetailsKeepup_Type(Integer32):
    """Custom type ccDetailsKeepup based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CcDetailsKeepup_Type.__name__ = "Integer32"
_CcDetailsKeepup_Object = MibTableColumn
ccDetailsKeepup = _CcDetailsKeepup_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 18),
    _CcDetailsKeepup_Type()
)
ccDetailsKeepup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsKeepup.setStatus("mandatory")


class _CcDetailsOutSetupCli_Type(Integer32):
    """Custom type ccDetailsOutSetupCli based on Integer32"""
    defaultValue = 1

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
        *(("calling", 2),
          ("interface", 3),
          ("nonumber", 4),
          ("off", 1))
    )


_CcDetailsOutSetupCli_Type.__name__ = "Integer32"
_CcDetailsOutSetupCli_Object = MibTableColumn
ccDetailsOutSetupCli = _CcDetailsOutSetupCli_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 19),
    _CcDetailsOutSetupCli_Type()
)
ccDetailsOutSetupCli.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsOutSetupCli.setStatus("mandatory")


class _CcDetailsOutSetupUser_Type(Integer32):
    """Custom type ccDetailsOutSetupUser based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("off", 1),
          ("remote", 3))
    )


_CcDetailsOutSetupUser_Type.__name__ = "Integer32"
_CcDetailsOutSetupUser_Object = MibTableColumn
ccDetailsOutSetupUser = _CcDetailsOutSetupUser_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 20),
    _CcDetailsOutSetupUser_Type()
)
ccDetailsOutSetupUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsOutSetupUser.setStatus("mandatory")


class _CcDetailsOutSetupCalledSub_Type(Integer32):
    """Custom type ccDetailsOutSetupCalledSub based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("off", 1),
          ("remote", 3))
    )


_CcDetailsOutSetupCalledSub_Type.__name__ = "Integer32"
_CcDetailsOutSetupCalledSub_Object = MibTableColumn
ccDetailsOutSetupCalledSub = _CcDetailsOutSetupCalledSub_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 21),
    _CcDetailsOutSetupCalledSub_Type()
)
ccDetailsOutSetupCalledSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsOutSetupCalledSub.setStatus("mandatory")


class _CcDetailsOutSubaddress_Type(OctetString):
    """Custom type ccDetailsOutSubaddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CcDetailsOutSubaddress_Type.__name__ = "OctetString"
_CcDetailsOutSubaddress_Object = MibTableColumn
ccDetailsOutSubaddress = _CcDetailsOutSubaddress_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 22),
    _CcDetailsOutSubaddress_Type()
)
ccDetailsOutSubaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsOutSubaddress.setStatus("mandatory")


class _CcDetailsCallback_Type(Integer32):
    """Custom type ccDetailsCallback based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CcDetailsCallback_Type.__name__ = "Integer32"
_CcDetailsCallback_Object = MibTableColumn
ccDetailsCallback = _CcDetailsCallback_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 23),
    _CcDetailsCallback_Type()
)
ccDetailsCallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsCallback.setStatus("mandatory")


class _CcDetailsCallbackDelay_Type(Integer32):
    """Custom type ccDetailsCallbackDelay based on Integer32"""
    defaultValue = 41

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CcDetailsCallbackDelay_Type.__name__ = "Integer32"
_CcDetailsCallbackDelay_Object = MibTableColumn
ccDetailsCallbackDelay = _CcDetailsCallbackDelay_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 24),
    _CcDetailsCallbackDelay_Type()
)
ccDetailsCallbackDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsCallbackDelay.setStatus("mandatory")


class _CcDetailsInSetupCalledSubSearch_Type(Integer32):
    """Custom type ccDetailsInSetupCalledSubSearch based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("off", 1),
          ("remote", 3))
    )


_CcDetailsInSetupCalledSubSearch_Type.__name__ = "Integer32"
_CcDetailsInSetupCalledSubSearch_Object = MibTableColumn
ccDetailsInSetupCalledSubSearch = _CcDetailsInSetupCalledSubSearch_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 25),
    _CcDetailsInSetupCalledSubSearch_Type()
)
ccDetailsInSetupCalledSubSearch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsInSetupCalledSubSearch.setStatus("mandatory")


class _CcDetailsInSetupUserSearch_Type(Integer32):
    """Custom type ccDetailsInSetupUserSearch based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("off", 1),
          ("remote", 3))
    )


_CcDetailsInSetupUserSearch_Type.__name__ = "Integer32"
_CcDetailsInSetupUserSearch_Object = MibTableColumn
ccDetailsInSetupUserSearch = _CcDetailsInSetupUserSearch_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 26),
    _CcDetailsInSetupUserSearch_Type()
)
ccDetailsInSetupUserSearch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsInSetupUserSearch.setStatus("mandatory")


class _CcDetailsInSetupCliSearch_Type(Integer32):
    """Custom type ccDetailsInSetupCliSearch based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("list", 3),
          ("off", 1),
          ("on", 2))
    )


_CcDetailsInSetupCliSearch_Type.__name__ = "Integer32"
_CcDetailsInSetupCliSearch_Object = MibTableColumn
ccDetailsInSetupCliSearch = _CcDetailsInSetupCliSearch_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 27),
    _CcDetailsInSetupCliSearch_Type()
)
ccDetailsInSetupCliSearch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsInSetupCliSearch.setStatus("mandatory")


class _CcDetailsInSetupCliSearchList_Type(Integer32):
    """Custom type ccDetailsInSetupCliSearchList based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CcDetailsInSetupCliSearchList_Type.__name__ = "Integer32"
_CcDetailsInSetupCliSearchList_Object = MibTableColumn
ccDetailsInSetupCliSearchList = _CcDetailsInSetupCliSearchList_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 28),
    _CcDetailsInSetupCliSearchList_Type()
)
ccDetailsInSetupCliSearchList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsInSetupCliSearchList.setStatus("mandatory")


class _CcDetailsInAnyFlag_Type(Integer32):
    """Custom type ccDetailsInAnyFlag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CcDetailsInAnyFlag_Type.__name__ = "Integer32"
_CcDetailsInAnyFlag_Object = MibTableColumn
ccDetailsInAnyFlag = _CcDetailsInAnyFlag_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 29),
    _CcDetailsInAnyFlag_Type()
)
ccDetailsInAnyFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsInAnyFlag.setStatus("mandatory")


class _CcDetailsInSetupCalledSubCheck_Type(Integer32):
    """Custom type ccDetailsInSetupCalledSubCheck based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("off", 1),
          ("remote", 3))
    )


_CcDetailsInSetupCalledSubCheck_Type.__name__ = "Integer32"
_CcDetailsInSetupCalledSubCheck_Object = MibTableColumn
ccDetailsInSetupCalledSubCheck = _CcDetailsInSetupCalledSubCheck_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 30),
    _CcDetailsInSetupCalledSubCheck_Type()
)
ccDetailsInSetupCalledSubCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsInSetupCalledSubCheck.setStatus("mandatory")


class _CcDetailsInSetupUserCheck_Type(Integer32):
    """Custom type ccDetailsInSetupUserCheck based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("off", 1),
          ("remote", 3))
    )


_CcDetailsInSetupUserCheck_Type.__name__ = "Integer32"
_CcDetailsInSetupUserCheck_Object = MibTableColumn
ccDetailsInSetupUserCheck = _CcDetailsInSetupUserCheck_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 31),
    _CcDetailsInSetupUserCheck_Type()
)
ccDetailsInSetupUserCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsInSetupUserCheck.setStatus("mandatory")


class _CcDetailsInSetupCliCheck_Type(Integer32):
    """Custom type ccDetailsInSetupCliCheck based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("present", 2),
          ("required", 3))
    )


_CcDetailsInSetupCliCheck_Type.__name__ = "Integer32"
_CcDetailsInSetupCliCheck_Object = MibTableColumn
ccDetailsInSetupCliCheck = _CcDetailsInSetupCliCheck_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 32),
    _CcDetailsInSetupCliCheck_Type()
)
ccDetailsInSetupCliCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsInSetupCliCheck.setStatus("mandatory")


class _CcDetailsInSetupCliCheckList_Type(Integer32):
    """Custom type ccDetailsInSetupCliCheckList based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CcDetailsInSetupCliCheckList_Type.__name__ = "Integer32"
_CcDetailsInSetupCliCheckList_Object = MibTableColumn
ccDetailsInSetupCliCheckList = _CcDetailsInSetupCliCheckList_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 33),
    _CcDetailsInSetupCliCheckList_Type()
)
ccDetailsInSetupCliCheckList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsInSetupCliCheckList.setStatus("mandatory")


class _CcDetailsUserType_Type(Integer32):
    """Custom type ccDetailsUserType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("attach", 1),
          ("ppp", 2))
    )


_CcDetailsUserType_Type.__name__ = "Integer32"
_CcDetailsUserType_Object = MibTableColumn
ccDetailsUserType = _CcDetailsUserType_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 34),
    _CcDetailsUserType_Type()
)
ccDetailsUserType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsUserType.setStatus("mandatory")


class _CcDetailsLoginType_Type(Integer32):
    """Custom type ccDetailsLoginType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("all", 8),
          ("chap", 5),
          ("none", 1),
          ("pap-radius", 6),
          ("pap-tacacs", 4),
          ("radius", 3),
          ("tacacs", 7),
          ("userdb", 2))
    )


_CcDetailsLoginType_Type.__name__ = "Integer32"
_CcDetailsLoginType_Object = MibTableColumn
ccDetailsLoginType = _CcDetailsLoginType_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 35),
    _CcDetailsLoginType_Type()
)
ccDetailsLoginType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsLoginType.setStatus("mandatory")


class _CcDetailsUsername_Type(Integer32):
    """Custom type ccDetailsUsername based on Integer32"""
    defaultValue = 1

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
        *(("calledsub", 3),
          ("callname", 5),
          ("cli", 2),
          ("none", 1),
          ("useruser", 4))
    )


_CcDetailsUsername_Type.__name__ = "Integer32"
_CcDetailsUsername_Object = MibTableColumn
ccDetailsUsername = _CcDetailsUsername_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 36),
    _CcDetailsUsername_Type()
)
ccDetailsUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsUsername.setStatus("mandatory")


class _CcDetailsPassword_Type(Integer32):
    """Custom type ccDetailsPassword based on Integer32"""
    defaultValue = 1

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
        *(("calledsub", 3),
          ("callname", 5),
          ("cli", 2),
          ("none", 1),
          ("useruser", 4))
    )


_CcDetailsPassword_Type.__name__ = "Integer32"
_CcDetailsPassword_Object = MibTableColumn
ccDetailsPassword = _CcDetailsPassword_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 37),
    _CcDetailsPassword_Type()
)
ccDetailsPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsPassword.setStatus("mandatory")


class _CcDetailsBumpDelay_Type(Integer32):
    """Custom type ccDetailsBumpDelay based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CcDetailsBumpDelay_Type.__name__ = "Integer32"
_CcDetailsBumpDelay_Object = MibTableColumn
ccDetailsBumpDelay = _CcDetailsBumpDelay_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 38),
    _CcDetailsBumpDelay_Type()
)
ccDetailsBumpDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsBumpDelay.setStatus("mandatory")


class _CcDetailsDataRate_Type(Integer32):
    """Custom type ccDetailsDataRate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rate-56k", 2),
          ("rate-64k", 1))
    )


_CcDetailsDataRate_Type.__name__ = "Integer32"
_CcDetailsDataRate_Object = MibTableColumn
ccDetailsDataRate = _CcDetailsDataRate_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 39),
    _CcDetailsDataRate_Type()
)
ccDetailsDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsDataRate.setStatus("mandatory")


class _CcDetailsPppTemplate_Type(Integer32):
    """Custom type ccDetailsPppTemplate based on Integer32"""
    defaultValue = 33

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
        ValueRangeConstraint(33, 33),
    )


_CcDetailsPppTemplate_Type.__name__ = "Integer32"
_CcDetailsPppTemplate_Object = MibTableColumn
ccDetailsPppTemplate = _CcDetailsPppTemplate_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 40),
    _CcDetailsPppTemplate_Type()
)
ccDetailsPppTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsPppTemplate.setStatus("mandatory")
_CcDetailsUserModule_Type = Integer32
_CcDetailsUserModule_Object = MibTableColumn
ccDetailsUserModule = _CcDetailsUserModule_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 41),
    _CcDetailsUserModule_Type()
)
ccDetailsUserModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDetailsUserModule.setStatus("mandatory")
_CcDetailsNumberAttachments_Type = Integer32
_CcDetailsNumberAttachments_Object = MibTableColumn
ccDetailsNumberAttachments = _CcDetailsNumberAttachments_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 1, 1, 42),
    _CcDetailsNumberAttachments_Type()
)
ccDetailsNumberAttachments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDetailsNumberAttachments.setStatus("mandatory")
_CcCliListTable_Object = MibTable
ccCliListTable = _CcCliListTable_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 2)
)
if mibBuilder.loadTexts:
    ccCliListTable.setStatus("mandatory")
_CcCliListEntry_Object = MibTableRow
ccCliListEntry = _CcCliListEntry_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 2, 1)
)
ccCliListEntry.setIndexNames(
    (0, "TELTREND-MIB", "ccCliListListIndex"),
    (0, "TELTREND-MIB", "ccCliListEntryIndex"),
)
if mibBuilder.loadTexts:
    ccCliListEntry.setStatus("mandatory")


class _CcCliListListIndex_Type(Integer32):
    """Custom type ccCliListListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcCliListListIndex_Type.__name__ = "Integer32"
_CcCliListListIndex_Object = MibTableColumn
ccCliListListIndex = _CcCliListListIndex_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 2, 1, 1),
    _CcCliListListIndex_Type()
)
ccCliListListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCliListListIndex.setStatus("mandatory")
_CcCliListEntryIndex_Type = Integer32
_CcCliListEntryIndex_Object = MibTableColumn
ccCliListEntryIndex = _CcCliListEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 2, 1, 2),
    _CcCliListEntryIndex_Type()
)
ccCliListEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCliListEntryIndex.setStatus("mandatory")


class _CcCliListNumber_Type(OctetString):
    """Custom type ccCliListNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CcCliListNumber_Type.__name__ = "OctetString"
_CcCliListNumber_Object = MibTableColumn
ccCliListNumber = _CcCliListNumber_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 2, 1, 3),
    _CcCliListNumber_Type()
)
ccCliListNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCliListNumber.setStatus("mandatory")
_CcActiveCallTable_Object = MibTable
ccActiveCallTable = _CcActiveCallTable_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 3)
)
if mibBuilder.loadTexts:
    ccActiveCallTable.setStatus("mandatory")
_CcActiveCallEntry_Object = MibTableRow
ccActiveCallEntry = _CcActiveCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 3, 1)
)
ccActiveCallEntry.setIndexNames(
    (0, "TELTREND-MIB", "ccActiveCallIndex"),
)
if mibBuilder.loadTexts:
    ccActiveCallEntry.setStatus("mandatory")


class _CcActiveCallIndex_Type(Integer32):
    """Custom type ccActiveCallIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CcActiveCallIndex_Type.__name__ = "Integer32"
_CcActiveCallIndex_Object = MibTableColumn
ccActiveCallIndex = _CcActiveCallIndex_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 3, 1, 1),
    _CcActiveCallIndex_Type()
)
ccActiveCallIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccActiveCallIndex.setStatus("mandatory")


class _CcActiveCallDetailsIndex_Type(Integer32):
    """Custom type ccActiveCallDetailsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CcActiveCallDetailsIndex_Type.__name__ = "Integer32"
_CcActiveCallDetailsIndex_Object = MibTableColumn
ccActiveCallDetailsIndex = _CcActiveCallDetailsIndex_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 3, 1, 2),
    _CcActiveCallDetailsIndex_Type()
)
ccActiveCallDetailsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccActiveCallDetailsIndex.setStatus("mandatory")
_CcActiveCallIfIndex_Type = InterfaceIndexOrZero
_CcActiveCallIfIndex_Object = MibTableColumn
ccActiveCallIfIndex = _CcActiveCallIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 3, 1, 3),
    _CcActiveCallIfIndex_Type()
)
ccActiveCallIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccActiveCallIfIndex.setStatus("mandatory")


class _CcActiveCallDataRate_Type(Integer32):
    """Custom type ccActiveCallDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rate-56k", 2),
          ("rate-64k", 1))
    )


_CcActiveCallDataRate_Type.__name__ = "Integer32"
_CcActiveCallDataRate_Object = MibTableColumn
ccActiveCallDataRate = _CcActiveCallDataRate_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 3, 1, 4),
    _CcActiveCallDataRate_Type()
)
ccActiveCallDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccActiveCallDataRate.setStatus("mandatory")


class _CcActiveCallState_Type(Integer32):
    """Custom type ccActiveCallState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("await1", 6),
          ("null", 1),
          ("off", 2),
          ("on", 4),
          ("try", 3),
          ("wait", 5))
    )


_CcActiveCallState_Type.__name__ = "Integer32"
_CcActiveCallState_Object = MibTableColumn
ccActiveCallState = _CcActiveCallState_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 3, 1, 5),
    _CcActiveCallState_Type()
)
ccActiveCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccActiveCallState.setStatus("mandatory")


class _CcActiveCallDirection_Type(Integer32):
    """Custom type ccActiveCallDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2),
          ("undefined", 3))
    )


_CcActiveCallDirection_Type.__name__ = "Integer32"
_CcActiveCallDirection_Object = MibTableColumn
ccActiveCallDirection = _CcActiveCallDirection_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 3, 1, 6),
    _CcActiveCallDirection_Type()
)
ccActiveCallDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccActiveCallDirection.setStatus("mandatory")
_CcActiveCallUserModule_Type = Integer32
_CcActiveCallUserModule_Object = MibTableColumn
ccActiveCallUserModule = _CcActiveCallUserModule_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 3, 1, 7),
    _CcActiveCallUserModule_Type()
)
ccActiveCallUserModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccActiveCallUserModule.setStatus("mandatory")
_CcActiveCallUserInstance_Type = Integer32
_CcActiveCallUserInstance_Object = MibTableColumn
ccActiveCallUserInstance = _CcActiveCallUserInstance_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 3, 1, 8),
    _CcActiveCallUserInstance_Type()
)
ccActiveCallUserInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccActiveCallUserInstance.setStatus("mandatory")


class _CcActiveCallBchannelIndex_Type(Integer32):
    """Custom type ccActiveCallBchannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_CcActiveCallBchannelIndex_Type.__name__ = "Integer32"
_CcActiveCallBchannelIndex_Object = MibTableColumn
ccActiveCallBchannelIndex = _CcActiveCallBchannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 3, 1, 9),
    _CcActiveCallBchannelIndex_Type()
)
ccActiveCallBchannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccActiveCallBchannelIndex.setStatus("mandatory")
_CcCallLogTable_Object = MibTable
ccCallLogTable = _CcCallLogTable_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 4)
)
if mibBuilder.loadTexts:
    ccCallLogTable.setStatus("mandatory")
_CcCallLogEntry_Object = MibTableRow
ccCallLogEntry = _CcCallLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 4, 1)
)
ccCallLogEntry.setIndexNames(
    (0, "TELTREND-MIB", "ccCallLogIndex"),
)
if mibBuilder.loadTexts:
    ccCallLogEntry.setStatus("mandatory")
_CcCallLogIndex_Type = Integer32
_CcCallLogIndex_Object = MibTableColumn
ccCallLogIndex = _CcCallLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 4, 1, 1),
    _CcCallLogIndex_Type()
)
ccCallLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCallLogIndex.setStatus("mandatory")


class _CcCallLogName_Type(DisplayString):
    """Custom type ccCallLogName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CcCallLogName_Type.__name__ = "DisplayString"
_CcCallLogName_Object = MibTableColumn
ccCallLogName = _CcCallLogName_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 4, 1, 2),
    _CcCallLogName_Type()
)
ccCallLogName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCallLogName.setStatus("mandatory")


class _CcCallLogState_Type(Integer32):
    """Custom type ccCallLogState based on Integer32"""
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
        *(("active", 2),
          ("cleared", 4),
          ("disconnected", 3),
          ("initial", 1))
    )


_CcCallLogState_Type.__name__ = "Integer32"
_CcCallLogState_Object = MibTableColumn
ccCallLogState = _CcCallLogState_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 4, 1, 3),
    _CcCallLogState_Type()
)
ccCallLogState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCallLogState.setStatus("mandatory")


class _CcCallLogTimeStarted_Type(DisplayString):
    """Custom type ccCallLogTimeStarted based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CcCallLogTimeStarted_Type.__name__ = "DisplayString"
_CcCallLogTimeStarted_Object = MibTableColumn
ccCallLogTimeStarted = _CcCallLogTimeStarted_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 4, 1, 4),
    _CcCallLogTimeStarted_Type()
)
ccCallLogTimeStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCallLogTimeStarted.setStatus("mandatory")


class _CcCallLogDirection_Type(Integer32):
    """Custom type ccCallLogDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_CcCallLogDirection_Type.__name__ = "Integer32"
_CcCallLogDirection_Object = MibTableColumn
ccCallLogDirection = _CcCallLogDirection_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 4, 1, 5),
    _CcCallLogDirection_Type()
)
ccCallLogDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCallLogDirection.setStatus("mandatory")
_CcCallLogDuration_Type = Integer32
_CcCallLogDuration_Object = MibTableColumn
ccCallLogDuration = _CcCallLogDuration_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 4, 1, 6),
    _CcCallLogDuration_Type()
)
ccCallLogDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCallLogDuration.setStatus("mandatory")


class _CcCallLogRemoteNumber_Type(DisplayString):
    """Custom type ccCallLogRemoteNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CcCallLogRemoteNumber_Type.__name__ = "DisplayString"
_CcCallLogRemoteNumber_Object = MibTableColumn
ccCallLogRemoteNumber = _CcCallLogRemoteNumber_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 4, 1, 7),
    _CcCallLogRemoteNumber_Type()
)
ccCallLogRemoteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCallLogRemoteNumber.setStatus("mandatory")
_CcAttachmentTable_Object = MibTable
ccAttachmentTable = _CcAttachmentTable_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 5)
)
if mibBuilder.loadTexts:
    ccAttachmentTable.setStatus("mandatory")
_CcAttachmentEntry_Object = MibTableRow
ccAttachmentEntry = _CcAttachmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 5, 1)
)
ccAttachmentEntry.setIndexNames(
    (0, "TELTREND-MIB", "ccAttachmentDetailsIndex"),
    (0, "TELTREND-MIB", "ccAttachmentEntryIndex"),
)
if mibBuilder.loadTexts:
    ccAttachmentEntry.setStatus("mandatory")


class _CcAttachmentDetailsIndex_Type(Integer32):
    """Custom type ccAttachmentDetailsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CcAttachmentDetailsIndex_Type.__name__ = "Integer32"
_CcAttachmentDetailsIndex_Object = MibTableColumn
ccAttachmentDetailsIndex = _CcAttachmentDetailsIndex_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 5, 1, 1),
    _CcAttachmentDetailsIndex_Type()
)
ccAttachmentDetailsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccAttachmentDetailsIndex.setStatus("mandatory")
_CcAttachmentEntryIndex_Type = Integer32
_CcAttachmentEntryIndex_Object = MibTableColumn
ccAttachmentEntryIndex = _CcAttachmentEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 5, 1, 2),
    _CcAttachmentEntryIndex_Type()
)
ccAttachmentEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccAttachmentEntryIndex.setStatus("mandatory")


class _CcAttachmentActiveCallIndex_Type(Integer32):
    """Custom type ccAttachmentActiveCallIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CcAttachmentActiveCallIndex_Type.__name__ = "Integer32"
_CcAttachmentActiveCallIndex_Object = MibTableColumn
ccAttachmentActiveCallIndex = _CcAttachmentActiveCallIndex_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 5, 1, 3),
    _CcAttachmentActiveCallIndex_Type()
)
ccAttachmentActiveCallIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccAttachmentActiveCallIndex.setStatus("mandatory")
_CcAttachmentUserInstance_Type = Integer32
_CcAttachmentUserInstance_Object = MibTableColumn
ccAttachmentUserInstance = _CcAttachmentUserInstance_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 5, 1, 4),
    _CcAttachmentUserInstance_Type()
)
ccAttachmentUserInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccAttachmentUserInstance.setStatus("mandatory")
_CcBchannelTable_Object = MibTable
ccBchannelTable = _CcBchannelTable_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 6)
)
if mibBuilder.loadTexts:
    ccBchannelTable.setStatus("mandatory")
_CcBchannelEntry_Object = MibTableRow
ccBchannelEntry = _CcBchannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 6, 1)
)
ccBchannelEntry.setIndexNames(
    (0, "TELTREND-MIB", "ccBchannelIfIndex"),
    (0, "TELTREND-MIB", "ccBchannelChannelIndex"),
)
if mibBuilder.loadTexts:
    ccBchannelEntry.setStatus("mandatory")
_CcBchannelIfIndex_Type = InterfaceIndexOrZero
_CcBchannelIfIndex_Object = MibTableColumn
ccBchannelIfIndex = _CcBchannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 6, 1, 1),
    _CcBchannelIfIndex_Type()
)
ccBchannelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccBchannelIfIndex.setStatus("mandatory")


class _CcBchannelChannelIndex_Type(Integer32):
    """Custom type ccBchannelChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_CcBchannelChannelIndex_Type.__name__ = "Integer32"
_CcBchannelChannelIndex_Object = MibTableColumn
ccBchannelChannelIndex = _CcBchannelChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 6, 1, 2),
    _CcBchannelChannelIndex_Type()
)
ccBchannelChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccBchannelChannelIndex.setStatus("mandatory")


class _CcBchannelAllocated_Type(Integer32):
    """Custom type ccBchannelAllocated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CcBchannelAllocated_Type.__name__ = "Integer32"
_CcBchannelAllocated_Object = MibTableColumn
ccBchannelAllocated = _CcBchannelAllocated_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 6, 1, 3),
    _CcBchannelAllocated_Type()
)
ccBchannelAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccBchannelAllocated.setStatus("mandatory")


class _CcBchannelCallType_Type(Integer32):
    """Custom type ccBchannelCallType based on Integer32"""
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
        *(("data", 2),
          ("undefined", 1),
          ("voice", 3),
          ("x25", 4))
    )


_CcBchannelCallType_Type.__name__ = "Integer32"
_CcBchannelCallType_Object = MibTableColumn
ccBchannelCallType = _CcBchannelCallType_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 6, 1, 4),
    _CcBchannelCallType_Type()
)
ccBchannelCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccBchannelCallType.setStatus("mandatory")


class _CcBchannelActiveCallIndex_Type(Integer32):
    """Custom type ccBchannelActiveCallIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CcBchannelActiveCallIndex_Type.__name__ = "Integer32"
_CcBchannelActiveCallIndex_Object = MibTableColumn
ccBchannelActiveCallIndex = _CcBchannelActiveCallIndex_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 6, 1, 5),
    _CcBchannelActiveCallIndex_Type()
)
ccBchannelActiveCallIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccBchannelActiveCallIndex.setStatus("mandatory")
_CcBchannelPriority_Type = Integer32
_CcBchannelPriority_Object = MibTableColumn
ccBchannelPriority = _CcBchannelPriority_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 6, 1, 6),
    _CcBchannelPriority_Type()
)
ccBchannelPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccBchannelPriority.setStatus("mandatory")


class _CcBchannelDirection_Type(Integer32):
    """Custom type ccBchannelDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2),
          ("unallocated", 3))
    )


_CcBchannelDirection_Type.__name__ = "Integer32"
_CcBchannelDirection_Object = MibTableColumn
ccBchannelDirection = _CcBchannelDirection_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 37, 6, 1, 7),
    _CcBchannelDirection_Type()
)
ccBchannelDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccBchannelDirection.setStatus("mandatory")
_Loader_ObjectIdentity = ObjectIdentity
loader = _Loader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 48)
)
_LoadTable_Object = MibTable
loadTable = _LoadTable_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 48, 1)
)
if mibBuilder.loadTexts:
    loadTable.setStatus("mandatory")
_LoadEntry_Object = MibTableRow
loadEntry = _LoadEntry_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 48, 1, 1)
)
loadEntry.setIndexNames(
    (0, "TELTREND-MIB", "loadIndex"),
)
if mibBuilder.loadTexts:
    loadEntry.setStatus("mandatory")


class _LoadIndex_Type(Integer32):
    """Custom type loadIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_LoadIndex_Type.__name__ = "Integer32"
_LoadIndex_Object = MibTableColumn
loadIndex = _LoadIndex_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 48, 1, 1, 1),
    _LoadIndex_Type()
)
loadIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadIndex.setStatus("mandatory")
_LoadServer_Type = IpAddress
_LoadServer_Object = MibTableColumn
loadServer = _LoadServer_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 48, 1, 1, 2),
    _LoadServer_Type()
)
loadServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadServer.setStatus("mandatory")


class _LoadDestination_Type(Integer32):
    """Custom type loadDestination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flash", 3),
          ("nvs", 2),
          ("undefined", 1))
    )


_LoadDestination_Type.__name__ = "Integer32"
_LoadDestination_Object = MibTableColumn
loadDestination = _LoadDestination_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 48, 1, 1, 3),
    _LoadDestination_Type()
)
loadDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadDestination.setStatus("mandatory")


class _LoadFilename_Type(DisplayString):
    """Custom type loadFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LoadFilename_Type.__name__ = "DisplayString"
_LoadFilename_Object = MibTableColumn
loadFilename = _LoadFilename_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 48, 1, 1, 4),
    _LoadFilename_Type()
)
loadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadFilename.setStatus("mandatory")
_LoadDelay_Type = Integer32
_LoadDelay_Object = MibTableColumn
loadDelay = _LoadDelay_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 48, 1, 1, 5),
    _LoadDelay_Type()
)
loadDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadDelay.setStatus("mandatory")


class _LoadStatus_Type(Integer32):
    """Custom type loadStatus based on Integer32"""
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
        *(("actionstart", 6),
          ("actionstop", 7),
          ("complete", 4),
          ("idle", 1),
          ("loading", 3),
          ("reset", 5),
          ("wait", 2))
    )


_LoadStatus_Type.__name__ = "Integer32"
_LoadStatus_Object = MibScalar
loadStatus = _LoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 48, 2),
    _LoadStatus_Type()
)
loadStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadStatus.setStatus("mandatory")
_Install_ObjectIdentity = ObjectIdentity
install = _Install_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 49)
)
_InstallTable_Object = MibTable
installTable = _InstallTable_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 49, 1)
)
if mibBuilder.loadTexts:
    installTable.setStatus("mandatory")
_InstallEntry_Object = MibTableRow
installEntry = _InstallEntry_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 49, 1, 1)
)
installEntry.setIndexNames(
    (0, "TELTREND-MIB", "instIndex"),
)
if mibBuilder.loadTexts:
    installEntry.setStatus("mandatory")


class _InstIndex_Type(Integer32):
    """Custom type instIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("preferred", 2),
          ("temporary", 1))
    )


_InstIndex_Type.__name__ = "Integer32"
_InstIndex_Object = MibTableColumn
instIndex = _InstIndex_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 49, 1, 1, 1),
    _InstIndex_Type()
)
instIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instIndex.setStatus("mandatory")


class _InstRelDevice_Type(Integer32):
    """Custom type instRelDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eprom", 2),
          ("flash", 3),
          ("none", 1))
    )


_InstRelDevice_Type.__name__ = "Integer32"
_InstRelDevice_Object = MibTableColumn
instRelDevice = _InstRelDevice_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 49, 1, 1, 2),
    _InstRelDevice_Type()
)
instRelDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    instRelDevice.setStatus("mandatory")


class _InstRelName_Type(DisplayString):
    """Custom type instRelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_InstRelName_Type.__name__ = "DisplayString"
_InstRelName_Object = MibTableColumn
instRelName = _InstRelName_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 49, 1, 1, 3),
    _InstRelName_Type()
)
instRelName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    instRelName.setStatus("mandatory")
_InstRelMajor_Type = Integer32
_InstRelMajor_Object = MibTableColumn
instRelMajor = _InstRelMajor_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 49, 1, 1, 4),
    _InstRelMajor_Type()
)
instRelMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instRelMajor.setStatus("mandatory")
_InstRelMinor_Type = Integer32
_InstRelMinor_Object = MibTableColumn
instRelMinor = _InstRelMinor_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 49, 1, 1, 5),
    _InstRelMinor_Type()
)
instRelMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instRelMinor.setStatus("mandatory")


class _InstPatDevice_Type(Integer32):
    """Custom type instPatDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("flash", 3),
          ("none", 1),
          ("nvs", 4))
    )


_InstPatDevice_Type.__name__ = "Integer32"
_InstPatDevice_Object = MibTableColumn
instPatDevice = _InstPatDevice_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 49, 1, 1, 6),
    _InstPatDevice_Type()
)
instPatDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    instPatDevice.setStatus("mandatory")


class _InstPatName_Type(DisplayString):
    """Custom type instPatName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_InstPatName_Type.__name__ = "DisplayString"
_InstPatName_Object = MibTableColumn
instPatName = _InstPatName_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 49, 1, 1, 7),
    _InstPatName_Type()
)
instPatName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    instPatName.setStatus("mandatory")
_InstRelInterim_Type = Integer32
_InstRelInterim_Object = MibTableColumn
instRelInterim = _InstRelInterim_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 49, 1, 1, 8),
    _InstRelInterim_Type()
)
instRelInterim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instRelInterim.setStatus("mandatory")
_InstallHistoryTable_Object = MibTable
installHistoryTable = _InstallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 49, 2)
)
if mibBuilder.loadTexts:
    installHistoryTable.setStatus("mandatory")
_InstallHistoryEntry_Object = MibTableRow
installHistoryEntry = _InstallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 49, 2, 1)
)
installHistoryEntry.setIndexNames(
    (0, "TELTREND-MIB", "instHistIndex"),
)
if mibBuilder.loadTexts:
    installHistoryEntry.setStatus("mandatory")
_InstHistIndex_Type = Integer32
_InstHistIndex_Object = MibTableColumn
instHistIndex = _InstHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 49, 2, 1, 1),
    _InstHistIndex_Type()
)
instHistIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instHistIndex.setStatus("mandatory")


class _InstHistLine_Type(DisplayString):
    """Custom type instHistLine based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_InstHistLine_Type.__name__ = "DisplayString"
_InstHistLine_Object = MibTableColumn
instHistLine = _InstHistLine_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 49, 2, 1, 2),
    _InstHistLine_Type()
)
instHistLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instHistLine.setStatus("mandatory")


class _ConfigFile_Type(DisplayString):
    """Custom type configFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ConfigFile_Type.__name__ = "DisplayString"
_ConfigFile_Object = MibScalar
configFile = _ConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 49, 3),
    _ConfigFile_Type()
)
configFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFile.setStatus("mandatory")
_LicenceTable_Object = MibTable
licenceTable = _LicenceTable_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 49, 4)
)
if mibBuilder.loadTexts:
    licenceTable.setStatus("mandatory")
_LicenceEntry_Object = MibTableRow
licenceEntry = _LicenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 49, 4, 1)
)
licenceEntry.setIndexNames(
    (0, "TELTREND-MIB", "licenceIndex"),
)
if mibBuilder.loadTexts:
    licenceEntry.setStatus("mandatory")
_LicenceIndex_Type = Integer32
_LicenceIndex_Object = MibTableColumn
licenceIndex = _LicenceIndex_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 49, 4, 1, 1),
    _LicenceIndex_Type()
)
licenceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenceIndex.setStatus("mandatory")


class _LicenceStatus_Type(Integer32):
    """Custom type licenceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deleting", 2),
          ("ok", 1))
    )


_LicenceStatus_Type.__name__ = "Integer32"
_LicenceStatus_Object = MibTableColumn
licenceStatus = _LicenceStatus_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 49, 4, 1, 2),
    _LicenceStatus_Type()
)
licenceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenceStatus.setStatus("mandatory")


class _LicenceRelease_Type(DisplayString):
    """Custom type licenceRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LicenceRelease_Type.__name__ = "DisplayString"
_LicenceRelease_Object = MibTableColumn
licenceRelease = _LicenceRelease_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 49, 4, 1, 3),
    _LicenceRelease_Type()
)
licenceRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenceRelease.setStatus("mandatory")
_LicenceMajor_Type = Integer32
_LicenceMajor_Object = MibTableColumn
licenceMajor = _LicenceMajor_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 49, 4, 1, 4),
    _LicenceMajor_Type()
)
licenceMajor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenceMajor.setStatus("mandatory")
_LicenceMinor_Type = Integer32
_LicenceMinor_Object = MibTableColumn
licenceMinor = _LicenceMinor_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 49, 4, 1, 5),
    _LicenceMinor_Type()
)
licenceMinor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenceMinor.setStatus("mandatory")


class _LicencePassword_Type(DisplayString):
    """Custom type licencePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LicencePassword_Type.__name__ = "DisplayString"
_LicencePassword_Object = MibTableColumn
licencePassword = _LicencePassword_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 49, 4, 1, 6),
    _LicencePassword_Type()
)
licencePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licencePassword.setStatus("mandatory")


class _LicenceExpiry_Type(DisplayString):
    """Custom type licenceExpiry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LicenceExpiry_Type.__name__ = "DisplayString"
_LicenceExpiry_Object = MibTableColumn
licenceExpiry = _LicenceExpiry_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 49, 4, 1, 7),
    _LicenceExpiry_Type()
)
licenceExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenceExpiry.setStatus("mandatory")
_LicenceInterim_Type = Integer32
_LicenceInterim_Object = MibTableColumn
licenceInterim = _LicenceInterim_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 49, 4, 1, 8),
    _LicenceInterim_Type()
)
licenceInterim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenceInterim.setStatus("mandatory")
_File_ObjectIdentity = ObjectIdentity
file = _File_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 56)
)
_FileTable_Object = MibTable
fileTable = _FileTable_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 56, 1)
)
if mibBuilder.loadTexts:
    fileTable.setStatus("mandatory")
_FileEntry_Object = MibTableRow
fileEntry = _FileEntry_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 56, 1, 1)
)
fileEntry.setIndexNames(
    (0, "TELTREND-MIB", "fileIndex"),
)
if mibBuilder.loadTexts:
    fileEntry.setStatus("mandatory")
_FileIndex_Type = Integer32
_FileIndex_Object = MibTableColumn
fileIndex = _FileIndex_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 56, 1, 1, 1),
    _FileIndex_Type()
)
fileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileIndex.setStatus("mandatory")


class _FileName_Type(DisplayString):
    """Custom type fileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FileName_Type.__name__ = "DisplayString"
_FileName_Object = MibTableColumn
fileName = _FileName_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 56, 1, 1, 2),
    _FileName_Type()
)
fileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileName.setStatus("mandatory")


class _FileDevice_Type(Integer32):
    """Custom type fileDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flash", 1),
          ("nvs", 2))
    )


_FileDevice_Type.__name__ = "Integer32"
_FileDevice_Object = MibTableColumn
fileDevice = _FileDevice_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 56, 1, 1, 3),
    _FileDevice_Type()
)
fileDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileDevice.setStatus("mandatory")


class _FileCreationTime_Type(DisplayString):
    """Custom type fileCreationTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FileCreationTime_Type.__name__ = "DisplayString"
_FileCreationTime_Object = MibTableColumn
fileCreationTime = _FileCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 56, 1, 1, 4),
    _FileCreationTime_Type()
)
fileCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileCreationTime.setStatus("mandatory")


class _FileStatus_Type(Integer32):
    """Custom type fileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deleting", 2),
          ("ok", 1))
    )


_FileStatus_Type.__name__ = "Integer32"
_FileStatus_Object = MibTableColumn
fileStatus = _FileStatus_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 56, 1, 1, 5),
    _FileStatus_Type()
)
fileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileStatus.setStatus("mandatory")
_FileSize_Type = Integer32
_FileSize_Object = MibTableColumn
fileSize = _FileSize_Object(
    (1, 3, 6, 1, 4, 1, 293, 2, 4, 56, 1, 1, 6),
    _FileSize_Type()
)
fileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSize.setStatus("mandatory")
_Interfaces_ObjectIdentity = ObjectIdentity
interfaces = _Interfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 5)
)
_Protocols_ObjectIdentity = ObjectIdentity
protocols = _Protocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 293, 2, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TELTREND-MIB",
    **{"InterfaceIndexOrZero": InterfaceIndexOrZero,
       "teltrend": teltrend,
       "products": products,
       "niqRouter": niqRouter,
       "niq-4820-2wan": niq_4820_2wan,
       "niq-2830-bri": niq_2830_bri,
       "niq-2820-2wan": niq_2820_2wan,
       "niq-2810-1wan": niq_2810_1wan,
       "niq-3830-bri": niq_3830_bri,
       "niq-3820-2wan": niq_3820_2wan,
       "niq-3810-1wan": niq_3810_1wan,
       "niq-1870-bri-wan": niq_1870_bri_wan,
       "niq-1830-bri": niq_1830_bri,
       "niq-1810-wan": niq_1810_wan,
       "niq-1100-bri-wan": niq_1100_bri_wan,
       "niq-1100-bri-bay": niq_1100_bri_bay,
       "niq-1100-wan-bay": niq_1100_wan_bay,
       "niq-1100-bay-bay": niq_1100_bay_bay,
       "niq-1900-bay-bay": niq_1900_bay_bay,
       "niq-3100": niq_3100,
       "niq-800-2-pots": niq_800_2_pots,
       "niq-800-no-pots": niq_800_no_pots,
       "niq-800-4-pots": niq_800_4_pots,
       "niq-5200": niq_5200,
       "niq-800u-no-pots": niq_800u_no_pots,
       "niq-800u-2-pots": niq_800u_2_pots,
       "niq-800u-4-pots": niq_800u_4_pots,
       "niq-800-syn": niq_800_syn,
       "niq-nac-wan": niq_nac_wan,
       "niq-pr2000": niq_pr2000,
       "niq-pr2000-50": niq_pr2000_50,
       "niq-pr3000": niq_pr3000,
       "niq-alpha": niq_alpha,
       "niq-nac-g703": niq_nac_g703,
       "niq-800-syn-bri": niq_800_syn_bri,
       "niq-800-2-eth-syn": niq_800_2_eth_syn,
       "niq-800-pri": niq_800_pri,
       "niq-800-g703": niq_800_g703,
       "niq-nac-60": niq_nac_60,
       "niq-800-syn-briu": niq_800_syn_briu,
       "niq": niq,
       "objects": objects,
       "boards": boards,
       "ppr-mpr-base": ppr_mpr_base,
       "ppr-mpr-sync4": ppr_mpr_sync4,
       "ppr-mpr-lan4": ppr_mpr_lan4,
       "ppr-mpr-async12": ppr_mpr_async12,
       "ppr-mpr-bri1": ppr_mpr_bri1,
       "ppr-mpr-async16": ppr_mpr_async16,
       "ppr-mpr-comp": ppr_mpr_comp,
       "ppr-mpr-pri2": ppr_mpr_pri2,
       "ppr-2830-bri": ppr_2830_bri,
       "ppr-2820-wan-ww": ppr_2820_wan_ww,
       "ppr-2810-wan-w": ppr_2810_wan_w,
       "ppr-3830-bri": ppr_3830_bri,
       "ppr-3820-wan-ww": ppr_3820_wan_ww,
       "ppr-3810-wan-w": ppr_3810_wan_w,
       "ppr-1870-ext-bri-wan": ppr_1870_ext_bri_wan,
       "ppr-1830-ext-bri": ppr_1830_ext_bri,
       "ppr-1850-pc-bri": ppr_1850_pc_bri,
       "ppr-1810-ext-wan": ppr_1810_ext_wan,
       "ppr-1810-pc-wan": ppr_1810_pc_wan,
       "ppr-mpr-sync2": ppr_mpr_sync2,
       "ppr-mpr-pri1": ppr_mpr_pri1,
       "ppr-mpr-bri2": ppr_mpr_bri2,
       "ppr-mpr-bri4": ppr_mpr_bri4,
       "ppr-mpr-enco-us": ppr_mpr_enco_us,
       "ppr-mpr-enco-hs": ppr_mpr_enco_hs,
       "ppr-mpr-cryp-us": ppr_mpr_cryp_us,
       "ppr-mpr-cryp-hs": ppr_mpr_cryp_hs,
       "ppr-mpr-comp-2": ppr_mpr_comp_2,
       "ppr-mpr-gio": ppr_mpr_gio,
       "ppr-iom-asyn4": ppr_iom_asyn4,
       "ppr-iom-bri1": ppr_iom_bri1,
       "ppr-iom-eth1": ppr_iom_eth1,
       "ppr-iom-pri1": ppr_iom_pri1,
       "ppr-iom-syn2": ppr_iom_syn2,
       "ppr-1000-bri-wan": ppr_1000_bri_wan,
       "ppr-1000-bri-bay": ppr_1000_bri_bay,
       "ppr-1000-wan-bay": ppr_1000_wan_bay,
       "ppr-1000-bay-bay": ppr_1000_bay_bay,
       "ppr-icm-syn1": ppr_icm_syn1,
       "ppr-icm-bri1": ppr_icm_bri1,
       "ppr-icm-eth1": ppr_icm_eth1,
       "ppr-icm-pots1": ppr_icm_pots1,
       "ppr-icm-pots2": ppr_icm_pots2,
       "ppr-icm-pots4": ppr_icm_pots4,
       "ppr-icm-pri1": ppr_icm_pri1,
       "ppr-icm-asyn4": ppr_icm_asyn4,
       "ppr-1900-bay-bay": ppr_1900_bay_bay,
       "ppr-3100": ppr_3100,
       "ppr-840": ppr_840,
       "ppr-iom-g703tdm": ppr_iom_g703tdm,
       "ppr-icm-g703tdm": ppr_icm_g703tdm,
       "ppr-820": ppr_820,
       "ppr-860": ppr_860,
       "ppr-5200": ppr_5200,
       "ppr-820U": ppr_820U,
       "ppr-840U": ppr_840U,
       "ppr-860U": ppr_860U,
       "ppr-800SYN": ppr_800SYN,
       "ppr-ICM-BRI1U": ppr_ICM_BRI1U,
       "ppr-NAS": ppr_NAS,
       "ppr-GIO-3100": ppr_GIO_3100,
       "ppr-PR2000": ppr_PR2000,
       "ppr-beta-cpu": ppr_beta_cpu,
       "ppr-PR3000": ppr_PR3000,
       "ppr-alpha-cpu": ppr_alpha_cpu,
       "ppr-NAC-G703": ppr_NAC_G703,
       "ppr-EMAC": ppr_EMAC,
       "ppr-CMAC": ppr_CMAC,
       "ppr-CEMAC": ppr_CEMAC,
       "ppr-800DUAL": ppr_800DUAL,
       "ppr-800SYNDUALETH": ppr_800SYNDUALETH,
       "ppr-800PRI": ppr_800PRI,
       "ppr-800PRITDMONLY": ppr_800PRITDMONLY,
       "ppr-NAC-60": ppr_NAC_60,
       "ppr-800DUAL-U": ppr_800DUAL_U,
       "ppr-icm-e1t1": ppr_icm_e1t1,
       "ppr-icm-e1t1tdmonly": ppr_icm_e1t1tdmonly,
       "release": release,
       "iftypes": iftypes,
       "iface-eth": iface_eth,
       "iface-syn": iface_syn,
       "iface-asyn": iface_asyn,
       "iface-bri": iface_bri,
       "iface-pri": iface_pri,
       "iface-pots": iface_pots,
       "chips": chips,
       "chip-68020-cpu": chip_68020_cpu,
       "chip-68340-cpu": chip_68340_cpu,
       "chip-68302-cpu": chip_68302_cpu,
       "chip-68360-cpu": chip_68360_cpu,
       "chip-rtc1": chip_rtc1,
       "chip-rtc2": chip_rtc2,
       "chip-rtc3": chip_rtc3,
       "chip-rtc4": chip_rtc4,
       "chip-ram-1mb": chip_ram_1mb,
       "chip-ram-2mb": chip_ram_2mb,
       "chip-ram-3mb": chip_ram_3mb,
       "chip-ram-4mb": chip_ram_4mb,
       "chip-ram-6mb": chip_ram_6mb,
       "chip-ram-8mb": chip_ram_8mb,
       "chip-ram-12mb": chip_ram_12mb,
       "chip-ram-16mb": chip_ram_16mb,
       "chip-ram-20mb": chip_ram_20mb,
       "chip-ram-32mb": chip_ram_32mb,
       "chip-flash-1mb": chip_flash_1mb,
       "chip-flash-2mb": chip_flash_2mb,
       "chip-flash-3mb": chip_flash_3mb,
       "chip-flash-4mb": chip_flash_4mb,
       "chip-flash-6mb": chip_flash_6mb,
       "chip-flash-8mb": chip_flash_8mb,
       "chip-pem": chip_pem,
       "traps": traps,
       "sysinfo": sysinfo,
       "modules": modules,
       "cc": cc,
       "ccDetailsTable": ccDetailsTable,
       "ccDetailsEntry": ccDetailsEntry,
       "ccDetailsIndex": ccDetailsIndex,
       "ccDetailsName": ccDetailsName,
       "ccDetailsRemoteName": ccDetailsRemoteName,
       "ccDetailsCalledNumber": ccDetailsCalledNumber,
       "ccDetailsCallingNumber": ccDetailsCallingNumber,
       "ccDetailsAlternateNumber": ccDetailsAlternateNumber,
       "ccDetailsEnabled": ccDetailsEnabled,
       "ccDetailsDirection": ccDetailsDirection,
       "ccDetailsPrecedence": ccDetailsPrecedence,
       "ccDetailsHoldupTime": ccDetailsHoldupTime,
       "ccDetailsPreferredIfIndex": ccDetailsPreferredIfIndex,
       "ccDetailsRequiredIfIndex": ccDetailsRequiredIfIndex,
       "ccDetailsPriority": ccDetailsPriority,
       "ccDetailsRetryT1": ccDetailsRetryT1,
       "ccDetailsRetryN1": ccDetailsRetryN1,
       "ccDetailsRetryT2": ccDetailsRetryT2,
       "ccDetailsRetryN2": ccDetailsRetryN2,
       "ccDetailsKeepup": ccDetailsKeepup,
       "ccDetailsOutSetupCli": ccDetailsOutSetupCli,
       "ccDetailsOutSetupUser": ccDetailsOutSetupUser,
       "ccDetailsOutSetupCalledSub": ccDetailsOutSetupCalledSub,
       "ccDetailsOutSubaddress": ccDetailsOutSubaddress,
       "ccDetailsCallback": ccDetailsCallback,
       "ccDetailsCallbackDelay": ccDetailsCallbackDelay,
       "ccDetailsInSetupCalledSubSearch": ccDetailsInSetupCalledSubSearch,
       "ccDetailsInSetupUserSearch": ccDetailsInSetupUserSearch,
       "ccDetailsInSetupCliSearch": ccDetailsInSetupCliSearch,
       "ccDetailsInSetupCliSearchList": ccDetailsInSetupCliSearchList,
       "ccDetailsInAnyFlag": ccDetailsInAnyFlag,
       "ccDetailsInSetupCalledSubCheck": ccDetailsInSetupCalledSubCheck,
       "ccDetailsInSetupUserCheck": ccDetailsInSetupUserCheck,
       "ccDetailsInSetupCliCheck": ccDetailsInSetupCliCheck,
       "ccDetailsInSetupCliCheckList": ccDetailsInSetupCliCheckList,
       "ccDetailsUserType": ccDetailsUserType,
       "ccDetailsLoginType": ccDetailsLoginType,
       "ccDetailsUsername": ccDetailsUsername,
       "ccDetailsPassword": ccDetailsPassword,
       "ccDetailsBumpDelay": ccDetailsBumpDelay,
       "ccDetailsDataRate": ccDetailsDataRate,
       "ccDetailsPppTemplate": ccDetailsPppTemplate,
       "ccDetailsUserModule": ccDetailsUserModule,
       "ccDetailsNumberAttachments": ccDetailsNumberAttachments,
       "ccCliListTable": ccCliListTable,
       "ccCliListEntry": ccCliListEntry,
       "ccCliListListIndex": ccCliListListIndex,
       "ccCliListEntryIndex": ccCliListEntryIndex,
       "ccCliListNumber": ccCliListNumber,
       "ccActiveCallTable": ccActiveCallTable,
       "ccActiveCallEntry": ccActiveCallEntry,
       "ccActiveCallIndex": ccActiveCallIndex,
       "ccActiveCallDetailsIndex": ccActiveCallDetailsIndex,
       "ccActiveCallIfIndex": ccActiveCallIfIndex,
       "ccActiveCallDataRate": ccActiveCallDataRate,
       "ccActiveCallState": ccActiveCallState,
       "ccActiveCallDirection": ccActiveCallDirection,
       "ccActiveCallUserModule": ccActiveCallUserModule,
       "ccActiveCallUserInstance": ccActiveCallUserInstance,
       "ccActiveCallBchannelIndex": ccActiveCallBchannelIndex,
       "ccCallLogTable": ccCallLogTable,
       "ccCallLogEntry": ccCallLogEntry,
       "ccCallLogIndex": ccCallLogIndex,
       "ccCallLogName": ccCallLogName,
       "ccCallLogState": ccCallLogState,
       "ccCallLogTimeStarted": ccCallLogTimeStarted,
       "ccCallLogDirection": ccCallLogDirection,
       "ccCallLogDuration": ccCallLogDuration,
       "ccCallLogRemoteNumber": ccCallLogRemoteNumber,
       "ccAttachmentTable": ccAttachmentTable,
       "ccAttachmentEntry": ccAttachmentEntry,
       "ccAttachmentDetailsIndex": ccAttachmentDetailsIndex,
       "ccAttachmentEntryIndex": ccAttachmentEntryIndex,
       "ccAttachmentActiveCallIndex": ccAttachmentActiveCallIndex,
       "ccAttachmentUserInstance": ccAttachmentUserInstance,
       "ccBchannelTable": ccBchannelTable,
       "ccBchannelEntry": ccBchannelEntry,
       "ccBchannelIfIndex": ccBchannelIfIndex,
       "ccBchannelChannelIndex": ccBchannelChannelIndex,
       "ccBchannelAllocated": ccBchannelAllocated,
       "ccBchannelCallType": ccBchannelCallType,
       "ccBchannelActiveCallIndex": ccBchannelActiveCallIndex,
       "ccBchannelPriority": ccBchannelPriority,
       "ccBchannelDirection": ccBchannelDirection,
       "loader": loader,
       "loadTable": loadTable,
       "loadEntry": loadEntry,
       "loadIndex": loadIndex,
       "loadServer": loadServer,
       "loadDestination": loadDestination,
       "loadFilename": loadFilename,
       "loadDelay": loadDelay,
       "loadStatus": loadStatus,
       "install": install,
       "installTable": installTable,
       "installEntry": installEntry,
       "instIndex": instIndex,
       "instRelDevice": instRelDevice,
       "instRelName": instRelName,
       "instRelMajor": instRelMajor,
       "instRelMinor": instRelMinor,
       "instPatDevice": instPatDevice,
       "instPatName": instPatName,
       "instRelInterim": instRelInterim,
       "installHistoryTable": installHistoryTable,
       "installHistoryEntry": installHistoryEntry,
       "instHistIndex": instHistIndex,
       "instHistLine": instHistLine,
       "configFile": configFile,
       "licenceTable": licenceTable,
       "licenceEntry": licenceEntry,
       "licenceIndex": licenceIndex,
       "licenceStatus": licenceStatus,
       "licenceRelease": licenceRelease,
       "licenceMajor": licenceMajor,
       "licenceMinor": licenceMinor,
       "licencePassword": licencePassword,
       "licenceExpiry": licenceExpiry,
       "licenceInterim": licenceInterim,
       "file": file,
       "fileTable": fileTable,
       "fileEntry": fileEntry,
       "fileIndex": fileIndex,
       "fileName": fileName,
       "fileDevice": fileDevice,
       "fileCreationTime": fileCreationTime,
       "fileStatus": fileStatus,
       "fileSize": fileSize,
       "interfaces": interfaces,
       "protocols": protocols}
)
