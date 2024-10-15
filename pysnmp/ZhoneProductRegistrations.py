# SNMP MIB module (ZhoneProductRegistrations) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZhoneProductRegistrations
# Produced by pysmi-1.5.4 at Mon Oct 14 23:23:21 2024
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

(zhoneModules,
 zhoneRegCpe,
 zhoneRegMalc,
 zhoneRegMux,
 zhoneRegPls,
 zhoneRegSechtor,
 zhoneRegistrations) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneModules",
    "zhoneRegCpe",
    "zhoneRegMalc",
    "zhoneRegMux",
    "zhoneRegPls",
    "zhoneRegSechtor",
    "zhoneRegistrations")


# MODULE-IDENTITY

zhoneRegistrationsModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 1)
)
zhoneRegistrationsModule.setRevisions(
        ("2012-08-01 16:11",
         "2011-11-30 11:56",
         "2011-08-15 07:13",
         "2011-05-13 05:14",
         "2010-09-23 14:40",
         "2010-08-03 10:12",
         "2010-02-11 15:38",
         "2009-08-13 14:04",
         "2008-10-28 13:44",
         "2007-11-15 12:08",
         "2007-10-31 13:13",
         "2007-06-27 11:54",
         "2007-06-11 16:12",
         "2007-05-11 16:00",
         "2007-05-09 10:56",
         "2007-04-03 10:48",
         "2007-03-09 14:13",
         "2006-10-26 15:17",
         "2006-08-31 20:02",
         "2006-07-13 16:07",
         "2006-05-22 16:01",
         "2006-05-05 15:42",
         "2006-04-28 13:36",
         "2006-04-27 13:23",
         "2006-04-24 12:06",
         "2006-04-18 17:43",
         "2006-03-27 11:14",
         "2005-12-09 14:14",
         "2004-09-08 17:28",
         "2004-08-30 11:07",
         "2004-05-25 12:30",
         "2004-05-21 14:25",
         "2004-05-21 13:26",
         "2004-04-06 01:45",
         "2004-03-17 10:54",
         "2004-03-02 14:00",
         "2003-10-31 14:26",
         "2003-07-10 12:19",
         "2003-05-16 17:04",
         "2003-02-11 14:58",
         "2002-10-23 10:18",
         "2002-10-10 09:43",
         "2002-10-10 09:42",
         "2001-06-26 17:04",
         "2001-06-07 11:59",
         "2001-05-15 11:53",
         "2001-02-01 13:10",
         "2000-09-28 16:48",
         "2000-09-12 10:55")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ban_2000_ObjectIdentity = ObjectIdentity
ban_2000 = _Ban_2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ban_2000.setStatus("current")
_Zedge64_ObjectIdentity = ObjectIdentity
zedge64 = _Zedge64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 1)
)
if mibBuilder.loadTexts:
    zedge64.setStatus("current")
_Zedge64_SHDSL_FXS_ObjectIdentity = ObjectIdentity
zedge64_SHDSL_FXS = _Zedge64_SHDSL_FXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    zedge64_SHDSL_FXS.setStatus("current")
_Zedge64_SHDSL_BRI_ObjectIdentity = ObjectIdentity
zedge64_SHDSL_BRI = _Zedge64_SHDSL_BRI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    zedge64_SHDSL_BRI.setStatus("current")
_Zedge64_T1_FXS_ObjectIdentity = ObjectIdentity
zedge64_T1_FXS = _Zedge64_T1_FXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    zedge64_T1_FXS.setStatus("current")
_Zedge64_E1_FXS_ObjectIdentity = ObjectIdentity
zedge64_E1_FXS = _Zedge64_E1_FXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    zedge64_E1_FXS.setStatus("current")
_Zedge6200_ObjectIdentity = ObjectIdentity
zedge6200 = _Zedge6200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 2)
)
if mibBuilder.loadTexts:
    zedge6200.setStatus("current")
_Zedge6200_IP_T1_ObjectIdentity = ObjectIdentity
zedge6200_IP_T1 = _Zedge6200_IP_T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    zedge6200_IP_T1.setStatus("current")
_Zedge6200_IP_EM_ObjectIdentity = ObjectIdentity
zedge6200_IP_EM = _Zedge6200_IP_EM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    zedge6200_IP_EM.setStatus("current")
_Zedge6200_IP_FXS_ObjectIdentity = ObjectIdentity
zedge6200_IP_FXS = _Zedge6200_IP_FXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    zedge6200_IP_FXS.setStatus("current")
_Zrg3xx_ObjectIdentity = ObjectIdentity
zrg3xx = _Zrg3xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 3)
)
if mibBuilder.loadTexts:
    zrg3xx.setStatus("current")
_Zrg300_IDU_ObjectIdentity = ObjectIdentity
zrg300_IDU = _Zrg300_IDU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    zrg300_IDU.setStatus("current")
_Zrg300_ODU_ObjectIdentity = ObjectIdentity
zrg300_ODU = _Zrg300_ODU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    zrg300_ODU.setStatus("current")
_Zrg5xx_ObjectIdentity = ObjectIdentity
zrg5xx = _Zrg5xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 4)
)
if mibBuilder.loadTexts:
    zrg5xx.setStatus("current")
_Zrg500_IDU_ObjectIdentity = ObjectIdentity
zrg500_IDU = _Zrg500_IDU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    zrg500_IDU.setStatus("current")
_Zrg500_ODU_ObjectIdentity = ObjectIdentity
zrg500_ODU = _Zrg500_ODU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    zrg500_ODU.setStatus("current")
_Zrg7xx_ObjectIdentity = ObjectIdentity
zrg7xx = _Zrg7xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 5)
)
if mibBuilder.loadTexts:
    zrg7xx.setStatus("current")
_Zrg700_IDU_ObjectIdentity = ObjectIdentity
zrg700_IDU = _Zrg700_IDU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    zrg700_IDU.setStatus("current")
_Zrg700_ODU_ObjectIdentity = ObjectIdentity
zrg700_ODU = _Zrg700_ODU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    zrg700_ODU.setStatus("current")
_Zrg6xx_ObjectIdentity = ObjectIdentity
zrg6xx = _Zrg6xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 6)
)
if mibBuilder.loadTexts:
    zrg6xx.setStatus("current")
_Zrg600_IDU_ObjectIdentity = ObjectIdentity
zrg600_IDU = _Zrg600_IDU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    zrg600_IDU.setStatus("current")
_Zrg600_ODU_ObjectIdentity = ObjectIdentity
zrg600_ODU = _Zrg600_ODU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    zrg600_ODU.setStatus("current")
_Zrg8xx_ObjectIdentity = ObjectIdentity
zrg8xx = _Zrg8xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 7)
)
if mibBuilder.loadTexts:
    zrg8xx.setStatus("current")
_Zrg800_IDU_ObjectIdentity = ObjectIdentity
zrg800_IDU = _Zrg800_IDU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    zrg800_IDU.setStatus("current")
_Zrg800_ODU_ObjectIdentity = ObjectIdentity
zrg800_ODU = _Zrg800_ODU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 7, 2)
)
if mibBuilder.loadTexts:
    zrg800_ODU.setStatus("current")
_EthXtendxx_ObjectIdentity = ObjectIdentity
ethXtendxx = _EthXtendxx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 8)
)
if mibBuilder.loadTexts:
    ethXtendxx.setStatus("current")
_EthXtendShdsl_ObjectIdentity = ObjectIdentity
ethXtendShdsl = _EthXtendShdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    ethXtendShdsl.setStatus("current")
_EthXtendT1E1_ObjectIdentity = ObjectIdentity
ethXtendT1E1 = _EthXtendT1E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 8, 2)
)
if mibBuilder.loadTexts:
    ethXtendT1E1.setStatus("current")
_EthXtend30xx_ObjectIdentity = ObjectIdentity
ethXtend30xx = _EthXtend30xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 8, 3)
)
if mibBuilder.loadTexts:
    ethXtend30xx.setStatus("current")
