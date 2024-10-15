# SNMP MIB module (HH3C-PRODUCT-ID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-PRODUCT-ID-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:33 2024
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

(hh3cProductId,
 hpNetworking) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cProductId",
    "hpNetworking")

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

_Hh3c_s5500_28C_EI_ObjectIdentity = ObjectIdentity
hh3c_s5500_28C_EI = _Hh3c_s5500_28C_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1)
)
_Hh3c_s5500_52C_EI_ObjectIdentity = ObjectIdentity
hh3c_s5500_52C_EI = _Hh3c_s5500_52C_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 2)
)
_Hh3c_s5500_28C_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_s5500_28C_PWR_EI = _Hh3c_s5500_28C_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 3)
)
_Hh3c_s5500_52C_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_s5500_52C_PWR_EI = _Hh3c_s5500_52C_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 4)
)
_Hh3c_s5500_28F_EI_ObjectIdentity = ObjectIdentity
hh3c_s5500_28F_EI = _Hh3c_s5500_28F_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 5)
)
_Hh3c_s5500_28C_EI_DC_ObjectIdentity = ObjectIdentity
hh3c_s5500_28C_EI_DC = _Hh3c_s5500_28C_EI_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 6)
)
_Hh3c_s6100_20Q_SI_ObjectIdentity = ObjectIdentity
hh3c_s6100_20Q_SI = _Hh3c_s6100_20Q_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 7)
)
_Hh3c_s5500_28C_SI_ObjectIdentity = ObjectIdentity
hh3c_s5500_28C_SI = _Hh3c_s5500_28C_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 8)
)
_Hh3c_s5500_52C_SI_ObjectIdentity = ObjectIdentity
hh3c_s5500_52C_SI = _Hh3c_s5500_52C_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 9)
)
_Hh3c_s5500_28C_PWR_SI_ObjectIdentity = ObjectIdentity
hh3c_s5500_28C_PWR_SI = _Hh3c_s5500_28C_PWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 10)
)
_Hh3c_s5500_52C_PWR_SI_ObjectIdentity = ObjectIdentity
hh3c_s5500_52C_PWR_SI = _Hh3c_s5500_52C_PWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 11)
)
_Hh3c_s5510_24P_ObjectIdentity = ObjectIdentity
hh3c_s5510_24P = _Hh3c_s5510_24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 12)
)
_Hh3c_s5510_24F_ObjectIdentity = ObjectIdentity
hh3c_s5510_24F = _Hh3c_s5510_24F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 13)
)
_Hh3c_s3610_28P_ObjectIdentity = ObjectIdentity
hh3c_s3610_28P = _Hh3c_s3610_28P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 14)
)
_Hh3c_s3610_52P_ObjectIdentity = ObjectIdentity
hh3c_s3610_52P = _Hh3c_s3610_52P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 15)
)
_Hh3c_s3610_28TP_ObjectIdentity = ObjectIdentity
hh3c_s3610_28TP = _Hh3c_s3610_28TP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 16)
)
_Hh3c_s3610_28F_ObjectIdentity = ObjectIdentity
hh3c_s3610_28F = _Hh3c_s3610_28F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 17)
)
_Hh3c_e126_ObjectIdentity = ObjectIdentity
hh3c_e126 = _Hh3c_e126_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 18)
)
_Hh3c_e328_ObjectIdentity = ObjectIdentity
hh3c_e328 = _Hh3c_e328_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 19)
)
_Hh3c_e352_ObjectIdentity = ObjectIdentity
hh3c_e352 = _Hh3c_e352_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 20)
)
_Hh3c_s3100_8C_SI_ObjectIdentity = ObjectIdentity
hh3c_s3100_8C_SI = _Hh3c_s3100_8C_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 21)
)
_Hh3c_s3100_16C_SI_ObjectIdentity = ObjectIdentity
hh3c_s3100_16C_SI = _Hh3c_s3100_16C_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 22)
)
_Hh3c_s3100_26C_SI_ObjectIdentity = ObjectIdentity
hh3c_s3100_26C_SI = _Hh3c_s3100_26C_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 23)
)
_Hh3c_s3100_8T_SI_ObjectIdentity = ObjectIdentity
hh3c_s3100_8T_SI = _Hh3c_s3100_8T_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 24)
)
_Hh3c_s3100_16T_SI_ObjectIdentity = ObjectIdentity
hh3c_s3100_16T_SI = _Hh3c_s3100_16T_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 25)
)
_Hh3c_s3100_26T_SI_ObjectIdentity = ObjectIdentity
hh3c_s3100_26T_SI = _Hh3c_s3100_26T_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 26)
)
_Hh3c_s3100_26TP_SI_ObjectIdentity = ObjectIdentity
hh3c_s3100_26TP_SI = _Hh3c_s3100_26TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 27)
)
_Hh3c_s5100_24P_EI_ObjectIdentity = ObjectIdentity
hh3c_s5100_24P_EI = _Hh3c_s5100_24P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 28)
)
_Hh3c_s5100_26C_EI_ObjectIdentity = ObjectIdentity
hh3c_s5100_26C_EI = _Hh3c_s5100_26C_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 29)
)
_Hh3c_s5100_50C_EI_ObjectIdentity = ObjectIdentity
hh3c_s5100_50C_EI = _Hh3c_s5100_50C_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 30)
)
_Hh3c_s5100_48P_EI_ObjectIdentity = ObjectIdentity
hh3c_s5100_48P_EI = _Hh3c_s5100_48P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 31)
)
_Hh3c_s3600_28P_SI_ObjectIdentity = ObjectIdentity
hh3c_s3600_28P_SI = _Hh3c_s3600_28P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 32)
)
_Hh3c_s3600_52P_SI_ObjectIdentity = ObjectIdentity
hh3c_s3600_52P_SI = _Hh3c_s3600_52P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 33)
)
_Hh3c_s3600_28TP_SI_ObjectIdentity = ObjectIdentity
hh3c_s3600_28TP_SI = _Hh3c_s3600_28TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 34)
)
_Hh3c_s3600_28P_PWR_SI_ObjectIdentity = ObjectIdentity
hh3c_s3600_28P_PWR_SI = _Hh3c_s3600_28P_PWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 35)
)
_Hh3c_s3600_52P_PWR_SI_ObjectIdentity = ObjectIdentity
hh3c_s3600_52P_PWR_SI = _Hh3c_s3600_52P_PWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 36)
)
_Hh3c_s3600_28P_EI_ObjectIdentity = ObjectIdentity
hh3c_s3600_28P_EI = _Hh3c_s3600_28P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 37)
)
_Hh3c_s3600_52P_EI_ObjectIdentity = ObjectIdentity
hh3c_s3600_52P_EI = _Hh3c_s3600_52P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 38)
)
_Hh3c_s3600_28P_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_s3600_28P_PWR_EI = _Hh3c_s3600_28P_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 39)
)
_Hh3c_s3600_52P_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_s3600_52P_PWR_EI = _Hh3c_s3600_52P_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 40)
)
_Hh3c_s3600_28F_EI_ObjectIdentity = ObjectIdentity
hh3c_s3600_28F_EI = _Hh3c_s3600_28F_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 41)
)
_Hh3c_s5600_26C_ObjectIdentity = ObjectIdentity
hh3c_s5600_26C = _Hh3c_s5600_26C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 42)
)
_Hh3c_s5600_50C_ObjectIdentity = ObjectIdentity
hh3c_s5600_50C = _Hh3c_s5600_50C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 43)
)
_Hh3c_s5600_26C_PWR_ObjectIdentity = ObjectIdentity
hh3c_s5600_26C_PWR = _Hh3c_s5600_26C_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 44)
)
_Hh3c_s5600_50C_PWR_ObjectIdentity = ObjectIdentity
hh3c_s5600_50C_PWR = _Hh3c_s5600_50C_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 45)
)
_Hh3c_s5600_26F_ObjectIdentity = ObjectIdentity
hh3c_s5600_26F = _Hh3c_s5600_26F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 46)
)
_Hh3c_s3600_52G_HI_ObjectIdentity = ObjectIdentity
hh3c_s3600_52G_HI = _Hh3c_s3600_52G_HI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 47)
)
_Hh3c_s3600_52P_HI_ObjectIdentity = ObjectIdentity
hh3c_s3600_52P_HI = _Hh3c_s3600_52P_HI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 48)
)
_Hh3c_s3600_28G_HI_ObjectIdentity = ObjectIdentity
hh3c_s3600_28G_HI = _Hh3c_s3600_28G_HI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 49)
)
_Hh3c_s3600_28P_HI_ObjectIdentity = ObjectIdentity
hh3c_s3600_28P_HI = _Hh3c_s3600_28P_HI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 50)
)
_Hh3c_s3600_52M_HI_ObjectIdentity = ObjectIdentity
hh3c_s3600_52M_HI = _Hh3c_s3600_52M_HI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 51)
)
_Hh3c_s7502_ObjectIdentity = ObjectIdentity
hh3c_s7502 = _Hh3c_s7502_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 52)
)
_Hh3c_s7503_ObjectIdentity = ObjectIdentity
hh3c_s7503 = _Hh3c_s7503_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 53)
)
_Hh3c_s7506_ObjectIdentity = ObjectIdentity
hh3c_s7506 = _Hh3c_s7506_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 54)
)
_Hh3c_s7506R_ObjectIdentity = ObjectIdentity
hh3c_s7506R = _Hh3c_s7506R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 55)
)
_Hh3c_ar28_09_ObjectIdentity = ObjectIdentity
hh3c_ar28_09 = _Hh3c_ar28_09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 57)
)
_Hh3c_ar28_10_ObjectIdentity = ObjectIdentity
hh3c_ar28_10 = _Hh3c_ar28_10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 58)
)
_Hh3c_ar28_11_ObjectIdentity = ObjectIdentity
hh3c_ar28_11 = _Hh3c_ar28_11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 59)
)
_Hh3c_ar28_12_ObjectIdentity = ObjectIdentity
hh3c_ar28_12 = _Hh3c_ar28_12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 60)
)
_Hh3c_ar28_13_ObjectIdentity = ObjectIdentity
hh3c_ar28_13 = _Hh3c_ar28_13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 61)
)
_Hh3c_ar28_14_ObjectIdentity = ObjectIdentity
hh3c_ar28_14 = _Hh3c_ar28_14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 62)
)
_Hh3c_ar28_30_ObjectIdentity = ObjectIdentity
hh3c_ar28_30 = _Hh3c_ar28_30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 63)
)
_Hh3c_ar28_31_ObjectIdentity = ObjectIdentity
hh3c_ar28_31 = _Hh3c_ar28_31_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 64)
)
_Hh3c_ar28_40_ObjectIdentity = ObjectIdentity
hh3c_ar28_40 = _Hh3c_ar28_40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 65)
)
_Hh3c_ar28_80_ObjectIdentity = ObjectIdentity
hh3c_ar28_80 = _Hh3c_ar28_80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 66)
)
_Hh3c_ar46_20_ObjectIdentity = ObjectIdentity
hh3c_ar46_20 = _Hh3c_ar46_20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 67)
)
_Hh3c_ar46_40_ObjectIdentity = ObjectIdentity
hh3c_ar46_40 = _Hh3c_ar46_40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 68)
)
_Hh3c_ar46_80_ObjectIdentity = ObjectIdentity
hh3c_ar46_80 = _Hh3c_ar46_80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 69)
)
_Hh3c_msr20_20_ObjectIdentity = ObjectIdentity
hh3c_msr20_20 = _Hh3c_msr20_20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 70)
)
_Hh3c_msr20_21_ObjectIdentity = ObjectIdentity
hh3c_msr20_21 = _Hh3c_msr20_21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 71)
)
_Hh3c_msr20_40_ObjectIdentity = ObjectIdentity
hh3c_msr20_40 = _Hh3c_msr20_40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 72)
)
_Hh3c_msr30_20_ObjectIdentity = ObjectIdentity
hh3c_msr30_20 = _Hh3c_msr30_20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 73)
)
_Hh3c_msr30_40_ObjectIdentity = ObjectIdentity
hh3c_msr30_40 = _Hh3c_msr30_40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 74)
)
_Hh3c_msr30_60_ObjectIdentity = ObjectIdentity
hh3c_msr30_60 = _Hh3c_msr30_60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 75)
)
_Hh3c_msr50_40_ObjectIdentity = ObjectIdentity
hh3c_msr50_40 = _Hh3c_msr50_40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 76)
)
_Hh3c_msr50_60_ObjectIdentity = ObjectIdentity
hh3c_msr50_60 = _Hh3c_msr50_60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 77)
)
_Hh3c_ar18_21_ObjectIdentity = ObjectIdentity
hh3c_ar18_21 = _Hh3c_ar18_21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 88)
)
_Hh3c_ar18_21A_ObjectIdentity = ObjectIdentity
hh3c_ar18_21A = _Hh3c_ar18_21A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 89)
)
_Hh3c_ar18_21B_ObjectIdentity = ObjectIdentity
hh3c_ar18_21B = _Hh3c_ar18_21B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 90)
)
_Hh3c_ar18_22_ObjectIdentity = ObjectIdentity
hh3c_ar18_22 = _Hh3c_ar18_22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 91)
)
_Hh3c_ar18_22_8_ObjectIdentity = ObjectIdentity
hh3c_ar18_22_8 = _Hh3c_ar18_22_8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 92)
)
_Hh3c_ar18_22S_8_ObjectIdentity = ObjectIdentity
hh3c_ar18_22S_8 = _Hh3c_ar18_22S_8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 93)
)
_Hh3c_ar18_22_24_ObjectIdentity = ObjectIdentity
hh3c_ar18_22_24 = _Hh3c_ar18_22_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 94)
)
_Hh3c_ar18_23_1_ObjectIdentity = ObjectIdentity
hh3c_ar18_23_1 = _Hh3c_ar18_23_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 95)
)
_Hh3c_ar18_23S_1_ObjectIdentity = ObjectIdentity
hh3c_ar18_23S_1 = _Hh3c_ar18_23S_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 96)
)
_Hh3c_ar18_30E_ObjectIdentity = ObjectIdentity
hh3c_ar18_30E = _Hh3c_ar18_30E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 98)
)
_Hh3c_ar18_31E_ObjectIdentity = ObjectIdentity
hh3c_ar18_31E = _Hh3c_ar18_31E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 100)
)
_Hh3c_ar18_32E_ObjectIdentity = ObjectIdentity
hh3c_ar18_32E = _Hh3c_ar18_32E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 102)
)
_Hh3c_ar18_33_ObjectIdentity = ObjectIdentity
hh3c_ar18_33 = _Hh3c_ar18_33_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 103)
)
_Hh3c_ar18_33E_ObjectIdentity = ObjectIdentity
hh3c_ar18_33E = _Hh3c_ar18_33E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 104)
)
_Hh3c_ar18_34_ObjectIdentity = ObjectIdentity
hh3c_ar18_34 = _Hh3c_ar18_34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 105)
)
_Hh3c_ar18_34E_ObjectIdentity = ObjectIdentity
hh3c_ar18_34E = _Hh3c_ar18_34E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 106)
)
_Hh3c_ar18_35E_ObjectIdentity = ObjectIdentity
hh3c_ar18_35E = _Hh3c_ar18_35E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 108)
)
_Hh3c_ar18_63_1_ObjectIdentity = ObjectIdentity
hh3c_ar18_63_1 = _Hh3c_ar18_63_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 109)
)
_Hh3c_secpathF100_C_ObjectIdentity = ObjectIdentity
hh3c_secpathF100_C = _Hh3c_secpathF100_C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 110)
)
_Hh3c_secpathF100_A_ObjectIdentity = ObjectIdentity
hh3c_secpathF100_A = _Hh3c_secpathF100_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 111)
)
_Hh3c_secpathF100_S_ObjectIdentity = ObjectIdentity
hh3c_secpathF100_S = _Hh3c_secpathF100_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 112)
)
_Hh3c_secpathF100_E_ObjectIdentity = ObjectIdentity
hh3c_secpathF100_E = _Hh3c_secpathF100_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 113)
)
_Hh3c_secpathF1000_S_ObjectIdentity = ObjectIdentity
hh3c_secpathF1000_S = _Hh3c_secpathF1000_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 114)
)
_Hh3c_secpathF1000_A_ObjectIdentity = ObjectIdentity
hh3c_secpathF1000_A = _Hh3c_secpathF1000_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 115)
)
_Hh3c_secpathF1800_A_ObjectIdentity = ObjectIdentity
hh3c_secpathF1800_A = _Hh3c_secpathF1800_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 116)
)
_Hh3c_secpathV100_S_ObjectIdentity = ObjectIdentity
hh3c_secpathV100_S = _Hh3c_secpathV100_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 117)
)
_Hh3c_secpathV1000_A_ObjectIdentity = ObjectIdentity
hh3c_secpathV1000_A = _Hh3c_secpathV1000_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 118)
)
_Hh3c_secpathF100_AW_ObjectIdentity = ObjectIdentity
hh3c_secpathF100_AW = _Hh3c_secpathF100_AW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 119)
)
_Hh3c_secpathF1800_S_ObjectIdentity = ObjectIdentity
hh3c_secpathF1800_S = _Hh3c_secpathF1800_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 120)
)
_Hh3c_secpathF1800_E_ObjectIdentity = ObjectIdentity
hh3c_secpathF1800_E = _Hh3c_secpathF1800_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 121)
)
_Hh3c_secpoint_ObjectIdentity = ObjectIdentity
hh3c_secpoint = _Hh3c_secpoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 122)
)
_Hh3c_vg10_10_ObjectIdentity = ObjectIdentity
hh3c_vg10_10 = _Hh3c_vg10_10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 123)
)
_Hh3c_vg10_11_ObjectIdentity = ObjectIdentity
hh3c_vg10_11 = _Hh3c_vg10_11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 124)
)
_Hh3c_vg10_40_ObjectIdentity = ObjectIdentity
hh3c_vg10_40 = _Hh3c_vg10_40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 125)
)
_Hh3c_vg10_41_ObjectIdentity = ObjectIdentity
hh3c_vg10_41 = _Hh3c_vg10_41_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 126)
)
_Hh3c_vg21_08_ObjectIdentity = ObjectIdentity
hh3c_vg21_08 = _Hh3c_vg21_08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 127)
)
_Hh3c_vg20_16_ObjectIdentity = ObjectIdentity
hh3c_vg20_16 = _Hh3c_vg20_16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 128)
)
_Hh3c_vg20_32_ObjectIdentity = ObjectIdentity
hh3c_vg20_32 = _Hh3c_vg20_32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 129)
)
_Hh3c_vg80_20_ObjectIdentity = ObjectIdentity
hh3c_vg80_20 = _Hh3c_vg80_20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 130)
)
_Hh3c_xe200_ObjectIdentity = ObjectIdentity
hh3c_xe200 = _Hh3c_xe200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 131)
)
_Hh3c_xe2000_ObjectIdentity = ObjectIdentity
hh3c_xe2000 = _Hh3c_xe2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 132)
)
_Hh3c_xe7200_ObjectIdentity = ObjectIdentity
hh3c_xe7200 = _Hh3c_xe7200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 133)
)
_Hh3c_xe7300_ObjectIdentity = ObjectIdentity
hh3c_xe7300 = _Hh3c_xe7300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 134)
)
_Hh3c_xe7500_ObjectIdentity = ObjectIdentity
hh3c_xe7500 = _Hh3c_xe7500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 135)
)
_Hh3c_xe7600_ObjectIdentity = ObjectIdentity
hh3c_xe7600 = _Hh3c_xe7600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 136)
)
_Hh3c_xe7205_ObjectIdentity = ObjectIdentity
hh3c_xe7205 = _Hh3c_xe7205_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 137)
)
_Hh3c_xe7305_ObjectIdentity = ObjectIdentity
hh3c_xe7305 = _Hh3c_xe7305_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 138)
)
_Hh3c_xe7505_ObjectIdentity = ObjectIdentity
hh3c_xe7505 = _Hh3c_xe7505_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 139)
)
_Hh3c_xe7605_ObjectIdentity = ObjectIdentity
hh3c_xe7605 = _Hh3c_xe7605_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 140)
)
_Hh3c_neoceanIX1000_ObjectIdentity = ObjectIdentity
hh3c_neoceanIX1000 = _Hh3c_neoceanIX1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 141)
)
_Hh3c_neoceanEX1000_ObjectIdentity = ObjectIdentity
hh3c_neoceanEX1000 = _Hh3c_neoceanEX1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 142)
)
_Hh3c_neoceanEX800_ObjectIdentity = ObjectIdentity
hh3c_neoceanEX800 = _Hh3c_neoceanEX800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 143)
)
_Hh3c_neoceanIX5000_ObjectIdentity = ObjectIdentity
hh3c_neoceanIX5000 = _Hh3c_neoceanIX5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 144)
)
_Hh3c_neoceanIV5100_ObjectIdentity = ObjectIdentity
hh3c_neoceanIV5100 = _Hh3c_neoceanIV5100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 145)
)
_Hh3c_neoceanIV5200_ObjectIdentity = ObjectIdentity
hh3c_neoceanIV5200 = _Hh3c_neoceanIV5200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 146)
)
_Hh3c_s9502_ObjectIdentity = ObjectIdentity
hh3c_s9502 = _Hh3c_s9502_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 147)
)
_Hh3c_s9505_ObjectIdentity = ObjectIdentity
hh3c_s9505 = _Hh3c_s9505_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 148)
)
_Hh3c_s9508_ObjectIdentity = ObjectIdentity
hh3c_s9508 = _Hh3c_s9508_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 149)
)
_Hh3c_s9508V_ObjectIdentity = ObjectIdentity
hh3c_s9508V = _Hh3c_s9508V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 150)
)
_Hh3c_s9512_ObjectIdentity = ObjectIdentity
hh3c_s9512 = _Hh3c_s9512_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 151)
)
_Hh3c_sR8812_ObjectIdentity = ObjectIdentity
hh3c_sR8812 = _Hh3c_sR8812_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 152)
)
_Hh3c_sR8808_ObjectIdentity = ObjectIdentity
hh3c_sR8808 = _Hh3c_sR8808_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 153)
)
_Hh3c_sR8805_ObjectIdentity = ObjectIdentity
hh3c_sR8805 = _Hh3c_sR8805_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 154)
)
_Hh3c_sR8802_ObjectIdentity = ObjectIdentity
hh3c_sR8802 = _Hh3c_sR8802_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 155)
)
_Hh3c_e126_SI_ObjectIdentity = ObjectIdentity
hh3c_e126_SI = _Hh3c_e126_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 156)
)
_Hh3c_vg31_08_ObjectIdentity = ObjectIdentity
hh3c_vg31_08 = _Hh3c_vg31_08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 157)
)
_Hh3c_dr834_ObjectIdentity = ObjectIdentity
hh3c_dr834 = _Hh3c_dr834_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 158)
)
_Hh3c_s7510E_ObjectIdentity = ObjectIdentity
hh3c_s7510E = _Hh3c_s7510E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 159)
)
_Hh3c_s5100_24P_SI_ObjectIdentity = ObjectIdentity
hh3c_s5100_24P_SI = _Hh3c_s5100_24P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 160)
)
_Hh3c_s5100_48P_SI_ObjectIdentity = ObjectIdentity
hh3c_s5100_48P_SI = _Hh3c_s5100_48P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 161)
)
_Hh3c_s5100_8P_SI_ObjectIdentity = ObjectIdentity
hh3c_s5100_8P_SI = _Hh3c_s5100_8P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 162)
)
_Hh3c_s5100_16P_SI_ObjectIdentity = ObjectIdentity
hh3c_s5100_16P_SI = _Hh3c_s5100_16P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 163)
)
_Hh3c_s5100_8P_EI_ObjectIdentity = ObjectIdentity
hh3c_s5100_8P_EI = _Hh3c_s5100_8P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 164)
)
_Hh3c_s5100_16P_EI_ObjectIdentity = ObjectIdentity
hh3c_s5100_16P_EI = _Hh3c_s5100_16P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 165)
)
_Hh3c_s5100_8P_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_s5100_8P_PWR_EI = _Hh3c_s5100_8P_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 166)
)
_Hh3c_s5100_16P_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_s5100_16P_PWR_EI = _Hh3c_s5100_16P_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 167)
)
_Hh3c_s5100_26C_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_s5100_26C_PWR_EI = _Hh3c_s5100_26C_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 168)
)
_Hh3c_s5100_50C_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_s5100_50C_PWR_EI = _Hh3c_s5100_50C_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 169)
)
_Hh3c_s3108TP_EI_ObjectIdentity = ObjectIdentity
hh3c_s3108TP_EI = _Hh3c_s3108TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 170)
)
_Hh3c_s3116TP_EI_ObjectIdentity = ObjectIdentity
hh3c_s3116TP_EI = _Hh3c_s3116TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 171)
)
_Hh3c_s3126TP_EI_ObjectIdentity = ObjectIdentity
hh3c_s3126TP_EI = _Hh3c_s3126TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 172)
)
_Hh3c_s3108TP_EI_PWR_ObjectIdentity = ObjectIdentity
hh3c_s3108TP_EI_PWR = _Hh3c_s3108TP_EI_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 173)
)
_Hh3c_s3116TP_EI_PWR_ObjectIdentity = ObjectIdentity
hh3c_s3116TP_EI_PWR = _Hh3c_s3116TP_EI_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 174)
)
_Hh3c_s3126TP_EI_PWR_ObjectIdentity = ObjectIdentity
hh3c_s3126TP_EI_PWR = _Hh3c_s3126TP_EI_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 175)
)
_Hh3c_s5500M_20C_ObjectIdentity = ObjectIdentity
hh3c_s5500M_20C = _Hh3c_s5500M_20C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 177)
)
_Hh3c_s5500M_20F_ObjectIdentity = ObjectIdentity
hh3c_s5500M_20F = _Hh3c_s5500M_20F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 178)
)
_Hh3c_bR304plus_ObjectIdentity = ObjectIdentity
hh3c_bR304plus = _Hh3c_bR304plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 179)
)
_Hh3c_s9505_V5_ObjectIdentity = ObjectIdentity
hh3c_s9505_V5 = _Hh3c_s9505_V5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 180)
)
_Hh3c_s9512_V5_ObjectIdentity = ObjectIdentity
hh3c_s9512_V5 = _Hh3c_s9512_V5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 181)
)
_Hh3c_s9508_V5_ObjectIdentity = ObjectIdentity
hh3c_s9508_V5 = _Hh3c_s9508_V5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 182)
)
_Hh3c_s9508V_V5_ObjectIdentity = ObjectIdentity
hh3c_s9508V_V5 = _Hh3c_s9508V_V5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 183)
)
_Hh3c_s9502_V5_ObjectIdentity = ObjectIdentity
hh3c_s9502_V5 = _Hh3c_s9502_V5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 184)
)
_Hh3c_sR8802_V5_ObjectIdentity = ObjectIdentity
hh3c_sR8802_V5 = _Hh3c_sR8802_V5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 185)
)
_Hh3c_sR8805_V5_ObjectIdentity = ObjectIdentity
hh3c_sR8805_V5 = _Hh3c_sR8805_V5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 186)
)
_Hh3c_sR8812_V5_ObjectIdentity = ObjectIdentity
hh3c_sR8812_V5 = _Hh3c_sR8812_V5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 187)
)
_Hh3c_sR8808_V5_ObjectIdentity = ObjectIdentity
hh3c_sR8808_V5 = _Hh3c_sR8808_V5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 188)
)
_Hh3c_s3100_52P_ObjectIdentity = ObjectIdentity
hh3c_s3100_52P = _Hh3c_s3100_52P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 189)
)
_Hh3c_e152_ObjectIdentity = ObjectIdentity
hh3c_e152 = _Hh3c_e152_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 190)
)
_Hh3c_s2008_ObjectIdentity = ObjectIdentity
hh3c_s2008 = _Hh3c_s2008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 191)
)
_Hh3c_s2026_ObjectIdentity = ObjectIdentity
hh3c_s2026 = _Hh3c_s2026_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 192)
)
_Hh3c_sr6602_ObjectIdentity = ObjectIdentity
hh3c_sr6602 = _Hh3c_sr6602_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 193)
)
_Hh3c_sr6608_ObjectIdentity = ObjectIdentity
hh3c_sr6608 = _Hh3c_sr6608_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 194)
)
_Hh3c_s3100_08TP_EI_ObjectIdentity = ObjectIdentity
hh3c_s3100_08TP_EI = _Hh3c_s3100_08TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 195)
)
_Hh3c_s3100_08TP_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_s3100_08TP_PWR_EI = _Hh3c_s3100_08TP_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 196)
)
_Hh3c_s3100_16TP_EI_ObjectIdentity = ObjectIdentity
hh3c_s3100_16TP_EI = _Hh3c_s3100_16TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 197)
)
_Hh3c_s3100_16TP_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_s3100_16TP_PWR_EI = _Hh3c_s3100_16TP_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 198)
)
_Hh3c_s3100_26TP_EI_ObjectIdentity = ObjectIdentity
hh3c_s3100_26TP_EI = _Hh3c_s3100_26TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 199)
)
_Hh3c_s3100_26TP_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_s3100_26TP_PWR_EI = _Hh3c_s3100_26TP_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 200)
)
_Hh3c_s7502_v5_ObjectIdentity = ObjectIdentity
hh3c_s7502_v5 = _Hh3c_s7502_v5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 201)
)
_Hh3c_vg80_21_ObjectIdentity = ObjectIdentity
hh3c_vg80_21 = _Hh3c_vg80_21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 202)
)
_Hh3c_vg80_80_ObjectIdentity = ObjectIdentity
hh3c_vg80_80 = _Hh3c_vg80_80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 203)
)
_Hh3c_wcm_wx5002_ObjectIdentity = ObjectIdentity
hh3c_wcm_wx5002 = _Hh3c_wcm_wx5002_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 204)
)
_Hh3c_wcm_wcma_ObjectIdentity = ObjectIdentity
hh3c_wcm_wcma = _Hh3c_wcm_wcma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 205)
)
_Hh3c_msr30_10_ObjectIdentity = ObjectIdentity
hh3c_msr30_10 = _Hh3c_msr30_10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 206)
)
_Hh3c_s7502e_ObjectIdentity = ObjectIdentity
hh3c_s7502e = _Hh3c_s7502e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 207)
)
_Hh3c_s7503E_ObjectIdentity = ObjectIdentity
hh3c_s7503E = _Hh3c_s7503E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 208)
)
_Hh3c_s7506E_ObjectIdentity = ObjectIdentity
hh3c_s7506E = _Hh3c_s7506E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 209)
)
_Hh3c_s7506E_V_ObjectIdentity = ObjectIdentity
hh3c_s7506E_V = _Hh3c_s7506E_V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 210)
)
_Hh3c_secBlade_FW_ObjectIdentity = ObjectIdentity
hh3c_secBlade_FW = _Hh3c_secBlade_FW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 211)
)
_Hh3c_secBlade_IPSec_ObjectIdentity = ObjectIdentity
hh3c_secBlade_IPSec = _Hh3c_secBlade_IPSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 212)
)
_Hh3c_s3100_8TP_SI_ObjectIdentity = ObjectIdentity
hh3c_s3100_8TP_SI = _Hh3c_s3100_8TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 213)
)
_Hh3c_s3100_16TP_SI_ObjectIdentity = ObjectIdentity
hh3c_s3100_16TP_SI = _Hh3c_s3100_16TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 214)
)
_Hh3c_e126A_ObjectIdentity = ObjectIdentity
hh3c_e126A = _Hh3c_e126A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 215)
)
_Hh3c_s3100_26TP_SI_B_ObjectIdentity = ObjectIdentity
hh3c_s3100_26TP_SI_B = _Hh3c_s3100_26TP_SI_B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 216)
)
_Hh3c_msr30_16_ObjectIdentity = ObjectIdentity
hh3c_msr30_16 = _Hh3c_msr30_16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 217)
)
_Hh3cOEMProductID_ObjectIdentity = ObjectIdentity
hh3cOEMProductID = _Hh3cOEMProductID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 218)
)
_Hh3c_s2126_ei_ObjectIdentity = ObjectIdentity
hh3c_s2126_ei = _Hh3c_s2126_ei_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 219)
)
_Hh3c_e150_si_ObjectIdentity = ObjectIdentity
hh3c_e150_si = _Hh3c_e150_si_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 220)
)
_Hh3c_msr30_11_ObjectIdentity = ObjectIdentity
hh3c_msr30_11 = _Hh3c_msr30_11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 221)
)
_Hh3c_neoceanIX3040_ObjectIdentity = ObjectIdentity
hh3c_neoceanIX3040 = _Hh3c_neoceanIX3040_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 222)
)
_Hh3c_neoceanIX3080_ObjectIdentity = ObjectIdentity
hh3c_neoceanIX3080 = _Hh3c_neoceanIX3080_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 223)
)
_Hh3c_secpathF100_M_ObjectIdentity = ObjectIdentity
hh3c_secpathF100_M = _Hh3c_secpathF100_M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 224)
)
_Hh3c_neoceanVX1500_ObjectIdentity = ObjectIdentity
hh3c_neoceanVX1500 = _Hh3c_neoceanVX1500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 225)
)
_Hh3c_neoceanIX1520_ObjectIdentity = ObjectIdentity
hh3c_neoceanIX1520 = _Hh3c_neoceanIX1520_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 226)
)
_Hh3c_neoceanIX1540_ObjectIdentity = ObjectIdentity
hh3c_neoceanIX1540 = _Hh3c_neoceanIX1540_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 227)
)
_Hh3c_wcm_wx5002_128ap_ObjectIdentity = ObjectIdentity
hh3c_wcm_wx5002_128ap = _Hh3c_wcm_wx5002_128ap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 228)
)
_Hh3c_msr20_10_ObjectIdentity = ObjectIdentity
hh3c_msr20_10 = _Hh3c_msr20_10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 229)
)
_Hh3c_msr20_11_ObjectIdentity = ObjectIdentity
hh3c_msr20_11 = _Hh3c_msr20_11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 230)
)
_Hh3c_msr20_13_ObjectIdentity = ObjectIdentity
hh3c_msr20_13 = _Hh3c_msr20_13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 231)
)
_Hh3c_msr20_15_ObjectIdentity = ObjectIdentity
hh3c_msr20_15 = _Hh3c_msr20_15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 232)
)
_Hh3c_neoceanDL1008_ObjectIdentity = ObjectIdentity
hh3c_neoceanDL1008 = _Hh3c_neoceanDL1008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 233)
)
_Hh3c_neoceanDL1008S_ObjectIdentity = ObjectIdentity
hh3c_neoceanDL1008S = _Hh3c_neoceanDL1008S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 234)
)
_Hh3c_neoceanDL1012_ObjectIdentity = ObjectIdentity
hh3c_neoceanDL1012 = _Hh3c_neoceanDL1012_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 235)
)
_Hh3c_s3610_52m_ObjectIdentity = ObjectIdentity
hh3c_s3610_52m = _Hh3c_s3610_52m_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 236)
)
_Hh3c_IV5680_ObjectIdentity = ObjectIdentity
hh3c_IV5680 = _Hh3c_IV5680_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 237)
)
_Hh3c_IV5240_ObjectIdentity = ObjectIdentity
hh3c_IV5240 = _Hh3c_IV5240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 238)
)
_Hh3c_F1000_E_ObjectIdentity = ObjectIdentity
hh3c_F1000_E = _Hh3c_F1000_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 239)
)
_Hh3c_S5024P_ObjectIdentity = ObjectIdentity
hh3c_S5024P = _Hh3c_S5024P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 240)
)
_Hh3c_S5016P_ObjectIdentity = ObjectIdentity
hh3c_S5016P = _Hh3c_S5016P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 241)
)
_Hh3c_LSQ1FWBSC0_ObjectIdentity = ObjectIdentity
hh3c_LSQ1FWBSC0 = _Hh3c_LSQ1FWBSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 242)
)
_Hh3c_LSB1FW2A0_ObjectIdentity = ObjectIdentity
hh3c_LSB1FW2A0 = _Hh3c_LSB1FW2A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 243)
)
_Hh3c_S3100_8TP_EI_ObjectIdentity = ObjectIdentity
hh3c_S3100_8TP_EI = _Hh3c_S3100_8TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 244)
)
_Hh3c_S3100_16TP_EI_ObjectIdentity = ObjectIdentity
hh3c_S3100_16TP_EI = _Hh3c_S3100_16TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 245)
)
_Hh3c_S3100_26TP_EI_ObjectIdentity = ObjectIdentity
hh3c_S3100_26TP_EI = _Hh3c_S3100_26TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 246)
)
_Hh3c_ET704_ObjectIdentity = ObjectIdentity
hh3c_ET704 = _Hh3c_ET704_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 247)
)
_Hh3c_ec1001_ObjectIdentity = ObjectIdentity
hh3c_ec1001 = _Hh3c_ec1001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 248)
)
_Hh3c_ec1001_hf_ObjectIdentity = ObjectIdentity
hh3c_ec1001_hf = _Hh3c_ec1001_hf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 249)
)
_Hh3c_ec1004_hc_ObjectIdentity = ObjectIdentity
hh3c_ec1004_hc = _Hh3c_ec1004_hc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 250)
)
_Hh3c_ec2004_hf_ObjectIdentity = ObjectIdentity
hh3c_ec2004_hf = _Hh3c_ec2004_hf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 251)
)
_Hh3c_dc1001_ObjectIdentity = ObjectIdentity
hh3c_dc1001 = _Hh3c_dc1001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 252)
)
_Hh3c_dm8000_ObjectIdentity = ObjectIdentity
hh3c_dm8000 = _Hh3c_dm8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 253)
)
_Hh3c_vm8000_ObjectIdentity = ObjectIdentity
hh3c_vm8000 = _Hh3c_vm8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 254)
)
_Hh3c_ms8000_ObjectIdentity = ObjectIdentity
hh3c_ms8000 = _Hh3c_ms8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 255)
)
_Hh3c_S3100_52TP_ObjectIdentity = ObjectIdentity
hh3c_S3100_52TP = _Hh3c_S3100_52TP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 256)
)
_Hh3c_msr20_12_ObjectIdentity = ObjectIdentity
hh3c_msr20_12 = _Hh3c_msr20_12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 257)
)
_Hh3c_s1550E_ObjectIdentity = ObjectIdentity
hh3c_s1550E = _Hh3c_s1550E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 258)
)
_Hh3c_s1550_ObjectIdentity = ObjectIdentity
hh3c_s1550 = _Hh3c_s1550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 259)
)
_Hh3c_s1526_EI_ObjectIdentity = ObjectIdentity
hh3c_s1526_EI = _Hh3c_s1526_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 260)
)
_Hh3c_msr20_12_T_ObjectIdentity = ObjectIdentity
hh3c_msr20_12_T = _Hh3c_msr20_12_T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 261)
)
_Hh3c_msr20_15_I_ObjectIdentity = ObjectIdentity
hh3c_msr20_15_I = _Hh3c_msr20_15_I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 262)
)
_Hh3c_msr20_15_N_ObjectIdentity = ObjectIdentity
hh3c_msr20_15_N = _Hh3c_msr20_15_N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 263)
)
_Hh3c_wx6100EWPX_ObjectIdentity = ObjectIdentity
hh3c_wx6100EWPX = _Hh3c_wx6100EWPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 264)
)
_Hh3c_wx6100LSQ_ObjectIdentity = ObjectIdentity
hh3c_wx6100LSQ = _Hh3c_wx6100LSQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 265)
)
_Hh3c_wx6100LSB_ObjectIdentity = ObjectIdentity
hh3c_wx6100LSB = _Hh3c_wx6100LSB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 266)
)
_Hh3c_wx6100SW_ObjectIdentity = ObjectIdentity
hh3c_wx6100SW = _Hh3c_wx6100SW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 267)
)
_Hh3c_dl1000_ObjectIdentity = ObjectIdentity
hh3c_dl1000 = _Hh3c_dl1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 268)
)
_Hh3c_dl1000s_ObjectIdentity = ObjectIdentity
hh3c_dl1000s = _Hh3c_dl1000s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 269)
)
_Hh3c_wa1208e_g_ObjectIdentity = ObjectIdentity
hh3c_wa1208e_g = _Hh3c_wa1208e_g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 270)
)
_Hh3c_wa1208e_dg_ObjectIdentity = ObjectIdentity
hh3c_wa1208e_dg = _Hh3c_wa1208e_dg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 271)
)
_Hh3c_wa1208e_ag_ObjectIdentity = ObjectIdentity
hh3c_wa1208e_ag = _Hh3c_wa1208e_ag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 272)
)
_Hh3c_wa1208e_agp_ObjectIdentity = ObjectIdentity
hh3c_wa1208e_agp = _Hh3c_wa1208e_agp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 273)
)
_Hh3c_S7501M_24T_ObjectIdentity = ObjectIdentity
hh3c_S7501M_24T = _Hh3c_S7501M_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 274)
)
_Hh3c_s7501M_24TP_ObjectIdentity = ObjectIdentity
hh3c_s7501M_24TP = _Hh3c_s7501M_24TP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 275)
)
_Hh3c_s7502M_ObjectIdentity = ObjectIdentity
hh3c_s7502M = _Hh3c_s7502M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 276)
)
_Hh3c_s7503M_ObjectIdentity = ObjectIdentity
hh3c_s7503M = _Hh3c_s7503M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 277)
)
_Hh3c_s7506M_ObjectIdentity = ObjectIdentity
hh3c_s7506M = _Hh3c_s7506M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 278)
)
_Hh3c_s7506M_V_ObjectIdentity = ObjectIdentity
hh3c_s7506M_V = _Hh3c_s7506M_V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 279)
)
_Hh3c_s7510M_ObjectIdentity = ObjectIdentity
hh3c_s7510M = _Hh3c_s7510M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 280)
)
_Hh3c_secpathT200_ObjectIdentity = ObjectIdentity
hh3c_secpathT200 = _Hh3c_secpathT200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 281)
)
_Hh3c_secpathT200E_ObjectIdentity = ObjectIdentity
hh3c_secpathT200E = _Hh3c_secpathT200E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 282)
)
_Hh3c_cc600_ObjectIdentity = ObjectIdentity
hh3c_cc600 = _Hh3c_cc600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 283)
)
_Hh3c_wa1208e_gp_ObjectIdentity = ObjectIdentity
hh3c_wa1208e_gp = _Hh3c_wa1208e_gp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 284)
)
_Hh3c_wb2321e_agp_ObjectIdentity = ObjectIdentity
hh3c_wb2321e_agp = _Hh3c_wb2321e_agp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 285)
)
_Hh3c_wh2520e_agp_ObjectIdentity = ObjectIdentity
hh3c_wh2520e_agp = _Hh3c_wh2520e_agp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 286)
)
_Hh3c_ICG2000_ObjectIdentity = ObjectIdentity
hh3c_ICG2000 = _Hh3c_ICG2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 287)
)
_Hh3c_ICG3000_ObjectIdentity = ObjectIdentity
hh3c_ICG3000 = _Hh3c_ICG3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 288)
)
_Hh3c_ICG5000_ObjectIdentity = ObjectIdentity
hh3c_ICG5000 = _Hh3c_ICG5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 289)
)
_Hh3c_S5520TP_SI_ObjectIdentity = ObjectIdentity
hh3c_S5520TP_SI = _Hh3c_S5520TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 290)
)
_Hh3c_wa2210_ag_ObjectIdentity = ObjectIdentity
hh3c_wa2210_ag = _Hh3c_wa2210_ag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 291)
)
_Hh3c_wa2220_ag_ObjectIdentity = ObjectIdentity
hh3c_wa2220_ag = _Hh3c_wa2220_ag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 292)
)
_Hh3c_wa2220e_ag_ObjectIdentity = ObjectIdentity
hh3c_wa2220e_ag = _Hh3c_wa2220e_ag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 293)
)
_Hh3c_wa2210x_g_ObjectIdentity = ObjectIdentity
hh3c_wa2210x_g = _Hh3c_wa2210x_g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 294)
)
_Hh3c_wa2220x_ag_ObjectIdentity = ObjectIdentity
hh3c_wa2220x_ag = _Hh3c_wa2220x_ag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 295)
)
_Hh3c_wa2220x_agp_ObjectIdentity = ObjectIdentity
hh3c_wa2220x_agp = _Hh3c_wa2220x_agp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 296)
)
_Hh3c_S3100_52TP_SI_ObjectIdentity = ObjectIdentity
hh3c_S3100_52TP_SI = _Hh3c_S3100_52TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 297)
)
_Hh3c_secpathASE5000_E_ObjectIdentity = ObjectIdentity
hh3c_secpathASE5000_E = _Hh3c_secpathASE5000_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 298)
)
_Hh3c_secpathASE5000_S_ObjectIdentity = ObjectIdentity
hh3c_secpathASE5000_S = _Hh3c_secpathASE5000_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 299)
)
_Hh3c_secpathU200_C_ObjectIdentity = ObjectIdentity
hh3c_secpathU200_C = _Hh3c_secpathU200_C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 300)
)
_Hh3c_secpathU200_S_ObjectIdentity = ObjectIdentity
hh3c_secpathU200_S = _Hh3c_secpathU200_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 301)
)
_Hh3c_secpathU200_A_ObjectIdentity = ObjectIdentity
hh3c_secpathU200_A = _Hh3c_secpathU200_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 302)
)
_Hh3c_secpathU200_M_ObjectIdentity = ObjectIdentity
hh3c_secpathU200_M = _Hh3c_secpathU200_M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 303)
)
_Hh3c_ec3016_hc_ObjectIdentity = ObjectIdentity
hh3c_ec3016_hc = _Hh3c_ec3016_hc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 304)
)
_Hh3c_dc1001_ff_ObjectIdentity = ObjectIdentity
hh3c_dc1001_ff = _Hh3c_dc1001_ff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 305)
)
_Hh3c_ecr3304_hf_ObjectIdentity = ObjectIdentity
hh3c_ecr3304_hf = _Hh3c_ecr3304_hf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 306)
)
_Hh3c_ecr3308_hd_ObjectIdentity = ObjectIdentity
hh3c_ecr3308_hd = _Hh3c_ecr3308_hd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 307)
)
_Hh3c_ecr3316_hc_ObjectIdentity = ObjectIdentity
hh3c_ecr3316_hc = _Hh3c_ecr3316_hc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 308)
)
_Hh3c_isc3000_ObjectIdentity = ObjectIdentity
hh3c_isc3000 = _Hh3c_isc3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 309)
)
_Hh3c_isc3100_ObjectIdentity = ObjectIdentity
hh3c_isc3100 = _Hh3c_isc3100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 310)
)
_Hh3c_vm9000_ObjectIdentity = ObjectIdentity
hh3c_vm9000 = _Hh3c_vm9000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 311)
)
_Hh3c_vm5000_ObjectIdentity = ObjectIdentity
hh3c_vm5000 = _Hh3c_vm5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 312)
)
_Hh3c_ms9000_vtdu_ObjectIdentity = ObjectIdentity
hh3c_ms9000_vtdu = _Hh3c_ms9000_vtdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 313)
)
_Hh3c_ms9000_nru_ObjectIdentity = ObjectIdentity
hh3c_ms9000_nru = _Hh3c_ms9000_nru_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 314)
)
_Hh3c_ums9005_ObjectIdentity = ObjectIdentity
hh3c_ums9005 = _Hh3c_ums9005_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 315)
)
_Hh3c_CS2104B_ObjectIdentity = ObjectIdentity
hh3c_CS2104B = _Hh3c_CS2104B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 316)
)
_Hh3c_CS2106B_ObjectIdentity = ObjectIdentity
hh3c_CS2106B = _Hh3c_CS2106B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 317)
)
_Hh3c_S5024E_ObjectIdentity = ObjectIdentity
hh3c_S5024E = _Hh3c_S5024E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 318)
)
_Hh3c_S5048E_ObjectIdentity = ObjectIdentity
hh3c_S5048E = _Hh3c_S5048E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 319)
)
_Hh3c_secpathF5000_A_ObjectIdentity = ObjectIdentity
hh3c_secpathF5000_A = _Hh3c_secpathF5000_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 320)
)
_Hh3c_neoceanIX3240_ObjectIdentity = ObjectIdentity
hh3c_neoceanIX3240 = _Hh3c_neoceanIX3240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 321)
)
_Hh3c_neoceanIX3620_ObjectIdentity = ObjectIdentity
hh3c_neoceanIX3620 = _Hh3c_neoceanIX3620_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 322)
)
_Hh3c_MSA7302_ObjectIdentity = ObjectIdentity
hh3c_MSA7302 = _Hh3c_MSA7302_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 323)
)
_Hh3c_MSA7306_ObjectIdentity = ObjectIdentity
hh3c_MSA7306 = _Hh3c_MSA7306_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 324)
)
_Hh3c_S7501E_ObjectIdentity = ObjectIdentity
hh3c_S7501E = _Hh3c_S7501E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 325)
)
_Hh3c_S3100_8C_EPON_EI_ObjectIdentity = ObjectIdentity
hh3c_S3100_8C_EPON_EI = _Hh3c_S3100_8C_EPON_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 326)
)
_Hh3c_S3100_16C_EPON_EI_ObjectIdentity = ObjectIdentity
hh3c_S3100_16C_EPON_EI = _Hh3c_S3100_16C_EPON_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 327)
)
_Hh3c_S3100_26C_EPON_EI_ObjectIdentity = ObjectIdentity
hh3c_S3100_26C_EPON_EI = _Hh3c_S3100_26C_EPON_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 328)
)
_Hh3c_secBlade_LSQ1AFCBSC0_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSQ1AFCBSC0 = _Hh3c_secBlade_LSQ1AFCBSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 329)
)
_Hh3c_secBlade_LSB1AFC1A0_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSB1AFC1A0 = _Hh3c_secBlade_LSB1AFC1A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 330)
)
_Hh3c_secpathF1000_C_ObjectIdentity = ObjectIdentity
hh3c_secpathF1000_C = _Hh3c_secpathF1000_C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 331)
)
_Hh3c_secpathF100_A_SI_ObjectIdentity = ObjectIdentity
hh3c_secpathF100_A_SI = _Hh3c_secpathF100_A_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 332)
)
_Hh3c_secpathV100_E_ObjectIdentity = ObjectIdentity
hh3c_secpathV100_E = _Hh3c_secpathV100_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 333)
)
_Hh3c_S5800_32C_ObjectIdentity = ObjectIdentity
hh3c_S5800_32C = _Hh3c_S5800_32C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 334)
)
_Hh3c_S5800_56C_ObjectIdentity = ObjectIdentity
hh3c_S5800_56C = _Hh3c_S5800_56C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 335)
)
_Hh3c_S5800_32C_PWR_ObjectIdentity = ObjectIdentity
hh3c_S5800_32C_PWR = _Hh3c_S5800_32C_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 336)
)
_Hh3c_S5800_56C_PWR_ObjectIdentity = ObjectIdentity
hh3c_S5800_56C_PWR = _Hh3c_S5800_56C_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 337)
)
_Hh3c_S5800_60C_PWR_ObjectIdentity = ObjectIdentity
hh3c_S5800_60C_PWR = _Hh3c_S5800_60C_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 338)
)
_Hh3c_S5800_32F_ObjectIdentity = ObjectIdentity
hh3c_S5800_32F = _Hh3c_S5800_32F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 339)
)
_Hh3c_S5820X_28C_ObjectIdentity = ObjectIdentity
hh3c_S5820X_28C = _Hh3c_S5820X_28C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 340)
)
_Hh3c_S5820X_28S_ObjectIdentity = ObjectIdentity
hh3c_S5820X_28S = _Hh3c_S5820X_28S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 341)
)
_Hh3c_cc602_ObjectIdentity = ObjectIdentity
hh3c_cc602 = _Hh3c_cc602_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 342)
)
_Hh3c_cr400_ObjectIdentity = ObjectIdentity
hh3c_cr400 = _Hh3c_cr400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 343)
)
_Hh3c_cc600E_ObjectIdentity = ObjectIdentity
hh3c_cc600E = _Hh3c_cc600E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 344)
)
_Hh3c_secpathT1000_M_ObjectIdentity = ObjectIdentity
hh3c_secpathT1000_M = _Hh3c_secpathT1000_M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 345)
)
_Hh3c_neoceanVX1540_ObjectIdentity = ObjectIdentity
hh3c_neoceanVX1540 = _Hh3c_neoceanVX1540_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 346)
)
_Hh3c_msr50_06_ObjectIdentity = ObjectIdentity
hh3c_msr50_06 = _Hh3c_msr50_06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 347)
)
_Hh3c_secpathACG2000_M_ObjectIdentity = ObjectIdentity
hh3c_secpathACG2000_M = _Hh3c_secpathACG2000_M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 348)
)
_Hh3c_secBlade_LSQ1ACGASC0_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSQ1ACGASC0 = _Hh3c_secBlade_LSQ1ACGASC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 349)
)
_Hh3c_secBlade_LSB1ACG1A0_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSB1ACG1A0 = _Hh3c_secBlade_LSB1ACG1A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 350)
)
_Hh3c_wx3024wcm_ObjectIdentity = ObjectIdentity
hh3c_wx3024wcm = _Hh3c_wx3024wcm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 351)
)
_Hh3c_wx3024lsw_ObjectIdentity = ObjectIdentity
hh3c_wx3024lsw = _Hh3c_wx3024lsw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 352)
)
_Hh3c_wx5004_ObjectIdentity = ObjectIdentity
hh3c_wx5004 = _Hh3c_wx5004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 353)
)
_Hh3c_sr6604_ObjectIdentity = ObjectIdentity
hh3c_sr6604 = _Hh3c_sr6604_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 354)
)
_Hh3c_iag5000_A_ObjectIdentity = ObjectIdentity
hh3c_iag5000_A = _Hh3c_iag5000_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 355)
)
_Hh3c_secBlade_SPE_FWM_ObjectIdentity = ObjectIdentity
hh3c_secBlade_SPE_FWM = _Hh3c_secBlade_SPE_FWM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 356)
)
_Hh3c_ICG2200_ObjectIdentity = ObjectIdentity
hh3c_ICG2200 = _Hh3c_ICG2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 357)
)
_Hh3c_S7602_ObjectIdentity = ObjectIdentity
hh3c_S7602 = _Hh3c_S7602_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 358)
)
_Hh3c_S7603_ObjectIdentity = ObjectIdentity
hh3c_S7603 = _Hh3c_S7603_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 359)
)
_Hh3c_S7606_ObjectIdentity = ObjectIdentity
hh3c_S7606 = _Hh3c_S7606_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 360)
)
_Hh3c_S7606_V_ObjectIdentity = ObjectIdentity
hh3c_S7606_V = _Hh3c_S7606_V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 361)
)
_Hh3c_S7610_ObjectIdentity = ObjectIdentity
hh3c_S7610 = _Hh3c_S7610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 362)
)
_Hh3c_wa2610e_agn_ObjectIdentity = ObjectIdentity
hh3c_wa2610e_agn = _Hh3c_wa2610e_agn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 363)
)
_Hh3c_wa2620e_agn_ObjectIdentity = ObjectIdentity
hh3c_wa2620e_agn = _Hh3c_wa2620e_agn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 364)
)
_Hh3c_wa1208e_g_v5_ObjectIdentity = ObjectIdentity
hh3c_wa1208e_g_v5 = _Hh3c_wa1208e_g_v5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 365)
)
_Hh3c_wa1208e_dg_v5_ObjectIdentity = ObjectIdentity
hh3c_wa1208e_dg_v5 = _Hh3c_wa1208e_dg_v5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 366)
)
_Hh3c_wa1208e_ag_v5_ObjectIdentity = ObjectIdentity
hh3c_wa1208e_ag_v5 = _Hh3c_wa1208e_ag_v5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 367)
)
_Hh3c_wa1208e_agp_v5_ObjectIdentity = ObjectIdentity
hh3c_wa1208e_agp_v5 = _Hh3c_wa1208e_agp_v5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 368)
)
_Hh3c_wa1208e_gp_v5_ObjectIdentity = ObjectIdentity
hh3c_wa1208e_gp_v5 = _Hh3c_wa1208e_gp_v5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 369)
)
_Hh3c_S7503E_S_ObjectIdentity = ObjectIdentity
hh3c_S7503E_S = _Hh3c_S7503E_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 370)
)
_Hh3c_secpathIAG2000_A_ObjectIdentity = ObjectIdentity
hh3c_secpathIAG2000_A = _Hh3c_secpathIAG2000_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 371)
)
_Hh3c_secpathT1000_A_ObjectIdentity = ObjectIdentity
hh3c_secpathT1000_A = _Hh3c_secpathT1000_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 372)
)
_Hh3c_secpathT1000_S_ObjectIdentity = ObjectIdentity
hh3c_secpathT1000_S = _Hh3c_secpathT1000_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 373)
)
_Hh3c_secBlade_EWPX1FWA0_ObjectIdentity = ObjectIdentity
hh3c_secBlade_EWPX1FWA0 = _Hh3c_secBlade_EWPX1FWA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 374)
)
_Hh3c_secBlade_LSQ1NSMSC0_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSQ1NSMSC0 = _Hh3c_secBlade_LSQ1NSMSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 375)
)
_Hh3c_secBlade_LSQ1AFDBSC0_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSQ1AFDBSC0 = _Hh3c_secBlade_LSQ1AFDBSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 376)
)
_Hh3c_secBlade_LSQ1LBSC0_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSQ1LBSC0 = _Hh3c_secBlade_LSQ1LBSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 377)
)
_Hh3c_secBlade_LSB1LB1A0_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSB1LB1A0 = _Hh3c_secBlade_LSB1LB1A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 378)
)
_Hh3c_neoceanIX1560_ObjectIdentity = ObjectIdentity
hh3c_neoceanIX1560 = _Hh3c_neoceanIX1560_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 379)
)
_Hh3c_neoceanEX1500S_ObjectIdentity = ObjectIdentity
hh3c_neoceanEX1500S = _Hh3c_neoceanEX1500S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 380)
)
_Hh3c_neoceanEX1520S_ObjectIdentity = ObjectIdentity
hh3c_neoceanEX1520S = _Hh3c_neoceanEX1520S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 381)
)
_Hh3c_neoceanEX1540S_ObjectIdentity = ObjectIdentity
hh3c_neoceanEX1540S = _Hh3c_neoceanEX1540S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 382)
)
_Hh3c_neoceanEX1560S_ObjectIdentity = ObjectIdentity
hh3c_neoceanEX1560S = _Hh3c_neoceanEX1560S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 383)
)
_Hh3c_ET716_ObjectIdentity = ObjectIdentity
hh3c_ET716 = _Hh3c_ET716_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 384)
)
_Hh3c_s3600_2P_OLT_ObjectIdentity = ObjectIdentity
hh3c_s3600_2P_OLT = _Hh3c_s3600_2P_OLT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 385)
)
_Hh3c_ER3200_ObjectIdentity = ObjectIdentity
hh3c_ER3200 = _Hh3c_ER3200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 386)
)
_Hh3c_ER3100_ObjectIdentity = ObjectIdentity
hh3c_ER3100 = _Hh3c_ER3100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 387)
)
_Hh3c_s9505E_ObjectIdentity = ObjectIdentity
hh3c_s9505E = _Hh3c_s9505E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 388)
)
_Hh3c_s9508E_V_ObjectIdentity = ObjectIdentity
hh3c_s9508E_V = _Hh3c_s9508E_V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 389)
)
_Hh3c_s9512E_ObjectIdentity = ObjectIdentity
hh3c_s9512E = _Hh3c_s9512E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 390)
)
_Hh3c_s12508_ObjectIdentity = ObjectIdentity
hh3c_s12508 = _Hh3c_s12508_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 391)
)
_Hh3c_s12518_ObjectIdentity = ObjectIdentity
hh3c_s12518 = _Hh3c_s12518_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 392)
)
_Hh3c_ET708_ObjectIdentity = ObjectIdentity
hh3c_ET708 = _Hh3c_ET708_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 393)
)
_Hh3c_ET724_ObjectIdentity = ObjectIdentity
hh3c_ET724 = _Hh3c_ET724_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 394)
)
_Hh3c_s2008TP_EA_ObjectIdentity = ObjectIdentity
hh3c_s2008TP_EA = _Hh3c_s2008TP_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 395)
)
_Hh3c_s2016TP_EA_ObjectIdentity = ObjectIdentity
hh3c_s2016TP_EA = _Hh3c_s2016TP_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 396)
)
_Hh3c_s2403TP_EA_ObjectIdentity = ObjectIdentity
hh3c_s2403TP_EA = _Hh3c_s2403TP_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 397)
)
_Hh3c_ICG2000_CT_ObjectIdentity = ObjectIdentity
hh3c_ICG2000_CT = _Hh3c_ICG2000_CT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 398)
)
_Hh3c_S3528P_EA_ObjectIdentity = ObjectIdentity
hh3c_S3528P_EA = _Hh3c_S3528P_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 400)
)
_Hh3c_S3552P_EA_ObjectIdentity = ObjectIdentity
hh3c_S3552P_EA = _Hh3c_S3552P_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 401)
)
_Hh3c_S3552F_EA_ObjectIdentity = ObjectIdentity
hh3c_S3552F_EA = _Hh3c_S3552F_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 402)
)
_Hh3c_S3528F_EA_ObjectIdentity = ObjectIdentity
hh3c_S3528F_EA = _Hh3c_S3528F_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 403)
)
_Hh3c_S3528TP_EA_ObjectIdentity = ObjectIdentity
hh3c_S3528TP_EA = _Hh3c_S3528TP_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 404)
)
_Hh3c_secpathAFD1000_A_ObjectIdentity = ObjectIdentity
hh3c_secpathAFD1000_A = _Hh3c_secpathAFD1000_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 405)
)
_Hh3c_secpathF100_C_EI_ObjectIdentity = ObjectIdentity
hh3c_secpathF100_C_EI = _Hh3c_secpathF100_C_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 406)
)
_Hh3c_ER3260_ObjectIdentity = ObjectIdentity
hh3c_ER3260 = _Hh3c_ER3260_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 407)
)
_Hh3c_ICG800_ObjectIdentity = ObjectIdentity
hh3c_ICG800 = _Hh3c_ICG800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 408)
)
_Hh3c_ICG800g_ObjectIdentity = ObjectIdentity
hh3c_ICG800g = _Hh3c_ICG800g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 409)
)
_Hh3c_ICG1000_ObjectIdentity = ObjectIdentity
hh3c_ICG1000 = _Hh3c_ICG1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 410)
)
_Hh3c_ICG1800_ObjectIdentity = ObjectIdentity
hh3c_ICG1800 = _Hh3c_ICG1800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 411)
)
_Hh3c_neoceanIX3240E_ObjectIdentity = ObjectIdentity
hh3c_neoceanIX3240E = _Hh3c_neoceanIX3240E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 412)
)
_Hh3c_neoceanIX3620E_ObjectIdentity = ObjectIdentity
hh3c_neoceanIX3620E = _Hh3c_neoceanIX3620E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 413)
)
_Hh3c_neoceanIX3640E_ObjectIdentity = ObjectIdentity
hh3c_neoceanIX3640E = _Hh3c_neoceanIX3640E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 414)
)
_Hh3c_secpathACG8800_S3_ObjectIdentity = ObjectIdentity
hh3c_secpathACG8800_S3 = _Hh3c_secpathACG8800_S3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 415)
)
_Hh3c_secpathT5000_S3_ObjectIdentity = ObjectIdentity
hh3c_secpathT5000_S3 = _Hh3c_secpathT5000_S3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 416)
)
_Hh3c_secpathIAG2000_S_ObjectIdentity = ObjectIdentity
hh3c_secpathIAG2000_S = _Hh3c_secpathIAG2000_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 417)
)
_Hh3c_secpathACG8800_S3_NS21S2MSPB0_ObjectIdentity = ObjectIdentity
hh3c_secpathACG8800_S3_NS21S2MSPB0 = _Hh3c_secpathACG8800_S3_NS21S2MSPB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 418)
)
_Hh3c_secpathT5000_S3_NS11S2MSPB0_ObjectIdentity = ObjectIdentity
hh3c_secpathT5000_S3_NS11S2MSPB0 = _Hh3c_secpathT5000_S3_NS11S2MSPB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 419)
)
_Hh3c_msr3010_ObjectIdentity = ObjectIdentity
hh3c_msr3010 = _Hh3c_msr3010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 420)
)
_Hh3c_msr3011E_ObjectIdentity = ObjectIdentity
hh3c_msr3011E = _Hh3c_msr3011E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 421)
)
_Hh3c_msr3011F_ObjectIdentity = ObjectIdentity
hh3c_msr3011F = _Hh3c_msr3011F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 422)
)
_Hh3c_secpathT200_A_ObjectIdentity = ObjectIdentity
hh3c_secpathT200_A = _Hh3c_secpathT200_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 423)
)
_Hh3c_secpathT200_M_ObjectIdentity = ObjectIdentity
hh3c_secpathT200_M = _Hh3c_secpathT200_M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 424)
)
_Hh3c_secpathF100_C2_ObjectIdentity = ObjectIdentity
hh3c_secpathF100_C2 = _Hh3c_secpathF100_C2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 425)
)
_Hh3c_DPtech_FW1000_GE_ObjectIdentity = ObjectIdentity
hh3c_DPtech_FW1000_GE = _Hh3c_DPtech_FW1000_GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 426)
)
_Hh3c_DPtech_FW1000_GA_ObjectIdentity = ObjectIdentity
hh3c_DPtech_FW1000_GA = _Hh3c_DPtech_FW1000_GA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 427)
)
_Hh3c_DPtech_FW1000_GS_ObjectIdentity = ObjectIdentity
hh3c_DPtech_FW1000_GS = _Hh3c_DPtech_FW1000_GS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 428)
)
_Hh3c_DPtech_FW1000_ME_ObjectIdentity = ObjectIdentity
hh3c_DPtech_FW1000_ME = _Hh3c_DPtech_FW1000_ME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 429)
)
_Hh3c_DPtech_FW1000_MA_ObjectIdentity = ObjectIdentity
hh3c_DPtech_FW1000_MA = _Hh3c_DPtech_FW1000_MA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 430)
)
_Hh3c_DPtech_FW1000_MM_ObjectIdentity = ObjectIdentity
hh3c_DPtech_FW1000_MM = _Hh3c_DPtech_FW1000_MM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 431)
)
_Hh3c_DPtech_FW1000_MC_ObjectIdentity = ObjectIdentity
hh3c_DPtech_FW1000_MC = _Hh3c_DPtech_FW1000_MC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 432)
)
_Hh3c_DPtech_UTM2000_MA_ObjectIdentity = ObjectIdentity
hh3c_DPtech_UTM2000_MA = _Hh3c_DPtech_UTM2000_MA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 433)
)
_Hh3c_DPtech_UTM2000_MM_ObjectIdentity = ObjectIdentity
hh3c_DPtech_UTM2000_MM = _Hh3c_DPtech_UTM2000_MM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 434)
)
_Hh3c_DPtech_UTM2000_MS_ObjectIdentity = ObjectIdentity
hh3c_DPtech_UTM2000_MS = _Hh3c_DPtech_UTM2000_MS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 435)
)
_Hh3c_DPtech_IPS2000_GM_ObjectIdentity = ObjectIdentity
hh3c_DPtech_IPS2000_GM = _Hh3c_DPtech_IPS2000_GM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 436)
)
_Hh3c_DPtech_IPS2000_MM_ObjectIdentity = ObjectIdentity
hh3c_DPtech_IPS2000_MM = _Hh3c_DPtech_IPS2000_MM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 437)
)
_Hh3c_sr6616_ObjectIdentity = ObjectIdentity
hh3c_sr6616 = _Hh3c_sr6616_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 438)
)
_Hh3c_s3620_28TP_EI_ObjectIdentity = ObjectIdentity
hh3c_s3620_28TP_EI = _Hh3c_s3620_28TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 439)
)
_Hh3c_s3620_28P_EI_ObjectIdentity = ObjectIdentity
hh3c_s3620_28P_EI = _Hh3c_s3620_28P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 440)
)
_Hh3c_s3620_52P_EI_ObjectIdentity = ObjectIdentity
hh3c_s3620_52P_EI = _Hh3c_s3620_52P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 441)
)
_Hh3c_s3620_28P_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_s3620_28P_PWR_EI = _Hh3c_s3620_28P_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 442)
)
_Hh3c_s3620_52P_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_s3620_52P_PWR_EI = _Hh3c_s3620_52P_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 443)
)
_Hh3c_s3620_28F_EI_ObjectIdentity = ObjectIdentity
hh3c_s3620_28F_EI = _Hh3c_s3620_28F_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 444)
)
_Hh3c_s3620_52M_ObjectIdentity = ObjectIdentity
hh3c_s3620_52M = _Hh3c_s3620_52M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 445)
)
_Hh3c_s3620_52M_DC_ObjectIdentity = ObjectIdentity
hh3c_s3620_52M_DC = _Hh3c_s3620_52M_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 446)
)
_Hh3c_s3620_28C_EI_ObjectIdentity = ObjectIdentity
hh3c_s3620_28C_EI = _Hh3c_s3620_28C_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 447)
)
_Hh3c_wa2210e_ge_ObjectIdentity = ObjectIdentity
hh3c_wa2210e_ge = _Hh3c_wa2210e_ge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 448)
)
_Hh3c_wa2220x_age_ObjectIdentity = ObjectIdentity
hh3c_wa2220x_age = _Hh3c_wa2220x_age_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 449)
)
_Hh3c_wa2210x_ge_ObjectIdentity = ObjectIdentity
hh3c_wa2210x_ge = _Hh3c_wa2210x_ge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 450)
)
_Hh3c_wb2320x_age_ObjectIdentity = ObjectIdentity
hh3c_wb2320x_age = _Hh3c_wb2320x_age_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 451)
)
_Hh3c_neoceanEX1540_ObjectIdentity = ObjectIdentity
hh3c_neoceanEX1540 = _Hh3c_neoceanEX1540_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 452)
)
_Hh3c_S5810_50S_ObjectIdentity = ObjectIdentity
hh3c_S5810_50S = _Hh3c_S5810_50S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 453)
)
_Hh3c_secBlade_LSQ1IPSSC0_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSQ1IPSSC0 = _Hh3c_secBlade_LSQ1IPSSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 454)
)
_Hh3c_secBlade_LSB1IPS1A0_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSB1IPS1A0 = _Hh3c_secBlade_LSB1IPS1A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 455)
)
_Hh3c_ER5100_ObjectIdentity = ObjectIdentity
hh3c_ER5100 = _Hh3c_ER5100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 456)
)
_Hh3c_ER5200_ObjectIdentity = ObjectIdentity
hh3c_ER5200 = _Hh3c_ER5200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 457)
)
_Hh3c_wx3010wcm_ObjectIdentity = ObjectIdentity
hh3c_wx3010wcm = _Hh3c_wx3010wcm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 458)
)
_Hh3c_wx3010lsw_ObjectIdentity = ObjectIdentity
hh3c_wx3010lsw = _Hh3c_wx3010lsw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 459)
)
_Hh3c_cc652E_ObjectIdentity = ObjectIdentity
hh3c_cc652E = _Hh3c_cc652E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 460)
)
_Hh3c_S5120_20P_SI_ObjectIdentity = ObjectIdentity
hh3c_S5120_20P_SI = _Hh3c_S5120_20P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 461)
)
_Hh3c_S5120_28P_SI_ObjectIdentity = ObjectIdentity
hh3c_S5120_28P_SI = _Hh3c_S5120_28P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 462)
)
_Hh3c_S5120_52P_SI_ObjectIdentity = ObjectIdentity
hh3c_S5120_52P_SI = _Hh3c_S5120_52P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 463)
)
_Hh3c_S5120_28P_EI_ObjectIdentity = ObjectIdentity
hh3c_S5120_28P_EI = _Hh3c_S5120_28P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 464)
)
_Hh3c_S5120_52P_EI_ObjectIdentity = ObjectIdentity
hh3c_S5120_52P_EI = _Hh3c_S5120_52P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 465)
)
_Hh3c_S5120_28P_LPWR_EI_ObjectIdentity = ObjectIdentity
hh3c_S5120_28P_LPWR_EI = _Hh3c_S5120_28P_LPWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 466)
)
_Hh3c_S5120_28P_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_S5120_28P_PWR_EI = _Hh3c_S5120_28P_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 467)
)
_Hh3c_wx6100LSR_ObjectIdentity = ObjectIdentity
hh3c_wx6100LSR = _Hh3c_wx6100LSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 468)
)
_Hh3c_s7506E_S_ObjectIdentity = ObjectIdentity
hh3c_s7506E_S = _Hh3c_s7506E_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 469)
)
_Hh3c_ICG2000B_ObjectIdentity = ObjectIdentity
hh3c_ICG2000B = _Hh3c_ICG2000B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 470)
)
_Hh3c_ICG2000C_ObjectIdentity = ObjectIdentity
hh3c_ICG2000C = _Hh3c_ICG2000C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 471)
)
_Hh3c_S1626_ObjectIdentity = ObjectIdentity
hh3c_S1626 = _Hh3c_S1626_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 472)
)
_Hh3c_S1650_ObjectIdentity = ObjectIdentity
hh3c_S1650 = _Hh3c_S1650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 473)
)
_Hh3c_S1626P_ObjectIdentity = ObjectIdentity
hh3c_S1626P = _Hh3c_S1626P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 474)
)
_Hh3c_neoceanIX3620S_ObjectIdentity = ObjectIdentity
hh3c_neoceanIX3620S = _Hh3c_neoceanIX3620S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 475)
)
_Hh3c_neoceanIX3080S_ObjectIdentity = ObjectIdentity
hh3c_neoceanIX3080S = _Hh3c_neoceanIX3080S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 476)
)
_Hh3c_ER3280g_ObjectIdentity = ObjectIdentity
hh3c_ER3280g = _Hh3c_ER3280g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 477)
)
_Hh3c_wa2610_agn_ObjectIdentity = ObjectIdentity
hh3c_wa2610_agn = _Hh3c_wa2610_agn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 478)
)
_Hh3c_wa2612_agn_ObjectIdentity = ObjectIdentity
hh3c_wa2612_agn = _Hh3c_wa2612_agn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 479)
)
_Hh3c_secpathT200_S_ObjectIdentity = ObjectIdentity
hh3c_secpathT200_S = _Hh3c_secpathT200_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 480)
)
_Hh3c_secpathU200_CS_ObjectIdentity = ObjectIdentity
hh3c_secpathU200_CS = _Hh3c_secpathU200_CS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 481)
)
_Hh3c_secpathU200_CM_ObjectIdentity = ObjectIdentity
hh3c_secpathU200_CM = _Hh3c_secpathU200_CM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 482)
)
_Hh3c_secpathU200_CA_ObjectIdentity = ObjectIdentity
hh3c_secpathU200_CA = _Hh3c_secpathU200_CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 483)
)
_Hh3c_secBlade_LSR1AFC2A1_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSR1AFC2A1 = _Hh3c_secBlade_LSR1AFC2A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 484)
)
_Hh3c_secBlade_LSR1FW2A1_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSR1FW2A1 = _Hh3c_secBlade_LSR1FW2A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 485)
)
_Hh3c_secBlade_LSR1LB1A1_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSR1LB1A1 = _Hh3c_secBlade_LSR1LB1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 486)
)
_Hh3c_secBlade_LSR1NSM1A1_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSR1NSM1A1 = _Hh3c_secBlade_LSR1NSM1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 487)
)
_Hh3c_cc650E_ObjectIdentity = ObjectIdentity
hh3c_cc650E = _Hh3c_cc650E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 488)
)
_Hh3c_LSWM1WCM10_ObjectIdentity = ObjectIdentity
hh3c_LSWM1WCM10 = _Hh3c_LSWM1WCM10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 489)
)
_Hh3c_LSWM1WCM20_ObjectIdentity = ObjectIdentity
hh3c_LSWM1WCM20 = _Hh3c_LSWM1WCM20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 490)
)
_Hh3c_EWPXM1WCMC0_ObjectIdentity = ObjectIdentity
hh3c_EWPXM1WCMC0 = _Hh3c_EWPXM1WCMC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 491)
)
_Hh3c_LSWM1IPS10_ObjectIdentity = ObjectIdentity
hh3c_LSWM1IPS10 = _Hh3c_LSWM1IPS10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 492)
)
_Hh3c_LSWM1FW10_ObjectIdentity = ObjectIdentity
hh3c_LSWM1FW10 = _Hh3c_LSWM1FW10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 493)
)
_Hh3c_secpathF1000_S_EI_ObjectIdentity = ObjectIdentity
hh3c_secpathF1000_S_EI = _Hh3c_secpathF1000_S_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 494)
)
_Hh3c_secpathF1000_A_EI_ObjectIdentity = ObjectIdentity
hh3c_secpathF1000_A_EI = _Hh3c_secpathF1000_A_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 495)
)
_Hh3c_msr50_06_V5_ObjectIdentity = ObjectIdentity
hh3c_msr50_06_V5 = _Hh3c_msr50_06_V5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 496)
)
_Hh3c_secBlade_LSR1ACG1A1_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSR1ACG1A1 = _Hh3c_secBlade_LSR1ACG1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 497)
)
_Hh3c_secBlade_LSR1IPS1A1_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSR1IPS1A1 = _Hh3c_secBlade_LSR1IPS1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 498)
)
_Hh3c_S7602_S_ObjectIdentity = ObjectIdentity
hh3c_S7602_S = _Hh3c_S7602_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 499)
)
_Hh3c_S7603_S_ObjectIdentity = ObjectIdentity
hh3c_S7603_S = _Hh3c_S7603_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 500)
)
_Hh3c_S7606_S_ObjectIdentity = ObjectIdentity
hh3c_S7606_S = _Hh3c_S7606_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 501)
)
_Hh3c_SSM_s5500G_ObjectIdentity = ObjectIdentity
hh3c_SSM_s5500G = _Hh3c_SSM_s5500G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 502)
)
_Hh3c_SSM_FIC_ObjectIdentity = ObjectIdentity
hh3c_SSM_FIC = _Hh3c_SSM_FIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 503)
)
_Hh3c_SSM_MIM_ObjectIdentity = ObjectIdentity
hh3c_SSM_MIM = _Hh3c_SSM_MIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 504)
)
_Hh3c_ER8300_ObjectIdentity = ObjectIdentity
hh3c_ER8300 = _Hh3c_ER8300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 505)
)
_Hh3c_wa2610x_gnp_ObjectIdentity = ObjectIdentity
hh3c_wa2610x_gnp = _Hh3c_wa2610x_gnp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 506)
)
_Hh3c_wb2360x_anp_ObjectIdentity = ObjectIdentity
hh3c_wb2360x_anp = _Hh3c_wb2360x_anp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 507)
)
_Hh3c_wh2530x_dag_ObjectIdentity = ObjectIdentity
hh3c_wh2530x_dag = _Hh3c_wh2530x_dag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 508)
)
_Hh3c_wa2620_agn_ObjectIdentity = ObjectIdentity
hh3c_wa2620_agn = _Hh3c_wa2620_agn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 509)
)
_Hh3c_cc610E_ObjectIdentity = ObjectIdentity
hh3c_cc610E = _Hh3c_cc610E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 510)
)
_Hh3c_DPtech_FW1000_GT_ObjectIdentity = ObjectIdentity
hh3c_DPtech_FW1000_GT = _Hh3c_DPtech_FW1000_GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 511)
)
_Hh3c_s2008TP_EA_SI_ObjectIdentity = ObjectIdentity
hh3c_s2008TP_EA_SI = _Hh3c_s2008TP_EA_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 512)
)
_Hh3c_s2016TP_EA_SI_ObjectIdentity = ObjectIdentity
hh3c_s2016TP_EA_SI = _Hh3c_s2016TP_EA_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 513)
)
_Hh3c_s2403TP_EA_SI_ObjectIdentity = ObjectIdentity
hh3c_s2403TP_EA_SI = _Hh3c_s2403TP_EA_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 514)
)
_Hh3c_S5120_24P_EI_ObjectIdentity = ObjectIdentity
hh3c_S5120_24P_EI = _Hh3c_S5120_24P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 515)
)
_Hh3c_S5120_48P_EI_ObjectIdentity = ObjectIdentity
hh3c_S5120_48P_EI = _Hh3c_S5120_48P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 516)
)
_Hh3c_S5120_28C_EI_ObjectIdentity = ObjectIdentity
hh3c_S5120_28C_EI = _Hh3c_S5120_28C_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 517)
)
_Hh3c_S5120_52C_EI_ObjectIdentity = ObjectIdentity
hh3c_S5120_52C_EI = _Hh3c_S5120_52C_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 518)
)
_Hh3c_S5120_28C_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_S5120_28C_PWR_EI = _Hh3c_S5120_28C_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 519)
)
_Hh3c_S5120_52C_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_S5120_52C_PWR_EI = _Hh3c_S5120_52C_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 520)
)
_Hh3c_wx3008wcm_ObjectIdentity = ObjectIdentity
hh3c_wx3008wcm = _Hh3c_wx3008wcm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 521)
)
_Hh3c_wx3008lsw_ObjectIdentity = ObjectIdentity
hh3c_wx3008lsw = _Hh3c_wx3008lsw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 522)
)
_Hh3c_msr900_ObjectIdentity = ObjectIdentity
hh3c_msr900 = _Hh3c_msr900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 523)
)
_Hh3c_msr920_ObjectIdentity = ObjectIdentity
hh3c_msr920 = _Hh3c_msr920_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 524)
)
_Hh3c_secBlade_LSQ1IAGSC0_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSQ1IAGSC0 = _Hh3c_secBlade_LSQ1IAGSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 525)
)
_Hh3c_WX7306_ObjectIdentity = ObjectIdentity
hh3c_WX7306 = _Hh3c_WX7306_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 526)
)
_Hh3c_WX7310_ObjectIdentity = ObjectIdentity
hh3c_WX7310 = _Hh3c_WX7310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 527)
)
_Hh3c_Blade5310_ObjectIdentity = ObjectIdentity
hh3c_Blade5310 = _Hh3c_Blade5310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 528)
)
_Hh3c_Blade55102_ObjectIdentity = ObjectIdentity
hh3c_Blade55102 = _Hh3c_Blade55102_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 529)
)
_Hh3c_Blade5512S_ObjectIdentity = ObjectIdentity
hh3c_Blade5512S = _Hh3c_Blade5512S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 530)
)
_Hh3c_Blade55110X_ObjectIdentity = ObjectIdentity
hh3c_Blade55110X = _Hh3c_Blade55110X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 531)
)
_Hh3c_wa2610e_gnp_ObjectIdentity = ObjectIdentity
hh3c_wa2610e_gnp = _Hh3c_wa2610e_gnp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 532)
)
_Hh3c_s3100_26TP_SI_UM_ObjectIdentity = ObjectIdentity
hh3c_s3100_26TP_SI_UM = _Hh3c_s3100_26TP_SI_UM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 533)
)
_Hh3c_s3100_52TP_SI_UM_ObjectIdentity = ObjectIdentity
hh3c_s3100_52TP_SI_UM = _Hh3c_s3100_52TP_SI_UM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 534)
)
_Hh3c_s5500_24P_SI_ObjectIdentity = ObjectIdentity
hh3c_s5500_24P_SI = _Hh3c_s5500_24P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 535)
)
_Hh3c_s5500_48P_SI_ObjectIdentity = ObjectIdentity
hh3c_s5500_48P_SI = _Hh3c_s5500_48P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 536)
)
_Hh3c_ME8000_ObjectIdentity = ObjectIdentity
hh3c_ME8000 = _Hh3c_ME8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 537)
)
_Hh3c_ME8600_ObjectIdentity = ObjectIdentity
hh3c_ME8600 = _Hh3c_ME8600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 538)
)
_Hh3c_ME5000_ObjectIdentity = ObjectIdentity
hh3c_ME5000 = _Hh3c_ME5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 539)
)
_Hh3c_MG6060_ObjectIdentity = ObjectIdentity
hh3c_MG6060 = _Hh3c_MG6060_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 540)
)
_Hh3c_MG6050_ObjectIdentity = ObjectIdentity
hh3c_MG6050 = _Hh3c_MG6050_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 541)
)
_Hh3c_MG6050S_ObjectIdentity = ObjectIdentity
hh3c_MG6050S = _Hh3c_MG6050S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 542)
)
_Hh3c_MG9010_ObjectIdentity = ObjectIdentity
hh3c_MG9010 = _Hh3c_MG9010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 543)
)
_Hh3c_MG9030_ObjectIdentity = ObjectIdentity
hh3c_MG9030 = _Hh3c_MG9030_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 544)
)
_Hh3c_MG9060_ObjectIdentity = ObjectIdentity
hh3c_MG9060 = _Hh3c_MG9060_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 545)
)
_Hh3c_neoceanVX1500_DC_ObjectIdentity = ObjectIdentity
hh3c_neoceanVX1500_DC = _Hh3c_neoceanVX1500_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 546)
)
_Hh3c_cc620E_ObjectIdentity = ObjectIdentity
hh3c_cc620E = _Hh3c_cc620E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 547)
)
_Hh3c_SIVX_S3628_ObjectIdentity = ObjectIdentity
hh3c_SIVX_S3628 = _Hh3c_SIVX_S3628_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 548)
)
_Hh3c_SIVX_S5528_ObjectIdentity = ObjectIdentity
hh3c_SIVX_S5528 = _Hh3c_SIVX_S5528_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 549)
)
_Hh3c_SIVX_VS1500_ObjectIdentity = ObjectIdentity
hh3c_SIVX_VS1500 = _Hh3c_SIVX_VS1500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 550)
)
_Hh3c_neoceanIX2540_ObjectIdentity = ObjectIdentity
hh3c_neoceanIX2540 = _Hh3c_neoceanIX2540_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 551)
)
_Hh3c_neoceanVX2500_ObjectIdentity = ObjectIdentity
hh3c_neoceanVX2500 = _Hh3c_neoceanVX2500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 552)
)
_Hh3c_S5120_28P_PWR_SI_ObjectIdentity = ObjectIdentity
hh3c_S5120_28P_PWR_SI = _Hh3c_S5120_28P_PWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 555)
)
_Hh3c_S5120_28P_HPWR_SI_ObjectIdentity = ObjectIdentity
hh3c_S5120_28P_HPWR_SI = _Hh3c_S5120_28P_HPWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 556)
)
_Hh3c_F1000_E_DC_ObjectIdentity = ObjectIdentity
hh3c_F1000_E_DC = _Hh3c_F1000_E_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 557)
)
_Hh3c_S5028_ObjectIdentity = ObjectIdentity
hh3c_S5028 = _Hh3c_S5028_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 558)
)
_Hh3c_ET824_ObjectIdentity = ObjectIdentity
hh3c_ET824 = _Hh3c_ET824_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 559)
)
_Hh3c_OSM_ObjectIdentity = ObjectIdentity
hh3c_OSM = _Hh3c_OSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 560)
)
_Hh3c_wx5002_v2_ObjectIdentity = ObjectIdentity
hh3c_wx5002_v2 = _Hh3c_wx5002_v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 561)
)
_Hh3c_wx5004_v2_ObjectIdentity = ObjectIdentity
hh3c_wx5004_v2 = _Hh3c_wx5004_v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 562)
)
_Hh3c_secpathT1000_C_ObjectIdentity = ObjectIdentity
hh3c_secpathT1000_C = _Hh3c_secpathT1000_C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 563)
)
_Hh3c_secBlade_LST1IPS1A1_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LST1IPS1A1 = _Hh3c_secBlade_LST1IPS1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 564)
)
_Hh3c_secBlade_LST1FW2A1_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LST1FW2A1 = _Hh3c_secBlade_LST1FW2A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 565)
)
_Hh3c_secBlade_LST1LB1A1_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LST1LB1A1 = _Hh3c_secBlade_LST1LB1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 566)
)
_Hh3c_secBlade_LST1NSM1A1_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LST1NSM1A1 = _Hh3c_secBlade_LST1NSM1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 567)
)
_Hh3c_secBlade_EWPX2IAGSC0_ObjectIdentity = ObjectIdentity
hh3c_secBlade_EWPX2IAGSC0 = _Hh3c_secBlade_EWPX2IAGSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 568)
)
_Hh3c_F1000_A_EI_ObjectIdentity = ObjectIdentity
hh3c_F1000_A_EI = _Hh3c_F1000_A_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 569)
)
_Hh3c_wx6108E_ObjectIdentity = ObjectIdentity
hh3c_wx6108E = _Hh3c_wx6108E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 570)
)
_Hh3c_wx6112E_ObjectIdentity = ObjectIdentity
hh3c_wx6112E = _Hh3c_wx6112E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 571)
)
_Hh3c_s5500_34C_HI_ObjectIdentity = ObjectIdentity
hh3c_s5500_34C_HI = _Hh3c_s5500_34C_HI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 572)
)
_Hh3c_s5500_58C_HI_ObjectIdentity = ObjectIdentity
hh3c_s5500_58C_HI = _Hh3c_s5500_58C_HI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 573)
)
_Hh3c_wa1208e_gp_h20_ObjectIdentity = ObjectIdentity
hh3c_wa1208e_gp_h20 = _Hh3c_wa1208e_gp_h20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 574)
)
_Hh3c_S5120_9P_SI_ObjectIdentity = ObjectIdentity
hh3c_S5120_9P_SI = _Hh3c_S5120_9P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 575)
)
_Hh3c_S5120_9P_PWR_SI_ObjectIdentity = ObjectIdentity
hh3c_S5120_9P_PWR_SI = _Hh3c_S5120_9P_PWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 576)
)
_Hh3c_S5120_9P_HPWR_SI_ObjectIdentity = ObjectIdentity
hh3c_S5120_9P_HPWR_SI = _Hh3c_S5120_9P_HPWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 577)
)
_Hh3c_e528_ObjectIdentity = ObjectIdentity
hh3c_e528 = _Hh3c_e528_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 578)
)
_Hh3c_e552_ObjectIdentity = ObjectIdentity
hh3c_e552 = _Hh3c_e552_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 579)
)
_Hh3c_s3600V2_28TP_EI_ObjectIdentity = ObjectIdentity
hh3c_s3600V2_28TP_EI = _Hh3c_s3600V2_28TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 580)
)
_Hh3c_s3600V2_52TP_EI_ObjectIdentity = ObjectIdentity
hh3c_s3600V2_52TP_EI = _Hh3c_s3600V2_52TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 581)
)
_Hh3c_s3600V2_28TP_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_s3600V2_28TP_PWR_EI = _Hh3c_s3600V2_28TP_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 582)
)
_Hh3c_s3600V2_52TP_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_s3600V2_52TP_PWR_EI = _Hh3c_s3600V2_52TP_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 583)
)
_Hh3c_s3600V2_28F_EI_ObjectIdentity = ObjectIdentity
hh3c_s3600V2_28F_EI = _Hh3c_s3600V2_28F_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 584)
)
_Hh3c_s3600V2_28TP_SI_ObjectIdentity = ObjectIdentity
hh3c_s3600V2_28TP_SI = _Hh3c_s3600V2_28TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 585)
)
_Hh3c_s3600V2_52TP_SI_ObjectIdentity = ObjectIdentity
hh3c_s3600V2_52TP_SI = _Hh3c_s3600V2_52TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 586)
)
_Hh3c_s3600V2_28TP_PWR_SI_ObjectIdentity = ObjectIdentity
hh3c_s3600V2_28TP_PWR_SI = _Hh3c_s3600V2_28TP_PWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 587)
)
_Hh3c_s3600V2_52TP_PWR_SI_ObjectIdentity = ObjectIdentity
hh3c_s3600V2_52TP_PWR_SI = _Hh3c_s3600V2_52TP_PWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 588)
)
_Hh3c_s3500V2_28TP_EA_ObjectIdentity = ObjectIdentity
hh3c_s3500V2_28TP_EA = _Hh3c_s3500V2_28TP_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 589)
)
_Hh3c_s3500V2_52TP_EA_ObjectIdentity = ObjectIdentity
hh3c_s3500V2_52TP_EA = _Hh3c_s3500V2_52TP_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 590)
)
_Hh3c_s3500V2_28F_EA_ObjectIdentity = ObjectIdentity
hh3c_s3500V2_28F_EA = _Hh3c_s3500V2_28F_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 591)
)
_Hh3c_s3500V2_28TP_SI_ObjectIdentity = ObjectIdentity
hh3c_s3500V2_28TP_SI = _Hh3c_s3500V2_28TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 592)
)
_Hh3c_s3500V2_52TP_SI_ObjectIdentity = ObjectIdentity
hh3c_s3500V2_52TP_SI = _Hh3c_s3500V2_52TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 593)
)
_Hh3c_s9508E_ObjectIdentity = ObjectIdentity
hh3c_s9508E = _Hh3c_s9508E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 594)
)
_Hh3c_s12504_ObjectIdentity = ObjectIdentity
hh3c_s12504 = _Hh3c_s12504_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 595)
)
_Hh3c_ICG2000B_GT_ObjectIdentity = ObjectIdentity
hh3c_ICG2000B_GT = _Hh3c_ICG2000B_GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 596)
)
_Hh3c_ICG3000B_ObjectIdentity = ObjectIdentity
hh3c_ICG3000B = _Hh3c_ICG3000B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 597)
)
_Hh3c_ICG3000S_ObjectIdentity = ObjectIdentity
hh3c_ICG3000S = _Hh3c_ICG3000S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 598)
)
_Hh3c_ICG5000B_ObjectIdentity = ObjectIdentity
hh3c_ICG5000B = _Hh3c_ICG5000B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 599)
)
_Hh3c_wh2640X_agnp_ObjectIdentity = ObjectIdentity
hh3c_wh2640X_agnp = _Hh3c_wh2640X_agnp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 600)
)
_Hh3c_wa2620X_agnp_ObjectIdentity = ObjectIdentity
hh3c_wa2620X_agnp = _Hh3c_wa2620X_agnp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 601)
)
_Hh3c_s3100_16TP_PWR_EI_F_ObjectIdentity = ObjectIdentity
hh3c_s3100_16TP_PWR_EI_F = _Hh3c_s3100_16TP_PWR_EI_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 602)
)
_Hh3c_cr16018_ObjectIdentity = ObjectIdentity
hh3c_cr16018 = _Hh3c_cr16018_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 603)
)
_Hh3c_cr16008_ObjectIdentity = ObjectIdentity
hh3c_cr16008 = _Hh3c_cr16008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 604)
)
_Hh3c_cr16004_ObjectIdentity = ObjectIdentity
hh3c_cr16004 = _Hh3c_cr16004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 605)
)
_Hh3c_F1000_A_SI_ObjectIdentity = ObjectIdentity
hh3c_F1000_A_SI = _Hh3c_F1000_A_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 606)
)
_Hh3c_F1000_E_SI_ObjectIdentity = ObjectIdentity
hh3c_F1000_E_SI = _Hh3c_F1000_E_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 607)
)
_Hh3c_secBlade_LST1ACG1A1_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LST1ACG1A1 = _Hh3c_secBlade_LST1ACG1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 608)
)
_Hh3c_secBlade_SPE_IPS_ObjectIdentity = ObjectIdentity
hh3c_secBlade_SPE_IPS = _Hh3c_secBlade_SPE_IPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 609)
)
_Hh3c_secBlade_SPE_ACG_ObjectIdentity = ObjectIdentity
hh3c_secBlade_SPE_ACG = _Hh3c_secBlade_SPE_ACG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 610)
)
_Hh3c_wx6103_ObjectIdentity = ObjectIdentity
hh3c_wx6103 = _Hh3c_wx6103_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 611)
)
_Hh3c_LSQ1WCMD0_ObjectIdentity = ObjectIdentity
hh3c_LSQ1WCMD0 = _Hh3c_LSQ1WCMD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 612)
)
_Hh3c_EWPX2WCMD0_ObjectIdentity = ObjectIdentity
hh3c_EWPX2WCMD0 = _Hh3c_EWPX2WCMD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 613)
)
_Hh3c_LSR1WCM3A1_ObjectIdentity = ObjectIdentity
hh3c_LSR1WCM3A1 = _Hh3c_LSR1WCM3A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 614)
)
_Hh3c_S5830_52SC_ObjectIdentity = ObjectIdentity
hh3c_S5830_52SC = _Hh3c_S5830_52SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 615)
)
_Hh3c_S5830_106S_ObjectIdentity = ObjectIdentity
hh3c_S5830_106S = _Hh3c_S5830_106S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 617)
)
_Hh3c_ET814_ObjectIdentity = ObjectIdentity
hh3c_ET814 = _Hh3c_ET814_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 618)
)
_Hh3c_S5120_28P_LI_ObjectIdentity = ObjectIdentity
hh3c_S5120_28P_LI = _Hh3c_S5120_28P_LI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 619)
)
_Hh3c_S5120_52P_LI_ObjectIdentity = ObjectIdentity
hh3c_S5120_52P_LI = _Hh3c_S5120_52P_LI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 620)
)
_Hh3c_secBlade_IM_FW_II_ObjectIdentity = ObjectIdentity
hh3c_secBlade_IM_FW_II = _Hh3c_secBlade_IM_FW_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 621)
)
_Hh3c_secBlade_IM_LB_ObjectIdentity = ObjectIdentity
hh3c_secBlade_IM_LB = _Hh3c_secBlade_IM_LB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 622)
)
_Hh3c_secBlade_IM_SSL_ObjectIdentity = ObjectIdentity
hh3c_secBlade_IM_SSL = _Hh3c_secBlade_IM_SSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 623)
)
_Hh3c_ER2210C_ObjectIdentity = ObjectIdentity
hh3c_ER2210C = _Hh3c_ER2210C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 625)
)
_Hh3c_VCX_Connect_100_ObjectIdentity = ObjectIdentity
hh3c_VCX_Connect_100 = _Hh3c_VCX_Connect_100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 626)
)
_Hh3c_VCX_Connect_200_ObjectIdentity = ObjectIdentity
hh3c_VCX_Connect_200 = _Hh3c_VCX_Connect_200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 627)
)
_Hh3c_VCX_V7005_ObjectIdentity = ObjectIdentity
hh3c_VCX_V7005 = _Hh3c_VCX_V7005_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 628)
)
_Hh3c_VCX_V7205_ObjectIdentity = ObjectIdentity
hh3c_VCX_V7205 = _Hh3c_VCX_V7205_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 629)
)
_Hh3c_VCX_MIM_ObjectIdentity = ObjectIdentity
hh3c_VCX_MIM = _Hh3c_VCX_MIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 630)
)
_Hh3c_VCX_Connect_MIM_Primary_ObjectIdentity = ObjectIdentity
hh3c_VCX_Connect_MIM_Primary = _Hh3c_VCX_Connect_MIM_Primary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 631)
)
_Hh3c_VCX_Connect_MIM_Secondary_ObjectIdentity = ObjectIdentity
hh3c_VCX_Connect_MIM_Secondary = _Hh3c_VCX_Connect_MIM_Secondary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 632)
)
_Hh3c_VCX_V7310_ObjectIdentity = ObjectIdentity
hh3c_VCX_V7310 = _Hh3c_VCX_V7310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 633)
)
_Hh3c_secBlade_IM_IPS_ObjectIdentity = ObjectIdentity
hh3c_secBlade_IM_IPS = _Hh3c_secBlade_IM_IPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 634)
)
_Hh3c_secBlade_IM_ACG_ObjectIdentity = ObjectIdentity
hh3c_secBlade_IM_ACG = _Hh3c_secBlade_IM_ACG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 635)
)
_Hh3c_s7508E_X_ObjectIdentity = ObjectIdentity
hh3c_s7508E_X = _Hh3c_s7508E_X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 636)
)
_Hh3c_s10504_ObjectIdentity = ObjectIdentity
hh3c_s10504 = _Hh3c_s10504_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 637)
)
_Hh3c_s10508_ObjectIdentity = ObjectIdentity
hh3c_s10508 = _Hh3c_s10508_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 638)
)
_Hh3c_s10508_V_ObjectIdentity = ObjectIdentity
hh3c_s10508_V = _Hh3c_s10508_V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 639)
)
_Hh3c_secBlade_SPE_FWM_200_ObjectIdentity = ObjectIdentity
hh3c_secBlade_SPE_FWM_200 = _Hh3c_secBlade_SPE_FWM_200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 640)
)
_Hh3c_secpathF1000_S_AI_ObjectIdentity = ObjectIdentity
hh3c_secpathF1000_S_AI = _Hh3c_secpathF1000_S_AI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 641)
)
_Hh3c_wx3024e_wcm_ObjectIdentity = ObjectIdentity
hh3c_wx3024e_wcm = _Hh3c_wx3024e_wcm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 642)
)
_Hh3c_wx3024e_lsw_ObjectIdentity = ObjectIdentity
hh3c_wx3024e_lsw = _Hh3c_wx3024e_lsw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 643)
)
_Hh3c_ER2100_ObjectIdentity = ObjectIdentity
hh3c_ER2100 = _Hh3c_ER2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 644)
)
_Hh3c_S5820X_34TC_ObjectIdentity = ObjectIdentity
hh3c_S5820X_34TC = _Hh3c_S5820X_34TC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 645)
)
_Hh3c_S5820X_34SC_ObjectIdentity = ObjectIdentity
hh3c_S5820X_34SC = _Hh3c_S5820X_34SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 646)
)
_Hh3c_S5820X_34C_ObjectIdentity = ObjectIdentity
hh3c_S5820X_34C = _Hh3c_S5820X_34C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 647)
)
_Hh3c_S5820X_64SC_ObjectIdentity = ObjectIdentity
hh3c_S5820X_64SC = _Hh3c_S5820X_64SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 648)
)
_Hh3c_cc720E_ObjectIdentity = ObjectIdentity
hh3c_cc720E = _Hh3c_cc720E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 649)
)
_Hh3c_S2126T_ObjectIdentity = ObjectIdentity
hh3c_S2126T = _Hh3c_S2126T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 650)
)
_Hh3c_S5800_54S_ObjectIdentity = ObjectIdentity
hh3c_S5800_54S = _Hh3c_S5800_54S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 651)
)
_Hh3c_S5820X_26S_ObjectIdentity = ObjectIdentity
hh3c_S5820X_26S = _Hh3c_S5820X_26S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 652)
)
_Hh3c_S3100V2_8TP_SI_ObjectIdentity = ObjectIdentity
hh3c_S3100V2_8TP_SI = _Hh3c_S3100V2_8TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 653)
)
_Hh3c_S3100V2_16TP_SI_ObjectIdentity = ObjectIdentity
hh3c_S3100V2_16TP_SI = _Hh3c_S3100V2_16TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 654)
)
_Hh3c_S3100V2_26TP_SI_ObjectIdentity = ObjectIdentity
hh3c_S3100V2_26TP_SI = _Hh3c_S3100V2_26TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 655)
)
_Hh3c_E126B_ObjectIdentity = ObjectIdentity
hh3c_E126B = _Hh3c_E126B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 656)
)
_Hh3c_S3100V2_8TP_EI_ObjectIdentity = ObjectIdentity
hh3c_S3100V2_8TP_EI = _Hh3c_S3100V2_8TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 657)
)
_Hh3c_S3100V2_16TP_EI_ObjectIdentity = ObjectIdentity
hh3c_S3100V2_16TP_EI = _Hh3c_S3100V2_16TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 658)
)
_Hh3c_S3100V2_26TP_EI_ObjectIdentity = ObjectIdentity
hh3c_S3100V2_26TP_EI = _Hh3c_S3100V2_26TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 659)
)
_Hh3c_S3100V2_8TP_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_S3100V2_8TP_PWR_EI = _Hh3c_S3100V2_8TP_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 660)
)
_Hh3c_S3100V2_16TP_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_S3100V2_16TP_PWR_EI = _Hh3c_S3100V2_16TP_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 661)
)
_Hh3c_S3100V2_26TP_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_S3100V2_26TP_PWR_EI = _Hh3c_S3100V2_26TP_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 662)
)
_Hh3c_S2008TP_EB_ObjectIdentity = ObjectIdentity
hh3c_S2008TP_EB = _Hh3c_S2008TP_EB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 663)
)
_Hh3c_S2016TP_EB_ObjectIdentity = ObjectIdentity
hh3c_S2016TP_EB = _Hh3c_S2016TP_EB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 664)
)
_Hh3c_S2403TP_EB_ObjectIdentity = ObjectIdentity
hh3c_S2403TP_EB = _Hh3c_S2403TP_EB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 665)
)
_Hh3c_S2008TP_PWR_EB_ObjectIdentity = ObjectIdentity
hh3c_S2008TP_PWR_EB = _Hh3c_S2008TP_PWR_EB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 666)
)
_Hh3c_S2016TP_PWR_EB_ObjectIdentity = ObjectIdentity
hh3c_S2016TP_PWR_EB = _Hh3c_S2016TP_PWR_EB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 667)
)
_Hh3c_S2403TP_PWR_EB_ObjectIdentity = ObjectIdentity
hh3c_S2403TP_PWR_EB = _Hh3c_S2403TP_PWR_EB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 668)
)
_Hh3c_S5800_LSW1FC4P0_ObjectIdentity = ObjectIdentity
hh3c_S5800_LSW1FC4P0 = _Hh3c_S5800_LSW1FC4P0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 669)
)
_Hh3c_S2403TP_EA_SI_D_ObjectIdentity = ObjectIdentity
hh3c_S2403TP_EA_SI_D = _Hh3c_S2403TP_EA_SI_D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 670)
)
_Hh3c_S3528P_EA_D_ObjectIdentity = ObjectIdentity
hh3c_S3528P_EA_D = _Hh3c_S3528P_EA_D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 671)
)
_Hh3c_OAP_FIC_V2_ObjectIdentity = ObjectIdentity
hh3c_OAP_FIC_V2 = _Hh3c_OAP_FIC_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 672)
)
_Hh3c_OAP_MIM_V2_ObjectIdentity = ObjectIdentity
hh3c_OAP_MIM_V2 = _Hh3c_OAP_MIM_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 673)
)
_Hh3c_OAPS_MIM_V2_ObjectIdentity = ObjectIdentity
hh3c_OAPS_MIM_V2 = _Hh3c_OAPS_MIM_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 674)
)
_Hh3c_S2008TP_PWR_EA_ObjectIdentity = ObjectIdentity
hh3c_S2008TP_PWR_EA = _Hh3c_S2008TP_PWR_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 675)
)
_Hh3c_S2008TP_PWR_EA_DC_ObjectIdentity = ObjectIdentity
hh3c_S2008TP_PWR_EA_DC = _Hh3c_S2008TP_PWR_EA_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 676)
)
_Hh3c_S2016TP_PWR_EA_ObjectIdentity = ObjectIdentity
hh3c_S2016TP_PWR_EA = _Hh3c_S2016TP_PWR_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 677)
)
_Hh3c_S2403TP_PWR_EA_ObjectIdentity = ObjectIdentity
hh3c_S2403TP_PWR_EA = _Hh3c_S2403TP_PWR_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 678)
)
_Hh3c_S5120_24P_EI_D_ObjectIdentity = ObjectIdentity
hh3c_S5120_24P_EI_D = _Hh3c_S5120_24P_EI_D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 679)
)
_Hh3c_S5120_24P_PWR_EI_D_ObjectIdentity = ObjectIdentity
hh3c_S5120_24P_PWR_EI_D = _Hh3c_S5120_24P_PWR_EI_D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 680)
)
_Hh3c_S5120_48P_EI_D_ObjectIdentity = ObjectIdentity
hh3c_S5120_48P_EI_D = _Hh3c_S5120_48P_EI_D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 681)
)
_Hh3c_S5024P_EI_ObjectIdentity = ObjectIdentity
hh3c_S5024P_EI = _Hh3c_S5024P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 682)
)
_Hh3c_S5500_28C_EI_D_ObjectIdentity = ObjectIdentity
hh3c_S5500_28C_EI_D = _Hh3c_S5500_28C_EI_D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 683)
)
_Hh3c_S5500_52C_EI_D_ObjectIdentity = ObjectIdentity
hh3c_S5500_52C_EI_D = _Hh3c_S5500_52C_EI_D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 684)
)
_Hh3c_S5500_28F_EI_D_ObjectIdentity = ObjectIdentity
hh3c_S5500_28F_EI_D = _Hh3c_S5500_28F_EI_D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 685)
)
_Hh3c_S5500_28C_EI_DC_D_ObjectIdentity = ObjectIdentity
hh3c_S5500_28C_EI_DC_D = _Hh3c_S5500_28C_EI_DC_D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 686)
)
_Hh3c_MG9050_ObjectIdentity = ObjectIdentity
hh3c_MG9050 = _Hh3c_MG9050_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 687)
)
_Hh3c_S5120_52SC_HI_ObjectIdentity = ObjectIdentity
hh3c_S5120_52SC_HI = _Hh3c_S5120_52SC_HI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 688)
)
_Hh3c_CE3000_32F_EI_ObjectIdentity = ObjectIdentity
hh3c_CE3000_32F_EI = _Hh3c_CE3000_32F_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 689)
)
_Hh3c_S5830X_24S_ObjectIdentity = ObjectIdentity
hh3c_S5830X_24S = _Hh3c_S5830X_24S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 690)
)
_Hh3cDC1801FH_ObjectIdentity = ObjectIdentity
hh3cDC1801FH = _Hh3cDC1801FH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 691)
)
_Hh3cDC2004FF_ObjectIdentity = ObjectIdentity
hh3cDC2004FF = _Hh3cDC2004FF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 692)
)
_Hh3cEC1101HF_ObjectIdentity = ObjectIdentity
hh3cEC1101HF = _Hh3cEC1101HF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 693)
)
_Hh3cEC1102HF_ObjectIdentity = ObjectIdentity
hh3cEC1102HF = _Hh3cEC1102HF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 694)
)
_Hh3cEC1501HF_ObjectIdentity = ObjectIdentity
hh3cEC1501HF = _Hh3cEC1501HF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 695)
)
_Hh3cEC1801HH_ObjectIdentity = ObjectIdentity
hh3cEC1801HH = _Hh3cEC1801HH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 696)
)
_Hh3cEC2516HF_ObjectIdentity = ObjectIdentity
hh3cEC2516HF = _Hh3cEC2516HF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 697)
)
_Hh3cEC2016HC_ObjectIdentity = ObjectIdentity
hh3cEC2016HC = _Hh3cEC2016HC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 698)
)
_Hh3cEC2016HC8CH_ObjectIdentity = ObjectIdentity
hh3cEC2016HC8CH = _Hh3cEC2016HC8CH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 699)
)
_Hh3cEC2016HC4CH_ObjectIdentity = ObjectIdentity
hh3cEC2016HC4CH = _Hh3cEC2016HC4CH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 700)
)
_Hh3cEC1504HF_ObjectIdentity = ObjectIdentity
hh3cEC1504HF = _Hh3cEC1504HF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 701)
)
_Hh3cHIC5421_ObjectIdentity = ObjectIdentity
hh3cHIC5421 = _Hh3cHIC5421_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 702)
)
_Hh3cHIC5401_ObjectIdentity = ObjectIdentity
hh3cHIC5401 = _Hh3cHIC5401_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 703)
)
_Hh3cHIC5221H_ObjectIdentity = ObjectIdentity
hh3cHIC5221H = _Hh3cHIC5221H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 704)
)
_Hh3cHIC5201H_ObjectIdentity = ObjectIdentity
hh3cHIC5201H = _Hh3cHIC5201H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 705)
)
_Hh3cVM8500_ObjectIdentity = ObjectIdentity
hh3cVM8500 = _Hh3cVM8500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 706)
)
_Hh3cMS8500_ObjectIdentity = ObjectIdentity
hh3cMS8500 = _Hh3cMS8500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 707)
)
_Hh3cDM8500_ObjectIdentity = ObjectIdentity
hh3cDM8500 = _Hh3cDM8500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 708)
)
_Hh3cVX500_ObjectIdentity = ObjectIdentity
hh3cVX500 = _Hh3cVX500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 709)
)
_Hh3cISC3000E_ObjectIdentity = ObjectIdentity
hh3cISC3000E = _Hh3cISC3000E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 710)
)
_Hh3cISC3000S_ObjectIdentity = ObjectIdentity
hh3cISC3000S = _Hh3cISC3000S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 711)
)
_Hh3cCC700E_ObjectIdentity = ObjectIdentity
hh3cCC700E = _Hh3cCC700E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 712)
)
_Hh3cDC1001FF_ObjectIdentity = ObjectIdentity
hh3cDC1001FF = _Hh3cDC1001FF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 713)
)
_Hh3cECR3316HC_ObjectIdentity = ObjectIdentity
hh3cECR3316HC = _Hh3cECR3316HC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 714)
)
_Hh3cECR3308HD_ObjectIdentity = ObjectIdentity
hh3cECR3308HD = _Hh3cECR3308HD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 715)
)
_Hh3cECR3316HC8CH_ObjectIdentity = ObjectIdentity
hh3cECR3316HC8CH = _Hh3cECR3316HC8CH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 716)
)
_Hh3cECR3316HC4CH_ObjectIdentity = ObjectIdentity
hh3cECR3316HC4CH = _Hh3cECR3316HC4CH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 717)
)
_Hh3cECR3308HD4CH_ObjectIdentity = ObjectIdentity
hh3cECR3308HD4CH = _Hh3cECR3308HD4CH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 718)
)
_Hh3cHIC65017L_ObjectIdentity = ObjectIdentity
hh3cHIC65017L = _Hh3cHIC65017L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 719)
)
_Hh3cEC2508HF_ObjectIdentity = ObjectIdentity
hh3cEC2508HF = _Hh3cEC2508HF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 720)
)
_Hh3cS3528EA_ObjectIdentity = ObjectIdentity
hh3cS3528EA = _Hh3cS3528EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 721)
)
_Hh3cS3552TPEA_ObjectIdentity = ObjectIdentity
hh3cS3552TPEA = _Hh3cS3552TPEA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 722)
)
_Hh3cWP3024_ObjectIdentity = ObjectIdentity
hh3cWP3024 = _Hh3cWP3024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 723)
)
_Hh3cWP3048_ObjectIdentity = ObjectIdentity
hh3cWP3048 = _Hh3cWP3048_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 724)
)
_Hh3cS3528FPEA_ObjectIdentity = ObjectIdentity
hh3cS3528FPEA = _Hh3cS3528FPEA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 725)
)
_Hh3cE328B_ObjectIdentity = ObjectIdentity
hh3cE328B = _Hh3cE328B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 726)
)
_Hh3cE352B_ObjectIdentity = ObjectIdentity
hh3cE352B = _Hh3cE352B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 727)
)
_Hh3cE152B_ObjectIdentity = ObjectIdentity
hh3cE152B = _Hh3cE152B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 728)
)
_Hh3cS3100V252TP_ObjectIdentity = ObjectIdentity
hh3cS3100V252TP = _Hh3cS3100V252TP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 729)
)
_Hh3cWP2008_ObjectIdentity = ObjectIdentity
hh3cWP2008 = _Hh3cWP2008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 730)
)
_Hh3cWP2016_ObjectIdentity = ObjectIdentity
hh3cWP2016 = _Hh3cWP2016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 731)
)
_Hh3cWP2024_ObjectIdentity = ObjectIdentity
hh3cWP2024 = _Hh3cWP2024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 732)
)
_Hh3cWP5024_ObjectIdentity = ObjectIdentity
hh3cWP5024 = _Hh3cWP5024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 733)
)
_Hh3cWP5048_ObjectIdentity = ObjectIdentity
hh3cWP5048 = _Hh3cWP5048_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 734)
)
_Hh3cS2052TPEA_ObjectIdentity = ObjectIdentity
hh3cS2052TPEA = _Hh3cS2052TPEA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 735)
)
_Hh3cS7604X_ObjectIdentity = ObjectIdentity
hh3cS7604X = _Hh3cS7604X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 736)
)
_Hh3cS7608X_ObjectIdentity = ObjectIdentity
hh3cS7608X = _Hh3cS7608X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 737)
)
_Hh3cS7608XV_ObjectIdentity = ObjectIdentity
hh3cS7608XV = _Hh3cS7608XV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 738)
)
_Hh3cWA3620iAGN_ObjectIdentity = ObjectIdentity
hh3cWA3620iAGN = _Hh3cWA3620iAGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 739)
)
_Hh3cWA3628iAGN_ObjectIdentity = ObjectIdentity
hh3cWA3628iAGN = _Hh3cWA3628iAGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 740)
)
_Hh3cWA3610iGN_ObjectIdentity = ObjectIdentity
hh3cWA3610iGN = _Hh3cWA3610iGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 741)
)
_Hh3cCC750E_ObjectIdentity = ObjectIdentity
hh3cCC750E = _Hh3cCC750E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 742)
)
_HpSwitch_ObjectIdentity = ObjectIdentity
hpSwitch = _HpSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1)
)
_HpA7502_ObjectIdentity = ObjectIdentity
hpA7502 = _HpA7502_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 1)
)
_HpA7503S_ObjectIdentity = ObjectIdentity
hpA7503S = _HpA7503S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 2)
)
_HpA7503_ObjectIdentity = ObjectIdentity
hpA7503 = _HpA7503_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 3)
)
_HpA7506_ObjectIdentity = ObjectIdentity
hpA7506 = _HpA7506_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 4)
)
_HpA7506V_ObjectIdentity = ObjectIdentity
hpA7506V = _HpA7506V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 5)
)
_HpA7510_ObjectIdentity = ObjectIdentity
hpA7510 = _HpA7510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 6)
)
_HpA36002POLT_ObjectIdentity = ObjectIdentity
hpA36002POLT = _HpA36002POLT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 7)
)
_HpV190524_ObjectIdentity = ObjectIdentity
hpV190524 = _HpV190524_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 8)
)
_HpV190524POE_ObjectIdentity = ObjectIdentity
hpV190524POE = _HpV190524POE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 9)
)
_HpV190548_ObjectIdentity = ObjectIdentity
hpV190548 = _HpV190548_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 10)
)
_HpA512016GSI_ObjectIdentity = ObjectIdentity
hpA512016GSI = _HpA512016GSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 11)
)
_HpA512024GSI_ObjectIdentity = ObjectIdentity
hpA512024GSI = _HpA512024GSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 12)
)
_HpA512048GSI_ObjectIdentity = ObjectIdentity
hpA512048GSI = _HpA512048GSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 13)
)
_HpA512024GPPOESI_ObjectIdentity = ObjectIdentity
hpA512024GPPOESI = _HpA512024GPPOESI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 14)
)
_HpA512024GPOESI_ObjectIdentity = ObjectIdentity
hpA512024GPOESI = _HpA512024GPOESI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 15)
)
_HpA580024G_ObjectIdentity = ObjectIdentity
hpA580024G = _HpA580024G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 16)
)
_HpA580024GPoEPlus_ObjectIdentity = ObjectIdentity
hpA580024GPoEPlus = _HpA580024GPoEPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 17)
)
_HpA580048G_ObjectIdentity = ObjectIdentity
hpA580048G = _HpA580048G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 18)
)
_HpA580048GPoEPlus_ObjectIdentity = ObjectIdentity
hpA580048GPoEPlus = _HpA580048GPoEPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 19)
)
_HpA580024GSFP_ObjectIdentity = ObjectIdentity
hpA580024GSFP = _HpA580024GSFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 20)
)
_HpA580048GPoEPlus2SLOT_ObjectIdentity = ObjectIdentity
hpA580048GPoEPlus2SLOT = _HpA580048GPoEPlus2SLOT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 21)
)
_HpA5820X14XGSFPPlus2SLOT_ObjectIdentity = ObjectIdentity
hpA5820X14XGSFPPlus2SLOT = _HpA5820X14XGSFPPlus2SLOT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 22)
)
_HpA5820X24XGSFPPlus_ObjectIdentity = ObjectIdentity
hpA5820X24XGSFPPlus = _HpA5820X24XGSFPPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 23)
)
_HpA550028CEI_ObjectIdentity = ObjectIdentity
hpA550028CEI = _HpA550028CEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 24)
)
_HpA550052CEI_ObjectIdentity = ObjectIdentity
hpA550052CEI = _HpA550052CEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 25)
)
_HpA550028CPWREI_ObjectIdentity = ObjectIdentity
hpA550028CPWREI = _HpA550028CPWREI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 26)
)
_HpA550052CPWREI_ObjectIdentity = ObjectIdentity
hpA550052CPWREI = _HpA550052CPWREI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 27)
)
_HpA550028FEI_ObjectIdentity = ObjectIdentity
hpA550028FEI = _HpA550028FEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 28)
)
_HpA550028CSI_ObjectIdentity = ObjectIdentity
hpA550028CSI = _HpA550028CSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 29)
)
_HpA550052CSI_ObjectIdentity = ObjectIdentity
hpA550052CSI = _HpA550052CSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 30)
)
_HpA550028CPWRSI_ObjectIdentity = ObjectIdentity
hpA550028CPWRSI = _HpA550028CPWRSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 31)
)
_HpA550052CPWRSI_ObjectIdentity = ObjectIdentity
hpA550052CPWRSI = _HpA550052CPWRSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 32)
)
_HpA512028CEI_ObjectIdentity = ObjectIdentity
hpA512028CEI = _HpA512028CEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 33)
)
_HpA512052CEI_ObjectIdentity = ObjectIdentity
hpA512052CEI = _HpA512052CEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 34)
)
_HpA512028CPWREI_ObjectIdentity = ObjectIdentity
hpA512028CPWREI = _HpA512028CPWREI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 35)
)
_HpA512052CPWREI_ObjectIdentity = ObjectIdentity
hpA512052CPWREI = _HpA512052CPWREI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 36)
)
_HpA512024PEI_ObjectIdentity = ObjectIdentity
hpA512024PEI = _HpA512024PEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 37)
)
_HpA512048PEI_ObjectIdentity = ObjectIdentity
hpA512048PEI = _HpA512048PEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 38)
)
_HpA9505_ObjectIdentity = ObjectIdentity
hpA9505 = _HpA9505_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 39)
)
_HpA9508V_ObjectIdentity = ObjectIdentity
hpA9508V = _HpA9508V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 40)
)
_HpA9508_ObjectIdentity = ObjectIdentity
hpA9508 = _HpA9508_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 41)
)
_HpA9512_ObjectIdentity = ObjectIdentity
hpA9512 = _HpA9512_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 42)
)
_HpA12508_ObjectIdentity = ObjectIdentity
hpA12508 = _HpA12508_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 43)
)
_HpA12518_ObjectIdentity = ObjectIdentity
hpA12518 = _HpA12518_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 44)
)
_HpA12504_ObjectIdentity = ObjectIdentity
hpA12504 = _HpA12504_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 45)
)
_HpA5800AF48G_ObjectIdentity = ObjectIdentity
hpA5800AF48G = _HpA5800AF48G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 46)
)
_HpA5820AF24XG_ObjectIdentity = ObjectIdentity
hpA5820AF24XG = _HpA5820AF24XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 47)
)
_HpA6125GXG_ObjectIdentity = ObjectIdentity
hpA6125GXG = _HpA6125GXG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 51)
)
_HpA31008SI_ObjectIdentity = ObjectIdentity
hpA31008SI = _HpA31008SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 52)
)
_HpA310016SI_ObjectIdentity = ObjectIdentity
hpA310016SI = _HpA310016SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 53)
)
_HpA310024SI_ObjectIdentity = ObjectIdentity
hpA310024SI = _HpA310024SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 54)
)
_HpA31008EI_ObjectIdentity = ObjectIdentity
hpA31008EI = _HpA31008EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 55)
)
_HpA310016EI_ObjectIdentity = ObjectIdentity
hpA310016EI = _HpA310016EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 56)
)
_HpA310024EI_ObjectIdentity = ObjectIdentity
hpA310024EI = _HpA310024EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 57)
)
_HpA31008POEEI_ObjectIdentity = ObjectIdentity
hpA31008POEEI = _HpA31008POEEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 58)
)
_HpA310016POEEI_ObjectIdentity = ObjectIdentity
hpA310016POEEI = _HpA310016POEEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 59)
)
_HpA310024POEEI_ObjectIdentity = ObjectIdentity
hpA310024POEEI = _HpA310024POEEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 60)
)
_HpA580024GTAA_ObjectIdentity = ObjectIdentity
hpA580024GTAA = _HpA580024GTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 61)
)
_HpA580024GPoEPlusTAA_ObjectIdentity = ObjectIdentity
hpA580024GPoEPlusTAA = _HpA580024GPoEPlusTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 62)
)
_HpA580024GSFPTAA_ObjectIdentity = ObjectIdentity
hpA580024GSFPTAA = _HpA580024GSFPTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 63)
)
_HpA580048GTAA_ObjectIdentity = ObjectIdentity
hpA580048GTAA = _HpA580048GTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 64)
)
_HpA580048GPoEPlusTAA2SLOT_ObjectIdentity = ObjectIdentity
hpA580048GPoEPlusTAA2SLOT = _HpA580048GPoEPlusTAA2SLOT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 65)
)
_HpA580048GPoEPlusTAA_ObjectIdentity = ObjectIdentity
hpA580048GPoEPlusTAA = _HpA580048GPoEPlusTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 66)
)
_HpA5820X14XGSFPPlusTAA2SLOT_ObjectIdentity = ObjectIdentity
hpA5820X14XGSFPPlusTAA2SLOT = _HpA5820X14XGSFPPlusTAA2SLOT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 67)
)
_HpA582024XGSFPPlusTAA_ObjectIdentity = ObjectIdentity
hpA582024XGSFPPlusTAA = _HpA582024XGSFPPlusTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 68)
)
_HpA512024GEITAA_ObjectIdentity = ObjectIdentity
hpA512024GEITAA = _HpA512024GEITAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 69)
)
_HpA512048GEITAA_ObjectIdentity = ObjectIdentity
hpA512048GEITAA = _HpA512048GEITAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 70)
)
_HpA512024GPOEEITAA_ObjectIdentity = ObjectIdentity
hpA512024GPOEEITAA = _HpA512024GPOEEITAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 71)
)
_HpA512048GPOEEITAA_ObjectIdentity = ObjectIdentity
hpA512048GPOEEITAA = _HpA512048GPOEEITAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 72)
)
_HpA550024GSFPEITAA_ObjectIdentity = ObjectIdentity
hpA550024GSFPEITAA = _HpA550024GSFPEITAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 73)
)
_HpA550024GEITAA_ObjectIdentity = ObjectIdentity
hpA550024GEITAA = _HpA550024GEITAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 74)
)
_HpA550048GEITAA_ObjectIdentity = ObjectIdentity
hpA550048GEITAA = _HpA550048GEITAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 75)
)
_HpA550024GPOEEITAA_ObjectIdentity = ObjectIdentity
hpA550024GPOEEITAA = _HpA550024GPOEEITAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 76)
)
_HpA550048GPOEEITAA_ObjectIdentity = ObjectIdentity
hpA550048GPOEEITAA = _HpA550048GPOEEITAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 77)
)
_HpA5830AF24XG_ObjectIdentity = ObjectIdentity
hpA5830AF24XG = _HpA5830AF24XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 78)
)
_HpA5830AF48G_ObjectIdentity = ObjectIdentity
hpA5830AF48G = _HpA5830AF48G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 79)
)
_HpA5830AF96G_ObjectIdentity = ObjectIdentity
hpA5830AF96G = _HpA5830AF96G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 80)
)
_HpV191016G_ObjectIdentity = ObjectIdentity
hpV191016G = _HpV191016G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 81)
)
_HpV191024G_ObjectIdentity = ObjectIdentity
hpV191024G = _HpV191024G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 82)
)
_HpV191024GPoE365W_ObjectIdentity = ObjectIdentity
hpV191024GPoE365W = _HpV191024GPoE365W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 83)
)
_HpV191024GPoE170W_ObjectIdentity = ObjectIdentity
hpV191024GPoE170W = _HpV191024GPoE170W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 84)
)
_HpV191048G_ObjectIdentity = ObjectIdentity
hpV191048G = _HpV191048G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 85)
)
_HpA10504_ObjectIdentity = ObjectIdentity
hpA10504 = _HpA10504_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 86)
)
_HpA10508_ObjectIdentity = ObjectIdentity
hpA10508 = _HpA10508_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 87)
)
_HpA10508V_ObjectIdentity = ObjectIdentity
hpA10508V = _HpA10508V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 88)
)
_HpA10512_ObjectIdentity = ObjectIdentity
hpA10512 = _HpA10512_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 89)
)
_HpA360024V2EI_ObjectIdentity = ObjectIdentity
hpA360024V2EI = _HpA360024V2EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 90)
)
_HpA360048V2EI_ObjectIdentity = ObjectIdentity
hpA360048V2EI = _HpA360048V2EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 91)
)
_HpA360024PoEPlusV2EI_ObjectIdentity = ObjectIdentity
hpA360024PoEPlusV2EI = _HpA360024PoEPlusV2EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 92)
)
_HpA360048PoEPlusV2EI_ObjectIdentity = ObjectIdentity
hpA360048PoEPlusV2EI = _HpA360048PoEPlusV2EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 93)
)
_HpA360024SFPV2EI_ObjectIdentity = ObjectIdentity
hpA360024SFPV2EI = _HpA360024SFPV2EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 94)
)
_HpA360024V2SI_ObjectIdentity = ObjectIdentity
hpA360024V2SI = _HpA360024V2SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 95)
)
_HpA360048V2SI_ObjectIdentity = ObjectIdentity
hpA360048V2SI = _HpA360048V2SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 96)
)
_HpA360024PoEPlusV2SI_ObjectIdentity = ObjectIdentity
hpA360024PoEPlusV2SI = _HpA360024PoEPlusV2SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 97)
)
_HpA360048PoEPlusV2SI_ObjectIdentity = ObjectIdentity
hpA360048PoEPlusV2SI = _HpA360048PoEPlusV2SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 98)
)
_HpA310048V2_ObjectIdentity = ObjectIdentity
hpA310048V2 = _HpA310048V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 99)
)
_HpRouter_ObjectIdentity = ObjectIdentity
hpRouter = _HpRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2)
)
_HpAMSR900_ObjectIdentity = ObjectIdentity
hpAMSR900 = _HpAMSR900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 1)
)
_HpAMSR920_ObjectIdentity = ObjectIdentity
hpAMSR920 = _HpAMSR920_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 2)
)
_HpAMSR2010_ObjectIdentity = ObjectIdentity
hpAMSR2010 = _HpAMSR2010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 3)
)
_HpAMSR2011_ObjectIdentity = ObjectIdentity
hpAMSR2011 = _HpAMSR2011_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 4)
)
_HpAMSR2012_ObjectIdentity = ObjectIdentity
hpAMSR2012 = _HpAMSR2012_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 5)
)
_HpAMSR2012T_ObjectIdentity = ObjectIdentity
hpAMSR2012T = _HpAMSR2012T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 6)
)
_HpAMSR2013_ObjectIdentity = ObjectIdentity
hpAMSR2013 = _HpAMSR2013_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 7)
)
_HpAMSR2020_ObjectIdentity = ObjectIdentity
hpAMSR2020 = _HpAMSR2020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 8)
)
_HpAMSR2021_ObjectIdentity = ObjectIdentity
hpAMSR2021 = _HpAMSR2021_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 9)
)
_HpAMSR2040_ObjectIdentity = ObjectIdentity
hpAMSR2040 = _HpAMSR2040_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 10)
)
_HpAMSR3010_ObjectIdentity = ObjectIdentity
hpAMSR3010 = _HpAMSR3010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 11)
)
_HpAMSR3011E_ObjectIdentity = ObjectIdentity
hpAMSR3011E = _HpAMSR3011E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 12)
)
_HpAMSR3011F_ObjectIdentity = ObjectIdentity
hpAMSR3011F = _HpAMSR3011F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 13)
)
_HpAMSR3016_ObjectIdentity = ObjectIdentity
hpAMSR3016 = _HpAMSR3016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 14)
)
_HpAMSR3020_ObjectIdentity = ObjectIdentity
hpAMSR3020 = _HpAMSR3020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 15)
)
_HpAMSR3040_ObjectIdentity = ObjectIdentity
hpAMSR3040 = _HpAMSR3040_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 16)
)
_HpAMSR3060_ObjectIdentity = ObjectIdentity
hpAMSR3060 = _HpAMSR3060_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 17)
)
_HpAMSR5040_ObjectIdentity = ObjectIdentity
hpAMSR5040 = _HpAMSR5040_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 18)
)
_HpAMSR5060_ObjectIdentity = ObjectIdentity
hpAMSR5060 = _HpAMSR5060_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 19)
)
_HpA6602_ObjectIdentity = ObjectIdentity
hpA6602 = _HpA6602_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 20)
)
_HpA6604_ObjectIdentity = ObjectIdentity
hpA6604 = _HpA6604_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 21)
)
_HpA6608_ObjectIdentity = ObjectIdentity
hpA6608 = _HpA6608_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 22)
)
_HpA6616_ObjectIdentity = ObjectIdentity
hpA6616 = _HpA6616_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 23)
)
_HpAMSR900W_ObjectIdentity = ObjectIdentity
hpAMSR900W = _HpAMSR900W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 24)
)
_HpAMSR900WNA_ObjectIdentity = ObjectIdentity
hpAMSR900WNA = _HpAMSR900WNA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 25)
)
_HpAMSR920W_ObjectIdentity = ObjectIdentity
hpAMSR920W = _HpAMSR920W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 26)
)
_HpAMSR920WNA_ObjectIdentity = ObjectIdentity
hpAMSR920WNA = _HpAMSR920WNA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 27)
)
_HpAMSR2012W_ObjectIdentity = ObjectIdentity
hpAMSR2012W = _HpAMSR2012W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 28)
)
_HpAMSR2012TW_ObjectIdentity = ObjectIdentity
hpAMSR2012TW = _HpAMSR2012TW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 29)
)
_HpAMSR2012TWNA_ObjectIdentity = ObjectIdentity
hpAMSR2012TWNA = _HpAMSR2012TWNA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 30)
)
_HpAMSR2013W_ObjectIdentity = ObjectIdentity
hpAMSR2013W = _HpAMSR2013W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 31)
)
_HpAMSR2013WNA_ObjectIdentity = ObjectIdentity
hpAMSR2013WNA = _HpAMSR2013WNA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 32)
)
_HpAMSR2020S_ObjectIdentity = ObjectIdentity
hpAMSR2020S = _HpAMSR2020S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 33)
)
_HpAMSR2021S_ObjectIdentity = ObjectIdentity
hpAMSR2021S = _HpAMSR2021S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 34)
)
_HpAMSR2040S_ObjectIdentity = ObjectIdentity
hpAMSR2040S = _HpAMSR2040S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 35)
)
_HpAMSR3010DC_ObjectIdentity = ObjectIdentity
hpAMSR3010DC = _HpAMSR3010DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 36)
)
_HpAMSR3016POE_ObjectIdentity = ObjectIdentity
hpAMSR3016POE = _HpAMSR3016POE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 37)
)
_HpAMSR3020AS_ObjectIdentity = ObjectIdentity
hpAMSR3020AS = _HpAMSR3020AS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 38)
)
_HpAMSR3020POE_ObjectIdentity = ObjectIdentity
hpAMSR3020POE = _HpAMSR3020POE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 39)
)
_HpAMSR3020DC_ObjectIdentity = ObjectIdentity
hpAMSR3020DC = _HpAMSR3020DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 40)
)
_HpAMSR3040AS_ObjectIdentity = ObjectIdentity
hpAMSR3040AS = _HpAMSR3040AS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 41)
)
_HpAMSR3040POE_ObjectIdentity = ObjectIdentity
hpAMSR3040POE = _HpAMSR3040POE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 42)
)
_HpAMSR3040DC_ObjectIdentity = ObjectIdentity
hpAMSR3040DC = _HpAMSR3040DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 43)
)
_HpAMSR3060AS_ObjectIdentity = ObjectIdentity
hpAMSR3060AS = _HpAMSR3060AS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 44)
)
_HpAMSR3060POE_ObjectIdentity = ObjectIdentity
hpAMSR3060POE = _HpAMSR3060POE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 45)
)
_HpAMSR3060DC_ObjectIdentity = ObjectIdentity
hpAMSR3060DC = _HpAMSR3060DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 46)
)
_HpAMSR5040DC_ObjectIdentity = ObjectIdentity
hpAMSR5040DC = _HpAMSR5040DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 47)
)
_HpAMSR5060DC_ObjectIdentity = ObjectIdentity
hpAMSR5060DC = _HpAMSR5060DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 48)
)
_HpA8805_ObjectIdentity = ObjectIdentity
hpA8805 = _HpA8805_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 49)
)
_HpA8808_ObjectIdentity = ObjectIdentity
hpA8808 = _HpA8808_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 50)
)
_HpA8812_ObjectIdentity = ObjectIdentity
hpA8812 = _HpA8812_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 51)
)
_HpWireless_ObjectIdentity = ObjectIdentity
hpWireless = _HpWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3)
)
_HpAWA2610EAGNFAT_ObjectIdentity = ObjectIdentity
hpAWA2610EAGNFAT = _HpAWA2610EAGNFAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 1)
)
_HpAWA2620EAGNFAT_ObjectIdentity = ObjectIdentity
hpAWA2620EAGNFAT = _HpAWA2620EAGNFAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 2)
)
_HpAWA2620AGNFAT_ObjectIdentity = ObjectIdentity
hpAWA2620AGNFAT = _HpAWA2620AGNFAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 3)
)
_HpA7500LSQM3WCMB0_ObjectIdentity = ObjectIdentity
hpA7500LSQM3WCMB0 = _HpA7500LSQM3WCMB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 4)
)
_HpA9500LSRM2WCM2A1_ObjectIdentity = ObjectIdentity
hpA9500LSRM2WCM2A1 = _HpA9500LSRM2WCM2A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 5)
)
_HpA5800LSWM2WCM10_ObjectIdentity = ObjectIdentity
hpA5800LSWM2WCM10 = _HpA5800LSWM2WCM10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 6)
)
_HpA5800LSWM2WCM20_ObjectIdentity = ObjectIdentity
hpA5800LSWM2WCM20 = _HpA5800LSWM2WCM20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 7)
)
_HpAWX5004EWPXZ65004_ObjectIdentity = ObjectIdentity
hpAWX5004EWPXZ65004 = _HpAWX5004EWPXZ65004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 8)
)
_HpAWX5002EWPXZ75002_ObjectIdentity = ObjectIdentity
hpAWX5002EWPXZ75002 = _HpAWX5002EWPXZ75002_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 9)
)
_HpA3000E_ObjectIdentity = ObjectIdentity
hpA3000E = _HpA3000E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 10)
)
_HpA3000ELSW_ObjectIdentity = ObjectIdentity
hpA3000ELSW = _HpA3000ELSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 11)
)
_HpAWA3620iAGN_ObjectIdentity = ObjectIdentity
hpAWA3620iAGN = _HpAWA3620iAGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 12)
)
_HpAWA3628iAGN_ObjectIdentity = ObjectIdentity
hpAWA3628iAGN = _HpAWA3628iAGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 13)
)
_HpAWA3610iGN_ObjectIdentity = ObjectIdentity
hpAWA3610iGN = _HpAWA3610iGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 14)
)
_HpSecurity_ObjectIdentity = ObjectIdentity
hpSecurity = _HpSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4)
)
_HpSecBladeIMFWII_ObjectIdentity = ObjectIdentity
hpSecBladeIMFWII = _HpSecBladeIMFWII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 1)
)
_HpSecBladeIMSSL_ObjectIdentity = ObjectIdentity
hpSecBladeIMSSL = _HpSecBladeIMSSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 2)
)
_HpSecBladeIMLB_ObjectIdentity = ObjectIdentity
hpSecBladeIMLB = _HpSecBladeIMLB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 3)
)
_HpSecBladeLSQ1FWBSC0_ObjectIdentity = ObjectIdentity
hpSecBladeLSQ1FWBSC0 = _HpSecBladeLSQ1FWBSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 4)
)
_HpSecBladeLSQM1LBC0_ObjectIdentity = ObjectIdentity
hpSecBladeLSQM1LBC0 = _HpSecBladeLSQM1LBC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 5)
)
_HpSecBladeLSQ1NSMSC0_ObjectIdentity = ObjectIdentity
hpSecBladeLSQ1NSMSC0 = _HpSecBladeLSQ1NSMSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 6)
)
_HpSecBladeLSR1FW2A1_ObjectIdentity = ObjectIdentity
hpSecBladeLSR1FW2A1 = _HpSecBladeLSR1FW2A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 7)
)
_HpSecBladeLSR1LB1A1_ObjectIdentity = ObjectIdentity
hpSecBladeLSR1LB1A1 = _HpSecBladeLSR1LB1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 8)
)
_HpSecBladeLSR1NSM1A1_ObjectIdentity = ObjectIdentity
hpSecBladeLSR1NSM1A1 = _HpSecBladeLSR1NSM1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 9)
)
_HpSecBladeLST1FW2A1_ObjectIdentity = ObjectIdentity
hpSecBladeLST1FW2A1 = _HpSecBladeLST1FW2A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 10)
)
_HpSecBladeLST1LB1A1_ObjectIdentity = ObjectIdentity
hpSecBladeLST1LB1A1 = _HpSecBladeLST1LB1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 11)
)
_HpSecBladeLST1NSM1A1_ObjectIdentity = ObjectIdentity
hpSecBladeLST1NSM1A1 = _HpSecBladeLST1NSM1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 12)
)
_HpSecBladeLSWM1FW10_ObjectIdentity = ObjectIdentity
hpSecBladeLSWM1FW10 = _HpSecBladeLSWM1FW10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 13)
)
_HpSecBladeSPEFWM200_ObjectIdentity = ObjectIdentity
hpSecBladeSPEFWM200 = _HpSecBladeSPEFWM200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 14)
)
_HpAF5000_ObjectIdentity = ObjectIdentity
hpAF5000 = _HpAF5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 15)
)
_HpAF1000E_ObjectIdentity = ObjectIdentity
hpAF1000E = _HpAF1000E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 16)
)
_HpAU200S_ObjectIdentity = ObjectIdentity
hpAU200S = _HpAU200S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 17)
)
_HpAU200A_ObjectIdentity = ObjectIdentity
hpAU200A = _HpAU200A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 18)
)
_HpAF1000SEI_ObjectIdentity = ObjectIdentity
hpAF1000SEI = _HpAF1000SEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 19)
)
_HpAF1000AEI_ObjectIdentity = ObjectIdentity
hpAF1000AEI = _HpAF1000AEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 20)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-PRODUCT-ID-MIB",
    **{"hh3c-s5500-28C-EI": hh3c_s5500_28C_EI,
       "hh3c-s5500-52C-EI": hh3c_s5500_52C_EI,
       "hh3c-s5500-28C-PWR-EI": hh3c_s5500_28C_PWR_EI,
       "hh3c-s5500-52C-PWR-EI": hh3c_s5500_52C_PWR_EI,
       "hh3c-s5500-28F-EI": hh3c_s5500_28F_EI,
       "hh3c-s5500-28C-EI-DC": hh3c_s5500_28C_EI_DC,
       "hh3c-s6100-20Q-SI": hh3c_s6100_20Q_SI,
       "hh3c-s5500-28C-SI": hh3c_s5500_28C_SI,
       "hh3c-s5500-52C-SI": hh3c_s5500_52C_SI,
       "hh3c-s5500-28C-PWR-SI": hh3c_s5500_28C_PWR_SI,
       "hh3c-s5500-52C-PWR-SI": hh3c_s5500_52C_PWR_SI,
       "hh3c-s5510-24P": hh3c_s5510_24P,
       "hh3c-s5510-24F": hh3c_s5510_24F,
       "hh3c-s3610-28P": hh3c_s3610_28P,
       "hh3c-s3610-52P": hh3c_s3610_52P,
       "hh3c-s3610-28TP": hh3c_s3610_28TP,
       "hh3c-s3610-28F": hh3c_s3610_28F,
       "hh3c-e126": hh3c_e126,
       "hh3c-e328": hh3c_e328,
       "hh3c-e352": hh3c_e352,
       "hh3c-s3100-8C-SI": hh3c_s3100_8C_SI,
       "hh3c-s3100-16C-SI": hh3c_s3100_16C_SI,
       "hh3c-s3100-26C-SI": hh3c_s3100_26C_SI,
       "hh3c-s3100-8T-SI": hh3c_s3100_8T_SI,
       "hh3c-s3100-16T-SI": hh3c_s3100_16T_SI,
       "hh3c-s3100-26T-SI": hh3c_s3100_26T_SI,
       "hh3c-s3100-26TP-SI": hh3c_s3100_26TP_SI,
       "hh3c-s5100-24P-EI": hh3c_s5100_24P_EI,
       "hh3c-s5100-26C-EI": hh3c_s5100_26C_EI,
       "hh3c-s5100-50C-EI": hh3c_s5100_50C_EI,
       "hh3c-s5100-48P-EI": hh3c_s5100_48P_EI,
       "hh3c-s3600-28P-SI": hh3c_s3600_28P_SI,
       "hh3c-s3600-52P-SI": hh3c_s3600_52P_SI,
       "hh3c-s3600-28TP-SI": hh3c_s3600_28TP_SI,
       "hh3c-s3600-28P-PWR-SI": hh3c_s3600_28P_PWR_SI,
       "hh3c-s3600-52P-PWR-SI": hh3c_s3600_52P_PWR_SI,
       "hh3c-s3600-28P-EI": hh3c_s3600_28P_EI,
       "hh3c-s3600-52P-EI": hh3c_s3600_52P_EI,
       "hh3c-s3600-28P-PWR-EI": hh3c_s3600_28P_PWR_EI,
       "hh3c-s3600-52P-PWR-EI": hh3c_s3600_52P_PWR_EI,
       "hh3c-s3600-28F-EI": hh3c_s3600_28F_EI,
       "hh3c-s5600-26C": hh3c_s5600_26C,
       "hh3c-s5600-50C": hh3c_s5600_50C,
       "hh3c-s5600-26C-PWR": hh3c_s5600_26C_PWR,
       "hh3c-s5600-50C-PWR": hh3c_s5600_50C_PWR,
       "hh3c-s5600-26F": hh3c_s5600_26F,
       "hh3c-s3600-52G-HI": hh3c_s3600_52G_HI,
       "hh3c-s3600-52P-HI": hh3c_s3600_52P_HI,
       "hh3c-s3600-28G-HI": hh3c_s3600_28G_HI,
       "hh3c-s3600-28P-HI": hh3c_s3600_28P_HI,
       "hh3c-s3600-52M-HI": hh3c_s3600_52M_HI,
       "hh3c-s7502": hh3c_s7502,
       "hh3c-s7503": hh3c_s7503,
       "hh3c-s7506": hh3c_s7506,
       "hh3c-s7506R": hh3c_s7506R,
       "hh3c-ar28-09": hh3c_ar28_09,
       "hh3c-ar28-10": hh3c_ar28_10,
       "hh3c-ar28-11": hh3c_ar28_11,
       "hh3c-ar28-12": hh3c_ar28_12,
       "hh3c-ar28-13": hh3c_ar28_13,
       "hh3c-ar28-14": hh3c_ar28_14,
       "hh3c-ar28-30": hh3c_ar28_30,
       "hh3c-ar28-31": hh3c_ar28_31,
       "hh3c-ar28-40": hh3c_ar28_40,
       "hh3c-ar28-80": hh3c_ar28_80,
       "hh3c-ar46-20": hh3c_ar46_20,
       "hh3c-ar46-40": hh3c_ar46_40,
       "hh3c-ar46-80": hh3c_ar46_80,
       "hh3c-msr20-20": hh3c_msr20_20,
       "hh3c-msr20-21": hh3c_msr20_21,
       "hh3c-msr20-40": hh3c_msr20_40,
       "hh3c-msr30-20": hh3c_msr30_20,
       "hh3c-msr30-40": hh3c_msr30_40,
       "hh3c-msr30-60": hh3c_msr30_60,
       "hh3c-msr50-40": hh3c_msr50_40,
       "hh3c-msr50-60": hh3c_msr50_60,
       "hh3c-ar18-21": hh3c_ar18_21,
       "hh3c-ar18-21A": hh3c_ar18_21A,
       "hh3c-ar18-21B": hh3c_ar18_21B,
       "hh3c-ar18-22": hh3c_ar18_22,
       "hh3c-ar18-22-8": hh3c_ar18_22_8,
       "hh3c-ar18-22S-8": hh3c_ar18_22S_8,
       "hh3c-ar18-22-24": hh3c_ar18_22_24,
       "hh3c-ar18-23-1": hh3c_ar18_23_1,
       "hh3c-ar18-23S-1": hh3c_ar18_23S_1,
       "hh3c-ar18-30E": hh3c_ar18_30E,
       "hh3c-ar18-31E": hh3c_ar18_31E,
       "hh3c-ar18-32E": hh3c_ar18_32E,
       "hh3c-ar18-33": hh3c_ar18_33,
       "hh3c-ar18-33E": hh3c_ar18_33E,
       "hh3c-ar18-34": hh3c_ar18_34,
       "hh3c-ar18-34E": hh3c_ar18_34E,
       "hh3c-ar18-35E": hh3c_ar18_35E,
       "hh3c-ar18-63-1": hh3c_ar18_63_1,
       "hh3c-secpathF100-C": hh3c_secpathF100_C,
       "hh3c-secpathF100-A": hh3c_secpathF100_A,
       "hh3c-secpathF100-S": hh3c_secpathF100_S,
       "hh3c-secpathF100-E": hh3c_secpathF100_E,
       "hh3c-secpathF1000-S": hh3c_secpathF1000_S,
       "hh3c-secpathF1000-A": hh3c_secpathF1000_A,
       "hh3c-secpathF1800-A": hh3c_secpathF1800_A,
       "hh3c-secpathV100-S": hh3c_secpathV100_S,
       "hh3c-secpathV1000-A": hh3c_secpathV1000_A,
       "hh3c-secpathF100-AW": hh3c_secpathF100_AW,
       "hh3c-secpathF1800-S": hh3c_secpathF1800_S,
       "hh3c-secpathF1800-E": hh3c_secpathF1800_E,
       "hh3c-secpoint": hh3c_secpoint,
       "hh3c-vg10-10": hh3c_vg10_10,
       "hh3c-vg10-11": hh3c_vg10_11,
       "hh3c-vg10-40": hh3c_vg10_40,
       "hh3c-vg10-41": hh3c_vg10_41,
       "hh3c-vg21-08": hh3c_vg21_08,
       "hh3c-vg20-16": hh3c_vg20_16,
       "hh3c-vg20-32": hh3c_vg20_32,
       "hh3c-vg80-20": hh3c_vg80_20,
       "hh3c-xe200": hh3c_xe200,
       "hh3c-xe2000": hh3c_xe2000,
       "hh3c-xe7200": hh3c_xe7200,
       "hh3c-xe7300": hh3c_xe7300,
       "hh3c-xe7500": hh3c_xe7500,
       "hh3c-xe7600": hh3c_xe7600,
       "hh3c-xe7205": hh3c_xe7205,
       "hh3c-xe7305": hh3c_xe7305,
       "hh3c-xe7505": hh3c_xe7505,
       "hh3c-xe7605": hh3c_xe7605,
       "hh3c-neoceanIX1000": hh3c_neoceanIX1000,
       "hh3c-neoceanEX1000": hh3c_neoceanEX1000,
       "hh3c-neoceanEX800": hh3c_neoceanEX800,
       "hh3c-neoceanIX5000": hh3c_neoceanIX5000,
       "hh3c-neoceanIV5100": hh3c_neoceanIV5100,
       "hh3c-neoceanIV5200": hh3c_neoceanIV5200,
       "hh3c-s9502": hh3c_s9502,
       "hh3c-s9505": hh3c_s9505,
       "hh3c-s9508": hh3c_s9508,
       "hh3c-s9508V": hh3c_s9508V,
       "hh3c-s9512": hh3c_s9512,
       "hh3c-sR8812": hh3c_sR8812,
       "hh3c-sR8808": hh3c_sR8808,
       "hh3c-sR8805": hh3c_sR8805,
       "hh3c-sR8802": hh3c_sR8802,
       "hh3c-e126-SI": hh3c_e126_SI,
       "hh3c-vg31-08": hh3c_vg31_08,
       "hh3c-dr834": hh3c_dr834,
       "hh3c-s7510E": hh3c_s7510E,
       "hh3c-s5100-24P-SI": hh3c_s5100_24P_SI,
       "hh3c-s5100-48P-SI": hh3c_s5100_48P_SI,
       "hh3c-s5100-8P-SI": hh3c_s5100_8P_SI,
       "hh3c-s5100-16P-SI": hh3c_s5100_16P_SI,
       "hh3c-s5100-8P-EI": hh3c_s5100_8P_EI,
       "hh3c-s5100-16P-EI": hh3c_s5100_16P_EI,
       "hh3c-s5100-8P-PWR-EI": hh3c_s5100_8P_PWR_EI,
       "hh3c-s5100-16P-PWR-EI": hh3c_s5100_16P_PWR_EI,
       "hh3c-s5100-26C-PWR-EI": hh3c_s5100_26C_PWR_EI,
       "hh3c-s5100-50C-PWR-EI": hh3c_s5100_50C_PWR_EI,
       "hh3c-s3108TP-EI": hh3c_s3108TP_EI,
       "hh3c-s3116TP-EI": hh3c_s3116TP_EI,
       "hh3c-s3126TP-EI": hh3c_s3126TP_EI,
       "hh3c-s3108TP-EI-PWR": hh3c_s3108TP_EI_PWR,
       "hh3c-s3116TP-EI-PWR": hh3c_s3116TP_EI_PWR,
       "hh3c-s3126TP-EI-PWR": hh3c_s3126TP_EI_PWR,
       "hh3c-s5500M-20C": hh3c_s5500M_20C,
       "hh3c-s5500M-20F": hh3c_s5500M_20F,
       "hh3c-bR304plus": hh3c_bR304plus,
       "hh3c-s9505-V5": hh3c_s9505_V5,
       "hh3c-s9512-V5": hh3c_s9512_V5,
       "hh3c-s9508-V5": hh3c_s9508_V5,
       "hh3c-s9508V-V5": hh3c_s9508V_V5,
       "hh3c-s9502-V5": hh3c_s9502_V5,
       "hh3c-sR8802-V5": hh3c_sR8802_V5,
       "hh3c-sR8805-V5": hh3c_sR8805_V5,
       "hh3c-sR8812-V5": hh3c_sR8812_V5,
       "hh3c-sR8808-V5": hh3c_sR8808_V5,
       "hh3c-s3100-52P": hh3c_s3100_52P,
       "hh3c-e152": hh3c_e152,
       "hh3c-s2008": hh3c_s2008,
       "hh3c-s2026": hh3c_s2026,
       "hh3c-sr6602": hh3c_sr6602,
       "hh3c-sr6608": hh3c_sr6608,
       "hh3c-s3100-08TP-EI": hh3c_s3100_08TP_EI,
       "hh3c-s3100-08TP-PWR-EI": hh3c_s3100_08TP_PWR_EI,
       "hh3c-s3100-16TP-EI": hh3c_s3100_16TP_EI,
       "hh3c-s3100-16TP-PWR-EI": hh3c_s3100_16TP_PWR_EI,
       "hh3c-s3100-26TP-EI": hh3c_s3100_26TP_EI,
       "hh3c-s3100-26TP-PWR-EI": hh3c_s3100_26TP_PWR_EI,
       "hh3c-s7502-v5": hh3c_s7502_v5,
       "hh3c-vg80-21": hh3c_vg80_21,
       "hh3c-vg80-80": hh3c_vg80_80,
       "hh3c-wcm-wx5002": hh3c_wcm_wx5002,
       "hh3c-wcm-wcma": hh3c_wcm_wcma,
       "hh3c-msr30-10": hh3c_msr30_10,
       "hh3c-s7502e": hh3c_s7502e,
       "hh3c-s7503E": hh3c_s7503E,
       "hh3c-s7506E": hh3c_s7506E,
       "hh3c-s7506E-V": hh3c_s7506E_V,
       "hh3c-secBlade-FW": hh3c_secBlade_FW,
       "hh3c-secBlade-IPSec": hh3c_secBlade_IPSec,
       "hh3c-s3100-8TP-SI": hh3c_s3100_8TP_SI,
       "hh3c-s3100-16TP-SI": hh3c_s3100_16TP_SI,
       "hh3c-e126A": hh3c_e126A,
       "hh3c-s3100-26TP-SI-B": hh3c_s3100_26TP_SI_B,
       "hh3c-msr30-16": hh3c_msr30_16,
       "hh3cOEMProductID": hh3cOEMProductID,
       "hh3c-s2126-ei": hh3c_s2126_ei,
       "hh3c-e150-si": hh3c_e150_si,
       "hh3c-msr30-11": hh3c_msr30_11,
       "hh3c-neoceanIX3040": hh3c_neoceanIX3040,
       "hh3c-neoceanIX3080": hh3c_neoceanIX3080,
       "hh3c-secpathF100-M": hh3c_secpathF100_M,
       "hh3c-neoceanVX1500": hh3c_neoceanVX1500,
       "hh3c-neoceanIX1520": hh3c_neoceanIX1520,
       "hh3c-neoceanIX1540": hh3c_neoceanIX1540,
       "hh3c-wcm-wx5002-128ap": hh3c_wcm_wx5002_128ap,
       "hh3c-msr20-10": hh3c_msr20_10,
       "hh3c-msr20-11": hh3c_msr20_11,
       "hh3c-msr20-13": hh3c_msr20_13,
       "hh3c-msr20-15": hh3c_msr20_15,
       "hh3c-neoceanDL1008": hh3c_neoceanDL1008,
       "hh3c-neoceanDL1008S": hh3c_neoceanDL1008S,
       "hh3c-neoceanDL1012": hh3c_neoceanDL1012,
       "hh3c-s3610-52m": hh3c_s3610_52m,
       "hh3c-IV5680": hh3c_IV5680,
       "hh3c-IV5240": hh3c_IV5240,
       "hh3c-F1000-E": hh3c_F1000_E,
       "hh3c-S5024P": hh3c_S5024P,
       "hh3c-S5016P": hh3c_S5016P,
       "hh3c-LSQ1FWBSC0": hh3c_LSQ1FWBSC0,
       "hh3c-LSB1FW2A0": hh3c_LSB1FW2A0,
       "hh3c-S3100-8TP-EI": hh3c_S3100_8TP_EI,
       "hh3c-S3100-16TP-EI": hh3c_S3100_16TP_EI,
       "hh3c-S3100-26TP-EI": hh3c_S3100_26TP_EI,
       "hh3c-ET704": hh3c_ET704,
       "hh3c-ec1001": hh3c_ec1001,
       "hh3c-ec1001-hf": hh3c_ec1001_hf,
       "hh3c-ec1004-hc": hh3c_ec1004_hc,
       "hh3c-ec2004-hf": hh3c_ec2004_hf,
       "hh3c-dc1001": hh3c_dc1001,
       "hh3c-dm8000": hh3c_dm8000,
       "hh3c-vm8000": hh3c_vm8000,
       "hh3c-ms8000": hh3c_ms8000,
       "hh3c-S3100-52TP": hh3c_S3100_52TP,
       "hh3c-msr20-12": hh3c_msr20_12,
       "hh3c-s1550E": hh3c_s1550E,
       "hh3c-s1550": hh3c_s1550,
       "hh3c-s1526-EI": hh3c_s1526_EI,
       "hh3c-msr20-12-T": hh3c_msr20_12_T,
       "hh3c-msr20-15-I": hh3c_msr20_15_I,
       "hh3c-msr20-15-N": hh3c_msr20_15_N,
       "hh3c-wx6100EWPX": hh3c_wx6100EWPX,
       "hh3c-wx6100LSQ": hh3c_wx6100LSQ,
       "hh3c-wx6100LSB": hh3c_wx6100LSB,
       "hh3c-wx6100SW": hh3c_wx6100SW,
       "hh3c-dl1000": hh3c_dl1000,
       "hh3c-dl1000s": hh3c_dl1000s,
       "hh3c-wa1208e-g": hh3c_wa1208e_g,
       "hh3c-wa1208e-dg": hh3c_wa1208e_dg,
       "hh3c-wa1208e-ag": hh3c_wa1208e_ag,
       "hh3c-wa1208e-agp": hh3c_wa1208e_agp,
       "hh3c-S7501M-24T": hh3c_S7501M_24T,
       "hh3c-s7501M-24TP": hh3c_s7501M_24TP,
       "hh3c-s7502M": hh3c_s7502M,
       "hh3c-s7503M": hh3c_s7503M,
       "hh3c-s7506M": hh3c_s7506M,
       "hh3c-s7506M-V": hh3c_s7506M_V,
       "hh3c-s7510M": hh3c_s7510M,
       "hh3c-secpathT200": hh3c_secpathT200,
       "hh3c-secpathT200E": hh3c_secpathT200E,
       "hh3c-cc600": hh3c_cc600,
       "hh3c-wa1208e-gp": hh3c_wa1208e_gp,
       "hh3c-wb2321e-agp": hh3c_wb2321e_agp,
       "hh3c-wh2520e-agp": hh3c_wh2520e_agp,
       "hh3c-ICG2000": hh3c_ICG2000,
       "hh3c-ICG3000": hh3c_ICG3000,
       "hh3c-ICG5000": hh3c_ICG5000,
       "hh3c-S5520TP-SI": hh3c_S5520TP_SI,
       "hh3c-wa2210-ag": hh3c_wa2210_ag,
       "hh3c-wa2220-ag": hh3c_wa2220_ag,
       "hh3c-wa2220e-ag": hh3c_wa2220e_ag,
       "hh3c-wa2210x-g": hh3c_wa2210x_g,
       "hh3c-wa2220x-ag": hh3c_wa2220x_ag,
       "hh3c-wa2220x-agp": hh3c_wa2220x_agp,
       "hh3c-S3100-52TP-SI": hh3c_S3100_52TP_SI,
       "hh3c-secpathASE5000-E": hh3c_secpathASE5000_E,
       "hh3c-secpathASE5000-S": hh3c_secpathASE5000_S,
       "hh3c-secpathU200-C": hh3c_secpathU200_C,
       "hh3c-secpathU200-S": hh3c_secpathU200_S,
       "hh3c-secpathU200-A": hh3c_secpathU200_A,
       "hh3c-secpathU200-M": hh3c_secpathU200_M,
       "hh3c-ec3016-hc": hh3c_ec3016_hc,
       "hh3c-dc1001-ff": hh3c_dc1001_ff,
       "hh3c-ecr3304-hf": hh3c_ecr3304_hf,
       "hh3c-ecr3308-hd": hh3c_ecr3308_hd,
       "hh3c-ecr3316-hc": hh3c_ecr3316_hc,
       "hh3c-isc3000": hh3c_isc3000,
       "hh3c-isc3100": hh3c_isc3100,
       "hh3c-vm9000": hh3c_vm9000,
       "hh3c-vm5000": hh3c_vm5000,
       "hh3c-ms9000-vtdu": hh3c_ms9000_vtdu,
       "hh3c-ms9000-nru": hh3c_ms9000_nru,
       "hh3c-ums9005": hh3c_ums9005,
       "hh3c-CS2104B": hh3c_CS2104B,
       "hh3c-CS2106B": hh3c_CS2106B,
       "hh3c-S5024E": hh3c_S5024E,
       "hh3c-S5048E": hh3c_S5048E,
       "hh3c-secpathF5000-A": hh3c_secpathF5000_A,
       "hh3c-neoceanIX3240": hh3c_neoceanIX3240,
       "hh3c-neoceanIX3620": hh3c_neoceanIX3620,
       "hh3c-MSA7302": hh3c_MSA7302,
       "hh3c-MSA7306": hh3c_MSA7306,
       "hh3c-S7501E": hh3c_S7501E,
       "hh3c-S3100-8C-EPON-EI": hh3c_S3100_8C_EPON_EI,
       "hh3c-S3100-16C-EPON-EI": hh3c_S3100_16C_EPON_EI,
       "hh3c-S3100-26C-EPON-EI": hh3c_S3100_26C_EPON_EI,
       "hh3c-secBlade-LSQ1AFCBSC0": hh3c_secBlade_LSQ1AFCBSC0,
       "hh3c-secBlade-LSB1AFC1A0": hh3c_secBlade_LSB1AFC1A0,
       "hh3c-secpathF1000-C": hh3c_secpathF1000_C,
       "hh3c-secpathF100-A-SI": hh3c_secpathF100_A_SI,
       "hh3c-secpathV100-E": hh3c_secpathV100_E,
       "hh3c-S5800-32C": hh3c_S5800_32C,
       "hh3c-S5800-56C": hh3c_S5800_56C,
       "hh3c-S5800-32C-PWR": hh3c_S5800_32C_PWR,
       "hh3c-S5800-56C-PWR": hh3c_S5800_56C_PWR,
       "hh3c-S5800-60C-PWR": hh3c_S5800_60C_PWR,
       "hh3c-S5800-32F": hh3c_S5800_32F,
       "hh3c-S5820X-28C": hh3c_S5820X_28C,
       "hh3c-S5820X-28S": hh3c_S5820X_28S,
       "hh3c-cc602": hh3c_cc602,
       "hh3c-cr400": hh3c_cr400,
       "hh3c-cc600E": hh3c_cc600E,
       "hh3c-secpathT1000-M": hh3c_secpathT1000_M,
       "hh3c-neoceanVX1540": hh3c_neoceanVX1540,
       "hh3c-msr50-06": hh3c_msr50_06,
       "hh3c-secpathACG2000-M": hh3c_secpathACG2000_M,
       "hh3c-secBlade-LSQ1ACGASC0": hh3c_secBlade_LSQ1ACGASC0,
       "hh3c-secBlade-LSB1ACG1A0": hh3c_secBlade_LSB1ACG1A0,
       "hh3c-wx3024wcm": hh3c_wx3024wcm,
       "hh3c-wx3024lsw": hh3c_wx3024lsw,
       "hh3c-wx5004": hh3c_wx5004,
       "hh3c-sr6604": hh3c_sr6604,
       "hh3c-iag5000-A": hh3c_iag5000_A,
       "hh3c-secBlade-SPE-FWM": hh3c_secBlade_SPE_FWM,
       "hh3c-ICG2200": hh3c_ICG2200,
       "hh3c-S7602": hh3c_S7602,
       "hh3c-S7603": hh3c_S7603,
       "hh3c-S7606": hh3c_S7606,
       "hh3c-S7606-V": hh3c_S7606_V,
       "hh3c-S7610": hh3c_S7610,
       "hh3c-wa2610e-agn": hh3c_wa2610e_agn,
       "hh3c-wa2620e-agn": hh3c_wa2620e_agn,
       "hh3c-wa1208e-g-v5": hh3c_wa1208e_g_v5,
       "hh3c-wa1208e-dg-v5": hh3c_wa1208e_dg_v5,
       "hh3c-wa1208e-ag-v5": hh3c_wa1208e_ag_v5,
       "hh3c-wa1208e-agp-v5": hh3c_wa1208e_agp_v5,
       "hh3c-wa1208e-gp-v5": hh3c_wa1208e_gp_v5,
       "hh3c-S7503E-S": hh3c_S7503E_S,
       "hh3c-secpathIAG2000-A": hh3c_secpathIAG2000_A,
       "hh3c-secpathT1000-A": hh3c_secpathT1000_A,
       "hh3c-secpathT1000-S": hh3c_secpathT1000_S,
       "hh3c-secBlade-EWPX1FWA0": hh3c_secBlade_EWPX1FWA0,
       "hh3c-secBlade-LSQ1NSMSC0": hh3c_secBlade_LSQ1NSMSC0,
       "hh3c-secBlade-LSQ1AFDBSC0": hh3c_secBlade_LSQ1AFDBSC0,
       "hh3c-secBlade-LSQ1LBSC0": hh3c_secBlade_LSQ1LBSC0,
       "hh3c-secBlade-LSB1LB1A0": hh3c_secBlade_LSB1LB1A0,
       "hh3c-neoceanIX1560": hh3c_neoceanIX1560,
       "hh3c-neoceanEX1500S": hh3c_neoceanEX1500S,
       "hh3c-neoceanEX1520S": hh3c_neoceanEX1520S,
       "hh3c-neoceanEX1540S": hh3c_neoceanEX1540S,
       "hh3c-neoceanEX1560S": hh3c_neoceanEX1560S,
       "hh3c-ET716": hh3c_ET716,
       "hh3c-s3600-2P-OLT": hh3c_s3600_2P_OLT,
       "hh3c-ER3200": hh3c_ER3200,
       "hh3c-ER3100": hh3c_ER3100,
       "hh3c-s9505E": hh3c_s9505E,
       "hh3c-s9508E-V": hh3c_s9508E_V,
       "hh3c-s9512E": hh3c_s9512E,
       "hh3c-s12508": hh3c_s12508,
       "hh3c-s12518": hh3c_s12518,
       "hh3c-ET708": hh3c_ET708,
       "hh3c-ET724": hh3c_ET724,
       "hh3c-s2008TP-EA": hh3c_s2008TP_EA,
       "hh3c-s2016TP-EA": hh3c_s2016TP_EA,
       "hh3c-s2403TP-EA": hh3c_s2403TP_EA,
       "hh3c-ICG2000-CT": hh3c_ICG2000_CT,
       "hh3c-S3528P-EA": hh3c_S3528P_EA,
       "hh3c-S3552P-EA": hh3c_S3552P_EA,
       "hh3c-S3552F-EA": hh3c_S3552F_EA,
       "hh3c-S3528F-EA": hh3c_S3528F_EA,
       "hh3c-S3528TP-EA": hh3c_S3528TP_EA,
       "hh3c-secpathAFD1000-A": hh3c_secpathAFD1000_A,
       "hh3c-secpathF100-C-EI": hh3c_secpathF100_C_EI,
       "hh3c-ER3260": hh3c_ER3260,
       "hh3c-ICG800": hh3c_ICG800,
       "hh3c-ICG800g": hh3c_ICG800g,
       "hh3c-ICG1000": hh3c_ICG1000,
       "hh3c-ICG1800": hh3c_ICG1800,
       "hh3c-neoceanIX3240E": hh3c_neoceanIX3240E,
       "hh3c-neoceanIX3620E": hh3c_neoceanIX3620E,
       "hh3c-neoceanIX3640E": hh3c_neoceanIX3640E,
       "hh3c-secpathACG8800-S3": hh3c_secpathACG8800_S3,
       "hh3c-secpathT5000-S3": hh3c_secpathT5000_S3,
       "hh3c-secpathIAG2000-S": hh3c_secpathIAG2000_S,
       "hh3c-secpathACG8800-S3-NS21S2MSPB0": hh3c_secpathACG8800_S3_NS21S2MSPB0,
       "hh3c-secpathT5000-S3-NS11S2MSPB0": hh3c_secpathT5000_S3_NS11S2MSPB0,
       "hh3c-msr3010": hh3c_msr3010,
       "hh3c-msr3011E": hh3c_msr3011E,
       "hh3c-msr3011F": hh3c_msr3011F,
       "hh3c-secpathT200-A": hh3c_secpathT200_A,
       "hh3c-secpathT200-M": hh3c_secpathT200_M,
       "hh3c-secpathF100-C2": hh3c_secpathF100_C2,
       "hh3c-DPtech-FW1000-GE": hh3c_DPtech_FW1000_GE,
       "hh3c-DPtech-FW1000-GA": hh3c_DPtech_FW1000_GA,
       "hh3c-DPtech-FW1000-GS": hh3c_DPtech_FW1000_GS,
       "hh3c-DPtech-FW1000-ME": hh3c_DPtech_FW1000_ME,
       "hh3c-DPtech-FW1000-MA": hh3c_DPtech_FW1000_MA,
       "hh3c-DPtech-FW1000-MM": hh3c_DPtech_FW1000_MM,
       "hh3c-DPtech-FW1000-MC": hh3c_DPtech_FW1000_MC,
       "hh3c-DPtech-UTM2000-MA": hh3c_DPtech_UTM2000_MA,
       "hh3c-DPtech-UTM2000-MM": hh3c_DPtech_UTM2000_MM,
       "hh3c-DPtech-UTM2000-MS": hh3c_DPtech_UTM2000_MS,
       "hh3c-DPtech-IPS2000-GM": hh3c_DPtech_IPS2000_GM,
       "hh3c-DPtech-IPS2000-MM": hh3c_DPtech_IPS2000_MM,
       "hh3c-sr6616": hh3c_sr6616,
       "hh3c-s3620-28TP-EI": hh3c_s3620_28TP_EI,
       "hh3c-s3620-28P-EI": hh3c_s3620_28P_EI,
       "hh3c-s3620-52P-EI": hh3c_s3620_52P_EI,
       "hh3c-s3620-28P-PWR-EI": hh3c_s3620_28P_PWR_EI,
       "hh3c-s3620-52P-PWR-EI": hh3c_s3620_52P_PWR_EI,
       "hh3c-s3620-28F-EI": hh3c_s3620_28F_EI,
       "hh3c-s3620-52M": hh3c_s3620_52M,
       "hh3c-s3620-52M-DC": hh3c_s3620_52M_DC,
       "hh3c-s3620-28C-EI": hh3c_s3620_28C_EI,
       "hh3c-wa2210e-ge": hh3c_wa2210e_ge,
       "hh3c-wa2220x-age": hh3c_wa2220x_age,
       "hh3c-wa2210x-ge": hh3c_wa2210x_ge,
       "hh3c-wb2320x-age": hh3c_wb2320x_age,
       "hh3c-neoceanEX1540": hh3c_neoceanEX1540,
       "hh3c-S5810-50S": hh3c_S5810_50S,
       "hh3c-secBlade-LSQ1IPSSC0": hh3c_secBlade_LSQ1IPSSC0,
       "hh3c-secBlade-LSB1IPS1A0": hh3c_secBlade_LSB1IPS1A0,
       "hh3c-ER5100": hh3c_ER5100,
       "hh3c-ER5200": hh3c_ER5200,
       "hh3c-wx3010wcm": hh3c_wx3010wcm,
       "hh3c-wx3010lsw": hh3c_wx3010lsw,
       "hh3c-cc652E": hh3c_cc652E,
       "hh3c-S5120-20P-SI": hh3c_S5120_20P_SI,
       "hh3c-S5120-28P-SI": hh3c_S5120_28P_SI,
       "hh3c-S5120-52P-SI": hh3c_S5120_52P_SI,
       "hh3c-S5120-28P-EI": hh3c_S5120_28P_EI,
       "hh3c-S5120-52P-EI": hh3c_S5120_52P_EI,
       "hh3c-S5120-28P-LPWR-EI": hh3c_S5120_28P_LPWR_EI,
       "hh3c-S5120-28P-PWR-EI": hh3c_S5120_28P_PWR_EI,
       "hh3c-wx6100LSR": hh3c_wx6100LSR,
       "hh3c-s7506E-S": hh3c_s7506E_S,
       "hh3c-ICG2000B": hh3c_ICG2000B,
       "hh3c-ICG2000C": hh3c_ICG2000C,
       "hh3c-S1626": hh3c_S1626,
       "hh3c-S1650": hh3c_S1650,
       "hh3c-S1626P": hh3c_S1626P,
       "hh3c-neoceanIX3620S": hh3c_neoceanIX3620S,
       "hh3c-neoceanIX3080S": hh3c_neoceanIX3080S,
       "hh3c-ER3280g": hh3c_ER3280g,
       "hh3c-wa2610-agn": hh3c_wa2610_agn,
       "hh3c-wa2612-agn": hh3c_wa2612_agn,
       "hh3c-secpathT200-S": hh3c_secpathT200_S,
       "hh3c-secpathU200-CS": hh3c_secpathU200_CS,
       "hh3c-secpathU200-CM": hh3c_secpathU200_CM,
       "hh3c-secpathU200-CA": hh3c_secpathU200_CA,
       "hh3c-secBlade-LSR1AFC2A1": hh3c_secBlade_LSR1AFC2A1,
       "hh3c-secBlade-LSR1FW2A1": hh3c_secBlade_LSR1FW2A1,
       "hh3c-secBlade-LSR1LB1A1": hh3c_secBlade_LSR1LB1A1,
       "hh3c-secBlade-LSR1NSM1A1": hh3c_secBlade_LSR1NSM1A1,
       "hh3c-cc650E": hh3c_cc650E,
       "hh3c-LSWM1WCM10": hh3c_LSWM1WCM10,
       "hh3c-LSWM1WCM20": hh3c_LSWM1WCM20,
       "hh3c-EWPXM1WCMC0": hh3c_EWPXM1WCMC0,
       "hh3c-LSWM1IPS10": hh3c_LSWM1IPS10,
       "hh3c-LSWM1FW10": hh3c_LSWM1FW10,
       "hh3c-secpathF1000-S-EI": hh3c_secpathF1000_S_EI,
       "hh3c-secpathF1000-A-EI": hh3c_secpathF1000_A_EI,
       "hh3c-msr50-06-V5": hh3c_msr50_06_V5,
       "hh3c-secBlade-LSR1ACG1A1": hh3c_secBlade_LSR1ACG1A1,
       "hh3c-secBlade-LSR1IPS1A1": hh3c_secBlade_LSR1IPS1A1,
       "hh3c-S7602-S": hh3c_S7602_S,
       "hh3c-S7603-S": hh3c_S7603_S,
       "hh3c-S7606-S": hh3c_S7606_S,
       "hh3c-SSM-s5500G": hh3c_SSM_s5500G,
       "hh3c-SSM-FIC": hh3c_SSM_FIC,
       "hh3c-SSM-MIM": hh3c_SSM_MIM,
       "hh3c-ER8300": hh3c_ER8300,
       "hh3c-wa2610x-gnp": hh3c_wa2610x_gnp,
       "hh3c-wb2360x-anp": hh3c_wb2360x_anp,
       "hh3c-wh2530x-dag": hh3c_wh2530x_dag,
       "hh3c-wa2620-agn": hh3c_wa2620_agn,
       "hh3c-cc610E": hh3c_cc610E,
       "hh3c-DPtech-FW1000-GT": hh3c_DPtech_FW1000_GT,
       "hh3c-s2008TP-EA-SI": hh3c_s2008TP_EA_SI,
       "hh3c-s2016TP-EA-SI": hh3c_s2016TP_EA_SI,
       "hh3c-s2403TP-EA-SI": hh3c_s2403TP_EA_SI,
       "hh3c-S5120-24P-EI": hh3c_S5120_24P_EI,
       "hh3c-S5120-48P-EI": hh3c_S5120_48P_EI,
       "hh3c-S5120-28C-EI": hh3c_S5120_28C_EI,
       "hh3c-S5120-52C-EI": hh3c_S5120_52C_EI,
       "hh3c-S5120-28C-PWR-EI": hh3c_S5120_28C_PWR_EI,
       "hh3c-S5120-52C-PWR-EI": hh3c_S5120_52C_PWR_EI,
       "hh3c-wx3008wcm": hh3c_wx3008wcm,
       "hh3c-wx3008lsw": hh3c_wx3008lsw,
       "hh3c-msr900": hh3c_msr900,
       "hh3c-msr920": hh3c_msr920,
       "hh3c-secBlade-LSQ1IAGSC0": hh3c_secBlade_LSQ1IAGSC0,
       "hh3c-WX7306": hh3c_WX7306,
       "hh3c-WX7310": hh3c_WX7310,
       "hh3c-Blade5310": hh3c_Blade5310,
       "hh3c-Blade55102": hh3c_Blade55102,
       "hh3c-Blade5512S": hh3c_Blade5512S,
       "hh3c-Blade55110X": hh3c_Blade55110X,
       "hh3c-wa2610e-gnp": hh3c_wa2610e_gnp,
       "hh3c-s3100-26TP-SI-UM": hh3c_s3100_26TP_SI_UM,
       "hh3c-s3100-52TP-SI-UM": hh3c_s3100_52TP_SI_UM,
       "hh3c-s5500-24P-SI": hh3c_s5500_24P_SI,
       "hh3c-s5500-48P-SI": hh3c_s5500_48P_SI,
       "hh3c-ME8000": hh3c_ME8000,
       "hh3c-ME8600": hh3c_ME8600,
       "hh3c-ME5000": hh3c_ME5000,
       "hh3c-MG6060": hh3c_MG6060,
       "hh3c-MG6050": hh3c_MG6050,
       "hh3c-MG6050S": hh3c_MG6050S,
       "hh3c-MG9010": hh3c_MG9010,
       "hh3c-MG9030": hh3c_MG9030,
       "hh3c-MG9060": hh3c_MG9060,
       "hh3c-neoceanVX1500-DC": hh3c_neoceanVX1500_DC,
       "hh3c-cc620E": hh3c_cc620E,
       "hh3c-SIVX-S3628": hh3c_SIVX_S3628,
       "hh3c-SIVX-S5528": hh3c_SIVX_S5528,
       "hh3c-SIVX-VS1500": hh3c_SIVX_VS1500,
       "hh3c-neoceanIX2540": hh3c_neoceanIX2540,
       "hh3c-neoceanVX2500": hh3c_neoceanVX2500,
       "hh3c-S5120-28P-PWR-SI": hh3c_S5120_28P_PWR_SI,
       "hh3c-S5120-28P-HPWR-SI": hh3c_S5120_28P_HPWR_SI,
       "hh3c-F1000-E-DC": hh3c_F1000_E_DC,
       "hh3c-S5028": hh3c_S5028,
       "hh3c-ET824": hh3c_ET824,
       "hh3c-OSM": hh3c_OSM,
       "hh3c-wx5002-v2": hh3c_wx5002_v2,
       "hh3c-wx5004-v2": hh3c_wx5004_v2,
       "hh3c-secpathT1000-C": hh3c_secpathT1000_C,
       "hh3c-secBlade-LST1IPS1A1": hh3c_secBlade_LST1IPS1A1,
       "hh3c-secBlade-LST1FW2A1": hh3c_secBlade_LST1FW2A1,
       "hh3c-secBlade-LST1LB1A1": hh3c_secBlade_LST1LB1A1,
       "hh3c-secBlade-LST1NSM1A1": hh3c_secBlade_LST1NSM1A1,
       "hh3c-secBlade-EWPX2IAGSC0": hh3c_secBlade_EWPX2IAGSC0,
       "hh3c-F1000-A-EI": hh3c_F1000_A_EI,
       "hh3c-wx6108E": hh3c_wx6108E,
       "hh3c-wx6112E": hh3c_wx6112E,
       "hh3c-s5500-34C-HI": hh3c_s5500_34C_HI,
       "hh3c-s5500-58C-HI": hh3c_s5500_58C_HI,
       "hh3c-wa1208e-gp-h20": hh3c_wa1208e_gp_h20,
       "hh3c-S5120-9P-SI": hh3c_S5120_9P_SI,
       "hh3c-S5120-9P-PWR-SI": hh3c_S5120_9P_PWR_SI,
       "hh3c-S5120-9P-HPWR-SI": hh3c_S5120_9P_HPWR_SI,
       "hh3c-e528": hh3c_e528,
       "hh3c-e552": hh3c_e552,
       "hh3c-s3600V2-28TP-EI": hh3c_s3600V2_28TP_EI,
       "hh3c-s3600V2-52TP-EI": hh3c_s3600V2_52TP_EI,
       "hh3c-s3600V2-28TP-PWR-EI": hh3c_s3600V2_28TP_PWR_EI,
       "hh3c-s3600V2-52TP-PWR-EI": hh3c_s3600V2_52TP_PWR_EI,
       "hh3c-s3600V2-28F-EI": hh3c_s3600V2_28F_EI,
       "hh3c-s3600V2-28TP-SI": hh3c_s3600V2_28TP_SI,
       "hh3c-s3600V2-52TP-SI": hh3c_s3600V2_52TP_SI,
       "hh3c-s3600V2-28TP-PWR-SI": hh3c_s3600V2_28TP_PWR_SI,
       "hh3c-s3600V2-52TP-PWR-SI": hh3c_s3600V2_52TP_PWR_SI,
       "hh3c-s3500V2-28TP-EA": hh3c_s3500V2_28TP_EA,
       "hh3c-s3500V2-52TP-EA": hh3c_s3500V2_52TP_EA,
       "hh3c-s3500V2-28F-EA": hh3c_s3500V2_28F_EA,
       "hh3c-s3500V2-28TP-SI": hh3c_s3500V2_28TP_SI,
       "hh3c-s3500V2-52TP-SI": hh3c_s3500V2_52TP_SI,
       "hh3c-s9508E": hh3c_s9508E,
       "hh3c-s12504": hh3c_s12504,
       "hh3c-ICG2000B-GT": hh3c_ICG2000B_GT,
       "hh3c-ICG3000B": hh3c_ICG3000B,
       "hh3c-ICG3000S": hh3c_ICG3000S,
       "hh3c-ICG5000B": hh3c_ICG5000B,
       "hh3c-wh2640X-agnp": hh3c_wh2640X_agnp,
       "hh3c-wa2620X-agnp": hh3c_wa2620X_agnp,
       "hh3c-s3100-16TP-PWR-EI-F": hh3c_s3100_16TP_PWR_EI_F,
       "hh3c-cr16018": hh3c_cr16018,
       "hh3c-cr16008": hh3c_cr16008,
       "hh3c-cr16004": hh3c_cr16004,
       "hh3c-F1000-A-SI": hh3c_F1000_A_SI,
       "hh3c-F1000-E-SI": hh3c_F1000_E_SI,
       "hh3c-secBlade-LST1ACG1A1": hh3c_secBlade_LST1ACG1A1,
       "hh3c-secBlade-SPE-IPS": hh3c_secBlade_SPE_IPS,
       "hh3c-secBlade-SPE-ACG": hh3c_secBlade_SPE_ACG,
       "hh3c-wx6103": hh3c_wx6103,
       "hh3c-LSQ1WCMD0": hh3c_LSQ1WCMD0,
       "hh3c-EWPX2WCMD0": hh3c_EWPX2WCMD0,
       "hh3c-LSR1WCM3A1": hh3c_LSR1WCM3A1,
       "hh3c-S5830-52SC": hh3c_S5830_52SC,
       "hh3c-S5830-106S": hh3c_S5830_106S,
       "hh3c-ET814": hh3c_ET814,
       "hh3c-S5120-28P-LI": hh3c_S5120_28P_LI,
       "hh3c-S5120-52P-LI": hh3c_S5120_52P_LI,
       "hh3c-secBlade-IM-FW-II": hh3c_secBlade_IM_FW_II,
       "hh3c-secBlade-IM-LB": hh3c_secBlade_IM_LB,
       "hh3c-secBlade-IM-SSL": hh3c_secBlade_IM_SSL,
       "hh3c-ER2210C": hh3c_ER2210C,
       "hh3c-VCX-Connect-100": hh3c_VCX_Connect_100,
       "hh3c-VCX-Connect-200": hh3c_VCX_Connect_200,
       "hh3c-VCX-V7005": hh3c_VCX_V7005,
       "hh3c-VCX-V7205": hh3c_VCX_V7205,
       "hh3c-VCX-MIM": hh3c_VCX_MIM,
       "hh3c-VCX-Connect-MIM-Primary": hh3c_VCX_Connect_MIM_Primary,
       "hh3c-VCX-Connect-MIM-Secondary": hh3c_VCX_Connect_MIM_Secondary,
       "hh3c-VCX-V7310": hh3c_VCX_V7310,
       "hh3c-secBlade-IM-IPS": hh3c_secBlade_IM_IPS,
       "hh3c-secBlade-IM-ACG": hh3c_secBlade_IM_ACG,
       "hh3c-s7508E-X": hh3c_s7508E_X,
       "hh3c-s10504": hh3c_s10504,
       "hh3c-s10508": hh3c_s10508,
       "hh3c-s10508-V": hh3c_s10508_V,
       "hh3c-secBlade-SPE-FWM-200": hh3c_secBlade_SPE_FWM_200,
       "hh3c-secpathF1000-S-AI": hh3c_secpathF1000_S_AI,
       "hh3c-wx3024e-wcm": hh3c_wx3024e_wcm,
       "hh3c-wx3024e-lsw": hh3c_wx3024e_lsw,
       "hh3c-ER2100": hh3c_ER2100,
       "hh3c-S5820X-34TC": hh3c_S5820X_34TC,
       "hh3c-S5820X-34SC": hh3c_S5820X_34SC,
       "hh3c-S5820X-34C": hh3c_S5820X_34C,
       "hh3c-S5820X-64SC": hh3c_S5820X_64SC,
       "hh3c-cc720E": hh3c_cc720E,
       "hh3c-S2126T": hh3c_S2126T,
       "hh3c-S5800-54S": hh3c_S5800_54S,
       "hh3c-S5820X-26S": hh3c_S5820X_26S,
       "hh3c-S3100V2-8TP-SI": hh3c_S3100V2_8TP_SI,
       "hh3c-S3100V2-16TP-SI": hh3c_S3100V2_16TP_SI,
       "hh3c-S3100V2-26TP-SI": hh3c_S3100V2_26TP_SI,
       "hh3c-E126B": hh3c_E126B,
       "hh3c-S3100V2-8TP-EI": hh3c_S3100V2_8TP_EI,
       "hh3c-S3100V2-16TP-EI": hh3c_S3100V2_16TP_EI,
       "hh3c-S3100V2-26TP-EI": hh3c_S3100V2_26TP_EI,
       "hh3c-S3100V2-8TP-PWR-EI": hh3c_S3100V2_8TP_PWR_EI,
       "hh3c-S3100V2-16TP-PWR-EI": hh3c_S3100V2_16TP_PWR_EI,
       "hh3c-S3100V2-26TP-PWR-EI": hh3c_S3100V2_26TP_PWR_EI,
       "hh3c-S2008TP-EB": hh3c_S2008TP_EB,
       "hh3c-S2016TP-EB": hh3c_S2016TP_EB,
       "hh3c-S2403TP-EB": hh3c_S2403TP_EB,
       "hh3c-S2008TP-PWR-EB": hh3c_S2008TP_PWR_EB,
       "hh3c-S2016TP-PWR-EB": hh3c_S2016TP_PWR_EB,
       "hh3c-S2403TP-PWR-EB": hh3c_S2403TP_PWR_EB,
       "hh3c-S5800-LSW1FC4P0": hh3c_S5800_LSW1FC4P0,
       "hh3c-S2403TP-EA-SI-D": hh3c_S2403TP_EA_SI_D,
       "hh3c-S3528P-EA-D": hh3c_S3528P_EA_D,
       "hh3c-OAP-FIC-V2": hh3c_OAP_FIC_V2,
       "hh3c-OAP-MIM-V2": hh3c_OAP_MIM_V2,
       "hh3c-OAPS-MIM-V2": hh3c_OAPS_MIM_V2,
       "hh3c-S2008TP-PWR-EA": hh3c_S2008TP_PWR_EA,
       "hh3c-S2008TP-PWR-EA-DC": hh3c_S2008TP_PWR_EA_DC,
       "hh3c-S2016TP-PWR-EA": hh3c_S2016TP_PWR_EA,
       "hh3c-S2403TP-PWR-EA": hh3c_S2403TP_PWR_EA,
       "hh3c-S5120-24P-EI-D": hh3c_S5120_24P_EI_D,
       "hh3c-S5120-24P-PWR-EI-D": hh3c_S5120_24P_PWR_EI_D,
       "hh3c-S5120-48P-EI-D": hh3c_S5120_48P_EI_D,
       "hh3c-S5024P-EI": hh3c_S5024P_EI,
       "hh3c-S5500-28C-EI-D": hh3c_S5500_28C_EI_D,
       "hh3c-S5500-52C-EI-D": hh3c_S5500_52C_EI_D,
       "hh3c-S5500-28F-EI-D": hh3c_S5500_28F_EI_D,
       "hh3c-S5500-28C-EI-DC-D": hh3c_S5500_28C_EI_DC_D,
       "hh3c-MG9050": hh3c_MG9050,
       "hh3c-S5120-52SC-HI": hh3c_S5120_52SC_HI,
       "hh3c-CE3000-32F-EI": hh3c_CE3000_32F_EI,
       "hh3c-S5830X-24S": hh3c_S5830X_24S,
       "hh3cDC1801FH": hh3cDC1801FH,
       "hh3cDC2004FF": hh3cDC2004FF,
       "hh3cEC1101HF": hh3cEC1101HF,
       "hh3cEC1102HF": hh3cEC1102HF,
       "hh3cEC1501HF": hh3cEC1501HF,
       "hh3cEC1801HH": hh3cEC1801HH,
       "hh3cEC2516HF": hh3cEC2516HF,
       "hh3cEC2016HC": hh3cEC2016HC,
       "hh3cEC2016HC8CH": hh3cEC2016HC8CH,
       "hh3cEC2016HC4CH": hh3cEC2016HC4CH,
       "hh3cEC1504HF": hh3cEC1504HF,
       "hh3cHIC5421": hh3cHIC5421,
       "hh3cHIC5401": hh3cHIC5401,
       "hh3cHIC5221H": hh3cHIC5221H,
       "hh3cHIC5201H": hh3cHIC5201H,
       "hh3cVM8500": hh3cVM8500,
       "hh3cMS8500": hh3cMS8500,
       "hh3cDM8500": hh3cDM8500,
       "hh3cVX500": hh3cVX500,
       "hh3cISC3000E": hh3cISC3000E,
       "hh3cISC3000S": hh3cISC3000S,
       "hh3cCC700E": hh3cCC700E,
       "hh3cDC1001FF": hh3cDC1001FF,
       "hh3cECR3316HC": hh3cECR3316HC,
       "hh3cECR3308HD": hh3cECR3308HD,
       "hh3cECR3316HC8CH": hh3cECR3316HC8CH,
       "hh3cECR3316HC4CH": hh3cECR3316HC4CH,
       "hh3cECR3308HD4CH": hh3cECR3308HD4CH,
       "hh3cHIC65017L": hh3cHIC65017L,
       "hh3cEC2508HF": hh3cEC2508HF,
       "hh3cS3528EA": hh3cS3528EA,
       "hh3cS3552TPEA": hh3cS3552TPEA,
       "hh3cWP3024": hh3cWP3024,
       "hh3cWP3048": hh3cWP3048,
       "hh3cS3528FPEA": hh3cS3528FPEA,
       "hh3cE328B": hh3cE328B,
       "hh3cE352B": hh3cE352B,
       "hh3cE152B": hh3cE152B,
       "hh3cS3100V252TP": hh3cS3100V252TP,
       "hh3cWP2008": hh3cWP2008,
       "hh3cWP2016": hh3cWP2016,
       "hh3cWP2024": hh3cWP2024,
       "hh3cWP5024": hh3cWP5024,
       "hh3cWP5048": hh3cWP5048,
       "hh3cS2052TPEA": hh3cS2052TPEA,
       "hh3cS7604X": hh3cS7604X,
       "hh3cS7608X": hh3cS7608X,
       "hh3cS7608XV": hh3cS7608XV,
       "hh3cWA3620iAGN": hh3cWA3620iAGN,
       "hh3cWA3628iAGN": hh3cWA3628iAGN,
       "hh3cWA3610iGN": hh3cWA3610iGN,
       "hh3cCC750E": hh3cCC750E,
       "hpSwitch": hpSwitch,
       "hpA7502": hpA7502,
       "hpA7503S": hpA7503S,
       "hpA7503": hpA7503,
       "hpA7506": hpA7506,
       "hpA7506V": hpA7506V,
       "hpA7510": hpA7510,
       "hpA36002POLT": hpA36002POLT,
       "hpV190524": hpV190524,
       "hpV190524POE": hpV190524POE,
       "hpV190548": hpV190548,
       "hpA512016GSI": hpA512016GSI,
       "hpA512024GSI": hpA512024GSI,
       "hpA512048GSI": hpA512048GSI,
       "hpA512024GPPOESI": hpA512024GPPOESI,
       "hpA512024GPOESI": hpA512024GPOESI,
       "hpA580024G": hpA580024G,
       "hpA580024GPoEPlus": hpA580024GPoEPlus,
       "hpA580048G": hpA580048G,
       "hpA580048GPoEPlus": hpA580048GPoEPlus,
       "hpA580024GSFP": hpA580024GSFP,
       "hpA580048GPoEPlus2SLOT": hpA580048GPoEPlus2SLOT,
       "hpA5820X14XGSFPPlus2SLOT": hpA5820X14XGSFPPlus2SLOT,
       "hpA5820X24XGSFPPlus": hpA5820X24XGSFPPlus,
       "hpA550028CEI": hpA550028CEI,
       "hpA550052CEI": hpA550052CEI,
       "hpA550028CPWREI": hpA550028CPWREI,
       "hpA550052CPWREI": hpA550052CPWREI,
       "hpA550028FEI": hpA550028FEI,
       "hpA550028CSI": hpA550028CSI,
       "hpA550052CSI": hpA550052CSI,
       "hpA550028CPWRSI": hpA550028CPWRSI,
       "hpA550052CPWRSI": hpA550052CPWRSI,
       "hpA512028CEI": hpA512028CEI,
       "hpA512052CEI": hpA512052CEI,
       "hpA512028CPWREI": hpA512028CPWREI,
       "hpA512052CPWREI": hpA512052CPWREI,
       "hpA512024PEI": hpA512024PEI,
       "hpA512048PEI": hpA512048PEI,
       "hpA9505": hpA9505,
       "hpA9508V": hpA9508V,
       "hpA9508": hpA9508,
       "hpA9512": hpA9512,
       "hpA12508": hpA12508,
       "hpA12518": hpA12518,
       "hpA12504": hpA12504,
       "hpA5800AF48G": hpA5800AF48G,
       "hpA5820AF24XG": hpA5820AF24XG,
       "hpA6125GXG": hpA6125GXG,
       "hpA31008SI": hpA31008SI,
       "hpA310016SI": hpA310016SI,
       "hpA310024SI": hpA310024SI,
       "hpA31008EI": hpA31008EI,
       "hpA310016EI": hpA310016EI,
       "hpA310024EI": hpA310024EI,
       "hpA31008POEEI": hpA31008POEEI,
       "hpA310016POEEI": hpA310016POEEI,
       "hpA310024POEEI": hpA310024POEEI,
       "hpA580024GTAA": hpA580024GTAA,
       "hpA580024GPoEPlusTAA": hpA580024GPoEPlusTAA,
       "hpA580024GSFPTAA": hpA580024GSFPTAA,
       "hpA580048GTAA": hpA580048GTAA,
       "hpA580048GPoEPlusTAA2SLOT": hpA580048GPoEPlusTAA2SLOT,
       "hpA580048GPoEPlusTAA": hpA580048GPoEPlusTAA,
       "hpA5820X14XGSFPPlusTAA2SLOT": hpA5820X14XGSFPPlusTAA2SLOT,
       "hpA582024XGSFPPlusTAA": hpA582024XGSFPPlusTAA,
       "hpA512024GEITAA": hpA512024GEITAA,
       "hpA512048GEITAA": hpA512048GEITAA,
       "hpA512024GPOEEITAA": hpA512024GPOEEITAA,
       "hpA512048GPOEEITAA": hpA512048GPOEEITAA,
       "hpA550024GSFPEITAA": hpA550024GSFPEITAA,
       "hpA550024GEITAA": hpA550024GEITAA,
       "hpA550048GEITAA": hpA550048GEITAA,
       "hpA550024GPOEEITAA": hpA550024GPOEEITAA,
       "hpA550048GPOEEITAA": hpA550048GPOEEITAA,
       "hpA5830AF24XG": hpA5830AF24XG,
       "hpA5830AF48G": hpA5830AF48G,
       "hpA5830AF96G": hpA5830AF96G,
       "hpV191016G": hpV191016G,
       "hpV191024G": hpV191024G,
       "hpV191024GPoE365W": hpV191024GPoE365W,
       "hpV191024GPoE170W": hpV191024GPoE170W,
       "hpV191048G": hpV191048G,
       "hpA10504": hpA10504,
       "hpA10508": hpA10508,
       "hpA10508V": hpA10508V,
       "hpA10512": hpA10512,
       "hpA360024V2EI": hpA360024V2EI,
       "hpA360048V2EI": hpA360048V2EI,
       "hpA360024PoEPlusV2EI": hpA360024PoEPlusV2EI,
       "hpA360048PoEPlusV2EI": hpA360048PoEPlusV2EI,
       "hpA360024SFPV2EI": hpA360024SFPV2EI,
       "hpA360024V2SI": hpA360024V2SI,
       "hpA360048V2SI": hpA360048V2SI,
       "hpA360024PoEPlusV2SI": hpA360024PoEPlusV2SI,
       "hpA360048PoEPlusV2SI": hpA360048PoEPlusV2SI,
       "hpA310048V2": hpA310048V2,
       "hpRouter": hpRouter,
       "hpAMSR900": hpAMSR900,
       "hpAMSR920": hpAMSR920,
       "hpAMSR2010": hpAMSR2010,
       "hpAMSR2011": hpAMSR2011,
       "hpAMSR2012": hpAMSR2012,
       "hpAMSR2012T": hpAMSR2012T,
       "hpAMSR2013": hpAMSR2013,
       "hpAMSR2020": hpAMSR2020,
       "hpAMSR2021": hpAMSR2021,
       "hpAMSR2040": hpAMSR2040,
       "hpAMSR3010": hpAMSR3010,
       "hpAMSR3011E": hpAMSR3011E,
       "hpAMSR3011F": hpAMSR3011F,
       "hpAMSR3016": hpAMSR3016,
       "hpAMSR3020": hpAMSR3020,
       "hpAMSR3040": hpAMSR3040,
       "hpAMSR3060": hpAMSR3060,
       "hpAMSR5040": hpAMSR5040,
       "hpAMSR5060": hpAMSR5060,
       "hpA6602": hpA6602,
       "hpA6604": hpA6604,
       "hpA6608": hpA6608,
       "hpA6616": hpA6616,
       "hpAMSR900W": hpAMSR900W,
       "hpAMSR900WNA": hpAMSR900WNA,
       "hpAMSR920W": hpAMSR920W,
       "hpAMSR920WNA": hpAMSR920WNA,
       "hpAMSR2012W": hpAMSR2012W,
       "hpAMSR2012TW": hpAMSR2012TW,
       "hpAMSR2012TWNA": hpAMSR2012TWNA,
       "hpAMSR2013W": hpAMSR2013W,
       "hpAMSR2013WNA": hpAMSR2013WNA,
       "hpAMSR2020S": hpAMSR2020S,
       "hpAMSR2021S": hpAMSR2021S,
       "hpAMSR2040S": hpAMSR2040S,
       "hpAMSR3010DC": hpAMSR3010DC,
       "hpAMSR3016POE": hpAMSR3016POE,
       "hpAMSR3020AS": hpAMSR3020AS,
       "hpAMSR3020POE": hpAMSR3020POE,
       "hpAMSR3020DC": hpAMSR3020DC,
       "hpAMSR3040AS": hpAMSR3040AS,
       "hpAMSR3040POE": hpAMSR3040POE,
       "hpAMSR3040DC": hpAMSR3040DC,
       "hpAMSR3060AS": hpAMSR3060AS,
       "hpAMSR3060POE": hpAMSR3060POE,
       "hpAMSR3060DC": hpAMSR3060DC,
       "hpAMSR5040DC": hpAMSR5040DC,
       "hpAMSR5060DC": hpAMSR5060DC,
       "hpA8805": hpA8805,
       "hpA8808": hpA8808,
       "hpA8812": hpA8812,
       "hpWireless": hpWireless,
       "hpAWA2610EAGNFAT": hpAWA2610EAGNFAT,
       "hpAWA2620EAGNFAT": hpAWA2620EAGNFAT,
       "hpAWA2620AGNFAT": hpAWA2620AGNFAT,
       "hpA7500LSQM3WCMB0": hpA7500LSQM3WCMB0,
       "hpA9500LSRM2WCM2A1": hpA9500LSRM2WCM2A1,
       "hpA5800LSWM2WCM10": hpA5800LSWM2WCM10,
       "hpA5800LSWM2WCM20": hpA5800LSWM2WCM20,
       "hpAWX5004EWPXZ65004": hpAWX5004EWPXZ65004,
       "hpAWX5002EWPXZ75002": hpAWX5002EWPXZ75002,
       "hpA3000E": hpA3000E,
       "hpA3000ELSW": hpA3000ELSW,
       "hpAWA3620iAGN": hpAWA3620iAGN,
       "hpAWA3628iAGN": hpAWA3628iAGN,
       "hpAWA3610iGN": hpAWA3610iGN,
       "hpSecurity": hpSecurity,
       "hpSecBladeIMFWII": hpSecBladeIMFWII,
       "hpSecBladeIMSSL": hpSecBladeIMSSL,
       "hpSecBladeIMLB": hpSecBladeIMLB,
       "hpSecBladeLSQ1FWBSC0": hpSecBladeLSQ1FWBSC0,
       "hpSecBladeLSQM1LBC0": hpSecBladeLSQM1LBC0,
       "hpSecBladeLSQ1NSMSC0": hpSecBladeLSQ1NSMSC0,
       "hpSecBladeLSR1FW2A1": hpSecBladeLSR1FW2A1,
       "hpSecBladeLSR1LB1A1": hpSecBladeLSR1LB1A1,
       "hpSecBladeLSR1NSM1A1": hpSecBladeLSR1NSM1A1,
       "hpSecBladeLST1FW2A1": hpSecBladeLST1FW2A1,
       "hpSecBladeLST1LB1A1": hpSecBladeLST1LB1A1,
       "hpSecBladeLST1NSM1A1": hpSecBladeLST1NSM1A1,
       "hpSecBladeLSWM1FW10": hpSecBladeLSWM1FW10,
       "hpSecBladeSPEFWM200": hpSecBladeSPEFWM200,
       "hpAF5000": hpAF5000,
       "hpAF1000E": hpAF1000E,
       "hpAU200S": hpAU200S,
       "hpAU200A": hpAU200A,
       "hpAF1000SEI": hpAF1000SEI,
       "hpAF1000AEI": hpAF1000AEI}
)
