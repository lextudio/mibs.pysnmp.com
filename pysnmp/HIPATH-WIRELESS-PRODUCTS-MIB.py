# SNMP MIB module (HIPATH-WIRELESS-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HIPATH-WIRELESS-PRODUCTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:31 2024
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

(hiPathWirelessModules,
 hiPathWirelessProducts) = mibBuilder.importSymbols(
    "HIPATH-WIRELESS-SMI",
    "hiPathWirelessModules",
    "hiPathWirelessProducts")

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

hiPathWirelessProductsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 5, 1)
)
hiPathWirelessProductsMIB.setRevisions(
        ("2016-08-05 15:56",
         "2016-07-19 22:21",
         "2016-02-23 18:26",
         "2015-09-21 12:02",
         "2015-08-13 11:02",
         "2014-11-06 16:54",
         "2014-10-28 16:00",
         "2014-06-30 15:55",
         "2014-04-03 15:53",
         "2013-11-12 15:53",
         "2013-11-06 14:45",
         "2013-03-06 15:53",
         "2012-08-20 15:53",
         "2012-06-19 11:06",
         "2012-02-13 15:33",
         "2011-07-14 13:45",
         "2011-04-25 14:20",
         "2011-01-13 11:10",
         "2010-04-29 17:44",
         "2009-01-20 15:43",
         "2008-11-19 10:21",
         "2007-08-07 13:57",
         "2006-09-11 18:03",
         "2005-07-21 14:50")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Control_ObjectIdentity = ObjectIdentity
control = _Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 1)
)
_C10_ObjectIdentity = ObjectIdentity
c10 = _C10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 1)
)
if mibBuilder.loadTexts:
    c10.setStatus("current")
_C100_ObjectIdentity = ObjectIdentity
c100 = _C100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 2)
)
if mibBuilder.loadTexts:
    c100.setStatus("current")
_C1000_ObjectIdentity = ObjectIdentity
c1000 = _C1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 3)
)
if mibBuilder.loadTexts:
    c1000.setStatus("current")
_HiPathWirelessManager_ObjectIdentity = ObjectIdentity
hiPathWirelessManager = _HiPathWirelessManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hiPathWirelessManager.setStatus("current")
_C2000_ObjectIdentity = ObjectIdentity
c2000 = _C2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 5)
)
if mibBuilder.loadTexts:
    c2000.setStatus("current")
_C20_ObjectIdentity = ObjectIdentity
c20 = _C20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 6)
)
if mibBuilder.loadTexts:
    c20.setStatus("current")
_C20N_ObjectIdentity = ObjectIdentity
c20N = _C20N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 7)
)
if mibBuilder.loadTexts:
    c20N.setStatus("current")
_Crbt8110_ObjectIdentity = ObjectIdentity
crbt8110 = _Crbt8110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 8)
)
if mibBuilder.loadTexts:
    crbt8110.setStatus("current")
_Crbt8210_ObjectIdentity = ObjectIdentity
crbt8210 = _Crbt8210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 9)
)
if mibBuilder.loadTexts:
    crbt8210.setStatus("current")
_C5110_ObjectIdentity = ObjectIdentity
c5110 = _C5110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 10)
)
if mibBuilder.loadTexts:
    c5110.setStatus("current")
_C4110_ObjectIdentity = ObjectIdentity
c4110 = _C4110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 11)
)
if mibBuilder.loadTexts:
    c4110.setStatus("current")
_C25_ObjectIdentity = ObjectIdentity
c25 = _C25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 12)
)
if mibBuilder.loadTexts:
    c25.setStatus("current")
_V2110_ObjectIdentity = ObjectIdentity
v2110 = _V2110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 13)
)
if mibBuilder.loadTexts:
    v2110.setStatus("current")
_C5210_ObjectIdentity = ObjectIdentity
c5210 = _C5210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 14)
)
if mibBuilder.loadTexts:
    c5210.setStatus("current")
_V2110H_ObjectIdentity = ObjectIdentity
v2110H = _V2110H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 15)
)
if mibBuilder.loadTexts:
    v2110H.setStatus("current")