_EthXtend31xx_ObjectIdentity = ObjectIdentity
ethXtend31xx = _EthXtend31xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 8, 4)
)
if mibBuilder.loadTexts:
    ethXtend31xx.setStatus("current")
_EthXtend32xx_ObjectIdentity = ObjectIdentity
ethXtend32xx = _EthXtend32xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 8, 5)
)
if mibBuilder.loadTexts:
    ethXtend32xx.setStatus("current")
_Znid_ObjectIdentity = ObjectIdentity
znid = _Znid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 9)
)
if mibBuilder.loadTexts:
    znid.setStatus("current")
_Znid42xx_ObjectIdentity = ObjectIdentity
znid42xx = _Znid42xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 9, 1)
)
if mibBuilder.loadTexts:
    znid42xx.setStatus("current")
_ZnidGPON42xx_ObjectIdentity = ObjectIdentity
znidGPON42xx = _ZnidGPON42xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 9, 1, 2)
)
if mibBuilder.loadTexts:
    znidGPON42xx.setStatus("current")
_ZnidEth422x_ObjectIdentity = ObjectIdentity
znidEth422x = _ZnidEth422x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 9, 1, 3)
)
if mibBuilder.loadTexts:
    znidEth422x.setStatus("current")
_Znid420x_ObjectIdentity = ObjectIdentity
znid420x = _Znid420x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 9, 2)
)
if mibBuilder.loadTexts:
    znid420x.setStatus("current")
_ZnidGPON420x_ObjectIdentity = ObjectIdentity
znidGPON420x = _ZnidGPON420x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 9, 2, 1)
)
if mibBuilder.loadTexts:
    znidGPON420x.setStatus("current")
_ZnidNextGen_ObjectIdentity = ObjectIdentity
znidNextGen = _ZnidNextGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 10)
)
if mibBuilder.loadTexts:
    znidNextGen.setStatus("current")
_ZnidNextGen22xx_ObjectIdentity = ObjectIdentity
znidNextGen22xx = _ZnidNextGen22xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 1)
)
if mibBuilder.loadTexts:
    znidNextGen22xx.setStatus("current")
_ZnidNextGenGE22xx_ObjectIdentity = ObjectIdentity
znidNextGenGE22xx = _ZnidNextGenGE22xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 1, 1)
)
if mibBuilder.loadTexts:
    znidNextGenGE22xx.setStatus("current")
_ZnidNextGen42xx_ObjectIdentity = ObjectIdentity
znidNextGen42xx = _ZnidNextGen42xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 2)
)
if mibBuilder.loadTexts:
    znidNextGen42xx.setStatus("current")
_ZnidNextGenGPON42xx_ObjectIdentity = ObjectIdentity
znidNextGenGPON42xx = _ZnidNextGenGPON42xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 2, 1)
)
if mibBuilder.loadTexts:
    znidNextGenGPON42xx.setStatus("current")
_ZnidNextGenGE42xx_ObjectIdentity = ObjectIdentity
znidNextGenGE42xx = _ZnidNextGenGE42xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 2, 2)
)
if mibBuilder.loadTexts:
    znidNextGenGE42xx.setStatus("current")
_ZnidNextGen9xxx_ObjectIdentity = ObjectIdentity
znidNextGen9xxx = _ZnidNextGen9xxx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 3)
)
if mibBuilder.loadTexts:
    znidNextGen9xxx.setStatus("current")
_ZnidNextGenGPON9xxx_ObjectIdentity = ObjectIdentity
znidNextGenGPON9xxx = _ZnidNextGenGPON9xxx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 3, 1)
)
if mibBuilder.loadTexts:
    znidNextGenGPON9xxx.setStatus("current")
_ZnidNextGenGE9xxx_ObjectIdentity = ObjectIdentity
znidNextGenGE9xxx = _ZnidNextGenGE9xxx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 3, 2)
)
if mibBuilder.loadTexts:
    znidNextGenGE9xxx.setStatus("current")
_ZnidNextGenGPON94xx_ObjectIdentity = ObjectIdentity
znidNextGenGPON94xx = _ZnidNextGenGPON94xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 3, 3)
)
if mibBuilder.loadTexts:
    znidNextGenGPON94xx.setStatus("current")
_ZnidNextGenGE94xx_ObjectIdentity = ObjectIdentity
znidNextGenGE94xx = _ZnidNextGenGE94xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 3, 4)
)
if mibBuilder.loadTexts:
    znidNextGenGE94xx.setStatus("current")
_ZnidNextGenGPON97xx_ObjectIdentity = ObjectIdentity
znidNextGenGPON97xx = _ZnidNextGenGPON97xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 3, 5)
)
if mibBuilder.loadTexts:
    znidNextGenGPON97xx.setStatus("current")
_ZnidNextGenGE97xx_ObjectIdentity = ObjectIdentity
znidNextGenGE97xx = _ZnidNextGenGE97xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 3, 6)
)
if mibBuilder.loadTexts:
    znidNextGenGE97xx.setStatus("current")
_FiberJack_ObjectIdentity = ObjectIdentity
fiberJack = _FiberJack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 4)
)
if mibBuilder.loadTexts:
    fiberJack.setStatus("current")
_ZnidNextGen21xx_ObjectIdentity = ObjectIdentity
znidNextGen21xx = _ZnidNextGen21xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 5)
)
if mibBuilder.loadTexts:
    znidNextGen21xx.setStatus("current")
_ZnidNextGenGPON21xx_ObjectIdentity = ObjectIdentity
znidNextGenGPON21xx = _ZnidNextGenGPON21xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 5, 1)
)
if mibBuilder.loadTexts:
    znidNextGenGPON21xx.setStatus("current")
_ZnidNextGenGE21xx_ObjectIdentity = ObjectIdentity
znidNextGenGE21xx = _ZnidNextGenGE21xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 5, 2)
)
if mibBuilder.loadTexts:
    znidNextGenGE21xx.setStatus("current")
_ZnidNextGen24xx_ObjectIdentity = ObjectIdentity
znidNextGen24xx = _ZnidNextGen24xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 6)
)
if mibBuilder.loadTexts:
    znidNextGen24xx.setStatus("current")
_ZnidNextGenGPON24xx_ObjectIdentity = ObjectIdentity
znidNextGenGPON24xx = _ZnidNextGenGPON24xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 6, 1)
)
if mibBuilder.loadTexts:
    znidNextGenGPON24xx.setStatus("current")
_ZnidNextGenGE24xx_ObjectIdentity = ObjectIdentity
znidNextGenGE24xx = _ZnidNextGenGE24xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 6, 2)
)
if mibBuilder.loadTexts:
    znidNextGenGE24xx.setStatus("current")
_ZnidNextGen26xx_ObjectIdentity = ObjectIdentity
znidNextGen26xx = _ZnidNextGen26xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 7)
)
if mibBuilder.loadTexts:
    znidNextGen26xx.setStatus("current")
_ZnidNextGenGPON26xx_ObjectIdentity = ObjectIdentity
znidNextGenGPON26xx = _ZnidNextGenGPON26xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 7, 1)
)
if mibBuilder.loadTexts:
    znidNextGenGPON26xx.setStatus("current")
_ZnidNextGenGE26xx_ObjectIdentity = ObjectIdentity
znidNextGenGE26xx = _ZnidNextGenGE26xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 7, 2)
)
if mibBuilder.loadTexts:
    znidNextGenGE26xx.setStatus("current")
_Z_plex10B_ObjectIdentity = ObjectIdentity
z_plex10B = _Z_plex10B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 3, 1)
)
if mibBuilder.loadTexts:
    z_plex10B.setStatus("current")
_Z_plex10B_FXS_FXO_ObjectIdentity = ObjectIdentity
z_plex10B_FXS_FXO = _Z_plex10B_FXS_FXO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    z_plex10B_FXS_FXO.setStatus("current")
_Z_plex10B_FXS_ObjectIdentity = ObjectIdentity
z_plex10B_FXS = _Z_plex10B_FXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    z_plex10B_FXS.setStatus("current")
_Sechtor_100_ObjectIdentity = ObjectIdentity
sechtor_100 = _Sechtor_100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 4, 1)
)
if mibBuilder.loadTexts:
    sechtor_100.setStatus("current")
