# SNMP MIB module (HUAWEI-PRODUCT-ID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-PRODUCT-ID-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:37 2024
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

(h3cProductId,
 lanSw,
 mlsr,
 products,
 quidway) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cProductId",
    "lanSw",
    "mlsr",
    "products",
    "quidway")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QuidwayRouter_ObjectIdentity = ObjectIdentity
quidwayRouter = _QuidwayRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1)
)
_HwRouter_ObjectIdentity = ObjectIdentity
hwRouter = _HwRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 1)
)
_Eudemon_ObjectIdentity = ObjectIdentity
eudemon = _Eudemon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 100)
)
_Quidway1600_ObjectIdentity = ObjectIdentity
quidway1600 = _Quidway1600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 1600)
)
_Quidway1602_ObjectIdentity = ObjectIdentity
quidway1602 = _Quidway1602_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 1602)
)
_Quidway1612_ObjectIdentity = ObjectIdentity
quidway1612 = _Quidway1612_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 1612)
)
_Quidway1613_ObjectIdentity = ObjectIdentity
quidway1613 = _Quidway1613_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 1613)
)
_Quidway1614_ObjectIdentity = ObjectIdentity
quidway1614 = _Quidway1614_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 1614)
)
_Quidway1615_ObjectIdentity = ObjectIdentity
quidway1615 = _Quidway1615_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 1615)
)
_Quidway1760_ObjectIdentity = ObjectIdentity
quidway1760 = _Quidway1760_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 1760)
)
_Quidway1760B_ObjectIdentity = ObjectIdentity
quidway1760B = _Quidway1760B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 1761)
)
_Quidway2501_ObjectIdentity = ObjectIdentity
quidway2501 = _Quidway2501_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 2501)
)
_Quidway2509_ObjectIdentity = ObjectIdentity
quidway2509 = _Quidway2509_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 2509)
)
_Quidway2511_ObjectIdentity = ObjectIdentity
quidway2511 = _Quidway2511_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 2511)
)
_Quidway2501E_ObjectIdentity = ObjectIdentity
quidway2501E = _Quidway2501E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 2601)
)
_Quidway4001E_ObjectIdentity = ObjectIdentity
quidway4001E = _Quidway4001E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 2606)
)
_Quidway2509E_ObjectIdentity = ObjectIdentity
quidway2509E = _Quidway2509E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 2608)
)
_Quidway2511E_ObjectIdentity = ObjectIdentity
quidway2511E = _Quidway2511E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 2609)
)
_Quidway2610_ObjectIdentity = ObjectIdentity
quidway2610 = _Quidway2610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 2610)
)
_Quidway2611_ObjectIdentity = ObjectIdentity
quidway2611 = _Quidway2611_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 2611)
)
_Quidway2620_ObjectIdentity = ObjectIdentity
quidway2620 = _Quidway2620_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 2620)
)
_Quidway2621_ObjectIdentity = ObjectIdentity
quidway2621 = _Quidway2621_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 2621)
)
_Quidway2630_ObjectIdentity = ObjectIdentity
quidway2630 = _Quidway2630_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 2630)
)
_Quidway2631_ObjectIdentity = ObjectIdentity
quidway2631 = _Quidway2631_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 2631)
)
_Quidway3640_ObjectIdentity = ObjectIdentity
quidway3640 = _Quidway3640_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 3640)
)
_Quidway3680_ObjectIdentity = ObjectIdentity
quidway3680 = _Quidway3680_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 3680)
)
_Quidway4001_ObjectIdentity = ObjectIdentity
quidway4001 = _Quidway4001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 4001)
)
_Ar18_12_ObjectIdentity = ObjectIdentity
ar18_12 = _Ar18_12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 11812)
)
_Ar18_13_ObjectIdentity = ObjectIdentity
ar18_13 = _Ar18_13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 11813)
)
_Ar18_15_ObjectIdentity = ObjectIdentity
ar18_15 = _Ar18_15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 11815)
)
_Ar18_16_ObjectIdentity = ObjectIdentity
ar18_16 = _Ar18_16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 11816)
)
_Ar28_09_ObjectIdentity = ObjectIdentity
ar28_09 = _Ar28_09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 12809)
)
_Ar28_10_ObjectIdentity = ObjectIdentity
ar28_10 = _Ar28_10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 12810)
)
_Ar28_11_ObjectIdentity = ObjectIdentity
ar28_11 = _Ar28_11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 12811)
)
_Ar28_30_ObjectIdentity = ObjectIdentity
ar28_30 = _Ar28_30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 12830)
)
_Ar28_31_ObjectIdentity = ObjectIdentity
ar28_31 = _Ar28_31_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 12831)
)
_Ar28_40_ObjectIdentity = ObjectIdentity
ar28_40 = _Ar28_40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 12840)
)
_Ar28_80_ObjectIdentity = ObjectIdentity
ar28_80 = _Ar28_80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 1, 1, 12880)
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
_S3026E_FM_ObjectIdentity = ObjectIdentity
s3026E_FM = _S3026E_FM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 25)
)
_S3026E_FS_ObjectIdentity = ObjectIdentity
s3026E_FS = _S3026E_FS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 26)
)
_S3526E_FM_ObjectIdentity = ObjectIdentity
s3526E_FM = _S3526E_FM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 27)
)
_S3526E_FS_ObjectIdentity = ObjectIdentity
s3526E_FS = _S3526E_FS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 28)
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
_Vdg10_40_ObjectIdentity = ObjectIdentity
vdg10_40 = _Vdg10_40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 52)
)
_Vdg10_41_ObjectIdentity = ObjectIdentity
vdg10_41 = _Vdg10_41_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 53)
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
_S2008_EI_ObjectIdentity = ObjectIdentity
s2008_EI = _S2008_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 1)
)
_S2016_EI_ObjectIdentity = ObjectIdentity
s2016_EI = _S2016_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 2)
)
_S2403H_EI_ObjectIdentity = ObjectIdentity
s2403H_EI = _S2403H_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 3)
)
_S3026PWR_ObjectIdentity = ObjectIdentity
s3026PWR = _S3026PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 4)
)
_Secpath1000_ObjectIdentity = ObjectIdentity
secpath1000 = _Secpath1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 5)
)
_Ar18_35_ObjectIdentity = ObjectIdentity
ar18_35 = _Ar18_35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 6)
)
_S3552F_HI_ObjectIdentity = ObjectIdentity
s3552F_HI = _S3552F_HI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 7)
)
_Secpath10_ObjectIdentity = ObjectIdentity
secpath10 = _Secpath10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 8)
)
_S3924_SI_ObjectIdentity = ObjectIdentity
s3924_SI = _S3924_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 9)
)
_S3928P_SI_ObjectIdentity = ObjectIdentity
s3928P_SI = _S3928P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 10)
)
_S3952P_SI_ObjectIdentity = ObjectIdentity
s3952P_SI = _S3952P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 11)
)
_S3928TP_SI_ObjectIdentity = ObjectIdentity
s3928TP_SI = _S3928TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 12)
)
_S3928P_EI_ObjectIdentity = ObjectIdentity
s3928P_EI = _S3928P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 13)
)
_S3952P_EI_ObjectIdentity = ObjectIdentity
s3952P_EI = _S3952P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 14)
)
_S3928P_PWR_EI_ObjectIdentity = ObjectIdentity
s3928P_PWR_EI = _S3928P_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 15)
)
_S3952P_PWR_EI_ObjectIdentity = ObjectIdentity
s3952P_PWR_EI = _S3952P_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 16)
)
_S3928F_EI_ObjectIdentity = ObjectIdentity
s3928F_EI = _S3928F_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 17)
)
_S5600M_ObjectIdentity = ObjectIdentity
s5600M = _S5600M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 18)
)
_Ar18_50_ObjectIdentity = ObjectIdentity
ar18_50 = _Ar18_50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 19)
)
_Ar18_33E_ObjectIdentity = ObjectIdentity
ar18_33E = _Ar18_33E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 20)
)
_Ar18_34E_ObjectIdentity = ObjectIdentity
ar18_34E = _Ar18_34E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 21)
)
_S8508_ObjectIdentity = ObjectIdentity
s8508 = _S8508_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 22)
)
_Secpath100N_ObjectIdentity = ObjectIdentity
secpath100N = _Secpath100N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 23)
)
_Secpath100V_ObjectIdentity = ObjectIdentity
secpath100V = _Secpath100V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 24)
)
_Secpath100F_ObjectIdentity = ObjectIdentity
secpath100F = _Secpath100F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 25)
)
_Secpath1000F_ObjectIdentity = ObjectIdentity
secpath1000F = _Secpath1000F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 26)
)
_Secpath500F_ObjectIdentity = ObjectIdentity
secpath500F = _Secpath500F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 27)
)
_Secpath10F_ObjectIdentity = ObjectIdentity
secpath10F = _Secpath10F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 28)
)
_Secpath100FS_ObjectIdentity = ObjectIdentity
secpath100FS = _Secpath100FS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 29)
)
_Secpath100FE_ObjectIdentity = ObjectIdentity
secpath100FE = _Secpath100FE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 30)
)
_Secpath100FW_ObjectIdentity = ObjectIdentity
secpath100FW = _Secpath100FW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 31)
)
_Secpath1800FS_ObjectIdentity = ObjectIdentity
secpath1800FS = _Secpath1800FS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 32)
)
_Secpath1800FE_ObjectIdentity = ObjectIdentity
secpath1800FE = _Secpath1800FE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 33)
)
_Sr8805_ObjectIdentity = ObjectIdentity
sr8805 = _Sr8805_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 40)
)
_Sr8808_ObjectIdentity = ObjectIdentity
sr8808 = _Sr8808_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 41)
)
_Sr8812_ObjectIdentity = ObjectIdentity
sr8812 = _Sr8812_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 42)
)
_S5624P_ObjectIdentity = ObjectIdentity
s5624P = _S5624P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 43)
)
_S5624P_PWR_ObjectIdentity = ObjectIdentity
s5624P_PWR = _S5624P_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 44)
)
_S5648P_ObjectIdentity = ObjectIdentity
s5648P = _S5648P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 45)
)
_S5648P_PWR_ObjectIdentity = ObjectIdentity
s5648P_PWR = _S5648P_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 46)
)
_S2008C_ObjectIdentity = ObjectIdentity
s2008C = _S2008C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 47)
)
_S2016C_ObjectIdentity = ObjectIdentity
s2016C = _S2016C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 48)
)
_S2024C_ObjectIdentity = ObjectIdentity
s2024C = _S2024C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 49)
)
_Ar18_13V_ObjectIdentity = ObjectIdentity
ar18_13V = _Ar18_13V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 50)
)
_Ar18_18V_ObjectIdentity = ObjectIdentity
ar18_18V = _Ar18_18V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 51)
)
_IsPath1000_ObjectIdentity = ObjectIdentity
isPath1000 = _IsPath1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 52)
)
_Ar18_20S_ObjectIdentity = ObjectIdentity
ar18_20S = _Ar18_20S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 53)
)
_Wellhope_ObjectIdentity = ObjectIdentity
wellhope = _Wellhope_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 54)
)
_Tph12616_ObjectIdentity = ObjectIdentity
tph12616 = _Tph12616_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 54, 1)
)
_Tph10408_ObjectIdentity = ObjectIdentity
tph10408 = _Tph10408_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 54, 2)
)
_Tph10404_ObjectIdentity = ObjectIdentity
tph10404 = _Tph10404_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 54, 3)
)
_Tph10402_ObjectIdentity = ObjectIdentity
tph10402 = _Tph10402_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 54, 4)
)
_Trt7554_ObjectIdentity = ObjectIdentity
trt7554 = _Trt7554_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 54, 5)
)
_Tab3740_ObjectIdentity = ObjectIdentity
tab3740 = _Tab3740_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 54, 6)
)
_Tab3680_ObjectIdentity = ObjectIdentity
tab3680 = _Tab3680_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 54, 7)
)
_Tab2609_ObjectIdentity = ObjectIdentity
tab2609 = _Tab2609_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 54, 8)
)
_Tab2611_ObjectIdentity = ObjectIdentity
tab2611 = _Tab2611_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 54, 9)
)
_Tab2631_ObjectIdentity = ObjectIdentity
tab2631 = _Tab2631_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 54, 10)
)
_Ts6061r_ObjectIdentity = ObjectIdentity
ts6061r = _Ts6061r_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 54, 11)
)
_Ts3262_ObjectIdentity = ObjectIdentity
ts3262 = _Ts3262_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 54, 12)
)
_Ts2502_ObjectIdentity = ObjectIdentity
ts2502 = _Ts2502_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 54, 13)
)
_Ts2262_ObjectIdentity = ObjectIdentity
ts2262 = _Ts2262_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 54, 14)
)
_Xe200_ObjectIdentity = ObjectIdentity
xe200 = _Xe200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 55)
)
_Xe2000_ObjectIdentity = ObjectIdentity
xe2000 = _Xe2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 56)
)
_E026T_ObjectIdentity = ObjectIdentity
e026T = _E026T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 57)
)
_E008_FE_ObjectIdentity = ObjectIdentity
e008_FE = _E008_FE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 58)
)
_E017_FE_ObjectIdentity = ObjectIdentity
e017_FE = _E017_FE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 59)
)
_E026_FE_ObjectIdentity = ObjectIdentity
e026_FE = _E026_FE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 60)
)
_Ar28_12_ObjectIdentity = ObjectIdentity
ar28_12 = _Ar28_12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 61)
)
_Ar28_13_ObjectIdentity = ObjectIdentity
ar28_13 = _Ar28_13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 62)
)
_Ar28_14_ObjectIdentity = ObjectIdentity
ar28_14 = _Ar28_14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 63)
)
_Ar18_10_ObjectIdentity = ObjectIdentity
ar18_10 = _Ar18_10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 64)
)
_Ar18_21_ObjectIdentity = ObjectIdentity
ar18_21 = _Ar18_21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 65)
)
_Ar18_21A_ObjectIdentity = ObjectIdentity
ar18_21A = _Ar18_21A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 66)
)
_Ar18_21B_ObjectIdentity = ObjectIdentity
ar18_21B = _Ar18_21B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 67)
)
_Ar18_21C_ObjectIdentity = ObjectIdentity
ar18_21C = _Ar18_21C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 68)
)
_Ar18_22_ObjectIdentity = ObjectIdentity
ar18_22 = _Ar18_22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 69)
)
_Ar18_22_8_ObjectIdentity = ObjectIdentity
ar18_22_8 = _Ar18_22_8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 70)
)
_Ar18_22_24_ObjectIdentity = ObjectIdentity
ar18_22_24 = _Ar18_22_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 71)
)
_Ar18_23_1_ObjectIdentity = ObjectIdentity
ar18_23_1 = _Ar18_23_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 72)
)
_Ar18_30E_ObjectIdentity = ObjectIdentity
ar18_30E = _Ar18_30E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 73)
)
_Ar18_31E_ObjectIdentity = ObjectIdentity
ar18_31E = _Ar18_31E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 74)
)
_Ar18_32E_ObjectIdentity = ObjectIdentity
ar18_32E = _Ar18_32E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 75)
)
_Ar18_35E_ObjectIdentity = ObjectIdentity
ar18_35E = _Ar18_35E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 76)
)
_Ar18_36E_ObjectIdentity = ObjectIdentity
ar18_36E = _Ar18_36E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 77)
)
_Ar18_37E_ObjectIdentity = ObjectIdentity
ar18_37E = _Ar18_37E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 78)
)
_Ar18_52_ObjectIdentity = ObjectIdentity
ar18_52 = _Ar18_52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 79)
)
_S6502_ObjectIdentity = ObjectIdentity
s6502 = _S6502_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 80)
)
_S5124P_EI_ObjectIdentity = ObjectIdentity
s5124P_EI = _S5124P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 81)
)
_S5126C_EI_ObjectIdentity = ObjectIdentity
s5126C_EI = _S5126C_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 82)
)
_S5148P_EI_ObjectIdentity = ObjectIdentity
s5148P_EI = _S5148P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 83)
)
_S5150C_EI_ObjectIdentity = ObjectIdentity
s5150C_EI = _S5150C_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 84)
)
_S5116P_SI_ObjectIdentity = ObjectIdentity
s5116P_SI = _S5116P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 85)
)
_S5124P_SI_ObjectIdentity = ObjectIdentity
s5124P_SI = _S5124P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 86)
)
_S5148P_SI_ObjectIdentity = ObjectIdentity
s5148P_SI = _S5148P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 87)
)
_Ar4620E_ObjectIdentity = ObjectIdentity
ar4620E = _Ar4620E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 88)
)
_Ar4640E_ObjectIdentity = ObjectIdentity
ar4640E = _Ar4640E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 89)
)
_Ar4680E_ObjectIdentity = ObjectIdentity
ar4680E = _Ar4680E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 90)
)
_Ar18_22s_8_ObjectIdentity = ObjectIdentity
ar18_22s_8 = _Ar18_22s_8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 91)
)
_Ar18_23s_1_ObjectIdentity = ObjectIdentity
ar18_23s_1 = _Ar18_23s_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 92)
)
_SecEngineP500_ObjectIdentity = ObjectIdentity
secEngineP500 = _SecEngineP500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 93)
)
_S2108_SI_ObjectIdentity = ObjectIdentity
s2108_SI = _S2108_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 94)
)
_S2116_SI_ObjectIdentity = ObjectIdentity
s2116_SI = _S2116_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 95)
)
_S2126_SI_ObjectIdentity = ObjectIdentity
s2126_SI = _S2126_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 96)
)
_S2108_EI_ObjectIdentity = ObjectIdentity
s2108_EI = _S2108_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 97)
)
_S2116_EI_ObjectIdentity = ObjectIdentity
s2116_EI = _S2116_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 98)
)
_S2126_EI_ObjectIdentity = ObjectIdentity
s2126_EI = _S2126_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 99)
)
_S5624F_ObjectIdentity = ObjectIdentity
s5624F = _S5624F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 100)
)
_S3224P_ObjectIdentity = ObjectIdentity
s3224P = _S3224P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 101)
)
_S3226T_ObjectIdentity = ObjectIdentity
s3226T = _S3226T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 102)
)
_S3226P_ObjectIdentity = ObjectIdentity
s3226P = _S3226P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 103)
)
_S3250T_ObjectIdentity = ObjectIdentity
s3250T = _S3250T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 104)
)
_S3250P_ObjectIdentity = ObjectIdentity
s3250P = _S3250P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 105)
)
_S3108T_ObjectIdentity = ObjectIdentity
s3108T = _S3108T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 106)
)
_S3116T_ObjectIdentity = ObjectIdentity
s3116T = _S3116T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 107)
)
_S3126T_ObjectIdentity = ObjectIdentity
s3126T = _S3126T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 108)
)
_S3108C_ObjectIdentity = ObjectIdentity
s3108C = _S3108C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 109)
)
_S3116C_ObjectIdentity = ObjectIdentity
s3116C = _S3116C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 110)
)
_S3126C_ObjectIdentity = ObjectIdentity
s3126C = _S3126C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 111)
)
_Ar28_12B_ObjectIdentity = ObjectIdentity
ar28_12B = _Ar28_12B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 112)
)
_SecBladeIDS_ObjectIdentity = ObjectIdentity
secBladeIDS = _SecBladeIDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 113)
)
_SecBladeIPS_ObjectIdentity = ObjectIdentity
secBladeIPS = _SecBladeIPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 114)
)
_SecEngineD500_ObjectIdentity = ObjectIdentity
secEngineD500 = _SecEngineD500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 115)
)
_S3928TP_V6_ObjectIdentity = ObjectIdentity
s3928TP_V6 = _S3928TP_V6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 116)
)
_S3928P_V6_ObjectIdentity = ObjectIdentity
s3928P_V6 = _S3928P_V6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 117)
)
_S3952P_V6_ObjectIdentity = ObjectIdentity
s3952P_V6 = _S3952P_V6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 118)
)
_S3928F_V6_ObjectIdentity = ObjectIdentity
s3928F_V6 = _S3928F_V6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 119)
)
_S5524P_ObjectIdentity = ObjectIdentity
s5524P = _S5524P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 120)
)
_S5524F_ObjectIdentity = ObjectIdentity
s5524F = _S5524F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 121)
)
_XE7000_ObjectIdentity = ObjectIdentity
xE7000 = _XE7000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 122)
)
_Vg10_40_ObjectIdentity = ObjectIdentity
vg10_40 = _Vg10_40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 123)
)
_Vg10_41_ObjectIdentity = ObjectIdentity
vg10_41 = _Vg10_41_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 124)
)
_Vg20_16_ObjectIdentity = ObjectIdentity
vg20_16 = _Vg20_16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 125)
)
_Vg20_32_ObjectIdentity = ObjectIdentity
vg20_32 = _Vg20_32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 126)
)
_Vg20_08L_ObjectIdentity = ObjectIdentity
vg20_08L = _Vg20_08L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 127)
)
_Vg80_20_ObjectIdentity = ObjectIdentity
vg80_20 = _Vg80_20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 128)
)
_Vg80_20T_ObjectIdentity = ObjectIdentity
vg80_20T = _Vg80_20T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 129)
)
_S2008CT_ObjectIdentity = ObjectIdentity
s2008CT = _S2008CT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 130)
)
_S2008CP_ObjectIdentity = ObjectIdentity
s2008CP = _S2008CP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 131)
)
_SecBladeFW_ObjectIdentity = ObjectIdentity
secBladeFW = _SecBladeFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 132)
)
_SecBladeVPN_ObjectIdentity = ObjectIdentity
secBladeVPN = _SecBladeVPN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 133)
)
_SecEngineD200_ObjectIdentity = ObjectIdentity
secEngineD200 = _SecEngineD200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 134)
)
_Intransa_ObjectIdentity = ObjectIdentity
intransa = _Intransa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 135)
)
_Ix5000_ObjectIdentity = ObjectIdentity
ix5000 = _Ix5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 135, 1)
)
_SJW59_ObjectIdentity = ObjectIdentity
sJW59 = _SJW59_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 136)
)
_Vg21_08_ObjectIdentity = ObjectIdentity
vg21_08 = _Vg21_08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 137)
)
_Ar19_61_ObjectIdentity = ObjectIdentity
ar19_61 = _Ar19_61_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 138)
)
_Ar19_62_ObjectIdentity = ObjectIdentity
ar19_62 = _Ar19_62_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 139)
)
_Ar29_01_ObjectIdentity = ObjectIdentity
ar29_01 = _Ar29_01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 140)
)
_Ar29_21_ObjectIdentity = ObjectIdentity
ar29_21 = _Ar29_21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 141)
)
_Ar29_41_ObjectIdentity = ObjectIdentity
ar29_41 = _Ar29_41_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 142)
)
_Ar29_61_ObjectIdentity = ObjectIdentity
ar29_61 = _Ar29_61_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 143)
)
_Ar49_45_ObjectIdentity = ObjectIdentity
ar49_45 = _Ar49_45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 144)
)
_Ar49_65_ObjectIdentity = ObjectIdentity
ar49_65 = _Ar49_65_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 145)
)
_S5112P_EI_ObjectIdentity = ObjectIdentity
s5112P_EI = _S5112P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 146)
)
_S5112C_EI_ObjectIdentity = ObjectIdentity
s5112C_EI = _S5112C_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 147)
)
_S5228C_ObjectIdentity = ObjectIdentity
s5228C = _S5228C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 148)
)
_S5252C_ObjectIdentity = ObjectIdentity
s5252C = _S5252C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 149)
)
_S5228C_PWR_ObjectIdentity = ObjectIdentity
s5228C_PWR = _S5228C_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 150)
)
_S5252C_PWR_ObjectIdentity = ObjectIdentity
s5252C_PWR = _S5252C_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 151)
)
_S2008_HI_ObjectIdentity = ObjectIdentity
s2008_HI = _S2008_HI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 152)
)
_S2016_HI_ObjectIdentity = ObjectIdentity
s2016_HI = _S2016_HI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 153)
)
_S2403H_HI_ObjectIdentity = ObjectIdentity
s2403H_HI = _S2403H_HI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 154)
)
_Vg31_08_ObjectIdentity = ObjectIdentity
vg31_08 = _Vg31_08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 155)
)
_S8508V_ObjectIdentity = ObjectIdentity
s8508V = _S8508V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 156)
)
_E126_ObjectIdentity = ObjectIdentity
e126 = _E126_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 157)
)
_S3126TP_ObjectIdentity = ObjectIdentity
s3126TP = _S3126TP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 158)
)
_E328_ObjectIdentity = ObjectIdentity
e328 = _E328_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 159)
)
_E352_ObjectIdentity = ObjectIdentity
e352 = _E352_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 160)
)
_S3928P_PWR_SI_ObjectIdentity = ObjectIdentity
s3928P_PWR_SI = _S3928P_PWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 161)
)
_Falcon_ObjectIdentity = ObjectIdentity
falcon = _Falcon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 162)
)
_Ix1000_ObjectIdentity = ObjectIdentity
ix1000 = _Ix1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 162, 1)
)
_S8502_ObjectIdentity = ObjectIdentity
s8502 = _S8502_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 163)
)
_Sr8802_ObjectIdentity = ObjectIdentity
sr8802 = _Sr8802_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 164)
)
_S3328P_SI_ObjectIdentity = ObjectIdentity
s3328P_SI = _S3328P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 165)
)
_S3352P_SI_ObjectIdentity = ObjectIdentity
s3352P_SI = _S3352P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 166)
)
_S3328TP_SI_ObjectIdentity = ObjectIdentity
s3328TP_SI = _S3328TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 167)
)
_S3328P_PWR_SI_ObjectIdentity = ObjectIdentity
s3328P_PWR_SI = _S3328P_PWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 168)
)
_S3328P_EI_ObjectIdentity = ObjectIdentity
s3328P_EI = _S3328P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 169)
)
_S3352P_EI_ObjectIdentity = ObjectIdentity
s3352P_EI = _S3352P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 170)
)
_S3328P_PWR_EI_ObjectIdentity = ObjectIdentity
s3328P_PWR_EI = _S3328P_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 171)
)
_S3352P_PWR_EI_ObjectIdentity = ObjectIdentity
s3352P_PWR_EI = _S3352P_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 172)
)
_S3328F_EI_ObjectIdentity = ObjectIdentity
s3328F_EI = _S3328F_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 173)
)
_S6502ME_ObjectIdentity = ObjectIdentity
s6502ME = _S6502ME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 174)
)
_S5528C_EI_ObjectIdentity = ObjectIdentity
s5528C_EI = _S5528C_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 175)
)
_S5552C_EI_ObjectIdentity = ObjectIdentity
s5552C_EI = _S5552C_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 176)
)
_S5528C_PWR_EI_ObjectIdentity = ObjectIdentity
s5528C_PWR_EI = _S5528C_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 177)
)
_S5552C_PWR_EI_ObjectIdentity = ObjectIdentity
s5552C_PWR_EI = _S5552C_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 178)
)
_S5528F_EI_ObjectIdentity = ObjectIdentity
s5528F_EI = _S5528F_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 179)
)
_S5528C_EI_DC_ObjectIdentity = ObjectIdentity
s5528C_EI_DC = _S5528C_EI_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 180)
)
_E126_SI_ObjectIdentity = ObjectIdentity
e126_SI = _E126_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 181)
)
_Dr814_ObjectIdentity = ObjectIdentity
dr814 = _Dr814_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 182)
)
_Dr814q_ObjectIdentity = ObjectIdentity
dr814q = _Dr814q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 183)
)
_Wdr854g_ObjectIdentity = ObjectIdentity
wdr854g = _Wdr854g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 184)
)
_Vdr824g_ObjectIdentity = ObjectIdentity
vdr824g = _Vdr824g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 185)
)
_Vdr824_ObjectIdentity = ObjectIdentity
vdr824 = _Vdr824_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 186)
)
_Vdr744_ObjectIdentity = ObjectIdentity
vdr744 = _Vdr744_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 187)
)
_Dr744_ObjectIdentity = ObjectIdentity
dr744 = _Dr744_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 188)
)
_S6502M_ObjectIdentity = ObjectIdentity
s6502M = _S6502M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 189)
)
_S6501M_GT_ObjectIdentity = ObjectIdentity
s6501M_GT = _S6501M_GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 190)
)
_S6501M_GP_ObjectIdentity = ObjectIdentity
s6501M_GP = _S6501M_GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 191)
)
_S8505_V5_ObjectIdentity = ObjectIdentity
s8505_V5 = _S8505_V5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 192)
)
_S8512_V5_ObjectIdentity = ObjectIdentity
s8512_V5 = _S8512_V5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 193)
)
_S8508_V5_ObjectIdentity = ObjectIdentity
s8508_V5 = _S8508_V5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 194)
)
_S8508V_V5_ObjectIdentity = ObjectIdentity
s8508V_V5 = _S8508V_V5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 195)
)
_S8502_V5_ObjectIdentity = ObjectIdentity
s8502_V5 = _S8502_V5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 196)
)
_S6502_V5_ObjectIdentity = ObjectIdentity
s6502_V5 = _S6502_V5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 197)
)
_S2008TP_EA_ObjectIdentity = ObjectIdentity
s2008TP_EA = _S2008TP_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 198)
)
_S2016TP_EA_ObjectIdentity = ObjectIdentity
s2016TP_EA = _S2016TP_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 199)
)
_S2403TP_EA_ObjectIdentity = ObjectIdentity
s2403TP_EA = _S2403TP_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 200)
)
_S2403TP_PWR_EA_ObjectIdentity = ObjectIdentity
s2403TP_PWR_EA = _S2403TP_PWR_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 201)
)
_S2008TP_MI_ObjectIdentity = ObjectIdentity
s2008TP_MI = _S2008TP_MI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 202)
)
_S2016TP_MI_ObjectIdentity = ObjectIdentity
s2016TP_MI = _S2016TP_MI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 203)
)
_S2403TP_MI_ObjectIdentity = ObjectIdentity
s2403TP_MI = _S2403TP_MI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 204)
)
_S7802_ObjectIdentity = ObjectIdentity
s7802 = _S7802_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 205)
)
_S7803_ObjectIdentity = ObjectIdentity
s7803 = _S7803_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 206)
)
_S7806_ObjectIdentity = ObjectIdentity
s7806 = _S7806_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 207)
)
_S7806_V_ObjectIdentity = ObjectIdentity
s7806_V = _S7806_V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 208)
)
_S7810_ObjectIdentity = ObjectIdentity
s7810 = _S7810_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 209)
)
_S2016TP_PWR_EA_ObjectIdentity = ObjectIdentity
s2016TP_PWR_EA = _S2016TP_PWR_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 210)
)
_S3552P_EA_ObjectIdentity = ObjectIdentity
s3552P_EA = _S3552P_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 211)
)
_S3528P_EA_ObjectIdentity = ObjectIdentity
s3528P_EA = _S3528P_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 212)
)
_S3528TP_EA_ObjectIdentity = ObjectIdentity
s3528TP_EA = _S3528TP_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 213)
)
_S3528F_EA_ObjectIdentity = ObjectIdentity
s3528F_EA = _S3528F_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 214)
)
_S3552f_ea_ObjectIdentity = ObjectIdentity
s3552f_ea = _S3552f_ea_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 215)
)
_S6902_ObjectIdentity = ObjectIdentity
s6902 = _S6902_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 216)
)
_S6903_ObjectIdentity = ObjectIdentity
s6903 = _S6903_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 217)
)
_S6906_ObjectIdentity = ObjectIdentity
s6906 = _S6906_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 218)
)
_S6906R_ObjectIdentity = ObjectIdentity
s6906R = _S6906R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 219)
)
_S3928P_SI_ACDC_ObjectIdentity = ObjectIdentity
s3928P_SI_ACDC = _S3928P_SI_ACDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 220)
)
_S5540F_ObjectIdentity = ObjectIdentity
s5540F = _S5540F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 221)
)
_S5540C_ObjectIdentity = ObjectIdentity
s5540C = _S5540C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 222)
)
_S5556C_ObjectIdentity = ObjectIdentity
s5556C = _S5556C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 223)
)
_Ar19_10_ObjectIdentity = ObjectIdentity
ar19_10 = _Ar19_10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 224)
)
_Ar19_13_ObjectIdentity = ObjectIdentity
ar19_13 = _Ar19_13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 225)
)
_Ar19_15_ObjectIdentity = ObjectIdentity
ar19_15 = _Ar19_15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 226)
)
_S3552P_SI_ObjectIdentity = ObjectIdentity
s3552P_SI = _S3552P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 227)
)
_S3528P_SI_ObjectIdentity = ObjectIdentity
s3528P_SI = _S3528P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 228)
)
_S5628C_HI_AC_ObjectIdentity = ObjectIdentity
s5628C_HI_AC = _S5628C_HI_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 229)
)
_S5628C_HI_DC_ObjectIdentity = ObjectIdentity
s5628C_HI_DC = _S5628C_HI_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 230)
)
_S5652C_HI_AC_ObjectIdentity = ObjectIdentity
s5652C_HI_AC = _S5652C_HI_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 231)
)
_S5628F_HI_ObjectIdentity = ObjectIdentity
s5628F_HI = _S5628F_HI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 232)
)
_S5628C_PWR_HI_ObjectIdentity = ObjectIdentity
s5628C_PWR_HI = _S5628C_PWR_HI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 233)
)
_S5652C_PWR_HI_ObjectIdentity = ObjectIdentity
s5652C_PWR_HI = _S5652C_PWR_HI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 234)
)
_SecBlade_LSQ1FWBSC1_ObjectIdentity = ObjectIdentity
secBlade_LSQ1FWBSC1 = _SecBlade_LSQ1FWBSC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 235)
)
_SecBlade_LSQ1NSMSC1_ObjectIdentity = ObjectIdentity
secBlade_LSQ1NSMSC1 = _SecBlade_LSQ1NSMSC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 236)
)
_S7803_L_ObjectIdentity = ObjectIdentity
s7803_L = _S7803_L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 237)
)
_S6503_v5_ObjectIdentity = ObjectIdentity
s6503_v5 = _S6503_v5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 238)
)
_S6506_v5_ObjectIdentity = ObjectIdentity
s6506_v5 = _S6506_v5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 239)
)
_S6506R_v5_ObjectIdentity = ObjectIdentity
s6506R_v5 = _S6506R_v5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 240)
)
_Ar19_03_ObjectIdentity = ObjectIdentity
ar19_03 = _Ar19_03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 241)
)
_Ar19_05_ObjectIdentity = ObjectIdentity
ar19_05 = _Ar19_05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 242)
)
_S7806_L_ObjectIdentity = ObjectIdentity
s7806_L = _S7806_L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 243)
)
_Ar29_11_ObjectIdentity = ObjectIdentity
ar29_11 = _Ar29_11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 1, 244)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-PRODUCT-ID-MIB",
    **{"quidwayRouter": quidwayRouter,
       "hwRouter": hwRouter,
       "eudemon": eudemon,
       "quidway1600": quidway1600,
       "quidway1602": quidway1602,
       "quidway1612": quidway1612,
       "quidway1613": quidway1613,
       "quidway1614": quidway1614,
       "quidway1615": quidway1615,
       "quidway1760": quidway1760,
       "quidway1760B": quidway1760B,
       "quidway2501": quidway2501,
       "quidway2509": quidway2509,
       "quidway2511": quidway2511,
       "quidway2501E": quidway2501E,
       "quidway4001E": quidway4001E,
       "quidway2509E": quidway2509E,
       "quidway2511E": quidway2511E,
       "quidway2610": quidway2610,
       "quidway2611": quidway2611,
       "quidway2620": quidway2620,
       "quidway2621": quidway2621,
       "quidway2630": quidway2630,
       "quidway2631": quidway2631,
       "quidway3640": quidway3640,
       "quidway3680": quidway3680,
       "quidway4001": quidway4001,
       "ar18-12": ar18_12,
       "ar18-13": ar18_13,
       "ar18-15": ar18_15,
       "ar18-16": ar18_16,
       "ar28-09": ar28_09,
       "ar28-10": ar28_10,
       "ar28-11": ar28_11,
       "ar28-30": ar28_30,
       "ar28-31": ar28_31,
       "ar28-40": ar28_40,
       "ar28-80": ar28_80,
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
       "s3026E-FM": s3026E_FM,
       "s3026E-FS": s3026E_FS,
       "s3526E-FM": s3526E_FM,
       "s3526E-FS": s3526E_FS,
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
       "ar46-20": ar46_20,
       "ar46-40": ar46_40,
       "ar46-80": ar46_80,
       "vdg10-40": vdg10_40,
       "vdg10-41": vdg10_41,
       "ar18-18": ar18_18,
       "ar18-20": ar18_20,
       "ar18-30": ar18_30,
       "ar18-31": ar18_31,
       "ar18-32": ar18_32,
       "ar18-33": ar18_33,
       "ar18-34": ar18_34,
       "ne5000": ne5000,
       "s2008-EI": s2008_EI,
       "s2016-EI": s2016_EI,
       "s2403H-EI": s2403H_EI,
       "s3026PWR": s3026PWR,
       "secpath1000": secpath1000,
       "ar18-35": ar18_35,
       "s3552F-HI": s3552F_HI,
       "secpath10": secpath10,
       "s3924-SI": s3924_SI,
       "s3928P-SI": s3928P_SI,
       "s3952P-SI": s3952P_SI,
       "s3928TP-SI": s3928TP_SI,
       "s3928P-EI": s3928P_EI,
       "s3952P-EI": s3952P_EI,
       "s3928P-PWR-EI": s3928P_PWR_EI,
       "s3952P-PWR-EI": s3952P_PWR_EI,
       "s3928F-EI": s3928F_EI,
       "s5600M": s5600M,
       "ar18-50": ar18_50,
       "ar18-33E": ar18_33E,
       "ar18-34E": ar18_34E,
       "s8508": s8508,
       "secpath100N": secpath100N,
       "secpath100V": secpath100V,
       "secpath100F": secpath100F,
       "secpath1000F": secpath1000F,
       "secpath500F": secpath500F,
       "secpath10F": secpath10F,
       "secpath100FS": secpath100FS,
       "secpath100FE": secpath100FE,
       "secpath100FW": secpath100FW,
       "secpath1800FS": secpath1800FS,
       "secpath1800FE": secpath1800FE,
       "sr8805": sr8805,
       "sr8808": sr8808,
       "sr8812": sr8812,
       "s5624P": s5624P,
       "s5624P-PWR": s5624P_PWR,
       "s5648P": s5648P,
       "s5648P-PWR": s5648P_PWR,
       "s2008C": s2008C,
       "s2016C": s2016C,
       "s2024C": s2024C,
       "ar18-13V": ar18_13V,
       "ar18-18V": ar18_18V,
       "isPath1000": isPath1000,
       "ar18-20S": ar18_20S,
       "wellhope": wellhope,
       "tph12616": tph12616,
       "tph10408": tph10408,
       "tph10404": tph10404,
       "tph10402": tph10402,
       "trt7554": trt7554,
       "tab3740": tab3740,
       "tab3680": tab3680,
       "tab2609": tab2609,
       "tab2611": tab2611,
       "tab2631": tab2631,
       "ts6061r": ts6061r,
       "ts3262": ts3262,
       "ts2502": ts2502,
       "ts2262": ts2262,
       "xe200": xe200,
       "xe2000": xe2000,
       "e026T": e026T,
       "e008-FE": e008_FE,
       "e017-FE": e017_FE,
       "e026-FE": e026_FE,
       "ar28-12": ar28_12,
       "ar28-13": ar28_13,
       "ar28-14": ar28_14,
       "ar18-10": ar18_10,
       "ar18-21": ar18_21,
       "ar18-21A": ar18_21A,
       "ar18-21B": ar18_21B,
       "ar18-21C": ar18_21C,
       "ar18-22": ar18_22,
       "ar18-22-8": ar18_22_8,
       "ar18-22-24": ar18_22_24,
       "ar18-23-1": ar18_23_1,
       "ar18-30E": ar18_30E,
       "ar18-31E": ar18_31E,
       "ar18-32E": ar18_32E,
       "ar18-35E": ar18_35E,
       "ar18-36E": ar18_36E,
       "ar18-37E": ar18_37E,
       "ar18-52": ar18_52,
       "s6502": s6502,
       "s5124P-EI": s5124P_EI,
       "s5126C-EI": s5126C_EI,
       "s5148P-EI": s5148P_EI,
       "s5150C-EI": s5150C_EI,
       "s5116P-SI": s5116P_SI,
       "s5124P-SI": s5124P_SI,
       "s5148P-SI": s5148P_SI,
       "ar4620E": ar4620E,
       "ar4640E": ar4640E,
       "ar4680E": ar4680E,
       "ar18-22s-8": ar18_22s_8,
       "ar18-23s-1": ar18_23s_1,
       "secEngineP500": secEngineP500,
       "s2108-SI": s2108_SI,
       "s2116-SI": s2116_SI,
       "s2126-SI": s2126_SI,
       "s2108-EI": s2108_EI,
       "s2116-EI": s2116_EI,
       "s2126-EI": s2126_EI,
       "s5624F": s5624F,
       "s3224P": s3224P,
       "s3226T": s3226T,
       "s3226P": s3226P,
       "s3250T": s3250T,
       "s3250P": s3250P,
       "s3108T": s3108T,
       "s3116T": s3116T,
       "s3126T": s3126T,
       "s3108C": s3108C,
       "s3116C": s3116C,
       "s3126C": s3126C,
       "ar28-12B": ar28_12B,
       "secBladeIDS": secBladeIDS,
       "secBladeIPS": secBladeIPS,
       "secEngineD500": secEngineD500,
       "s3928TP-V6": s3928TP_V6,
       "s3928P-V6": s3928P_V6,
       "s3952P-V6": s3952P_V6,
       "s3928F-V6": s3928F_V6,
       "s5524P": s5524P,
       "s5524F": s5524F,
       "xE7000": xE7000,
       "vg10-40": vg10_40,
       "vg10-41": vg10_41,
       "vg20-16": vg20_16,
       "vg20-32": vg20_32,
       "vg20-08L": vg20_08L,
       "vg80-20": vg80_20,
       "vg80-20T": vg80_20T,
       "s2008CT": s2008CT,
       "s2008CP": s2008CP,
       "secBladeFW": secBladeFW,
       "secBladeVPN": secBladeVPN,
       "secEngineD200": secEngineD200,
       "intransa": intransa,
       "ix5000": ix5000,
       "sJW59": sJW59,
       "vg21-08": vg21_08,
       "ar19-61": ar19_61,
       "ar19-62": ar19_62,
       "ar29-01": ar29_01,
       "ar29-21": ar29_21,
       "ar29-41": ar29_41,
       "ar29-61": ar29_61,
       "ar49-45": ar49_45,
       "ar49-65": ar49_65,
       "s5112P-EI": s5112P_EI,
       "s5112C-EI": s5112C_EI,
       "s5228C": s5228C,
       "s5252C": s5252C,
       "s5228C-PWR": s5228C_PWR,
       "s5252C-PWR": s5252C_PWR,
       "s2008-HI": s2008_HI,
       "s2016-HI": s2016_HI,
       "s2403H-HI": s2403H_HI,
       "vg31-08": vg31_08,
       "s8508V": s8508V,
       "e126": e126,
       "s3126TP": s3126TP,
       "e328": e328,
       "e352": e352,
       "s3928P-PWR-SI": s3928P_PWR_SI,
       "falcon": falcon,
       "ix1000": ix1000,
       "s8502": s8502,
       "sr8802": sr8802,
       "s3328P-SI": s3328P_SI,
       "s3352P-SI": s3352P_SI,
       "s3328TP-SI": s3328TP_SI,
       "s3328P-PWR-SI": s3328P_PWR_SI,
       "s3328P-EI": s3328P_EI,
       "s3352P-EI": s3352P_EI,
       "s3328P-PWR-EI": s3328P_PWR_EI,
       "s3352P-PWR-EI": s3352P_PWR_EI,
       "s3328F-EI": s3328F_EI,
       "s6502ME": s6502ME,
       "s5528C-EI": s5528C_EI,
       "s5552C-EI": s5552C_EI,
       "s5528C-PWR-EI": s5528C_PWR_EI,
       "s5552C-PWR-EI": s5552C_PWR_EI,
       "s5528F-EI": s5528F_EI,
       "s5528C-EI-DC": s5528C_EI_DC,
       "e126-SI": e126_SI,
       "dr814": dr814,
       "dr814q": dr814q,
       "wdr854g": wdr854g,
       "vdr824g": vdr824g,
       "vdr824": vdr824,
       "vdr744": vdr744,
       "dr744": dr744,
       "s6502M": s6502M,
       "s6501M-GT": s6501M_GT,
       "s6501M-GP": s6501M_GP,
       "s8505-V5": s8505_V5,
       "s8512-V5": s8512_V5,
       "s8508-V5": s8508_V5,
       "s8508V-V5": s8508V_V5,
       "s8502-V5": s8502_V5,
       "s6502-V5": s6502_V5,
       "s2008TP-EA": s2008TP_EA,
       "s2016TP-EA": s2016TP_EA,
       "s2403TP-EA": s2403TP_EA,
       "s2403TP-PWR-EA": s2403TP_PWR_EA,
       "s2008TP-MI": s2008TP_MI,
       "s2016TP-MI": s2016TP_MI,
       "s2403TP-MI": s2403TP_MI,
       "s7802": s7802,
       "s7803": s7803,
       "s7806": s7806,
       "s7806-V": s7806_V,
       "s7810": s7810,
       "s2016TP-PWR-EA": s2016TP_PWR_EA,
       "s3552P-EA": s3552P_EA,
       "s3528P-EA": s3528P_EA,
       "s3528TP-EA": s3528TP_EA,
       "s3528F-EA": s3528F_EA,
       "s3552f-ea": s3552f_ea,
       "s6902": s6902,
       "s6903": s6903,
       "s6906": s6906,
       "s6906R": s6906R,
       "s3928P-SI-ACDC": s3928P_SI_ACDC,
       "s5540F": s5540F,
       "s5540C": s5540C,
       "s5556C": s5556C,
       "ar19-10": ar19_10,
       "ar19-13": ar19_13,
       "ar19-15": ar19_15,
       "s3552P-SI": s3552P_SI,
       "s3528P-SI": s3528P_SI,
       "s5628C-HI-AC": s5628C_HI_AC,
       "s5628C-HI-DC": s5628C_HI_DC,
       "s5652C-HI-AC": s5652C_HI_AC,
       "s5628F-HI": s5628F_HI,
       "s5628C-PWR-HI": s5628C_PWR_HI,
       "s5652C-PWR-HI": s5652C_PWR_HI,
       "secBlade-LSQ1FWBSC1": secBlade_LSQ1FWBSC1,
       "secBlade-LSQ1NSMSC1": secBlade_LSQ1NSMSC1,
       "s7803-L": s7803_L,
       "s6503-v5": s6503_v5,
       "s6506-v5": s6506_v5,
       "s6506R-v5": s6506R_v5,
       "ar19-03": ar19_03,
       "ar19-05": ar19_05,
       "s7806-L": s7806_L,
       "ar29-11": ar29_11}
)