_C35_ObjectIdentity = ObjectIdentity
c35 = _C35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 17)
)
if mibBuilder.loadTexts:
    c35.setStatus("current")
_Access_ObjectIdentity = ObjectIdentity
access = _Access_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2)
)
_Ap26xx_ObjectIdentity = ObjectIdentity
ap26xx = _Ap26xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ap26xx.setStatus("current")
_Ap2600_ObjectIdentity = ObjectIdentity
ap2600 = _Ap2600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ap2600.setStatus("current")
_Ap2650_ObjectIdentity = ObjectIdentity
ap2650 = _Ap2650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ap2650.setStatus("current")
_ApW786_ObjectIdentity = ObjectIdentity
apW786 = _ApW786_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 5)
)
if mibBuilder.loadTexts:
    apW786.setStatus("current")
_ApW788_ObjectIdentity = ObjectIdentity
apW788 = _ApW788_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 6)
)
if mibBuilder.loadTexts:
    apW788.setStatus("current")
_Ap3610_ObjectIdentity = ObjectIdentity
ap3610 = _Ap3610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 7)
)
if mibBuilder.loadTexts:
    ap3610.setStatus("current")
_Ap2605_ObjectIdentity = ObjectIdentity
ap2605 = _Ap2605_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 8)
)
if mibBuilder.loadTexts:
    ap2605.setStatus("current")
_Ap3630_ObjectIdentity = ObjectIdentity
ap3630 = _Ap3630_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 9)
)
if mibBuilder.loadTexts:
    ap3630.setStatus("current")
_Ap3640_ObjectIdentity = ObjectIdentity
ap3640 = _Ap3640_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 10)
)
if mibBuilder.loadTexts:
    ap3640.setStatus("current")
_Ap2650Rev1_ObjectIdentity = ObjectIdentity
ap2650Rev1 = _Ap2650Rev1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 11)
)
if mibBuilder.loadTexts:
    ap2650Rev1.setStatus("current")
_ApW786Rev1_ObjectIdentity = ObjectIdentity
apW786Rev1 = _ApW786Rev1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 12)
)
if mibBuilder.loadTexts:
    apW786Rev1.setStatus("current")
_Ap4102_ObjectIdentity = ObjectIdentity
ap4102 = _Ap4102_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 13)
)
if mibBuilder.loadTexts:
    ap4102.setStatus("current")
_Ap4102c_ObjectIdentity = ObjectIdentity
ap4102c = _Ap4102c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 14)
)
if mibBuilder.loadTexts:
    ap4102c.setStatus("current")
_Ap4102RevEU_ObjectIdentity = ObjectIdentity
ap4102RevEU = _Ap4102RevEU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 15)
)
if mibBuilder.loadTexts:
    ap4102RevEU.setStatus("current")
_Ap4102cRevEU_ObjectIdentity = ObjectIdentity
ap4102cRevEU = _Ap4102cRevEU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 16)
)
if mibBuilder.loadTexts:
    ap4102cRevEU.setStatus("current")
_Ap2600Rev1_ObjectIdentity = ObjectIdentity
ap2600Rev1 = _Ap2600Rev1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 17)
)
if mibBuilder.loadTexts:
    ap2600Rev1.setStatus("current")
_Ap3600Rev1_ObjectIdentity = ObjectIdentity
ap3600Rev1 = _Ap3600Rev1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 18)
)
if mibBuilder.loadTexts:
    ap3600Rev1.setStatus("current")
_Ap2650Rev2_ObjectIdentity = ObjectIdentity
ap2650Rev2 = _Ap2650Rev2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 19)
)
if mibBuilder.loadTexts:
    ap2650Rev2.setStatus("current")
_ApW786Rev2_ObjectIdentity = ObjectIdentity
apW786Rev2 = _ApW786Rev2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 20)
)
if mibBuilder.loadTexts:
    apW786Rev2.setStatus("current")
_Ap3600_ObjectIdentity = ObjectIdentity
ap3600 = _Ap3600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 21)
)
if mibBuilder.loadTexts:
    ap3600.setStatus("current")
_Ap3605_ObjectIdentity = ObjectIdentity
ap3605 = _Ap3605_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 22)
)
if mibBuilder.loadTexts:
    ap3605.setStatus("current")