_S100_ATM_SM_16T1_ObjectIdentity = ObjectIdentity
s100_ATM_SM_16T1 = _S100_ATM_SM_16T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    s100_ATM_SM_16T1.setStatus("current")
_S100_ATM_SM_16E1_ObjectIdentity = ObjectIdentity
s100_ATM_SM_16E1 = _S100_ATM_SM_16E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    s100_ATM_SM_16E1.setStatus("current")
_Sechtor_300_ObjectIdentity = ObjectIdentity
sechtor_300 = _Sechtor_300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 4, 2)
)
if mibBuilder.loadTexts:
    sechtor_300.setStatus("current")
_ZhoneRegWtn_ObjectIdentity = ObjectIdentity
zhoneRegWtn = _ZhoneRegWtn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5)
)
if mibBuilder.loadTexts:
    zhoneRegWtn.setStatus("current")
_Node5700Mhz_ObjectIdentity = ObjectIdentity
node5700Mhz = _Node5700Mhz_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 1)
)
if mibBuilder.loadTexts:
    node5700Mhz.setStatus("current")
_SkyZhone45_ObjectIdentity = ObjectIdentity
skyZhone45 = _SkyZhone45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    skyZhone45.setStatus("current")
_OduTypeA_ObjectIdentity = ObjectIdentity
oduTypeA = _OduTypeA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    oduTypeA.setStatus("current")
_OduTypeB_ObjectIdentity = ObjectIdentity
oduTypeB = _OduTypeB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    oduTypeB.setStatus("current")
_Node23000Mhz_ObjectIdentity = ObjectIdentity
node23000Mhz = _Node23000Mhz_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2)
)
if mibBuilder.loadTexts:
    node23000Mhz.setStatus("current")
_SkyZhone8e1_ObjectIdentity = ObjectIdentity
skyZhone8e1 = _SkyZhone8e1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    skyZhone8e1.setStatus("current")
_OduTypeE1A_ObjectIdentity = ObjectIdentity
oduTypeE1A = _OduTypeE1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    oduTypeE1A.setStatus("current")
_OduTypeE1B_ObjectIdentity = ObjectIdentity
oduTypeE1B = _OduTypeE1B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 1, 2)
)
if mibBuilder.loadTexts:
    oduTypeE1B.setStatus("current")
_SkyZhone8e2_ObjectIdentity = ObjectIdentity
skyZhone8e2 = _SkyZhone8e2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    skyZhone8e2.setStatus("current")
_OduTypeE2A_ObjectIdentity = ObjectIdentity
oduTypeE2A = _OduTypeE2A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 2, 1)
)
if mibBuilder.loadTexts:
    oduTypeE2A.setStatus("current")
_OduTypeE2B_ObjectIdentity = ObjectIdentity
oduTypeE2B = _OduTypeE2B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 2, 2)
)
if mibBuilder.loadTexts:
    oduTypeE2B.setStatus("current")
_SkyZhone8e3_ObjectIdentity = ObjectIdentity
skyZhone8e3 = _SkyZhone8e3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 3)
)
if mibBuilder.loadTexts:
    skyZhone8e3.setStatus("current")
_OduTypeE3A_ObjectIdentity = ObjectIdentity
oduTypeE3A = _OduTypeE3A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 3, 1)
)
if mibBuilder.loadTexts:
    oduTypeE3A.setStatus("current")
_OduTypeE3B_ObjectIdentity = ObjectIdentity
oduTypeE3B = _OduTypeE3B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 3, 2)
)
if mibBuilder.loadTexts:
    oduTypeE3B.setStatus("current")
_SkyZhone8e4_ObjectIdentity = ObjectIdentity
skyZhone8e4 = _SkyZhone8e4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 4)
)
if mibBuilder.loadTexts:
    skyZhone8e4.setStatus("current")
_OduTypeE4A_ObjectIdentity = ObjectIdentity
oduTypeE4A = _OduTypeE4A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 4, 1)
)
if mibBuilder.loadTexts:
    oduTypeE4A.setStatus("current")
_OduTypeE4B_ObjectIdentity = ObjectIdentity
oduTypeE4B = _OduTypeE4B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 4, 2)
)
if mibBuilder.loadTexts:
    oduTypeE4B.setStatus("current")
_SkyZhone8t1_ObjectIdentity = ObjectIdentity
skyZhone8t1 = _SkyZhone8t1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 5)
)
if mibBuilder.loadTexts:
    skyZhone8t1.setStatus("current")
_OduTypeT1A_ObjectIdentity = ObjectIdentity
oduTypeT1A = _OduTypeT1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 5, 1)
)
if mibBuilder.loadTexts:
    oduTypeT1A.setStatus("current")
_OduTypeT1B_ObjectIdentity = ObjectIdentity
oduTypeT1B = _OduTypeT1B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 5, 2)
)
if mibBuilder.loadTexts:
    oduTypeT1B.setStatus("current")
_SkyZhone8t2_ObjectIdentity = ObjectIdentity
skyZhone8t2 = _SkyZhone8t2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 6)
)
if mibBuilder.loadTexts:
    skyZhone8t2.setStatus("current")
_OduTypeT2A_ObjectIdentity = ObjectIdentity
oduTypeT2A = _OduTypeT2A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 6, 1)
)
if mibBuilder.loadTexts:
    oduTypeT2A.setStatus("current")
_OduTypeT2B_ObjectIdentity = ObjectIdentity
oduTypeT2B = _OduTypeT2B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 6, 2)
)
if mibBuilder.loadTexts:
    oduTypeT2B.setStatus("current")
_SkyZhone8t3_ObjectIdentity = ObjectIdentity
skyZhone8t3 = _SkyZhone8t3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 7)
)
if mibBuilder.loadTexts:
    skyZhone8t3.setStatus("current")
_OduTypeT3A_ObjectIdentity = ObjectIdentity
oduTypeT3A = _OduTypeT3A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 7, 1)
)
if mibBuilder.loadTexts:
    oduTypeT3A.setStatus("current")
_OduTypeT3B_ObjectIdentity = ObjectIdentity
oduTypeT3B = _OduTypeT3B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 7, 2)
)
if mibBuilder.loadTexts:
    oduTypeT3B.setStatus("current")
_SkyZhone8t4_ObjectIdentity = ObjectIdentity
skyZhone8t4 = _SkyZhone8t4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 8)
)
if mibBuilder.loadTexts:
    skyZhone8t4.setStatus("current")
_OduTypeT4A_ObjectIdentity = ObjectIdentity
oduTypeT4A = _OduTypeT4A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 8, 1)
)
if mibBuilder.loadTexts:
    oduTypeT4A.setStatus("current")
_OduTypeT4B_ObjectIdentity = ObjectIdentity
oduTypeT4B = _OduTypeT4B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 8, 2)
)
if mibBuilder.loadTexts:
    oduTypeT4B.setStatus("current")
_SkyZhone155s1_ObjectIdentity = ObjectIdentity
skyZhone155s1 = _SkyZhone155s1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 9)
)
if mibBuilder.loadTexts:
    skyZhone155s1.setStatus("current")
_OduTypeS1A_ObjectIdentity = ObjectIdentity
oduTypeS1A = _OduTypeS1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 9, 1)
)
if mibBuilder.loadTexts:
    oduTypeS1A.setStatus("current")
_OduTypeS1B_ObjectIdentity = ObjectIdentity
oduTypeS1B = _OduTypeS1B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 9, 2)
)
if mibBuilder.loadTexts:
    oduTypeS1B.setStatus("current")
_SkyZhone155s2_ObjectIdentity = ObjectIdentity
skyZhone155s2 = _SkyZhone155s2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 10)
)
if mibBuilder.loadTexts:
    skyZhone155s2.setStatus("current")
