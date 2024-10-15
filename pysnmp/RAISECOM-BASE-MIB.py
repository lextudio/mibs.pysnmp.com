# SNMP MIB module (RAISECOM-BASE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RAISECOM-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:28 2024
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

_Raisecom_ObjectIdentity = ObjectIdentity
raisecom = _Raisecom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886)
)
_RaisecomAgent_ObjectIdentity = ObjectIdentity
raisecomAgent = _RaisecomAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1)
)
_RaisecomCluster_ObjectIdentity = ObjectIdentity
raisecomCluster = _RaisecomCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6)
)
_Rc002_ObjectIdentity = ObjectIdentity
rc002 = _Rc002_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2)
)
_Rc003_ObjectIdentity = ObjectIdentity
rc003 = _Rc003_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 3)
)
_Rc004_ObjectIdentity = ObjectIdentity
rc004 = _Rc004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 4)
)
_Rc701FE_ObjectIdentity = ObjectIdentity
rc701FE = _Rc701FE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 5)
)
_IscomSeries_ObjectIdentity = ObjectIdentity
iscomSeries = _IscomSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6)
)
_IscomSwitch_ObjectIdentity = ObjectIdentity
iscomSwitch = _IscomSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1)
)
_Iscom3026_ObjectIdentity = ObjectIdentity
iscom3026 = _Iscom3026_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 2)
)
_Iscom2826_ObjectIdentity = ObjectIdentity
iscom2826 = _Iscom2826_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 3)
)
_Iscom4124_ObjectIdentity = ObjectIdentity
iscom4124 = _Iscom4124_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 4)
)
_Iscom2126_ObjectIdentity = ObjectIdentity
iscom2126 = _Iscom2126_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 5)
)
_Iscom2016_ObjectIdentity = ObjectIdentity
iscom2016 = _Iscom2016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 6)
)
_Iscom2008_ObjectIdentity = ObjectIdentity
iscom2008 = _Iscom2008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 7)
)
_Iscom4300_ObjectIdentity = ObjectIdentity
iscom4300 = _Iscom4300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 8)
)
_Iscom2026B_ObjectIdentity = ObjectIdentity
iscom2026B = _Iscom2026B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 9)
)
_Iscom2826E_ObjectIdentity = ObjectIdentity
iscom2826E = _Iscom2826E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 10)
)
_Iscom2828F_ObjectIdentity = ObjectIdentity
iscom2828F = _Iscom2828F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 11)
)
_Iscom2812GF_ObjectIdentity = ObjectIdentity
iscom2812GF = _Iscom2812GF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 12)
)
_Iscom2109F_ObjectIdentity = ObjectIdentity
iscom2109F = _Iscom2109F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 13)
)
_Iscom2026_ObjectIdentity = ObjectIdentity
iscom2026 = _Iscom2026_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 14)
)
_Iscom2025_ObjectIdentity = ObjectIdentity
iscom2025 = _Iscom2025_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 15)
)
_Iscom2017_ObjectIdentity = ObjectIdentity
iscom2017 = _Iscom2017_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 16)
)
_Iscom2009_ObjectIdentity = ObjectIdentity
iscom2009 = _Iscom2009_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 17)
)
_Iscom2125_ObjectIdentity = ObjectIdentity
iscom2125 = _Iscom2125_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 18)
)
_Iscom2117_ObjectIdentity = ObjectIdentity
iscom2117 = _Iscom2117_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 19)
)
_Iscom2109_ObjectIdentity = ObjectIdentity
iscom2109 = _Iscom2109_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 20)
)
_Iscom2126e_ObjectIdentity = ObjectIdentity
iscom2126e = _Iscom2126e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 21)
)
_Iscom2852_ObjectIdentity = ObjectIdentity
iscom2852 = _Iscom2852_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 22)
)
_Iscom2126F_ObjectIdentity = ObjectIdentity
iscom2126F = _Iscom2126F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 23)
)
_IscomEpon_ObjectIdentity = ObjectIdentity
iscomEpon = _IscomEpon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 24)
)
_Iscom2924GF_ObjectIdentity = ObjectIdentity
iscom2924GF = _Iscom2924GF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 25)
)
_Iscom2126S_ObjectIdentity = ObjectIdentity
iscom2126S = _Iscom2126S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 26)
)
_Iscom5504_ObjectIdentity = ObjectIdentity
iscom5504 = _Iscom5504_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 27)
)
_Iscom2009A_ObjectIdentity = ObjectIdentity
iscom2009A = _Iscom2009A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 28)
)
_Iscom2109A_ObjectIdentity = ObjectIdentity
iscom2109A = _Iscom2109A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 29)
)
_Iscom2926_ObjectIdentity = ObjectIdentity
iscom2926 = _Iscom2926_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 30)
)
_Iscom2926F_ObjectIdentity = ObjectIdentity
iscom2926F = _Iscom2926F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 31)
)
_Iscom2017A_ObjectIdentity = ObjectIdentity
iscom2017A = _Iscom2017A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 32)
)
_Iscom3012GF_ObjectIdentity = ObjectIdentity
iscom3012GF = _Iscom3012GF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 33)
)
_Iscom2016C_ObjectIdentity = ObjectIdentity
iscom2016C = _Iscom2016C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 34)
)
_Iscom3026E_ObjectIdentity = ObjectIdentity
iscom3026E = _Iscom3026E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 35)
)
_Iscom3028F_ObjectIdentity = ObjectIdentity
iscom3028F = _Iscom3028F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 36)
)
_Iscom3052_ObjectIdentity = ObjectIdentity
iscom3052 = _Iscom3052_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 37)
)
_Iscom5124_ObjectIdentity = ObjectIdentity
iscom5124 = _Iscom5124_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 38)
)
_Iscom2150_MA_ObjectIdentity = ObjectIdentity
iscom2150_MA = _Iscom2150_MA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 39)
)
_Iscom2118_ObjectIdentity = ObjectIdentity
iscom2118 = _Iscom2118_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 40)
)
_Iscom2828_ObjectIdentity = ObjectIdentity
iscom2828 = _Iscom2828_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 44)
)
_Iscom2109_MA_ObjectIdentity = ObjectIdentity
iscom2109_MA = _Iscom2109_MA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 45)
)
_Iscom2109A_MA_ObjectIdentity = ObjectIdentity
iscom2109A_MA = _Iscom2109A_MA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 46)
)
_Iscom2118_MA_ObjectIdentity = ObjectIdentity
iscom2118_MA = _Iscom2118_MA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 47)
)
_Iscom2126S_MA_ObjectIdentity = ObjectIdentity
iscom2126S_MA = _Iscom2126S_MA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 48)
)
_Iscom2126E_MA_ObjectIdentity = ObjectIdentity
iscom2126E_MA = _Iscom2126E_MA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 50)
)
_Iscom2126F_MA_ObjectIdentity = ObjectIdentity
iscom2126F_MA = _Iscom2126F_MA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 51)
)
_Iscom2126FL_MA_ObjectIdentity = ObjectIdentity
iscom2126FL_MA = _Iscom2126FL_MA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 52)
)
_Iscom2017S_ObjectIdentity = ObjectIdentity
iscom2017S = _Iscom2017S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 53)
)
_Iscom2126EA_MA_ObjectIdentity = ObjectIdentity
iscom2126EA_MA = _Iscom2126EA_MA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 54)
)
_Iscom2110A_MA_ObjectIdentity = ObjectIdentity
iscom2110A_MA = _Iscom2110A_MA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 55)
)
_Iscom2009A_MA_ObjectIdentity = ObjectIdentity
iscom2009A_MA = _Iscom2009A_MA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 56)
)
_Iscom2824G_ObjectIdentity = ObjectIdentity
iscom2824G = _Iscom2824G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 57)
)
_Iscom2110A_MA_PWR4_ObjectIdentity = ObjectIdentity
iscom2110A_MA_PWR4 = _Iscom2110A_MA_PWR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 58)
)
_Iscom2828F_C_ObjectIdentity = ObjectIdentity
iscom2828F_C = _Iscom2828F_C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 62)
)
_Iscom2828_MA_ObjectIdentity = ObjectIdentity
iscom2828_MA = _Iscom2828_MA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 63)
)
_OpcomSeries_ObjectIdentity = ObjectIdentity
opcomSeries = _OpcomSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 7)
)
_Opcom3100_ObjectIdentity = ObjectIdentity
opcom3100 = _Opcom3100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 7, 1)
)
_Opcom100_4_ObjectIdentity = ObjectIdentity
opcom100_4 = _Opcom100_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 7, 2)
)
_Opcom3500_ObjectIdentity = ObjectIdentity
opcom3500 = _Opcom3500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 7, 3)
)
_Opcom3101_ObjectIdentity = ObjectIdentity
opcom3101 = _Opcom3101_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 7, 4)
)
_Opcom3102_ObjectIdentity = ObjectIdentity
opcom3102 = _Opcom3102_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 7, 5)
)
_Opcom3103_ObjectIdentity = ObjectIdentity
opcom3103 = _Opcom3103_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 7, 6)
)
_Opcom100_2c_ObjectIdentity = ObjectIdentity
opcom100_2c = _Opcom100_2c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 7, 7)
)
_Opcom3500e_ObjectIdentity = ObjectIdentity
opcom3500e = _Opcom3500e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 7, 8)
)
_Opcom3500e_6_ObjectIdentity = ObjectIdentity
opcom3500e_6 = _Opcom3500e_6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 7, 9)
)
_Opcom3105_ObjectIdentity = ObjectIdentity
opcom3105 = _Opcom3105_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 7, 10)
)
_Opcom3107_ObjectIdentity = ObjectIdentity
opcom3107 = _Opcom3107_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 7, 11)
)
_Opcom3109_ObjectIdentity = ObjectIdentity
opcom3109 = _Opcom3109_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 7, 12)
)
_Opcom_100_oau_ObjectIdentity = ObjectIdentity
opcom_100_oau = _Opcom_100_oau_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 7, 15)
)
_Opcom3500e_c_ObjectIdentity = ObjectIdentity
opcom3500e_c = _Opcom3500e_c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 7, 16)
)
_RaisecomManager_ObjectIdentity = ObjectIdentity
raisecomManager = _RaisecomManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 8)
)
_IscomPM_ObjectIdentity = ObjectIdentity
iscomPM = _IscomPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 8, 1)
)
_PcAgent_ObjectIdentity = ObjectIdentity
pcAgent = _PcAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 9)
)
_PccomSeries_ObjectIdentity = ObjectIdentity
pccomSeries = _PccomSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 10)
)
_OemSeries_ObjectIdentity = ObjectIdentity
oemSeries = _OemSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 11)
)
_Iscom3408_ObjectIdentity = ObjectIdentity
iscom3408 = _Iscom3408_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 11, 1)
)
_RcSeries_ObjectIdentity = ObjectIdentity
rcSeries = _RcSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12)
)
_Rc951_ObjectIdentity = ObjectIdentity
rc951 = _Rc951_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 1)
)
_Rc957_ObjectIdentity = ObjectIdentity
rc957 = _Rc957_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 2)
)
_Rc952_ObjectIdentity = ObjectIdentity
rc952 = _Rc952_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 3)
)
_Opticaltransceiver_ObjectIdentity = ObjectIdentity
opticaltransceiver = _Opticaltransceiver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 4)
)
_Rc006_ObjectIdentity = ObjectIdentity
rc006 = _Rc006_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 5)
)
_Rc702_ObjectIdentity = ObjectIdentity
rc702 = _Rc702_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 6)
)
_Rc702c_ObjectIdentity = ObjectIdentity
rc702c = _Rc702c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 7)
)
_Rc006_1_ObjectIdentity = ObjectIdentity
rc006_1 = _Rc006_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 8)
)
_Rc953_gestm1_ObjectIdentity = ObjectIdentity
rc953_gestm1 = _Rc953_gestm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 9)
)
_Rc953e_3fe16e1_ObjectIdentity = ObjectIdentity
rc953e_3fe16e1 = _Rc953e_3fe16e1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 10)
)
_Rc3000_15_ObjectIdentity = ObjectIdentity
rc3000_15 = _Rc3000_15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 11)
)
_Rc953e_gestm1_ObjectIdentity = ObjectIdentity
rc953e_gestm1 = _Rc953e_gestm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 12)
)
_Rc959_4fe16e1_ObjectIdentity = ObjectIdentity
rc959_4fe16e1 = _Rc959_4fe16e1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 13)
)
_Rc702_gestm4_ObjectIdentity = ObjectIdentity
rc702_gestm4 = _Rc702_gestm4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 14)
)
_Rc702gestm4_ObjectIdentity = ObjectIdentity
rc702gestm4 = _Rc702gestm4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 15)
)
_Rc702d_ObjectIdentity = ObjectIdentity
rc702d = _Rc702d_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 16)
)
_Rc006_6_ObjectIdentity = ObjectIdentity
rc006_6 = _Rc006_6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 17)
)
_Rc959_gestm1_ObjectIdentity = ObjectIdentity
rc959_gestm1 = _Rc959_gestm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 18)
)
_Rc3000_6_ObjectIdentity = ObjectIdentity
rc3000_6 = _Rc3000_6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 19)
)
_Rc552_ge_ObjectIdentity = ObjectIdentity
rc552_ge = _Rc552_ge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 20)
)
_Rc006_3m_s_ObjectIdentity = ObjectIdentity
rc006_3m_s = _Rc006_3m_s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 21)
)
_Rc3000e_ObjectIdentity = ObjectIdentity
rc3000e = _Rc3000e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 22)
)
_Rc953_4fexe1t1_ObjectIdentity = ObjectIdentity
rc953_4fexe1t1 = _Rc953_4fexe1t1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 23)
)
_Rc905g_4fe16e1_ObjectIdentity = ObjectIdentity
rc905g_4fe16e1 = _Rc905g_4fe16e1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 24)
)
_Rc905g_gestm1_ObjectIdentity = ObjectIdentity
rc905g_gestm1 = _Rc905g_gestm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 25)
)
_Rc953eb_gestm1_ObjectIdentity = ObjectIdentity
rc953eb_gestm1 = _Rc953eb_gestm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 26)
)
_Rc953_4fe8e1t1bl_ObjectIdentity = ObjectIdentity
rc953_4fe8e1t1bl = _Rc953_4fe8e1t1bl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 27)
)
_Rc953_4fe4e1t1bl_ObjectIdentity = ObjectIdentity
rc953_4fe4e1t1bl = _Rc953_4fe4e1t1bl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 28)
)
_Rc953_4fe8e1_ObjectIdentity = ObjectIdentity
rc953_4fe8e1 = _Rc953_4fe8e1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 29)
)
_Rc953_4fe4e1_ObjectIdentity = ObjectIdentity
rc953_4fe4e1 = _Rc953_4fe4e1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 30)
)
_Rc951e_4fee1_ObjectIdentity = ObjectIdentity
rc951e_4fee1 = _Rc951e_4fee1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 31)
)
_Rc1106e_fe_2wx4_ObjectIdentity = ObjectIdentity
rc1106e_fe_2wx4 = _Rc1106e_fe_2wx4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 32)
)
_Rc1106e_fe_2wx8_ObjectIdentity = ObjectIdentity
rc1106e_fe_2wx8 = _Rc1106e_fe_2wx8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12, 33)
)
_RaisecomOptSysCommon_ObjectIdentity = ObjectIdentity
raisecomOptSysCommon = _RaisecomOptSysCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 15)
)
_OptSysMgmt_ObjectIdentity = ObjectIdentity
optSysMgmt = _OptSysMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1)
)
_OptSysModules_ObjectIdentity = ObjectIdentity
optSysModules = _OptSysModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 15, 2)
)
_OptAgentCapability_ObjectIdentity = ObjectIdentity
optAgentCapability = _OptAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 15, 3)
)
_OptUdSysMgmt_ObjectIdentity = ObjectIdentity
optUdSysMgmt = _OptUdSysMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 15, 4)
)
_OptUdSysModules_ObjectIdentity = ObjectIdentity
optUdSysModules = _OptUdSysModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 15, 5)
)
_RosliteSeries_ObjectIdentity = ObjectIdentity
rosliteSeries = _RosliteSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 16)
)
_IscomMediaConvertor_ObjectIdentity = ObjectIdentity
iscomMediaConvertor = _IscomMediaConvertor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1)
)
_Rc581FE_ObjectIdentity = ObjectIdentity
rc581FE = _Rc581FE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 16, 2)
)
_Rc581GE_ObjectIdentity = ObjectIdentity
rc581GE = _Rc581GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 16, 3)
)
_Rc551_FE_ObjectIdentity = ObjectIdentity
rc551_FE = _Rc551_FE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 16, 4)
)
_Rc551_GE_ObjectIdentity = ObjectIdentity
rc551_GE = _Rc551_GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 16, 5)
)
_Rc551_4FE_ObjectIdentity = ObjectIdentity
rc551_4FE = _Rc551_4FE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 16, 6)
)
_Rc551B_FE_ObjectIdentity = ObjectIdentity
rc551B_FE = _Rc551B_FE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 16, 7)
)
_Rc551B_GE_ObjectIdentity = ObjectIdentity
rc551B_GE = _Rc551B_GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 16, 8)
)
_Rc551B_4FE_ObjectIdentity = ObjectIdentity
rc551B_4FE = _Rc551B_4FE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 16, 9)
)
_Rc551B_GE4FE_ObjectIdentity = ObjectIdentity
rc551B_GE4FE = _Rc551B_GE4FE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 16, 10)
)
_Rc551E_4GE_ObjectIdentity = ObjectIdentity
rc551E_4GE = _Rc551E_4GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 16, 11)
)
_Rc551E_GE_ObjectIdentity = ObjectIdentity
rc551E_GE = _Rc551E_GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 16, 12)
)
_Rc551E_4GEF_ObjectIdentity = ObjectIdentity
rc551E_4GEF = _Rc551E_4GEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 16, 13)
)
_Draft_ObjectIdentity = ObjectIdentity
draft = _Draft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 17)
)
_Oam_ObjectIdentity = ObjectIdentity
oam = _Oam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 17, 1)
)
_Epon_ObjectIdentity = ObjectIdentity
epon = _Epon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 17, 2)
)
_PonSeries_ObjectIdentity = ObjectIdentity
ponSeries = _PonSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18)
)
_TdmopSeries_ObjectIdentity = ObjectIdentity
tdmopSeries = _TdmopSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 19)
)
_DlcomSeries_ObjectIdentity = ObjectIdentity
dlcomSeries = _DlcomSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 20)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-BASE-MIB",
    **{"raisecom": raisecom,
       "raisecomAgent": raisecomAgent,
       "raisecomCluster": raisecomCluster,
       "rc002": rc002,
       "rc003": rc003,
       "rc004": rc004,
       "rc701FE": rc701FE,
       "iscomSeries": iscomSeries,
       "iscomSwitch": iscomSwitch,
       "iscom3026": iscom3026,
       "iscom2826": iscom2826,
       "iscom4124": iscom4124,
       "iscom2126": iscom2126,
       "iscom2016": iscom2016,
       "iscom2008": iscom2008,
       "iscom4300": iscom4300,
       "iscom2026B": iscom2026B,
       "iscom2826E": iscom2826E,
       "iscom2828F": iscom2828F,
       "iscom2812GF": iscom2812GF,
       "iscom2109F": iscom2109F,
       "iscom2026": iscom2026,
       "iscom2025": iscom2025,
       "iscom2017": iscom2017,
       "iscom2009": iscom2009,
       "iscom2125": iscom2125,
       "iscom2117": iscom2117,
       "iscom2109": iscom2109,
       "iscom2126e": iscom2126e,
       "iscom2852": iscom2852,
       "iscom2126F": iscom2126F,
       "iscomEpon": iscomEpon,
       "iscom2924GF": iscom2924GF,
       "iscom2126S": iscom2126S,
       "iscom5504": iscom5504,
       "iscom2009A": iscom2009A,
       "iscom2109A": iscom2109A,
       "iscom2926": iscom2926,
       "iscom2926F": iscom2926F,
       "iscom2017A": iscom2017A,
       "iscom3012GF": iscom3012GF,
       "iscom2016C": iscom2016C,
       "iscom3026E": iscom3026E,
       "iscom3028F": iscom3028F,
       "iscom3052": iscom3052,
       "iscom5124": iscom5124,
       "iscom2150-MA": iscom2150_MA,
       "iscom2118": iscom2118,
       "iscom2828": iscom2828,
       "iscom2109-MA": iscom2109_MA,
       "iscom2109A-MA": iscom2109A_MA,
       "iscom2118-MA": iscom2118_MA,
       "iscom2126S-MA": iscom2126S_MA,
       "iscom2126E-MA": iscom2126E_MA,
       "iscom2126F-MA": iscom2126F_MA,
       "iscom2126FL-MA": iscom2126FL_MA,
       "iscom2017S": iscom2017S,
       "iscom2126EA-MA": iscom2126EA_MA,
       "iscom2110A-MA": iscom2110A_MA,
       "iscom2009A-MA": iscom2009A_MA,
       "iscom2824G": iscom2824G,
       "iscom2110A-MA-PWR4": iscom2110A_MA_PWR4,
       "iscom2828F-C": iscom2828F_C,
       "iscom2828-MA": iscom2828_MA,
       "opcomSeries": opcomSeries,
       "opcom3100": opcom3100,
       "opcom100-4": opcom100_4,
       "opcom3500": opcom3500,
       "opcom3101": opcom3101,
       "opcom3102": opcom3102,
       "opcom3103": opcom3103,
       "opcom100-2c": opcom100_2c,
       "opcom3500e": opcom3500e,
       "opcom3500e-6": opcom3500e_6,
       "opcom3105": opcom3105,
       "opcom3107": opcom3107,
       "opcom3109": opcom3109,
       "opcom-100-oau": opcom_100_oau,
       "opcom3500e-c": opcom3500e_c,
       "raisecomManager": raisecomManager,
       "iscomPM": iscomPM,
       "pcAgent": pcAgent,
       "pccomSeries": pccomSeries,
       "oemSeries": oemSeries,
       "iscom3408": iscom3408,
       "rcSeries": rcSeries,
       "rc951": rc951,
       "rc957": rc957,
       "rc952": rc952,
       "opticaltransceiver": opticaltransceiver,
       "rc006": rc006,
       "rc702": rc702,
       "rc702c": rc702c,
       "rc006-1": rc006_1,
       "rc953-gestm1": rc953_gestm1,
       "rc953e-3fe16e1": rc953e_3fe16e1,
       "rc3000-15": rc3000_15,
       "rc953e-gestm1": rc953e_gestm1,
       "rc959-4fe16e1": rc959_4fe16e1,
       "rc702-gestm4": rc702_gestm4,
       "rc702gestm4": rc702gestm4,
       "rc702d": rc702d,
       "rc006-6": rc006_6,
       "rc959-gestm1": rc959_gestm1,
       "rc3000-6": rc3000_6,
       "rc552-ge": rc552_ge,
       "rc006-3m-s": rc006_3m_s,
       "rc3000e": rc3000e,
       "rc953-4fexe1t1": rc953_4fexe1t1,
       "rc905g-4fe16e1": rc905g_4fe16e1,
       "rc905g-gestm1": rc905g_gestm1,
       "rc953eb-gestm1": rc953eb_gestm1,
       "rc953-4fe8e1t1bl": rc953_4fe8e1t1bl,
       "rc953-4fe4e1t1bl": rc953_4fe4e1t1bl,
       "rc953-4fe8e1": rc953_4fe8e1,
       "rc953-4fe4e1": rc953_4fe4e1,
       "rc951e-4fee1": rc951e_4fee1,
       "rc1106e-fe-2wx4": rc1106e_fe_2wx4,
       "rc1106e-fe-2wx8": rc1106e_fe_2wx8,
       "raisecomOptSysCommon": raisecomOptSysCommon,
       "optSysMgmt": optSysMgmt,
       "optSysModules": optSysModules,
       "optAgentCapability": optAgentCapability,
       "optUdSysMgmt": optUdSysMgmt,
       "optUdSysModules": optUdSysModules,
       "rosliteSeries": rosliteSeries,
       "iscomMediaConvertor": iscomMediaConvertor,
       "rc581FE": rc581FE,
       "rc581GE": rc581GE,
       "rc551-FE": rc551_FE,
       "rc551-GE": rc551_GE,
       "rc551-4FE": rc551_4FE,
       "rc551B-FE": rc551B_FE,
       "rc551B-GE": rc551B_GE,
       "rc551B-4FE": rc551B_4FE,
       "rc551B-GE4FE": rc551B_GE4FE,
       "rc551E-4GE": rc551E_4GE,
       "rc551E-GE": rc551E_GE,
       "rc551E-4GEF": rc551E_4GEF,
       "draft": draft,
       "oam": oam,
       "epon": epon,
       "ponSeries": ponSeries,
       "tdmopSeries": tdmopSeries,
       "dlcomSeries": dlcomSeries}
)