_Ap3660_ObjectIdentity = ObjectIdentity
ap3660 = _Ap3660_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 23)
)
if mibBuilder.loadTexts:
    ap3660.setStatus("current")
_Ap2660Rev2_ObjectIdentity = ObjectIdentity
ap2660Rev2 = _Ap2660Rev2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 24)
)
if mibBuilder.loadTexts:
    ap2660Rev2.setStatus("current")
_ApW786Rev2PROe2_ObjectIdentity = ObjectIdentity
apW786Rev2PROe2 = _ApW786Rev2PROe2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 25)
)
if mibBuilder.loadTexts:
    apW786Rev2PROe2.setStatus("current")
_ApW786Rev2PROeFO2_ObjectIdentity = ObjectIdentity
apW786Rev2PROeFO2 = _ApW786Rev2PROeFO2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 26)
)
if mibBuilder.loadTexts:
    apW786Rev2PROeFO2.setStatus("current")
_ApW786Rev2PROiFO2_ObjectIdentity = ObjectIdentity
apW786Rev2PROiFO2 = _ApW786Rev2PROiFO2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 27)
)
if mibBuilder.loadTexts:
    apW786Rev2PROiFO2.setStatus("current")
_Ap3630NAMInternal_ObjectIdentity = ObjectIdentity
ap3630NAMInternal = _Ap3630NAMInternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 28)
)
if mibBuilder.loadTexts:
    ap3630NAMInternal.setStatus("current")
_Ap3640NAMExternal_ObjectIdentity = ObjectIdentity
ap3640NAMExternal = _Ap3640NAMExternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 29)
)
if mibBuilder.loadTexts:
    ap3640NAMExternal.setStatus("current")
_Ap3630ROWInternal_ObjectIdentity = ObjectIdentity
ap3630ROWInternal = _Ap3630ROWInternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 30)
)
if mibBuilder.loadTexts:
    ap3630ROWInternal.setStatus("current")
_Ap3640ROWExternal_ObjectIdentity = ObjectIdentity
ap3640ROWExternal = _Ap3640ROWExternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 31)
)
if mibBuilder.loadTexts:
    ap3640ROWExternal.setStatus("current")
_Ap3630ILInternal_ObjectIdentity = ObjectIdentity
ap3630ILInternal = _Ap3630ILInternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 32)
)
if mibBuilder.loadTexts:
    ap3630ILInternal.setStatus("current")
_Ap3640ILExternal_ObjectIdentity = ObjectIdentity
ap3640ILExternal = _Ap3640ILExternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 33)
)
if mibBuilder.loadTexts:
    ap3640ILExternal.setStatus("current")
_ApW786C2RJ45_ObjectIdentity = ObjectIdentity
apW786C2RJ45 = _ApW786C2RJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 34)
)
if mibBuilder.loadTexts:
    apW786C2RJ45.setStatus("current")
_ApW786C2IARJ45_ObjectIdentity = ObjectIdentity
apW786C2IARJ45 = _ApW786C2IARJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 35)
)
if mibBuilder.loadTexts:
    apW786C2IARJ45.setStatus("current")
_ApW788C2RJ45_ObjectIdentity = ObjectIdentity
apW788C2RJ45 = _ApW788C2RJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 36)
)
if mibBuilder.loadTexts:
    apW788C2RJ45.setStatus("current")
_ApW788C2M12_ObjectIdentity = ObjectIdentity
apW788C2M12 = _ApW788C2M12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 37)
)
if mibBuilder.loadTexts:
    apW788C2M12.setStatus("current")
_Ap3705_ObjectIdentity = ObjectIdentity
ap3705 = _Ap3705_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 38)
)
if mibBuilder.loadTexts:
    ap3705.setStatus("obsolete")
_Ap3765i_ObjectIdentity = ObjectIdentity
ap3765i = _Ap3765i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 39)
)
if mibBuilder.loadTexts:
    ap3765i.setStatus("current")
