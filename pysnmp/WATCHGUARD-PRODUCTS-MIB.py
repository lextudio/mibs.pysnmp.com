# SNMP MIB module (WATCHGUARD-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WATCHGUARD-PRODUCTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:37 2024
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

(watchguard,) = mibBuilder.importSymbols(
    "WATCHGUARD-SMI",
    "watchguard")


# MODULE-IDENTITY

wgProducts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1)
)
wgProducts.setRevisions(
        ("2008-11-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FbXSeries_ObjectIdentity = ObjectIdentity
fbXSeries = _FbXSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4)
)
_FbX500_ObjectIdentity = ObjectIdentity
fbX500 = _FbX500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 1)
)
_FbX550e_ObjectIdentity = ObjectIdentity
fbX550e = _FbX550e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 2)
)
_FbX700_ObjectIdentity = ObjectIdentity
fbX700 = _FbX700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 3)
)
_FbX750e_ObjectIdentity = ObjectIdentity
fbX750e = _FbX750e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 4)
)
_FbX750e_4_ObjectIdentity = ObjectIdentity
fbX750e_4 = _FbX750e_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 5)
)
_FbX1000_ObjectIdentity = ObjectIdentity
fbX1000 = _FbX1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 6)
)
_FbX1250e_ObjectIdentity = ObjectIdentity
fbX1250e = _FbX1250e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 7)
)
_FbX1250e_4_ObjectIdentity = ObjectIdentity
fbX1250e_4 = _FbX1250e_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 8)
)
_FbX2500_ObjectIdentity = ObjectIdentity
fbX2500 = _FbX2500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 9)
)
_FbX5000_ObjectIdentity = ObjectIdentity
fbX5000 = _FbX5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 10)
)
_FbX5500e_ObjectIdentity = ObjectIdentity
fbX5500e = _FbX5500e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 11)
)
_FbX6000_ObjectIdentity = ObjectIdentity
fbX6000 = _FbX6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 12)
)
_FbX6500e_ObjectIdentity = ObjectIdentity
fbX6500e = _FbX6500e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 13)
)
_FbX8000_ObjectIdentity = ObjectIdentity
fbX8000 = _FbX8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 14)
)
_FbX8500e_ObjectIdentity = ObjectIdentity
fbX8500e = _FbX8500e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 15)
)
_FbX8500e_F_ObjectIdentity = ObjectIdentity
fbX8500e_F = _FbX8500e_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 16)
)
_FbX10e_ObjectIdentity = ObjectIdentity
fbX10e = _FbX10e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 17)
)
_FbX10e_W_ObjectIdentity = ObjectIdentity
fbX10e_W = _FbX10e_W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 18)
)
_FbX20e_ObjectIdentity = ObjectIdentity
fbX20e = _FbX20e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 19)
)
_FbX20e_W_ObjectIdentity = ObjectIdentity
fbX20e_W = _FbX20e_W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 20)
)
_FbX55e_ObjectIdentity = ObjectIdentity
fbX55e = _FbX55e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 21)
)
_FbX55e_W_ObjectIdentity = ObjectIdentity
fbX55e_W = _FbX55e_W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 22)
)
_XtmSeries_ObjectIdentity = ObjectIdentity
xtmSeries = _XtmSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5)
)
_Xtm1050_ObjectIdentity = ObjectIdentity
xtm1050 = _Xtm1050_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 1)
)
_Xtm1050_F_ObjectIdentity = ObjectIdentity
xtm1050_F = _Xtm1050_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 2)
)
_Xtm830_F_ObjectIdentity = ObjectIdentity
xtm830_F = _Xtm830_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 3)
)
_Xtm830_ObjectIdentity = ObjectIdentity
xtm830 = _Xtm830_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 4)
)
_Xtm820_ObjectIdentity = ObjectIdentity
xtm820 = _Xtm820_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 5)
)
_Xtm810_ObjectIdentity = ObjectIdentity
xtm810 = _Xtm810_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 6)
)
_Xtm530_ObjectIdentity = ObjectIdentity
xtm530 = _Xtm530_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 7)
)
_Xtm520_ObjectIdentity = ObjectIdentity
xtm520 = _Xtm520_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 8)
)
_Xtm510_ObjectIdentity = ObjectIdentity
xtm510 = _Xtm510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 9)
)
_Xtm505_ObjectIdentity = ObjectIdentity
xtm505 = _Xtm505_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 10)
)
_Xtm23_ObjectIdentity = ObjectIdentity
xtm23 = _Xtm23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 11)
)
_Xtm22_ObjectIdentity = ObjectIdentity
xtm22 = _Xtm22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 12)
)
_Xtm21_ObjectIdentity = ObjectIdentity
xtm21 = _Xtm21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 13)
)
_Xtm23_W_ObjectIdentity = ObjectIdentity
xtm23_W = _Xtm23_W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 14)
)
_Xtm22_W_ObjectIdentity = ObjectIdentity
xtm22_W = _Xtm22_W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 15)
)
_Xtm21_W_ObjectIdentity = ObjectIdentity
xtm21_W = _Xtm21_W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 16)
)
_Xtm2050_ObjectIdentity = ObjectIdentity
xtm2050 = _Xtm2050_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 17)
)
_Xtm25_ObjectIdentity = ObjectIdentity
xtm25 = _Xtm25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 18)
)
_Xtm25_W_ObjectIdentity = ObjectIdentity
xtm25_W = _Xtm25_W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 19)
)
_Xtm26_ObjectIdentity = ObjectIdentity
xtm26 = _Xtm26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 20)
)
_Xtm26_W_ObjectIdentity = ObjectIdentity
xtm26_W = _Xtm26_W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 21)
)
_Xtm33_ObjectIdentity = ObjectIdentity
xtm33 = _Xtm33_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 22)
)
_Xtm33_W_ObjectIdentity = ObjectIdentity
xtm33_W = _Xtm33_W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 23)
)
_Xtm330_ObjectIdentity = ObjectIdentity
xtm330 = _Xtm330_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 24)
)
_Xtm545_ObjectIdentity = ObjectIdentity
xtm545 = _Xtm545_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 25)
)
_Xtm535_ObjectIdentity = ObjectIdentity
xtm535 = _Xtm535_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 26)
)
_Xtm525_ObjectIdentity = ObjectIdentity
xtm525 = _Xtm525_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 27)
)
_Xtm515_ObjectIdentity = ObjectIdentity
xtm515 = _Xtm515_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 28)
)
_Xtm2050A_ObjectIdentity = ObjectIdentity
xtm2050A = _Xtm2050A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 29)
)
_Xtm850_ObjectIdentity = ObjectIdentity
xtm850 = _Xtm850_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 30)
)
_Xtm860_ObjectIdentity = ObjectIdentity
xtm860 = _Xtm860_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 31)
)
_Xtm870_ObjectIdentity = ObjectIdentity
xtm870 = _Xtm870_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 32)
)
_Xtm870_F_ObjectIdentity = ObjectIdentity
xtm870_F = _Xtm870_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 33)
)
_Xtm1520_ObjectIdentity = ObjectIdentity
xtm1520 = _Xtm1520_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 34)
)
_Xtm1525_ObjectIdentity = ObjectIdentity
xtm1525 = _Xtm1525_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 35)
)
_Xtm2520_ObjectIdentity = ObjectIdentity
xtm2520 = _Xtm2520_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 36)
)
_Xtmv_SM_ObjectIdentity = ObjectIdentity
xtmv_SM = _Xtmv_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 37)
)
_Xtmv_MED_ObjectIdentity = ObjectIdentity
xtmv_MED = _Xtmv_MED_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 38)
)
_Xtmv_LG_ObjectIdentity = ObjectIdentity
xtmv_LG = _Xtmv_LG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 39)
)
_Xtmv_DC_ObjectIdentity = ObjectIdentity
xtmv_DC = _Xtmv_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 40)
)
_Xtmv_EXP_ObjectIdentity = ObjectIdentity
xtmv_EXP = _Xtmv_EXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 41)
)
_Xtmv_ObjectIdentity = ObjectIdentity
xtmv = _Xtmv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 42)
)
_Xtm1520_RP_ObjectIdentity = ObjectIdentity
xtm1520_RP = _Xtm1520_RP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 43)
)
_Xtm1525_RP_ObjectIdentity = ObjectIdentity
xtm1525_RP = _Xtm1525_RP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 44)
)
_T10_ObjectIdentity = ObjectIdentity
T10 = _T10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 45)
)
_M440_ObjectIdentity = ObjectIdentity
M440 = _M440_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 46)
)
_T10_D_ObjectIdentity = ObjectIdentity
T10_D = _T10_D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 47)
)
_T10_W_ObjectIdentity = ObjectIdentity
T10_W = _T10_W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 48)
)
_M400_ObjectIdentity = ObjectIdentity
M400 = _M400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 49)
)
_M500_ObjectIdentity = ObjectIdentity
M500 = _M500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 5, 50)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WATCHGUARD-PRODUCTS-MIB",
    **{"wgProducts": wgProducts,
       "fbXSeries": fbXSeries,
       "fbX500": fbX500,
       "fbX550e": fbX550e,
       "fbX700": fbX700,
       "fbX750e": fbX750e,
       "fbX750e-4": fbX750e_4,
       "fbX1000": fbX1000,
       "fbX1250e": fbX1250e,
       "fbX1250e-4": fbX1250e_4,
       "fbX2500": fbX2500,
       "fbX5000": fbX5000,
       "fbX5500e": fbX5500e,
       "fbX6000": fbX6000,
       "fbX6500e": fbX6500e,
       "fbX8000": fbX8000,
       "fbX8500e": fbX8500e,
       "fbX8500e-F": fbX8500e_F,
       "fbX10e": fbX10e,
       "fbX10e-W": fbX10e_W,
       "fbX20e": fbX20e,
       "fbX20e-W": fbX20e_W,
       "fbX55e": fbX55e,
       "fbX55e-W": fbX55e_W,
       "xtmSeries": xtmSeries,
       "xtm1050": xtm1050,
       "xtm1050-F": xtm1050_F,
       "xtm830-F": xtm830_F,
       "xtm830": xtm830,
       "xtm820": xtm820,
       "xtm810": xtm810,
       "xtm530": xtm530,
       "xtm520": xtm520,
       "xtm510": xtm510,
       "xtm505": xtm505,
       "xtm23": xtm23,
       "xtm22": xtm22,
       "xtm21": xtm21,
       "xtm23-W": xtm23_W,
       "xtm22-W": xtm22_W,
       "xtm21-W": xtm21_W,
       "xtm2050": xtm2050,
       "xtm25": xtm25,
       "xtm25-W": xtm25_W,
       "xtm26": xtm26,
       "xtm26-W": xtm26_W,
       "xtm33": xtm33,
       "xtm33-W": xtm33_W,
       "xtm330": xtm330,
       "xtm545": xtm545,
       "xtm535": xtm535,
       "xtm525": xtm525,
       "xtm515": xtm515,
       "xtm2050A": xtm2050A,
       "xtm850": xtm850,
       "xtm860": xtm860,
       "xtm870": xtm870,
       "xtm870-F": xtm870_F,
       "xtm1520": xtm1520,
       "xtm1525": xtm1525,
       "xtm2520": xtm2520,
       "xtmv-SM": xtmv_SM,
       "xtmv-MED": xtmv_MED,
       "xtmv-LG": xtmv_LG,
       "xtmv-DC": xtmv_DC,
       "xtmv-EXP": xtmv_EXP,
       "xtmv": xtmv,
       "xtm1520-RP": xtm1520_RP,
       "xtm1525-RP": xtm1525_RP,
       "T10": T10,
       "M440": M440,
       "T10-D": T10_D,
       "T10-W": T10_W,
       "M400": M400,
       "M500": M500}
)