_OduTypeS2A_ObjectIdentity = ObjectIdentity
oduTypeS2A = _OduTypeS2A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 10, 1)
)
if mibBuilder.loadTexts:
    oduTypeS2A.setStatus("current")
_OduTypeS2B_ObjectIdentity = ObjectIdentity
oduTypeS2B = _OduTypeS2B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 10, 2)
)
if mibBuilder.loadTexts:
    oduTypeS2B.setStatus("current")
_SkyZhone155s3_ObjectIdentity = ObjectIdentity
skyZhone155s3 = _SkyZhone155s3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 11)
)
if mibBuilder.loadTexts:
    skyZhone155s3.setStatus("current")
_OduTypeS3A_ObjectIdentity = ObjectIdentity
oduTypeS3A = _OduTypeS3A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 11, 1)
)
if mibBuilder.loadTexts:
    oduTypeS3A.setStatus("current")
_OduTypeS3B_ObjectIdentity = ObjectIdentity
oduTypeS3B = _OduTypeS3B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 11, 2)
)
if mibBuilder.loadTexts:
    oduTypeS3B.setStatus("current")
_SkyZhone155s4_ObjectIdentity = ObjectIdentity
skyZhone155s4 = _SkyZhone155s4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 12)
)
if mibBuilder.loadTexts:
    skyZhone155s4.setStatus("current")
_OduTypeS4A_ObjectIdentity = ObjectIdentity
oduTypeS4A = _OduTypeS4A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 12, 1)
)
if mibBuilder.loadTexts:
    oduTypeS4A.setStatus("current")
_OduTypeS4B_ObjectIdentity = ObjectIdentity
oduTypeS4B = _OduTypeS4B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 12, 2)
)
if mibBuilder.loadTexts:
    oduTypeS4B.setStatus("current")
_SkyZhone1xxx_ObjectIdentity = ObjectIdentity
skyZhone1xxx = _SkyZhone1xxx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 5, 3)
)
if mibBuilder.loadTexts:
    skyZhone1xxx.setStatus("current")
_Malc19_ObjectIdentity = ObjectIdentity
malc19 = _Malc19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 1)
)
if mibBuilder.loadTexts:
    malc19.setStatus("current")
_Malc23_ObjectIdentity = ObjectIdentity
malc23 = _Malc23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 2)
)
if mibBuilder.loadTexts:
    malc23.setStatus("current")
_Malc319_ObjectIdentity = ObjectIdentity
malc319 = _Malc319_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 3)
)
if mibBuilder.loadTexts:
    malc319.setStatus("current")
_Raptor319A_ObjectIdentity = ObjectIdentity
raptor319A = _Raptor319A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 4)
)
if mibBuilder.loadTexts:
    raptor319A.setStatus("current")
_Raptor319I_ObjectIdentity = ObjectIdentity
raptor319I = _Raptor319I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 5)
)
if mibBuilder.loadTexts:
    raptor319I.setStatus("current")
_Raptor719A_ObjectIdentity = ObjectIdentity
raptor719A = _Raptor719A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 6)
)
if mibBuilder.loadTexts:
    raptor719A.setStatus("current")
_Raptor719I_ObjectIdentity = ObjectIdentity
raptor719I = _Raptor719I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 7)
)
if mibBuilder.loadTexts:
    raptor719I.setStatus("current")
_Raptor723A_ObjectIdentity = ObjectIdentity
raptor723A = _Raptor723A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 8)
)
if mibBuilder.loadTexts:
    raptor723A.setStatus("current")
_Raptor723I_ObjectIdentity = ObjectIdentity
raptor723I = _Raptor723I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 9)
)
if mibBuilder.loadTexts:
    raptor723I.setStatus("current")
_Raptor100A_ObjectIdentity = ObjectIdentity
raptor100A = _Raptor100A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 10)
)
if mibBuilder.loadTexts:
    raptor100A.setStatus("current")
_Raptor100I_ObjectIdentity = ObjectIdentity
raptor100I = _Raptor100I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 11)
)
if mibBuilder.loadTexts:
    raptor100I.setStatus("current")
_Raptor100LP_ObjectIdentity = ObjectIdentity
raptor100LP = _Raptor100LP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 12)
)
if mibBuilder.loadTexts:
    raptor100LP.setStatus("current")
_Raptor50Gshdsl_ObjectIdentity = ObjectIdentity
raptor50Gshdsl = _Raptor50Gshdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 13)
)
if mibBuilder.loadTexts:
    raptor50Gshdsl.setStatus("current")
_Isc303_ObjectIdentity = ObjectIdentity
isc303 = _Isc303_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 14)
)
if mibBuilder.loadTexts:
    isc303.setStatus("current")
_R100adsl2Pxxx_ObjectIdentity = ObjectIdentity
r100adsl2Pxxx = _R100adsl2Pxxx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 15)
)
if mibBuilder.loadTexts:
    r100adsl2Pxxx.setStatus("current")
_R100adsl2pip_ObjectIdentity = ObjectIdentity
r100adsl2pip = _R100adsl2pip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 15, 1)
)
if mibBuilder.loadTexts:
    r100adsl2pip.setStatus("current")
_R100adsl2phdsl4_ObjectIdentity = ObjectIdentity
r100adsl2phdsl4 = _R100adsl2phdsl4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 15, 2)
)
if mibBuilder.loadTexts:
    r100adsl2phdsl4.setStatus("current")
_R100adsl2pt1ima_ObjectIdentity = ObjectIdentity
r100adsl2pt1ima = _R100adsl2pt1ima_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 15, 3)
)
if mibBuilder.loadTexts:
    r100adsl2pt1ima.setStatus("current")
_R100adsl2pgige_ObjectIdentity = ObjectIdentity
r100adsl2pgige = _R100adsl2pgige_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 15, 4)
)
if mibBuilder.loadTexts:
    r100adsl2pgige.setStatus("current")
_R100adsl2pgm_ObjectIdentity = ObjectIdentity
r100adsl2pgm = _R100adsl2pgm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 15, 5)
)
if mibBuilder.loadTexts:
    r100adsl2pgm.setStatus("obsolete")
_R100adsl2pgte_ObjectIdentity = ObjectIdentity
r100adsl2pgte = _R100adsl2pgte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 15, 6)
)
if mibBuilder.loadTexts:
    r100adsl2pgte.setStatus("obsolete")
_R100adsl2panxb_ObjectIdentity = ObjectIdentity
r100adsl2panxb = _R100adsl2panxb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 15, 7)
)
if mibBuilder.loadTexts:
    r100adsl2panxb.setStatus("current")
_M100_ObjectIdentity = ObjectIdentity
m100 = _M100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 16)
)
if mibBuilder.loadTexts:
    m100.setStatus("current")
_M100adsl2pxxx_ObjectIdentity = ObjectIdentity
m100adsl2pxxx = _M100adsl2pxxx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 16, 1)
)
if mibBuilder.loadTexts:
    m100adsl2pxxx.setStatus("current")
_M100adsl2pgige_ObjectIdentity = ObjectIdentity
m100adsl2pgige = _M100adsl2pgige_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 16, 1, 1)
)
if mibBuilder.loadTexts:
    m100adsl2pgige.setStatus("current")
_M100adsl2pgm_ObjectIdentity = ObjectIdentity
m100adsl2pgm = _M100adsl2pgm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 16, 1, 2)
)
if mibBuilder.loadTexts:
    m100adsl2pgm.setStatus("obsolete")
_M100Adsl2pAnxB_ObjectIdentity = ObjectIdentity
m100Adsl2pAnxB = _M100Adsl2pAnxB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 16, 1, 3)
)
if mibBuilder.loadTexts:
    m100Adsl2pAnxB.setStatus("current")
_M100Vdsl2xxx_ObjectIdentity = ObjectIdentity
m100Vdsl2xxx = _M100Vdsl2xxx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 16, 2)
)
if mibBuilder.loadTexts:
    m100Vdsl2xxx.setStatus("obsolete")