_Ap3660Rev1_ObjectIdentity = ObjectIdentity
ap3660Rev1 = _Ap3660Rev1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 40)
)
if mibBuilder.loadTexts:
    ap3660Rev1.setStatus("current")
_Ap3765e_ObjectIdentity = ObjectIdentity
ap3765e = _Ap3765e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 41)
)
if mibBuilder.loadTexts:
    ap3765e.setStatus("current")
_Ap3767e_ObjectIdentity = ObjectIdentity
ap3767e = _Ap3767e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 42)
)
if mibBuilder.loadTexts:
    ap3767e.setStatus("current")
_Ap3705i_ObjectIdentity = ObjectIdentity
ap3705i = _Ap3705i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 43)
)
if mibBuilder.loadTexts:
    ap3705i.setStatus("current")
_Ap3710i_ObjectIdentity = ObjectIdentity
ap3710i = _Ap3710i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 44)
)
if mibBuilder.loadTexts:
    ap3710i.setStatus("current")
_Ap3710e_ObjectIdentity = ObjectIdentity
ap3710e = _Ap3710e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 45)
)
if mibBuilder.loadTexts:
    ap3710e.setStatus("current")
_Ap3725i_ObjectIdentity = ObjectIdentity
ap3725i = _Ap3725i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 46)
)
if mibBuilder.loadTexts:
    ap3725i.setStatus("current")
_Ap3725e_ObjectIdentity = ObjectIdentity
ap3725e = _Ap3725e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 47)
)
if mibBuilder.loadTexts:
    ap3725e.setStatus("current")
_Ap3715i_ObjectIdentity = ObjectIdentity
ap3715i = _Ap3715i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 48)
)
if mibBuilder.loadTexts:
    ap3715i.setStatus("current")
_Ap3715e_ObjectIdentity = ObjectIdentity
ap3715e = _Ap3715e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 49)
)
if mibBuilder.loadTexts:
    ap3715e.setStatus("current")
_Ap3630ROW1i_ObjectIdentity = ObjectIdentity
ap3630ROW1i = _Ap3630ROW1i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 50)
)
if mibBuilder.loadTexts:
    ap3630ROW1i.setStatus("current")
_Ap3640ROW1e_ObjectIdentity = ObjectIdentity
ap3640ROW1e = _Ap3640ROW1e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 51)
)
if mibBuilder.loadTexts:
    ap3640ROW1e.setStatus("current")
_Ap3715i_1_ObjectIdentity = ObjectIdentity
ap3715i_1 = _Ap3715i_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 52)
)
if mibBuilder.loadTexts:
    ap3715i_1.setStatus("current")
_Ap3825i_ObjectIdentity = ObjectIdentity
ap3825i = _Ap3825i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 53)
)
if mibBuilder.loadTexts:
    ap3825i.setStatus("current")
_Ap3825e_ObjectIdentity = ObjectIdentity
ap3825e = _Ap3825e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 54)
)
if mibBuilder.loadTexts:
    ap3825e.setStatus("current")
_Ap3865e_ObjectIdentity = ObjectIdentity
ap3865e = _Ap3865e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 55)
)
if mibBuilder.loadTexts:
    ap3865e.setStatus("current")
_Ap3805i_ObjectIdentity = ObjectIdentity
ap3805i = _Ap3805i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 56)
)
if mibBuilder.loadTexts:
    ap3805i.setStatus("current")
_Ap3805e_ObjectIdentity = ObjectIdentity
ap3805e = _Ap3805e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 57)
)
if mibBuilder.loadTexts:
    ap3805e.setStatus("current")
_Ap3801i_ObjectIdentity = ObjectIdentity
ap3801i = _Ap3801i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 58)
)
if mibBuilder.loadTexts:
    ap3801i.setStatus("current")
_Ap3935FCCe_ObjectIdentity = ObjectIdentity
ap3935FCCe = _Ap3935FCCe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 59)
)
if mibBuilder.loadTexts:
    ap3935FCCe.setStatus("current")
_Ap3965FCCe_ObjectIdentity = ObjectIdentity
ap3965FCCe = _Ap3965FCCe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 60)
)
if mibBuilder.loadTexts:
    ap3965FCCe.setStatus("current")