_M100vdsl2gm_ObjectIdentity = ObjectIdentity
m100vdsl2gm = _M100vdsl2gm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 16, 2, 1)
)
if mibBuilder.loadTexts:
    m100vdsl2gm.setStatus("obsolete")
_R100Vdsl2xx_ObjectIdentity = ObjectIdentity
r100Vdsl2xx = _R100Vdsl2xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 17)
)
if mibBuilder.loadTexts:
    r100Vdsl2xx.setStatus("obsolete")
_R100vdsl2gm_ObjectIdentity = ObjectIdentity
r100vdsl2gm = _R100vdsl2gm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 17, 1)
)
if mibBuilder.loadTexts:
    r100vdsl2gm.setStatus("obsolete")
_FiberSlam_ObjectIdentity = ObjectIdentity
fiberSlam = _FiberSlam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 18)
)
if mibBuilder.loadTexts:
    fiberSlam.setStatus("current")
_Fs105_ObjectIdentity = ObjectIdentity
fs105 = _Fs105_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 18, 1)
)
if mibBuilder.loadTexts:
    fs105.setStatus("current")
_Fs101_ObjectIdentity = ObjectIdentity
fs101 = _Fs101_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 18, 2)
)
if mibBuilder.loadTexts:
    fs101.setStatus("current")
_RaptorXP_ObjectIdentity = ObjectIdentity
raptorXP = _RaptorXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 19)
)
if mibBuilder.loadTexts:
    raptorXP.setStatus("current")
_RaptorXP150A_ObjectIdentity = ObjectIdentity
raptorXP150A = _RaptorXP150A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 1)
)
if mibBuilder.loadTexts:
    raptorXP150A.setStatus("current")
_RaptorXP150A_ISP_ObjectIdentity = ObjectIdentity
raptorXP150A_ISP = _RaptorXP150A_ISP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 1, 1)
)
if mibBuilder.loadTexts:
    raptorXP150A_ISP.setStatus("current")
_RaptorXP150A_OSP_ObjectIdentity = ObjectIdentity
raptorXP150A_OSP = _RaptorXP150A_OSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 1, 2)
)
if mibBuilder.loadTexts:
    raptorXP150A_OSP.setStatus("current")
_RaptorXP350A_ObjectIdentity = ObjectIdentity
raptorXP350A = _RaptorXP350A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 2)
)
if mibBuilder.loadTexts:
    raptorXP350A.setStatus("current")
_RaptorXP350A_ISP_ObjectIdentity = ObjectIdentity
raptorXP350A_ISP = _RaptorXP350A_ISP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 2, 1)
)
if mibBuilder.loadTexts:
    raptorXP350A_ISP.setStatus("current")
_RaptorXP350A_OSP_ObjectIdentity = ObjectIdentity
raptorXP350A_OSP = _RaptorXP350A_OSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 2, 2)
)
if mibBuilder.loadTexts:
    raptorXP350A_OSP.setStatus("current")
_RaptorXP160_ObjectIdentity = ObjectIdentity
raptorXP160 = _RaptorXP160_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 3)
)
if mibBuilder.loadTexts:
    raptorXP160.setStatus("current")
_RaptorXP160_ISP_ObjectIdentity = ObjectIdentity
raptorXP160_ISP = _RaptorXP160_ISP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 3, 1)
)
if mibBuilder.loadTexts:
    raptorXP160_ISP.setStatus("current")
_RaptorXP160_OSP_ObjectIdentity = ObjectIdentity
raptorXP160_OSP = _RaptorXP160_OSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 3, 2)
)
if mibBuilder.loadTexts:
    raptorXP160_OSP.setStatus("current")
_RaptorXP170_ObjectIdentity = ObjectIdentity
raptorXP170 = _RaptorXP170_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 4)
)
if mibBuilder.loadTexts:
    raptorXP170.setStatus("current")
_RaptorXP170_WC_ObjectIdentity = ObjectIdentity
raptorXP170_WC = _RaptorXP170_WC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 4, 1)
)
if mibBuilder.loadTexts:
    raptorXP170_WC.setStatus("current")
_RaptorXP170_ISP_WC_ObjectIdentity = ObjectIdentity
raptorXP170_ISP_WC = _RaptorXP170_ISP_WC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 4, 1, 1)
)
if mibBuilder.loadTexts:
    raptorXP170_ISP_WC.setStatus("current")
_RaptorXP170_OSP_WC_ObjectIdentity = ObjectIdentity
raptorXP170_OSP_WC = _RaptorXP170_OSP_WC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 4, 1, 2)
)
if mibBuilder.loadTexts:
    raptorXP170_OSP_WC.setStatus("current")
_RaptorXP170_WC_SD_ObjectIdentity = ObjectIdentity
raptorXP170_WC_SD = _RaptorXP170_WC_SD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 4, 2)
)
if mibBuilder.loadTexts:
    raptorXP170_WC_SD.setStatus("current")
_RaptorXP170_ISP_WC_SD_ObjectIdentity = ObjectIdentity
raptorXP170_ISP_WC_SD = _RaptorXP170_ISP_WC_SD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 4, 2, 1)
)
if mibBuilder.loadTexts:
    raptorXP170_ISP_WC_SD.setStatus("current")
_RaptorXP170_OSP_WC_SD_ObjectIdentity = ObjectIdentity
raptorXP170_OSP_WC_SD = _RaptorXP170_OSP_WC_SD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 4, 2, 2)
)
if mibBuilder.loadTexts:
    raptorXP170_OSP_WC_SD.setStatus("current")
_RaptorXP170_LP_ObjectIdentity = ObjectIdentity
raptorXP170_LP = _RaptorXP170_LP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 4, 3)
)
if mibBuilder.loadTexts:
    raptorXP170_LP.setStatus("current")
_RaptorXP170_ISP_LP_ObjectIdentity = ObjectIdentity
raptorXP170_ISP_LP = _RaptorXP170_ISP_LP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 4, 3, 1)
)
if mibBuilder.loadTexts:
    raptorXP170_ISP_LP.setStatus("current")
_RaptorXP170_OSP_LP_ObjectIdentity = ObjectIdentity
raptorXP170_OSP_LP = _RaptorXP170_OSP_LP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 4, 3, 2)
)
if mibBuilder.loadTexts:
    raptorXP170_OSP_LP.setStatus("current")
_RaptorXP170_LP_SD_ObjectIdentity = ObjectIdentity
raptorXP170_LP_SD = _RaptorXP170_LP_SD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 4, 4)
)
if mibBuilder.loadTexts:
    raptorXP170_LP_SD.setStatus("current")
_RaptorXP170_ISP_LP_SD_ObjectIdentity = ObjectIdentity
raptorXP170_ISP_LP_SD = _RaptorXP170_ISP_LP_SD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 4, 4, 1)
)
if mibBuilder.loadTexts:
    raptorXP170_ISP_LP_SD.setStatus("current")
_RaptorXP170_OSP_LP_SD_ObjectIdentity = ObjectIdentity
raptorXP170_OSP_LP_SD = _RaptorXP170_OSP_LP_SD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 4, 4, 2)
)
if mibBuilder.loadTexts:
    raptorXP170_OSP_LP_SD.setStatus("current")
_MalcXP_ObjectIdentity = ObjectIdentity
malcXP = _MalcXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 20)
)
if mibBuilder.loadTexts:
    malcXP.setStatus("current")
_MalcXP150A_ObjectIdentity = ObjectIdentity
malcXP150A = _MalcXP150A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 20, 1)
)
if mibBuilder.loadTexts:
    malcXP150A.setStatus("current")
_MalcXP150A_ISP_ObjectIdentity = ObjectIdentity
malcXP150A_ISP = _MalcXP150A_ISP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 20, 1, 1)
)
if mibBuilder.loadTexts:
    malcXP150A_ISP.setStatus("current")
_MalcXP150A_OSP_ObjectIdentity = ObjectIdentity
malcXP150A_OSP = _MalcXP150A_OSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 20, 1, 2)
)
if mibBuilder.loadTexts:
    malcXP150A_OSP.setStatus("current")
_MalcXP350A_ObjectIdentity = ObjectIdentity
malcXP350A = _MalcXP350A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 20, 4)
)
if mibBuilder.loadTexts:
    malcXP350A.setStatus("current")
_MalcXP350A_ISP_ObjectIdentity = ObjectIdentity
malcXP350A_ISP = _MalcXP350A_ISP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 20, 4, 1)
)
if mibBuilder.loadTexts:
    malcXP350A_ISP.setStatus("current")
_MalcXP350A_OSP_ObjectIdentity = ObjectIdentity
malcXP350A_OSP = _MalcXP350A_OSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 20, 4, 2)
)
if mibBuilder.loadTexts:
    malcXP350A_OSP.setStatus("current")
_MalcXP160_ObjectIdentity = ObjectIdentity
malcXP160 = _MalcXP160_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 20, 5)
)
if mibBuilder.loadTexts:
    malcXP160.setStatus("current")
_MalcXP160_ISP_ObjectIdentity = ObjectIdentity
malcXP160_ISP = _MalcXP160_ISP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 20, 5, 1)
)
if mibBuilder.loadTexts:
    malcXP160_ISP.setStatus("current")
_MalcXP160_OSP_ObjectIdentity = ObjectIdentity
malcXP160_OSP = _MalcXP160_OSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 6, 20, 5, 2)
)
if mibBuilder.loadTexts:
    malcXP160_OSP.setStatus("current")
_ZhoneRegMxNextGen_ObjectIdentity = ObjectIdentity
zhoneRegMxNextGen = _ZhoneRegMxNextGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7)
)
if mibBuilder.loadTexts:
    zhoneRegMxNextGen.setStatus("current")
_Mx19_ObjectIdentity = ObjectIdentity
mx19 = _Mx19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 1)
)
if mibBuilder.loadTexts:
    mx19.setStatus("current")
_Mx23_ObjectIdentity = ObjectIdentity
mx23 = _Mx23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 2)
)
if mibBuilder.loadTexts:
    mx23.setStatus("current")
_Mx319_ObjectIdentity = ObjectIdentity
mx319 = _Mx319_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 3)
)
if mibBuilder.loadTexts:
    mx319.setStatus("current")
_Mx1U_ObjectIdentity = ObjectIdentity
mx1U = _Mx1U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 4)
)
if mibBuilder.loadTexts:
    mx1U.setStatus("current")
_Mx1Ux6x_ObjectIdentity = ObjectIdentity
mx1Ux6x = _Mx1Ux6x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 1)
)
if mibBuilder.loadTexts:
    mx1Ux6x.setStatus("current")
_Mx1U16x_ObjectIdentity = ObjectIdentity
mx1U16x = _Mx1U16x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 1, 1)
)
if mibBuilder.loadTexts:
    mx1U16x.setStatus("current")
_Mx1U160_ObjectIdentity = ObjectIdentity
mx1U160 = _Mx1U160_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mx1U160.setStatus("current")
_Mx1U161_ObjectIdentity = ObjectIdentity
mx1U161 = _Mx1U161_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mx1U161.setStatus("current")
_Mx1U162_ObjectIdentity = ObjectIdentity
mx1U162 = _Mx1U162_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    mx1U162.setStatus("current")
_Mx1U26x_ObjectIdentity = ObjectIdentity
mx1U26x = _Mx1U26x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 1, 2)
)
if mibBuilder.loadTexts:
    mx1U26x.setStatus("current")
_Mx1U260_ObjectIdentity = ObjectIdentity
mx1U260 = _Mx1U260_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mx1U260.setStatus("current")
_Mx1U261_ObjectIdentity = ObjectIdentity
mx1U261 = _Mx1U261_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mx1U261.setStatus("current")
_Mx1U262_ObjectIdentity = ObjectIdentity
mx1U262 = _Mx1U262_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mx1U262.setStatus("current")
_Mx1Ux80_ObjectIdentity = ObjectIdentity
mx1Ux80 = _Mx1Ux80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 2)
)
if mibBuilder.loadTexts:
    mx1Ux80.setStatus("current")
_Mx1U180_ObjectIdentity = ObjectIdentity
mx1U180 = _Mx1U180_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mx1U180.setStatus("current")
_Mx1U280_ObjectIdentity = ObjectIdentity
mx1U280 = _Mx1U280_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 2, 2)
)
if mibBuilder.loadTexts:
    mx1U280.setStatus("current")
_Mx1U180_TP_RJ45_ObjectIdentity = ObjectIdentity
mx1U180_TP_RJ45 = _Mx1U180_TP_RJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 2, 3)
)
if mibBuilder.loadTexts:
    mx1U180_TP_RJ45.setStatus("current")
_Mx1U280_TP_RJ45_ObjectIdentity = ObjectIdentity
mx1U280_TP_RJ45 = _Mx1U280_TP_RJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 2, 4)
)
if mibBuilder.loadTexts:
    mx1U280_TP_RJ45.setStatus("current")
_Mx1U180_LT_TP_RJ45_ObjectIdentity = ObjectIdentity
mx1U180_LT_TP_RJ45 = _Mx1U180_LT_TP_RJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 2, 5)
)
if mibBuilder.loadTexts:
    mx1U180_LT_TP_RJ45.setStatus("current")
_Mx1U280_LT_TP_RJ45_ObjectIdentity = ObjectIdentity
mx1U280_LT_TP_RJ45 = _Mx1U280_LT_TP_RJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 2, 6)
)
if mibBuilder.loadTexts:
    mx1U280_LT_TP_RJ45.setStatus("current")
_Mx1U19x_ObjectIdentity = ObjectIdentity
mx1U19x = _Mx1U19x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 3)
)
if mibBuilder.loadTexts:
    mx1U19x.setStatus("current")
_Mx1U194_ObjectIdentity = ObjectIdentity
mx1U194 = _Mx1U194_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 3, 1)
)
if mibBuilder.loadTexts:
    mx1U194.setStatus("current")
_Mx1U198_ObjectIdentity = ObjectIdentity
mx1U198 = _Mx1U198_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 3, 2)
)
if mibBuilder.loadTexts:
    mx1U198.setStatus("current")
_Mx1U194_10GE_ObjectIdentity = ObjectIdentity
mx1U194_10GE = _Mx1U194_10GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 3, 3)
)
if mibBuilder.loadTexts:
    mx1U194_10GE.setStatus("current")
_Mx1U198_10GE_ObjectIdentity = ObjectIdentity
mx1U198_10GE = _Mx1U198_10GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 3, 4)
)
if mibBuilder.loadTexts:
    mx1U198_10GE.setStatus("current")
_Mx1U194_TOP_ObjectIdentity = ObjectIdentity
mx1U194_TOP = _Mx1U194_TOP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 3, 5)
)
if mibBuilder.loadTexts:
    mx1U194_TOP.setStatus("current")
_Mx1U198_TOP_ObjectIdentity = ObjectIdentity
mx1U198_TOP = _Mx1U198_TOP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 3, 6)
)
if mibBuilder.loadTexts:
    mx1U198_TOP.setStatus("current")
_Mx1U194_10GE_TOP_ObjectIdentity = ObjectIdentity
mx1U194_10GE_TOP = _Mx1U194_10GE_TOP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 3, 7)
)
if mibBuilder.loadTexts:
    mx1U194_10GE_TOP.setStatus("current")
_Mx1U198_10GE_TOP_ObjectIdentity = ObjectIdentity
mx1U198_10GE_TOP = _Mx1U198_10GE_TOP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 3, 8)
)
if mibBuilder.loadTexts:
    mx1U198_10GE_TOP.setStatus("current")
_Mx1Ux5x_ObjectIdentity = ObjectIdentity
mx1Ux5x = _Mx1Ux5x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 4)
)
if mibBuilder.loadTexts:
    mx1Ux5x.setStatus("current")
_Mx1U15x_ObjectIdentity = ObjectIdentity
mx1U15x = _Mx1U15x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 4, 1)
)
if mibBuilder.loadTexts:
    mx1U15x.setStatus("current")