_Ap3935ROWe_ObjectIdentity = ObjectIdentity
ap3935ROWe = _Ap3935ROWe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 61)
)
if mibBuilder.loadTexts:
    ap3935ROWe.setStatus("current")
_Ap3965ROWe_ObjectIdentity = ObjectIdentity
ap3965ROWe = _Ap3965ROWe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 62)
)
if mibBuilder.loadTexts:
    ap3965ROWe.setStatus("current")
_Ap3935FCCi_ObjectIdentity = ObjectIdentity
ap3935FCCi = _Ap3935FCCi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 63)
)
if mibBuilder.loadTexts:
    ap3935FCCi.setStatus("current")
_Ap3965FCCi_ObjectIdentity = ObjectIdentity
ap3965FCCi = _Ap3965FCCi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 64)
)
if mibBuilder.loadTexts:
    ap3965FCCi.setStatus("current")
_Ap3935ROWi_ObjectIdentity = ObjectIdentity
ap3935ROWi = _Ap3935ROWi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 65)
)
if mibBuilder.loadTexts:
    ap3935ROWi.setStatus("current")
_Ap3965ROWi_ObjectIdentity = ObjectIdentity
ap3965ROWi = _Ap3965ROWi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 66)
)
if mibBuilder.loadTexts:
    ap3965ROWi.setStatus("current")
_ApW786C2SFP_ObjectIdentity = ObjectIdentity
apW786C2SFP = _ApW786C2SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 67)
)
if mibBuilder.loadTexts:
    apW786C2SFP.setStatus("current")
_Ap3805FCCi_ObjectIdentity = ObjectIdentity
ap3805FCCi = _Ap3805FCCi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 68)
)
if mibBuilder.loadTexts:
    ap3805FCCi.setStatus("current")
_Ap3805FCCe_ObjectIdentity = ObjectIdentity
ap3805FCCe = _Ap3805FCCe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 69)
)
if mibBuilder.loadTexts:
    ap3805FCCe.setStatus("current")
_Ap3805ROWi_ObjectIdentity = ObjectIdentity
ap3805ROWi = _Ap3805ROWi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 70)
)
if mibBuilder.loadTexts:
    ap3805ROWi.setStatus("current")
_Ap3805ROWe_ObjectIdentity = ObjectIdentity
ap3805ROWe = _Ap3805ROWe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 71)
)
if mibBuilder.loadTexts:
    ap3805ROWe.setStatus("current")
_Ap3825i_1_ObjectIdentity = ObjectIdentity
ap3825i_1 = _Ap3825i_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 72)
)
if mibBuilder.loadTexts:
    ap3825i_1.setStatus("current")
_Ap3825e_1_ObjectIdentity = ObjectIdentity
ap3825e_1 = _Ap3825e_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 73)
)
if mibBuilder.loadTexts:
    ap3825e_1.setStatus("current")
_ApVMAPFCCi_ObjectIdentity = ObjectIdentity
apVMAPFCCi = _ApVMAPFCCi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 74)
)
if mibBuilder.loadTexts:
    apVMAPFCCi.setStatus("current")
_ApVMAPROWi_ObjectIdentity = ObjectIdentity
apVMAPROWi = _ApVMAPROWi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 75)
)
if mibBuilder.loadTexts:
    apVMAPROWi.setStatus("current")
_Ap3935i_IL_ObjectIdentity = ObjectIdentity
ap3935i_IL = _Ap3935i_IL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 76)
)
if mibBuilder.loadTexts:
    ap3935i_IL.setStatus("current")
_Ap3912FCCi_ObjectIdentity = ObjectIdentity
ap3912FCCi = _Ap3912FCCi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 77)
)
if mibBuilder.loadTexts:
    ap3912FCCi.setStatus("current")
_Ap3912ROWi_ObjectIdentity = ObjectIdentity
ap3912ROWi = _Ap3912ROWi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 78)
)
if mibBuilder.loadTexts:
    ap3912ROWi.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HIPATH-WIRELESS-PRODUCTS-MIB",
    **{"control": control,
       "c10": c10,
       "c100": c100,
       "c1000": c1000,
       "hiPathWirelessManager": hiPathWirelessManager,
       "c2000": c2000,
       "c20": c20,
       "c20N": c20N,
       "crbt8110": crbt8110,
       "crbt8210": crbt8210,
       "c5110": c5110,
       "c4110": c4110,
       "c25": c25,
       "v2110": v2110,
       "c5210": c5210,
       "v2110H": v2110H,
       "c35": c35,
       "access": access,
       "ap26xx": ap26xx,
       "ap2600": ap2600,
       "ap2650": ap2650,
       "apW786": apW786,
       "apW788": apW788,
       "ap3610": ap3610,
       "ap2605": ap2605,
       "ap3630": ap3630,
       "ap3640": ap3640,
       "ap2650Rev1": ap2650Rev1,
       "apW786Rev1": apW786Rev1,
       "ap4102": ap4102,
       "ap4102c": ap4102c,
       "ap4102RevEU": ap4102RevEU,
       "ap4102cRevEU": ap4102cRevEU,
       "ap2600Rev1": ap2600Rev1,
       "ap3600Rev1": ap3600Rev1,
       "ap2650Rev2": ap2650Rev2,
       "apW786Rev2": apW786Rev2,
       "ap3600": ap3600,
       "ap3605": ap3605,
       "ap3660": ap3660,
       "ap2660Rev2": ap2660Rev2,
       "apW786Rev2PROe2": apW786Rev2PROe2,
       "apW786Rev2PROeFO2": apW786Rev2PROeFO2,
       "apW786Rev2PROiFO2": apW786Rev2PROiFO2,
       "ap3630NAMInternal": ap3630NAMInternal,
       "ap3640NAMExternal": ap3640NAMExternal,
       "ap3630ROWInternal": ap3630ROWInternal,
       "ap3640ROWExternal": ap3640ROWExternal,
       "ap3630ILInternal": ap3630ILInternal,
       "ap3640ILExternal": ap3640ILExternal,
       "apW786C2RJ45": apW786C2RJ45,
       "apW786C2IARJ45": apW786C2IARJ45,
       "apW788C2RJ45": apW788C2RJ45,
       "apW788C2M12": apW788C2M12,
       "ap3705": ap3705,
       "ap3765i": ap3765i,
       "ap3660Rev1": ap3660Rev1,
       "ap3765e": ap3765e,
       "ap3767e": ap3767e,
       "ap3705i": ap3705i,
       "ap3710i": ap3710i,
       "ap3710e": ap3710e,
       "ap3725i": ap3725i,
       "ap3725e": ap3725e,
       "ap3715i": ap3715i,
       "ap3715e": ap3715e,
       "ap3630ROW1i": ap3630ROW1i,
       "ap3640ROW1e": ap3640ROW1e,
       "ap3715i-1": ap3715i_1,
       "ap3825i": ap3825i,
       "ap3825e": ap3825e,
       "ap3865e": ap3865e,
       "ap3805i": ap3805i,
       "ap3805e": ap3805e,
       "ap3801i": ap3801i,
       "ap3935FCCe": ap3935FCCe,
       "ap3965FCCe": ap3965FCCe,
       "ap3935ROWe": ap3935ROWe,
       "ap3965ROWe": ap3965ROWe,
       "ap3935FCCi": ap3935FCCi,
       "ap3965FCCi": ap3965FCCi,
       "ap3935ROWi": ap3935ROWi,
       "ap3965ROWi": ap3965ROWi,
       "apW786C2SFP": apW786C2SFP,
       "ap3805FCCi": ap3805FCCi,
       "ap3805FCCe": ap3805FCCe,
       "ap3805ROWi": ap3805ROWi,
       "ap3805ROWe": ap3805ROWe,
       "ap3825i-1": ap3825i_1,
       "ap3825e-1": ap3825e_1,
       "apVMAPFCCi": apVMAPFCCi,
       "apVMAPROWi": apVMAPROWi,
       "ap3935i-IL": ap3935i_IL,
       "ap3912FCCi": ap3912FCCi,
       "ap3912ROWi": ap3912ROWi,
       "hiPathWirelessProductsMIB": hiPathWirelessProductsMIB}
)