_Mx1U150_ObjectIdentity = ObjectIdentity
mx1U150 = _Mx1U150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 4, 1, 1)
)
if mibBuilder.loadTexts:
    mx1U150.setStatus("current")
_Mx1U151_ObjectIdentity = ObjectIdentity
mx1U151 = _Mx1U151_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 4, 1, 2)
)
if mibBuilder.loadTexts:
    mx1U151.setStatus("current")
_Mx1U152_ObjectIdentity = ObjectIdentity
mx1U152 = _Mx1U152_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 4, 1, 3)
)
if mibBuilder.loadTexts:
    mx1U152.setStatus("current")
_Mxp1U_ObjectIdentity = ObjectIdentity
mxp1U = _Mxp1U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 5)
)
if mibBuilder.loadTexts:
    mxp1U.setStatus("current")
_Mxp1Ux60_ObjectIdentity = ObjectIdentity
mxp1Ux60 = _Mxp1Ux60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 5, 1)
)
if mibBuilder.loadTexts:
    mxp1Ux60.setStatus("current")
_Mxp1U160Family_ObjectIdentity = ObjectIdentity
mxp1U160Family = _Mxp1U160Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 5, 1, 1)
)
if mibBuilder.loadTexts:
    mxp1U160Family.setStatus("current")
_Mxp1U160_ObjectIdentity = ObjectIdentity
mxp1U160 = _Mxp1U160_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mxp1U160.setStatus("current")
_Mxp1U260Family_ObjectIdentity = ObjectIdentity
mxp1U260Family = _Mxp1U260Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 5, 1, 2)
)
if mibBuilder.loadTexts:
    mxp1U260Family.setStatus("current")
_Mxp1U260_ObjectIdentity = ObjectIdentity
mxp1U260 = _Mxp1U260_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mxp1U260.setStatus("current")
_Mxp1Ux80_ObjectIdentity = ObjectIdentity
mxp1Ux80 = _Mxp1Ux80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 5, 2)
)
if mibBuilder.loadTexts:
    mxp1Ux80.setStatus("current")
_Mxp1U180_ObjectIdentity = ObjectIdentity
mxp1U180 = _Mxp1U180_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mxp1U180.setStatus("current")
_Mxp1U280_ObjectIdentity = ObjectIdentity
mxp1U280 = _Mxp1U280_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 5, 2, 2)
)
if mibBuilder.loadTexts:
    mxp1U280.setStatus("current")
_Mxp1U180_TP_RJ45_ObjectIdentity = ObjectIdentity
mxp1U180_TP_RJ45 = _Mxp1U180_TP_RJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 5, 2, 3)
)
if mibBuilder.loadTexts:
    mxp1U180_TP_RJ45.setStatus("current")
_Mxp1U280_TP_RJ45_ObjectIdentity = ObjectIdentity
mxp1U280_TP_RJ45 = _Mxp1U280_TP_RJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 5, 2, 4)
)
if mibBuilder.loadTexts:
    mxp1U280_TP_RJ45.setStatus("current")
_Mxp1Ux5x_ObjectIdentity = ObjectIdentity
mxp1Ux5x = _Mxp1Ux5x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 5, 3)
)
if mibBuilder.loadTexts:
    mxp1Ux5x.setStatus("current")
_Mxp1U15xFamily_ObjectIdentity = ObjectIdentity
mxp1U15xFamily = _Mxp1U15xFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 5, 3, 1)
)
if mibBuilder.loadTexts:
    mxp1U15xFamily.setStatus("current")
_Mxp1U150_ObjectIdentity = ObjectIdentity
mxp1U150 = _Mxp1U150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 1, 7, 5, 3, 1, 1)
)
if mibBuilder.loadTexts:
    mxp1U150.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZhoneProductRegistrations",
    **{"ban-2000": ban_2000,
       "zedge64": zedge64,
       "zedge64-SHDSL-FXS": zedge64_SHDSL_FXS,
       "zedge64-SHDSL-BRI": zedge64_SHDSL_BRI,
       "zedge64-T1-FXS": zedge64_T1_FXS,
       "zedge64-E1-FXS": zedge64_E1_FXS,
       "zedge6200": zedge6200,
       "zedge6200-IP-T1": zedge6200_IP_T1,
       "zedge6200-IP-EM": zedge6200_IP_EM,
       "zedge6200-IP-FXS": zedge6200_IP_FXS,
       "zrg3xx": zrg3xx,
       "zrg300-IDU": zrg300_IDU,
       "zrg300-ODU": zrg300_ODU,
       "zrg5xx": zrg5xx,
       "zrg500-IDU": zrg500_IDU,
       "zrg500-ODU": zrg500_ODU,
       "zrg7xx": zrg7xx,
       "zrg700-IDU": zrg700_IDU,
       "zrg700-ODU": zrg700_ODU,
       "zrg6xx": zrg6xx,
       "zrg600-IDU": zrg600_IDU,
       "zrg600-ODU": zrg600_ODU,
       "zrg8xx": zrg8xx,
       "zrg800-IDU": zrg800_IDU,
       "zrg800-ODU": zrg800_ODU,
       "ethXtendxx": ethXtendxx,
       "ethXtendShdsl": ethXtendShdsl,
       "ethXtendT1E1": ethXtendT1E1,
       "ethXtend30xx": ethXtend30xx,
       "ethXtend31xx": ethXtend31xx,
       "ethXtend32xx": ethXtend32xx,
       "znid": znid,
       "znid42xx": znid42xx,
       "znidGPON42xx": znidGPON42xx,
       "znidEth422x": znidEth422x,
       "znid420x": znid420x,
       "znidGPON420x": znidGPON420x,
       "znidNextGen": znidNextGen,
       "znidNextGen22xx": znidNextGen22xx,
       "znidNextGenGE22xx": znidNextGenGE22xx,
       "znidNextGen42xx": znidNextGen42xx,
       "znidNextGenGPON42xx": znidNextGenGPON42xx,
       "znidNextGenGE42xx": znidNextGenGE42xx,
       "znidNextGen9xxx": znidNextGen9xxx,
       "znidNextGenGPON9xxx": znidNextGenGPON9xxx,
       "znidNextGenGE9xxx": znidNextGenGE9xxx,
       "znidNextGenGPON94xx": znidNextGenGPON94xx,
       "znidNextGenGE94xx": znidNextGenGE94xx,
       "znidNextGenGPON97xx": znidNextGenGPON97xx,
       "znidNextGenGE97xx": znidNextGenGE97xx,
       "fiberJack": fiberJack,
       "znidNextGen21xx": znidNextGen21xx,
       "znidNextGenGPON21xx": znidNextGenGPON21xx,
       "znidNextGenGE21xx": znidNextGenGE21xx,
       "znidNextGen24xx": znidNextGen24xx,
       "znidNextGenGPON24xx": znidNextGenGPON24xx,
       "znidNextGenGE24xx": znidNextGenGE24xx,
       "znidNextGen26xx": znidNextGen26xx,
       "znidNextGenGPON26xx": znidNextGenGPON26xx,
       "znidNextGenGE26xx": znidNextGenGE26xx,
       "z-plex10B": z_plex10B,
       "z-plex10B-FXS-FXO": z_plex10B_FXS_FXO,
       "z-plex10B-FXS": z_plex10B_FXS,
       "sechtor-100": sechtor_100,
       "s100-ATM-SM-16T1": s100_ATM_SM_16T1,
       "s100-ATM-SM-16E1": s100_ATM_SM_16E1,
       "sechtor-300": sechtor_300,
       "zhoneRegWtn": zhoneRegWtn,
       "node5700Mhz": node5700Mhz,
       "skyZhone45": skyZhone45,
       "oduTypeA": oduTypeA,
       "oduTypeB": oduTypeB,
       "node23000Mhz": node23000Mhz,
       "skyZhone8e1": skyZhone8e1,
       "oduTypeE1A": oduTypeE1A,
       "oduTypeE1B": oduTypeE1B,
       "skyZhone8e2": skyZhone8e2,
       "oduTypeE2A": oduTypeE2A,
       "oduTypeE2B": oduTypeE2B,
       "skyZhone8e3": skyZhone8e3,
       "oduTypeE3A": oduTypeE3A,
       "oduTypeE3B": oduTypeE3B,
       "skyZhone8e4": skyZhone8e4,
       "oduTypeE4A": oduTypeE4A,
       "oduTypeE4B": oduTypeE4B,
       "skyZhone8t1": skyZhone8t1,
       "oduTypeT1A": oduTypeT1A,
       "oduTypeT1B": oduTypeT1B,
       "skyZhone8t2": skyZhone8t2,
       "oduTypeT2A": oduTypeT2A,
       "oduTypeT2B": oduTypeT2B,
       "skyZhone8t3": skyZhone8t3,
       "oduTypeT3A": oduTypeT3A,
       "oduTypeT3B": oduTypeT3B,
       "skyZhone8t4": skyZhone8t4,
       "oduTypeT4A": oduTypeT4A,
       "oduTypeT4B": oduTypeT4B,
       "skyZhone155s1": skyZhone155s1,
       "oduTypeS1A": oduTypeS1A,
       "oduTypeS1B": oduTypeS1B,
       "skyZhone155s2": skyZhone155s2,
       "oduTypeS2A": oduTypeS2A,
       "oduTypeS2B": oduTypeS2B,
       "skyZhone155s3": skyZhone155s3,
       "oduTypeS3A": oduTypeS3A,
       "oduTypeS3B": oduTypeS3B,
       "skyZhone155s4": skyZhone155s4,
       "oduTypeS4A": oduTypeS4A,
       "oduTypeS4B": oduTypeS4B,
       "skyZhone1xxx": skyZhone1xxx,
       "malc19": malc19,
       "malc23": malc23,
       "malc319": malc319,
       "raptor319A": raptor319A,
       "raptor319I": raptor319I,
       "raptor719A": raptor719A,
       "raptor719I": raptor719I,
       "raptor723A": raptor723A,
       "raptor723I": raptor723I,
       "raptor100A": raptor100A,
       "raptor100I": raptor100I,
       "raptor100LP": raptor100LP,
       "raptor50Gshdsl": raptor50Gshdsl,
       "isc303": isc303,
       "r100adsl2Pxxx": r100adsl2Pxxx,
       "r100adsl2pip": r100adsl2pip,
       "r100adsl2phdsl4": r100adsl2phdsl4,
       "r100adsl2pt1ima": r100adsl2pt1ima,
       "r100adsl2pgige": r100adsl2pgige,
       "r100adsl2pgm": r100adsl2pgm,
       "r100adsl2pgte": r100adsl2pgte,
       "r100adsl2panxb": r100adsl2panxb,
       "m100": m100,
       "m100adsl2pxxx": m100adsl2pxxx,
       "m100adsl2pgige": m100adsl2pgige,
       "m100adsl2pgm": m100adsl2pgm,
       "m100Adsl2pAnxB": m100Adsl2pAnxB,
       "m100Vdsl2xxx": m100Vdsl2xxx,
       "m100vdsl2gm": m100vdsl2gm,
       "r100Vdsl2xx": r100Vdsl2xx,
       "r100vdsl2gm": r100vdsl2gm,
       "fiberSlam": fiberSlam,
       "fs105": fs105,
       "fs101": fs101,
       "raptorXP": raptorXP,
       "raptorXP150A": raptorXP150A,
       "raptorXP150A_ISP": raptorXP150A_ISP,
       "raptorXP150A_OSP": raptorXP150A_OSP,
       "raptorXP350A": raptorXP350A,
       "raptorXP350A_ISP": raptorXP350A_ISP,
       "raptorXP350A_OSP": raptorXP350A_OSP,
       "raptorXP160": raptorXP160,
       "raptorXP160_ISP": raptorXP160_ISP,
       "raptorXP160_OSP": raptorXP160_OSP,
       "raptorXP170": raptorXP170,
       "raptorXP170_WC": raptorXP170_WC,
       "raptorXP170_ISP_WC": raptorXP170_ISP_WC,
       "raptorXP170_OSP_WC": raptorXP170_OSP_WC,
       "raptorXP170_WC_SD": raptorXP170_WC_SD,
       "raptorXP170_ISP_WC_SD": raptorXP170_ISP_WC_SD,
       "raptorXP170_OSP_WC_SD": raptorXP170_OSP_WC_SD,
       "raptorXP170_LP": raptorXP170_LP,
       "raptorXP170_ISP_LP": raptorXP170_ISP_LP,
       "raptorXP170_OSP_LP": raptorXP170_OSP_LP,
       "raptorXP170_LP_SD": raptorXP170_LP_SD,
       "raptorXP170_ISP_LP_SD": raptorXP170_ISP_LP_SD,
       "raptorXP170_OSP_LP_SD": raptorXP170_OSP_LP_SD,
       "malcXP": malcXP,
       "malcXP150A": malcXP150A,
       "malcXP150A_ISP": malcXP150A_ISP,
       "malcXP150A_OSP": malcXP150A_OSP,
       "malcXP350A": malcXP350A,
       "malcXP350A_ISP": malcXP350A_ISP,
       "malcXP350A_OSP": malcXP350A_OSP,
       "malcXP160": malcXP160,
       "malcXP160_ISP": malcXP160_ISP,
       "malcXP160_OSP": malcXP160_OSP,
       "zhoneRegMxNextGen": zhoneRegMxNextGen,
       "mx19": mx19,
       "mx23": mx23,
       "mx319": mx319,
       "mx1U": mx1U,
       "mx1Ux6x": mx1Ux6x,
       "mx1U16x": mx1U16x,
       "mx1U160": mx1U160,
       "mx1U161": mx1U161,
       "mx1U162": mx1U162,
       "mx1U26x": mx1U26x,
       "mx1U260": mx1U260,
       "mx1U261": mx1U261,
       "mx1U262": mx1U262,
       "mx1Ux80": mx1Ux80,
       "mx1U180": mx1U180,
       "mx1U280": mx1U280,
       "mx1U180_TP_RJ45": mx1U180_TP_RJ45,
       "mx1U280_TP_RJ45": mx1U280_TP_RJ45,
       "mx1U180_LT_TP_RJ45": mx1U180_LT_TP_RJ45,
       "mx1U280_LT_TP_RJ45": mx1U280_LT_TP_RJ45,
       "mx1U19x": mx1U19x,
       "mx1U194": mx1U194,
       "mx1U198": mx1U198,
       "mx1U194_10GE": mx1U194_10GE,
       "mx1U198_10GE": mx1U198_10GE,
       "mx1U194_TOP": mx1U194_TOP,
       "mx1U198_TOP": mx1U198_TOP,
       "mx1U194_10GE_TOP": mx1U194_10GE_TOP,
       "mx1U198_10GE_TOP": mx1U198_10GE_TOP,
       "mx1Ux5x": mx1Ux5x,
       "mx1U15x": mx1U15x,
       "mx1U150": mx1U150,
       "mx1U151": mx1U151,
       "mx1U152": mx1U152,
       "mxp1U": mxp1U,
       "mxp1Ux60": mxp1Ux60,
       "mxp1U160Family": mxp1U160Family,
       "mxp1U160": mxp1U160,
       "mxp1U260Family": mxp1U260Family,
       "mxp1U260": mxp1U260,
       "mxp1Ux80": mxp1Ux80,
       "mxp1U180": mxp1U180,
       "mxp1U280": mxp1U280,
       "mxp1U180_TP_RJ45": mxp1U180_TP_RJ45,
       "mxp1U280_TP_RJ45": mxp1U280_TP_RJ45,
       "mxp1Ux5x": mxp1Ux5x,
       "mxp1U15xFamily": mxp1U15xFamily,
       "mxp1U150": mxp1U150,
       "zhoneRegistrationsModule": zhoneRegistrationsModule}
)
