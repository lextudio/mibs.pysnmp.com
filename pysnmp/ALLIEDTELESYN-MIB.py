# SNMP MIB module (ALLIEDTELESYN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALLIEDTELESYN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:43 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 NotificationType,
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
    "NotificationType",
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



class InterfaceIndexOrZero(Integer32):
    """Custom type InterfaceIndexOrZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlliedTelesyn_ObjectIdentity = ObjectIdentity
alliedTelesyn = _AlliedTelesyn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1)
)
_BridgeRouter_ObjectIdentity = ObjectIdentity
bridgeRouter = _BridgeRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1)
)
_CentreCOM_AR300Router_ObjectIdentity = ObjectIdentity
centreCOM_AR300Router = _CentreCOM_AR300Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 8)
)
_CentreCOM_AR720Router_ObjectIdentity = ObjectIdentity
centreCOM_AR720Router = _CentreCOM_AR720Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 11)
)
_CentreCOM_AR300LRouter_ObjectIdentity = ObjectIdentity
centreCOM_AR300LRouter = _CentreCOM_AR300LRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 12)
)
_CentreCOM_AR310Router_ObjectIdentity = ObjectIdentity
centreCOM_AR310Router = _CentreCOM_AR310Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 13)
)
_CentreCOM_AR300LURouter_ObjectIdentity = ObjectIdentity
centreCOM_AR300LURouter = _CentreCOM_AR300LURouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 14)
)
_CentreCOM_AR300URouter_ObjectIdentity = ObjectIdentity
centreCOM_AR300URouter = _CentreCOM_AR300URouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 15)
)
_CentreCOM_AR310URouter_ObjectIdentity = ObjectIdentity
centreCOM_AR310URouter = _CentreCOM_AR310URouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 16)
)
_CentreCOM_AR350Router_ObjectIdentity = ObjectIdentity
centreCOM_AR350Router = _CentreCOM_AR350Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 17)
)
_CentreCOM_AR370Router_ObjectIdentity = ObjectIdentity
centreCOM_AR370Router = _CentreCOM_AR370Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 18)
)
_CentreCOM_AR330Router_ObjectIdentity = ObjectIdentity
centreCOM_AR330Router = _CentreCOM_AR330Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 19)
)
_CentreCOM_AR395Router_ObjectIdentity = ObjectIdentity
centreCOM_AR395Router = _CentreCOM_AR395Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 20)
)
_CentreCOM_AR390Router_ObjectIdentity = ObjectIdentity
centreCOM_AR390Router = _CentreCOM_AR390Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 21)
)
_CentreCOM_AR370URouter_ObjectIdentity = ObjectIdentity
centreCOM_AR370URouter = _CentreCOM_AR370URouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 22)
)
_CentreCOM_AR740Router_ObjectIdentity = ObjectIdentity
centreCOM_AR740Router = _CentreCOM_AR740Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 23)
)
_CentreCOM_AR140SRouter_ObjectIdentity = ObjectIdentity
centreCOM_AR140SRouter = _CentreCOM_AR140SRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 24)
)
_CentreCOM_AR140URouter_ObjectIdentity = ObjectIdentity
centreCOM_AR140URouter = _CentreCOM_AR140URouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 25)
)
_CentreCOM_AR320Router_ObjectIdentity = ObjectIdentity
centreCOM_AR320Router = _CentreCOM_AR320Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 26)
)
_CentreCOM_AR130SRouter_ObjectIdentity = ObjectIdentity
centreCOM_AR130SRouter = _CentreCOM_AR130SRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 27)
)
_CentreCOM_AR130URouter_ObjectIdentity = ObjectIdentity
centreCOM_AR130URouter = _CentreCOM_AR130URouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 28)
)
_CentreCOM_AR160Router_ObjectIdentity = ObjectIdentity
centreCOM_AR160Router = _CentreCOM_AR160Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 29)
)
_At_AR740RouterDC_ObjectIdentity = ObjectIdentity
at_AR740RouterDC = _At_AR740RouterDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 43)
)
_CentreCOM_AR120Router_ObjectIdentity = ObjectIdentity
centreCOM_AR120Router = _CentreCOM_AR120Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 44)
)
_At_AR410Router_ObjectIdentity = ObjectIdentity
at_AR410Router = _At_AR410Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 47)
)
_At_AR725Router_ObjectIdentity = ObjectIdentity
at_AR725Router = _At_AR725Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 48)
)
_At_AR745Router_ObjectIdentity = ObjectIdentity
at_AR745Router = _At_AR745Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 49)
)
_At_AR410v2Router_ObjectIdentity = ObjectIdentity
at_AR410v2Router = _At_AR410v2Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 50)
)
_At_AR410v3Router_ObjectIdentity = ObjectIdentity
at_AR410v3Router = _At_AR410v3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 51)
)
_At_AR725RouterDC_ObjectIdentity = ObjectIdentity
at_AR725RouterDC = _At_AR725RouterDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 52)
)
_At_AR745RouterDC_ObjectIdentity = ObjectIdentity
at_AR745RouterDC = _At_AR745RouterDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 53)
)
_At_AR450Router_ObjectIdentity = ObjectIdentity
at_AR450Router = _At_AR450Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 54)
)
_At_AR450DualRouter_ObjectIdentity = ObjectIdentity
at_AR450DualRouter = _At_AR450DualRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 55)
)
_At_AR440Router_ObjectIdentity = ObjectIdentity
at_AR440Router = _At_AR440Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 59)
)
_At_AR441Router_ObjectIdentity = ObjectIdentity
at_AR441Router = _At_AR441Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 60)
)
_At_AR442Router_ObjectIdentity = ObjectIdentity
at_AR442Router = _At_AR442Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 61)
)
_At_AR443Router_ObjectIdentity = ObjectIdentity
at_AR443Router = _At_AR443Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 62)
)
_At_AR444Router_ObjectIdentity = ObjectIdentity
at_AR444Router = _At_AR444Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 63)
)
_At_AR420Router_ObjectIdentity = ObjectIdentity
at_AR420Router = _At_AR420Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 64)
)
_At_AR550Router_ObjectIdentity = ObjectIdentity
at_AR550Router = _At_AR550Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 73)
)
_At_AR551Router_ObjectIdentity = ObjectIdentity
at_AR551Router = _At_AR551Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 74)
)
_At_AR552Router_ObjectIdentity = ObjectIdentity
at_AR552Router = _At_AR552Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 75)
)
_RouterSwitch_ObjectIdentity = ObjectIdentity
routerSwitch = _RouterSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14)
)
_At_Rapier24_ObjectIdentity = ObjectIdentity
at_Rapier24 = _At_Rapier24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 1)
)
_At_Rapier16fSC_ObjectIdentity = ObjectIdentity
at_Rapier16fSC = _At_Rapier16fSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 2)
)
_At_Rapier16fVF_ObjectIdentity = ObjectIdentity
at_Rapier16fVF = _At_Rapier16fVF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 3)
)
_At_Rapier16fMT_ObjectIdentity = ObjectIdentity
at_Rapier16fMT = _At_Rapier16fMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 4)
)
_At_Rapier48_ObjectIdentity = ObjectIdentity
at_Rapier48 = _At_Rapier48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 5)
)
_At_Rapier8t8fSC_ObjectIdentity = ObjectIdentity
at_Rapier8t8fSC = _At_Rapier8t8fSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 6)
)
_At_Rapier8t8fSCi_ObjectIdentity = ObjectIdentity
at_Rapier8t8fSCi = _At_Rapier8t8fSCi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 7)
)
_At_Rapier8t8fMT_ObjectIdentity = ObjectIdentity
at_Rapier8t8fMT = _At_Rapier8t8fMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 8)
)
_At_Rapier8t8fMTi_ObjectIdentity = ObjectIdentity
at_Rapier8t8fMTi = _At_Rapier8t8fMTi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 9)
)
_At_Rapier8fSC_ObjectIdentity = ObjectIdentity
at_Rapier8fSC = _At_Rapier8fSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 10)
)
_At_Rapier8fSCi_ObjectIdentity = ObjectIdentity
at_Rapier8fSCi = _At_Rapier8fSCi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 11)
)
_At_Rapier8fMT_ObjectIdentity = ObjectIdentity
at_Rapier8fMT = _At_Rapier8fMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 12)
)
_At_Rapier8fMTi_ObjectIdentity = ObjectIdentity
at_Rapier8fMTi = _At_Rapier8fMTi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 13)
)
_At_Rapier16fMTi_ObjectIdentity = ObjectIdentity
at_Rapier16fMTi = _At_Rapier16fMTi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 14)
)
_At_RapierG6_ObjectIdentity = ObjectIdentity
at_RapierG6 = _At_RapierG6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 15)
)
_At_RapierG6SX_ObjectIdentity = ObjectIdentity
at_RapierG6SX = _At_RapierG6SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 16)
)
_At_RapierG6LX_ObjectIdentity = ObjectIdentity
at_RapierG6LX = _At_RapierG6LX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 17)
)
_At_RapierG6MT_ObjectIdentity = ObjectIdentity
at_RapierG6MT = _At_RapierG6MT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 18)
)
_At_Rapier16fSCi_ObjectIdentity = ObjectIdentity
at_Rapier16fSCi = _At_Rapier16fSCi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 19)
)
_At_Rapier24i_ObjectIdentity = ObjectIdentity
at_Rapier24i = _At_Rapier24i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 20)
)
_At_Rapier48i_ObjectIdentity = ObjectIdentity
at_Rapier48i = _At_Rapier48i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 21)
)
_At_Switchblade4AC_ObjectIdentity = ObjectIdentity
at_Switchblade4AC = _At_Switchblade4AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 22)
)
_At_Switchblade4DC_ObjectIdentity = ObjectIdentity
at_Switchblade4DC = _At_Switchblade4DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 23)
)
_At_Switchblade8AC_ObjectIdentity = ObjectIdentity
at_Switchblade8AC = _At_Switchblade8AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 24)
)
_At_Switchblade8DC_ObjectIdentity = ObjectIdentity
at_Switchblade8DC = _At_Switchblade8DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 25)
)
_At_9816GF_ObjectIdentity = ObjectIdentity
at_9816GF = _At_9816GF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 26)
)
_At_9812TF_ObjectIdentity = ObjectIdentity
at_9812TF = _At_9812TF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 27)
)
_At_9816GB_ObjectIdentity = ObjectIdentity
at_9816GB = _At_9816GB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 28)
)
_At_9812T_ObjectIdentity = ObjectIdentity
at_9812T = _At_9812T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 29)
)
_At_8724XL_ObjectIdentity = ObjectIdentity
at_8724XL = _At_8724XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 30)
)
_At_8748XL_ObjectIdentity = ObjectIdentity
at_8748XL = _At_8748XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 31)
)
_At_8724XLDC_ObjectIdentity = ObjectIdentity
at_8724XLDC = _At_8724XLDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 32)
)
_At_8748XLDC_ObjectIdentity = ObjectIdentity
at_8748XLDC = _At_8748XLDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 33)
)
_At_9816GB_DC_ObjectIdentity = ObjectIdentity
at_9816GB_DC = _At_9816GB_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 34)
)
_At_9812T_DC_ObjectIdentity = ObjectIdentity
at_9812T_DC = _At_9812T_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 35)
)
_At_8824_ObjectIdentity = ObjectIdentity
at_8824 = _At_8824_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 36)
)
_At_8848_ObjectIdentity = ObjectIdentity
at_8848 = _At_8848_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 37)
)
_At_8824_DC_ObjectIdentity = ObjectIdentity
at_8824_DC = _At_8824_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 38)
)
_At_8848_DC_ObjectIdentity = ObjectIdentity
at_8848_DC = _At_8848_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 39)
)
_At_8624XL_80_ObjectIdentity = ObjectIdentity
at_8624XL_80 = _At_8624XL_80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 41)
)
_At_8724XL_80_ObjectIdentity = ObjectIdentity
at_8724XL_80 = _At_8724XL_80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 42)
)
_At_8748XL_80_ObjectIdentity = ObjectIdentity
at_8748XL_80 = _At_8748XL_80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 43)
)
_At_8948EX_ObjectIdentity = ObjectIdentity
at_8948EX = _At_8948EX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 44)
)
_At_8948MX_ObjectIdentity = ObjectIdentity
at_8948MX = _At_8948MX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 45)
)
_At_8624T2M_ObjectIdentity = ObjectIdentity
at_8624T2M = _At_8624T2M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 46)
)
_At_Rapier24i_DC_NEBS_ObjectIdentity = ObjectIdentity
at_Rapier24i_DC_NEBS = _At_Rapier24i_DC_NEBS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 47)
)
_At_8724XL_DC_NEBS_ObjectIdentity = ObjectIdentity
at_8724XL_DC_NEBS = _At_8724XL_DC_NEBS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 48)
)
_At_9924T_ObjectIdentity = ObjectIdentity
at_9924T = _At_9924T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 49)
)
_At_9924SP_ObjectIdentity = ObjectIdentity
at_9924SP = _At_9924SP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 50)
)
_At_9924T_4SP_ObjectIdentity = ObjectIdentity
at_9924T_4SP = _At_9924T_4SP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 51)
)
_At_9924TEMC_ObjectIdentity = ObjectIdentity
at_9924TEMC = _At_9924TEMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 53)
)
_At_8724MLB_ObjectIdentity = ObjectIdentity
at_8724MLB = _At_8724MLB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 55)
)
_At_8624POE_ObjectIdentity = ObjectIdentity
at_8624POE = _At_8624POE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 56)
)
_At_86482SP_ObjectIdentity = ObjectIdentity
at_86482SP = _At_86482SP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 58)
)
_MibObject_ObjectIdentity = ObjectIdentity
mibObject = _MibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8)
)
_BrouterMib_ObjectIdentity = ObjectIdentity
brouterMib = _BrouterMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4)
)
_AtRouter_ObjectIdentity = ObjectIdentity
atRouter = _AtRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4)
)
_Objects_ObjectIdentity = ObjectIdentity
objects = _Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1)
)
_Boards_ObjectIdentity = ObjectIdentity
boards = _Boards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1)
)
_PprIcmAr023_ObjectIdentity = ObjectIdentity
pprIcmAr023 = _PprIcmAr023_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 39)
)
_PprIcmAr021s_ObjectIdentity = ObjectIdentity
pprIcmAr021s = _PprIcmAr021s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 40)
)
_PprIcmAr022_ObjectIdentity = ObjectIdentity
pprIcmAr022 = _PprIcmAr022_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 41)
)
_PprIcmAr025_ObjectIdentity = ObjectIdentity
pprIcmAr025 = _PprIcmAr025_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 45)
)
_PprIcmAr024_ObjectIdentity = ObjectIdentity
pprIcmAr024 = _PprIcmAr024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 46)
)
_PprAr300_ObjectIdentity = ObjectIdentity
pprAr300 = _PprAr300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 49)
)
_PprAr300L_ObjectIdentity = ObjectIdentity
pprAr300L = _PprAr300L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 52)
)
_PprAr310_ObjectIdentity = ObjectIdentity
pprAr310 = _PprAr310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 53)
)
_PprAr120_ObjectIdentity = ObjectIdentity
pprAr120 = _PprAr120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 54)
)
_PprAr300Lu_ObjectIdentity = ObjectIdentity
pprAr300Lu = _PprAr300Lu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 55)
)
_PprAr300u_ObjectIdentity = ObjectIdentity
pprAr300u = _PprAr300u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 56)
)
_PprAr310u_ObjectIdentity = ObjectIdentity
pprAr310u = _PprAr310u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 57)
)
_PprAr350_ObjectIdentity = ObjectIdentity
pprAr350 = _PprAr350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 58)
)
_PprIcmAr021u_ObjectIdentity = ObjectIdentity
pprIcmAr021u = _PprIcmAr021u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 59)
)
_PprAr720_ObjectIdentity = ObjectIdentity
pprAr720 = _PprAr720_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 63)
)
_PprAr010_ObjectIdentity = ObjectIdentity
pprAr010 = _PprAr010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 67)
)
_PprAr012_ObjectIdentity = ObjectIdentity
pprAr012 = _PprAr012_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 68)
)
_PprAr011_ObjectIdentity = ObjectIdentity
pprAr011 = _PprAr011_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 69)
)
_PprAr370_ObjectIdentity = ObjectIdentity
pprAr370 = _PprAr370_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 70)
)
_PprAr330_ObjectIdentity = ObjectIdentity
pprAr330 = _PprAr330_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 71)
)
_PprAr395_ObjectIdentity = ObjectIdentity
pprAr395 = _PprAr395_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 72)
)
_PprAr390_ObjectIdentity = ObjectIdentity
pprAr390 = _PprAr390_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 73)
)
_PprAr370u_ObjectIdentity = ObjectIdentity
pprAr370u = _PprAr370u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 75)
)
_PprIcmAr020_ObjectIdentity = ObjectIdentity
pprIcmAr020 = _PprIcmAr020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 76)
)
_PprAr740_ObjectIdentity = ObjectIdentity
pprAr740 = _PprAr740_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 79)
)
_PprAr140s_ObjectIdentity = ObjectIdentity
pprAr140s = _PprAr140s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 80)
)
_PprAr140u_ObjectIdentity = ObjectIdentity
pprAr140u = _PprAr140u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 81)
)
_PprAr160su_ObjectIdentity = ObjectIdentity
pprAr160su = _PprAr160su_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 82)
)
_PprAr320_ObjectIdentity = ObjectIdentity
pprAr320 = _PprAr320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 83)
)
_PprAr130s_ObjectIdentity = ObjectIdentity
pprAr130s = _PprAr130s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 85)
)
_PprAr130u_ObjectIdentity = ObjectIdentity
pprAr130u = _PprAr130u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 86)
)
_PprRapier24_ObjectIdentity = ObjectIdentity
pprRapier24 = _PprRapier24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 87)
)
_PprNsm0404Pic_ObjectIdentity = ObjectIdentity
pprNsm0404Pic = _PprNsm0404Pic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 88)
)
_PprA35SXSC_ObjectIdentity = ObjectIdentity
pprA35SXSC = _PprA35SXSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 89)
)
_PprA35LXSC_ObjectIdentity = ObjectIdentity
pprA35LXSC = _PprA35LXSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 90)
)
_PprA36MTRJ_ObjectIdentity = ObjectIdentity
pprA36MTRJ = _PprA36MTRJ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 91)
)
_PprA37VF45_ObjectIdentity = ObjectIdentity
pprA37VF45 = _PprA37VF45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 92)
)
_PprA38LC_ObjectIdentity = ObjectIdentity
pprA38LC = _PprA38LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 93)
)
_PprA39Tx_ObjectIdentity = ObjectIdentity
pprA39Tx = _PprA39Tx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 94)
)
_PprAr740DC_ObjectIdentity = ObjectIdentity
pprAr740DC = _PprAr740DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 95)
)
_PprNsm0418BRI_ObjectIdentity = ObjectIdentity
pprNsm0418BRI = _PprNsm0418BRI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 96)
)
_PprRapier16fSC_ObjectIdentity = ObjectIdentity
pprRapier16fSC = _PprRapier16fSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 97)
)
_Ppr8624xl80_ObjectIdentity = ObjectIdentity
ppr8624xl80 = _Ppr8624xl80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 98)
)
_PprRapier16fMT_ObjectIdentity = ObjectIdentity
pprRapier16fMT = _PprRapier16fMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 99)
)
_PprRapier16fMTi_ObjectIdentity = ObjectIdentity
pprRapier16fMTi = _PprRapier16fMTi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 100)
)
_PprRapier8t8fSC_ObjectIdentity = ObjectIdentity
pprRapier8t8fSC = _PprRapier8t8fSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 101)
)
_PprRapier8t8fSCi_ObjectIdentity = ObjectIdentity
pprRapier8t8fSCi = _PprRapier8t8fSCi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 102)
)
_PprRapier8t8fMT_ObjectIdentity = ObjectIdentity
pprRapier8t8fMT = _PprRapier8t8fMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 103)
)
_PprRapier8t8fMTi_ObjectIdentity = ObjectIdentity
pprRapier8t8fMTi = _PprRapier8t8fMTi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 104)
)
_PprRapier8fSC_ObjectIdentity = ObjectIdentity
pprRapier8fSC = _PprRapier8fSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 105)
)
_PprRapier8fSCi_ObjectIdentity = ObjectIdentity
pprRapier8fSCi = _PprRapier8fSCi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 106)
)
_PprRapier8fMT_ObjectIdentity = ObjectIdentity
pprRapier8fMT = _PprRapier8fMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 107)
)
_PprRapier8fMTi_ObjectIdentity = ObjectIdentity
pprRapier8fMTi = _PprRapier8fMTi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 108)
)
_PprRapierG6_ObjectIdentity = ObjectIdentity
pprRapierG6 = _PprRapierG6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 110)
)
_PprRapierG6SX_ObjectIdentity = ObjectIdentity
pprRapierG6SX = _PprRapierG6SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 111)
)
_PprRapierG6LX_ObjectIdentity = ObjectIdentity
pprRapierG6LX = _PprRapierG6LX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 112)
)
_PprRapierG6MT_ObjectIdentity = ObjectIdentity
pprRapierG6MT = _PprRapierG6MT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 113)
)
_PprRapier16fSCi_ObjectIdentity = ObjectIdentity
pprRapier16fSCi = _PprRapier16fSCi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 114)
)
_PprRapier24i_ObjectIdentity = ObjectIdentity
pprRapier24i = _PprRapier24i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 115)
)
_PprAr824_ObjectIdentity = ObjectIdentity
pprAr824 = _PprAr824_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 116)
)
_PprAr816fSC_ObjectIdentity = ObjectIdentity
pprAr816fSC = _PprAr816fSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 117)
)
_PprAr816fSCi_ObjectIdentity = ObjectIdentity
pprAr816fSCi = _PprAr816fSCi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 118)
)
_PprAr816fMT_ObjectIdentity = ObjectIdentity
pprAr816fMT = _PprAr816fMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 119)
)
_PprAr816fMTi_ObjectIdentity = ObjectIdentity
pprAr816fMTi = _PprAr816fMTi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 120)
)
_PprAr88t8fSC_ObjectIdentity = ObjectIdentity
pprAr88t8fSC = _PprAr88t8fSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 121)
)
_PprAr88t8fSCi_ObjectIdentity = ObjectIdentity
pprAr88t8fSCi = _PprAr88t8fSCi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 122)
)
_PprAr88t8fMT_ObjectIdentity = ObjectIdentity
pprAr88t8fMT = _PprAr88t8fMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 123)
)
_PprAr88t8fMTi_ObjectIdentity = ObjectIdentity
pprAr88t8fMTi = _PprAr88t8fMTi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 124)
)
_PprAr88fSC_ObjectIdentity = ObjectIdentity
pprAr88fSC = _PprAr88fSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 125)
)
_PprAr88fSCi_ObjectIdentity = ObjectIdentity
pprAr88fSCi = _PprAr88fSCi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 126)
)
_PprAr88fMT_ObjectIdentity = ObjectIdentity
pprAr88fMT = _PprAr88fMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 127)
)
_PprAr88fMTi_ObjectIdentity = ObjectIdentity
pprAr88fMTi = _PprAr88fMTi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 128)
)
_PprAr824i_ObjectIdentity = ObjectIdentity
pprAr824i = _PprAr824i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 129)
)
_PprAt8724XL_ObjectIdentity = ObjectIdentity
pprAt8724XL = _PprAt8724XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 130)
)
_PprAt8748XL_ObjectIdentity = ObjectIdentity
pprAt8748XL = _PprAt8748XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 131)
)
_PprAt8724XLDC_ObjectIdentity = ObjectIdentity
pprAt8724XLDC = _PprAt8724XLDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 132)
)
_PprAt8748XLDC_ObjectIdentity = ObjectIdentity
pprAt8748XLDC = _PprAt8748XLDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 133)
)
_PprAt8824_ObjectIdentity = ObjectIdentity
pprAt8824 = _PprAt8824_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 134)
)
_PprAt8824DC_ObjectIdentity = ObjectIdentity
pprAt8824DC = _PprAt8824DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 135)
)
_Ppr8724XLDC_ObjectIdentity = ObjectIdentity
ppr8724XLDC = _Ppr8724XLDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 141)
)
_Ppr8748XLDC_ObjectIdentity = ObjectIdentity
ppr8748XLDC = _Ppr8748XLDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 142)
)
_PprRapier24iDC_NEBS_ObjectIdentity = ObjectIdentity
pprRapier24iDC_NEBS = _PprRapier24iDC_NEBS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 144)
)
_PprAt8724XLDC_NEBS_ObjectIdentity = ObjectIdentity
pprAt8724XLDC_NEBS = _PprAt8724XLDC_NEBS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 146)
)
_PprAt8848DC_ObjectIdentity = ObjectIdentity
pprAt8848DC = _PprAt8848DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 147)
)
_PprRapier48_ObjectIdentity = ObjectIdentity
pprRapier48 = _PprRapier48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 148)
)
_PprAt8848_ObjectIdentity = ObjectIdentity
pprAt8848 = _PprAt8848_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 149)
)
_PprRapier48i_ObjectIdentity = ObjectIdentity
pprRapier48i = _PprRapier48i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 150)
)
_PprNsm0424BRI_ObjectIdentity = ObjectIdentity
pprNsm0424BRI = _PprNsm0424BRI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 151)
)
_PprIcmAR026_ObjectIdentity = ObjectIdentity
pprIcmAR026 = _PprIcmAR026_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 153)
)
_Ppr9816GF_ObjectIdentity = ObjectIdentity
ppr9816GF = _Ppr9816GF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 157)
)
_Ppr9812TF_ObjectIdentity = ObjectIdentity
ppr9812TF = _Ppr9812TF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 158)
)
_PprSbChassis4AC_ObjectIdentity = ObjectIdentity
pprSbChassis4AC = _PprSbChassis4AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 159)
)
_PprSbChassis4DC_ObjectIdentity = ObjectIdentity
pprSbChassis4DC = _PprSbChassis4DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 160)
)
_PprSbChassis8AC_ObjectIdentity = ObjectIdentity
pprSbChassis8AC = _PprSbChassis8AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 161)
)
_PprSbChassis8DC_ObjectIdentity = ObjectIdentity
pprSbChassis8DC = _PprSbChassis8DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 162)
)
_PprSbChassis16AC_ObjectIdentity = ObjectIdentity
pprSbChassis16AC = _PprSbChassis16AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 163)
)
_PprSbChassis16DC_ObjectIdentity = ObjectIdentity
pprSbChassis16DC = _PprSbChassis16DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 164)
)
_PprSbControl_ObjectIdentity = ObjectIdentity
pprSbControl = _PprSbControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 165)
)
_PprSbControlDTM_ObjectIdentity = ObjectIdentity
pprSbControlDTM = _PprSbControlDTM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 166)
)
_PprSb48t_ObjectIdentity = ObjectIdentity
pprSb48t = _PprSb48t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 167)
)
_PprSb96t_ObjectIdentity = ObjectIdentity
pprSb96t = _PprSb96t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 168)
)
_PprSb32fSC_ObjectIdentity = ObjectIdentity
pprSb32fSC = _PprSb32fSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 169)
)
_PprSb32fMT_ObjectIdentity = ObjectIdentity
pprSb32fMT = _PprSb32fMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 170)
)
_PprSb8fRJ_ObjectIdentity = ObjectIdentity
pprSb8fRJ = _PprSb8fRJ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 172)
)
_PprSb8fSXSC_ObjectIdentity = ObjectIdentity
pprSb8fSXSC = _PprSb8fSXSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 173)
)
_PprSb8fSXMT_ObjectIdentity = ObjectIdentity
pprSb8fSXMT = _PprSb8fSXMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 174)
)
_PprSb8fLXSC_ObjectIdentity = ObjectIdentity
pprSb8fLXSC = _PprSb8fLXSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 175)
)
_PprSb8fLXMT_ObjectIdentity = ObjectIdentity
pprSb8fLXMT = _PprSb8fLXMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 176)
)
_PprAr410_ObjectIdentity = ObjectIdentity
pprAr410 = _PprAr410_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 177)
)
_PprA40SC_ObjectIdentity = ObjectIdentity
pprA40SC = _PprA40SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 178)
)
_PprA40MTRJ_ObjectIdentity = ObjectIdentity
pprA40MTRJ = _PprA40MTRJ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 179)
)
_PprA41SC_ObjectIdentity = ObjectIdentity
pprA41SC = _PprA41SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 180)
)
_PprA41MTRJ_ObjectIdentity = ObjectIdentity
pprA41MTRJ = _PprA41MTRJ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 181)
)
_PprAr725_ObjectIdentity = ObjectIdentity
pprAr725 = _PprAr725_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 182)
)
_PprAr745_ObjectIdentity = ObjectIdentity
pprAr745 = _PprAr745_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 183)
)
_PprSb8GBIC_ObjectIdentity = ObjectIdentity
pprSb8GBIC = _PprSb8GBIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 184)
)
_PprA42GBIC_ObjectIdentity = ObjectIdentity
pprA42GBIC = _PprA42GBIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 185)
)
_Ppr9816GB_ObjectIdentity = ObjectIdentity
ppr9816GB = _Ppr9816GB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 186)
)
_Ppr9812T_ObjectIdentity = ObjectIdentity
ppr9812T = _Ppr9812T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 187)
)
_PprNsm048DS3_ObjectIdentity = ObjectIdentity
pprNsm048DS3 = _PprNsm048DS3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 188)
)
_PprAr450_ObjectIdentity = ObjectIdentity
pprAr450 = _PprAr450_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 191)
)
_PprAr450Dual_ObjectIdentity = ObjectIdentity
pprAr450Dual = _PprAr450Dual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 192)
)
_PprSbExpander_ObjectIdentity = ObjectIdentity
pprSbExpander = _PprSbExpander_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 193)
)
_PprAr725DC_ObjectIdentity = ObjectIdentity
pprAr725DC = _PprAr725DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 194)
)
_PprAr745DC_ObjectIdentity = ObjectIdentity
pprAr745DC = _PprAr745DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 195)
)
_PprAr410v2_ObjectIdentity = ObjectIdentity
pprAr410v2 = _PprAr410v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 196)
)
_PprAr410v3_ObjectIdentity = ObjectIdentity
pprAr410v3 = _PprAr410v3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 197)
)
_PprIcmAr027_ObjectIdentity = ObjectIdentity
pprIcmAr027 = _PprIcmAr027_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 198)
)
_Ppr8948EX_ObjectIdentity = ObjectIdentity
ppr8948EX = _Ppr8948EX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 202)
)
_Ppr8948MX_ObjectIdentity = ObjectIdentity
ppr8948MX = _Ppr8948MX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 203)
)
_Ppr9816GBDC_ObjectIdentity = ObjectIdentity
ppr9816GBDC = _Ppr9816GBDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 204)
)
_Ppr9812TDC_ObjectIdentity = ObjectIdentity
ppr9812TDC = _Ppr9812TDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 205)
)
_PprIcmAr021v2s_ObjectIdentity = ObjectIdentity
pprIcmAr021v2s = _PprIcmAr021v2s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 206)
)
_PprA50_ObjectIdentity = ObjectIdentity
pprA50 = _PprA50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 207)
)
_PprA51_ObjectIdentity = ObjectIdentity
pprA51 = _PprA51_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 208)
)
_PprA52_ObjectIdentity = ObjectIdentity
pprA52 = _PprA52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 209)
)
_PprA53_ObjectIdentity = ObjectIdentity
pprA53 = _PprA53_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 210)
)
_PprFanA01_ObjectIdentity = ObjectIdentity
pprFanA01 = _PprFanA01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 212)
)
_PprAtPwr01AC_ObjectIdentity = ObjectIdentity
pprAtPwr01AC = _PprAtPwr01AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 213)
)
_PprAtPwr01DC_ObjectIdentity = ObjectIdentity
pprAtPwr01DC = _PprAtPwr01DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 214)
)
_PprAtFan01_ObjectIdentity = ObjectIdentity
pprAtFan01 = _PprAtFan01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 215)
)
_PprSb24RJ_ObjectIdentity = ObjectIdentity
pprSb24RJ = _PprSb24RJ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 216)
)
_PprSb1XFP_ObjectIdentity = ObjectIdentity
pprSb1XFP = _PprSb1XFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 217)
)
_Ppr9924T_ObjectIdentity = ObjectIdentity
ppr9924T = _Ppr9924T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 218)
)
_Ppr9924SP_ObjectIdentity = ObjectIdentity
ppr9924SP = _Ppr9924SP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 219)
)
_Ppr9924TEMC_ObjectIdentity = ObjectIdentity
ppr9924TEMC = _Ppr9924TEMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 220)
)
_Ppr9924T4SP_ObjectIdentity = ObjectIdentity
ppr9924T4SP = _Ppr9924T4SP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 221)
)
_PprAR440_ObjectIdentity = ObjectIdentity
pprAR440 = _PprAR440_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 227)
)
_PprAR441_ObjectIdentity = ObjectIdentity
pprAR441 = _PprAR441_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 228)
)
_PprAR442_ObjectIdentity = ObjectIdentity
pprAR442 = _PprAR442_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 229)
)
_PprAR443_ObjectIdentity = ObjectIdentity
pprAR443 = _PprAR443_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 230)
)
_PprAR444_ObjectIdentity = ObjectIdentity
pprAR444 = _PprAR444_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 231)
)
_PprAR420_ObjectIdentity = ObjectIdentity
pprAR420 = _PprAR420_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 232)
)
_PprAt8624T2M_ObjectIdentity = ObjectIdentity
pprAt8624T2M = _PprAt8624T2M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 239)
)
_PprA46Tx_ObjectIdentity = ObjectIdentity
pprA46Tx = _PprA46Tx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 240)
)
_PprAR550_ObjectIdentity = ObjectIdentity
pprAR550 = _PprAR550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 241)
)
_PprAR551_ObjectIdentity = ObjectIdentity
pprAR551 = _PprAR551_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 242)
)
_PprAR552_ObjectIdentity = ObjectIdentity
pprAR552 = _PprAR552_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 243)
)
_PprC8724MLB_ObjectIdentity = ObjectIdentity
pprC8724MLB = _PprC8724MLB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 248)
)
_PprAt86482SP_ObjectIdentity = ObjectIdentity
pprAt86482SP = _PprAt86482SP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 252)
)
_PprAt8624POE_ObjectIdentity = ObjectIdentity
pprAt8624POE = _PprAt8624POE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 253)
)
_PprAtPwr01RAC_ObjectIdentity = ObjectIdentity
pprAtPwr01RAC = _PprAtPwr01RAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 254)
)
_PprAtFan01R_ObjectIdentity = ObjectIdentity
pprAtFan01R = _PprAtFan01R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 255)
)
_PprAtPwr02AC_ObjectIdentity = ObjectIdentity
pprAtPwr02AC = _PprAtPwr02AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 264)
)
_PprAtPwr02RAC_ObjectIdentity = ObjectIdentity
pprAtPwr02RAC = _PprAtPwr02RAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 265)
)
_PprSb24SFP_ObjectIdentity = ObjectIdentity
pprSb24SFP = _PprSb24SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 269)
)
_Release_ObjectIdentity = ObjectIdentity
release = _Release_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 2)
)
_Iftypes_ObjectIdentity = ObjectIdentity
iftypes = _Iftypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 3)
)
_IfaceEth_ObjectIdentity = ObjectIdentity
ifaceEth = _IfaceEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 3, 1)
)
_IfaceSyn_ObjectIdentity = ObjectIdentity
ifaceSyn = _IfaceSyn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 3, 2)
)
_IfaceAsyn_ObjectIdentity = ObjectIdentity
ifaceAsyn = _IfaceAsyn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 3, 3)
)
_IfaceBri_ObjectIdentity = ObjectIdentity
ifaceBri = _IfaceBri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 3, 4)
)
_IfacePri_ObjectIdentity = ObjectIdentity
ifacePri = _IfacePri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 3, 5)
)
_IfacePots_ObjectIdentity = ObjectIdentity
ifacePots = _IfacePots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 3, 6)
)
_IfaceGBIC_ObjectIdentity = ObjectIdentity
ifaceGBIC = _IfaceGBIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 3, 7)
)
_Chips_ObjectIdentity = ObjectIdentity
chips = _Chips_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4)
)
_Chip68020Cpu_ObjectIdentity = ObjectIdentity
chip68020Cpu = _Chip68020Cpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 1)
)
_Chip68340Cpu_ObjectIdentity = ObjectIdentity
chip68340Cpu = _Chip68340Cpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 2)
)
_Chip68302Cpu_ObjectIdentity = ObjectIdentity
chip68302Cpu = _Chip68302Cpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 3)
)
_Chip68360Cpu_ObjectIdentity = ObjectIdentity
chip68360Cpu = _Chip68360Cpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 4)
)
_Chip860TCpu_ObjectIdentity = ObjectIdentity
chip860TCpu = _Chip860TCpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 5)
)
_ChipRtc1_ObjectIdentity = ObjectIdentity
chipRtc1 = _ChipRtc1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 21)
)
_ChipRtc2_ObjectIdentity = ObjectIdentity
chipRtc2 = _ChipRtc2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 22)
)
_ChipRtc3_ObjectIdentity = ObjectIdentity
chipRtc3 = _ChipRtc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 23)
)
_ChipRtc4_ObjectIdentity = ObjectIdentity
chipRtc4 = _ChipRtc4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 24)
)
_ChipRam1mb_ObjectIdentity = ObjectIdentity
chipRam1mb = _ChipRam1mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 31)
)
_ChipRam2mb_ObjectIdentity = ObjectIdentity
chipRam2mb = _ChipRam2mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 32)
)
_ChipRam3mb_ObjectIdentity = ObjectIdentity
chipRam3mb = _ChipRam3mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 33)
)
_ChipRam4mb_ObjectIdentity = ObjectIdentity
chipRam4mb = _ChipRam4mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 34)
)
_ChipRam6mb_ObjectIdentity = ObjectIdentity
chipRam6mb = _ChipRam6mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 36)
)
_ChipRam8mb_ObjectIdentity = ObjectIdentity
chipRam8mb = _ChipRam8mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 38)
)
_ChipRam12mb_ObjectIdentity = ObjectIdentity
chipRam12mb = _ChipRam12mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 42)
)
_ChipRam16mb_ObjectIdentity = ObjectIdentity
chipRam16mb = _ChipRam16mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 46)
)
_ChipRam20mb_ObjectIdentity = ObjectIdentity
chipRam20mb = _ChipRam20mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 50)
)
_ChipRam32mb_ObjectIdentity = ObjectIdentity
chipRam32mb = _ChipRam32mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 62)
)
_ChipFlash1mb_ObjectIdentity = ObjectIdentity
chipFlash1mb = _ChipFlash1mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 71)
)
_ChipFlash2mb_ObjectIdentity = ObjectIdentity
chipFlash2mb = _ChipFlash2mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 72)
)
_ChipFlash3mb_ObjectIdentity = ObjectIdentity
chipFlash3mb = _ChipFlash3mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 73)
)
_ChipFlash4mb_ObjectIdentity = ObjectIdentity
chipFlash4mb = _ChipFlash4mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 74)
)
_ChipFlash6mb_ObjectIdentity = ObjectIdentity
chipFlash6mb = _ChipFlash6mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 76)
)
_ChipFlash8mb_ObjectIdentity = ObjectIdentity
chipFlash8mb = _ChipFlash8mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 78)
)
_ChipPem_ObjectIdentity = ObjectIdentity
chipPem = _ChipPem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 120)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 2)
)
_Sysinfo_ObjectIdentity = ObjectIdentity
sysinfo = _Sysinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3)
)
_FanAndPs_ObjectIdentity = ObjectIdentity
fanAndPs = _FanAndPs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1)
)


class _FanAndPsRpsConnectionStatus_Type(Integer32):
    """Custom type fanAndPsRpsConnectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("non-supported", 0),
          ("not-connected", 2),
          ("not-monitoring", 3))
    )


_FanAndPsRpsConnectionStatus_Type.__name__ = "Integer32"
_FanAndPsRpsConnectionStatus_Object = MibScalar
fanAndPsRpsConnectionStatus = _FanAndPsRpsConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 1),
    _FanAndPsRpsConnectionStatus_Type()
)
fanAndPsRpsConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsRpsConnectionStatus.setStatus("mandatory")


class _FanAndPsMainPSUStatus_Type(Integer32):
    """Custom type fanAndPsMainPSUStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 3),
          ("off", 2),
          ("on", 1))
    )


_FanAndPsMainPSUStatus_Type.__name__ = "Integer32"
_FanAndPsMainPSUStatus_Object = MibScalar
fanAndPsMainPSUStatus = _FanAndPsMainPSUStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 2),
    _FanAndPsMainPSUStatus_Type()
)
fanAndPsMainPSUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsMainPSUStatus.setStatus("mandatory")


class _FanAndPsRedundantPSUStatus_Type(Integer32):
    """Custom type fanAndPsRedundantPSUStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("non-supported", 0),
          ("not-monitoring", 3),
          ("off", 2),
          ("on", 1))
    )


_FanAndPsRedundantPSUStatus_Type.__name__ = "Integer32"
_FanAndPsRedundantPSUStatus_Object = MibScalar
fanAndPsRedundantPSUStatus = _FanAndPsRedundantPSUStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 3),
    _FanAndPsRedundantPSUStatus_Type()
)
fanAndPsRedundantPSUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsRedundantPSUStatus.setStatus("mandatory")


class _FanAndPsRpsMonitoringStatus_Type(Integer32):
    """Custom type fanAndPsRpsMonitoringStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-supported", 0),
          ("off", 2),
          ("on", 1))
    )


_FanAndPsRpsMonitoringStatus_Type.__name__ = "Integer32"
_FanAndPsRpsMonitoringStatus_Object = MibScalar
fanAndPsRpsMonitoringStatus = _FanAndPsRpsMonitoringStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 4),
    _FanAndPsRpsMonitoringStatus_Type()
)
fanAndPsRpsMonitoringStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanAndPsRpsMonitoringStatus.setStatus("mandatory")


class _FanAndPsMainFanStatus_Type(Integer32):
    """Custom type fanAndPsMainFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("non-supported", 0),
          ("not-ok", 2),
          ("ok", 1),
          ("warning", 3))
    )


_FanAndPsMainFanStatus_Type.__name__ = "Integer32"
_FanAndPsMainFanStatus_Object = MibScalar
fanAndPsMainFanStatus = _FanAndPsMainFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 5),
    _FanAndPsMainFanStatus_Type()
)
fanAndPsMainFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsMainFanStatus.setStatus("mandatory")


class _FanAndPsRedundantFanStatus_Type(Integer32):
    """Custom type fanAndPsRedundantFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("non-supported", 0),
          ("not-monitoring", 3),
          ("not-ok", 2),
          ("ok", 1))
    )


_FanAndPsRedundantFanStatus_Type.__name__ = "Integer32"
_FanAndPsRedundantFanStatus_Object = MibScalar
fanAndPsRedundantFanStatus = _FanAndPsRedundantFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 6),
    _FanAndPsRedundantFanStatus_Type()
)
fanAndPsRedundantFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsRedundantFanStatus.setStatus("mandatory")


class _FanAndPsTemperatureStatus_Type(Integer32):
    """Custom type fanAndPsTemperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-ok", 2),
          ("ok", 1))
    )


_FanAndPsTemperatureStatus_Type.__name__ = "Integer32"
_FanAndPsTemperatureStatus_Object = MibScalar
fanAndPsTemperatureStatus = _FanAndPsTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 7),
    _FanAndPsTemperatureStatus_Type()
)
fanAndPsTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsTemperatureStatus.setStatus("mandatory")


class _FanAndPsFanTrayPresent_Type(Integer32):
    """Custom type fanAndPsFanTrayPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-supported", 0),
          ("not-present", 2),
          ("present", 1))
    )


_FanAndPsFanTrayPresent_Type.__name__ = "Integer32"
_FanAndPsFanTrayPresent_Object = MibScalar
fanAndPsFanTrayPresent = _FanAndPsFanTrayPresent_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 8),
    _FanAndPsFanTrayPresent_Type()
)
fanAndPsFanTrayPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsFanTrayPresent.setStatus("mandatory")


class _FanAndPsFanTrayStatus_Type(Integer32):
    """Custom type fanAndPsFanTrayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-supported", 0),
          ("not-ok", 2),
          ("ok", 1))
    )


_FanAndPsFanTrayStatus_Type.__name__ = "Integer32"
_FanAndPsFanTrayStatus_Object = MibScalar
fanAndPsFanTrayStatus = _FanAndPsFanTrayStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 9),
    _FanAndPsFanTrayStatus_Type()
)
fanAndPsFanTrayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsFanTrayStatus.setStatus("mandatory")


class _FanAndPsMainMonitoringStatus_Type(Integer32):
    """Custom type fanAndPsMainMonitoringStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-supported", 0),
          ("not-ok", 2),
          ("ok", 1))
    )


_FanAndPsMainMonitoringStatus_Type.__name__ = "Integer32"
_FanAndPsMainMonitoringStatus_Object = MibScalar
fanAndPsMainMonitoringStatus = _FanAndPsMainMonitoringStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 10),
    _FanAndPsMainMonitoringStatus_Type()
)
fanAndPsMainMonitoringStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsMainMonitoringStatus.setStatus("mandatory")
_FanAndPsPsuStatusTable_Object = MibTable
fanAndPsPsuStatusTable = _FanAndPsPsuStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 11)
)
if mibBuilder.loadTexts:
    fanAndPsPsuStatusTable.setStatus("mandatory")
_FanAndPsPsuStatusEntry_Object = MibTableRow
fanAndPsPsuStatusEntry = _FanAndPsPsuStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 11, 1)
)
fanAndPsPsuStatusEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "fanAndPsPsuNumber"),
)
if mibBuilder.loadTexts:
    fanAndPsPsuStatusEntry.setStatus("mandatory")
_FanAndPsPsuNumber_Type = Integer32
_FanAndPsPsuNumber_Object = MibTableColumn
fanAndPsPsuNumber = _FanAndPsPsuNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 11, 1, 1),
    _FanAndPsPsuNumber_Type()
)
fanAndPsPsuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsPsuNumber.setStatus("mandatory")


class _FanAndPsPsuPresent_Type(Integer32):
    """Custom type fanAndPsPsuPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 0))
    )


_FanAndPsPsuPresent_Type.__name__ = "Integer32"
_FanAndPsPsuPresent_Object = MibTableColumn
fanAndPsPsuPresent = _FanAndPsPsuPresent_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 11, 1, 2),
    _FanAndPsPsuPresent_Type()
)
fanAndPsPsuPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsPsuPresent.setStatus("mandatory")


class _FanAndPsPsuType_Type(Integer32):
    """Custom type fanAndPsPsuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ac", 0),
          ("dc", 1),
          ("fan", 2),
          ("not-present", 3),
          ("not-supported", 4))
    )


_FanAndPsPsuType_Type.__name__ = "Integer32"
_FanAndPsPsuType_Object = MibTableColumn
fanAndPsPsuType = _FanAndPsPsuType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 11, 1, 3),
    _FanAndPsPsuType_Type()
)
fanAndPsPsuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsPsuType.setStatus("mandatory")


class _FanAndPsPsuFan_Type(Integer32):
    """Custom type fanAndPsPsuFan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 1),
          ("not-present", 2),
          ("not-supported", 3),
          ("ok", 0))
    )


_FanAndPsPsuFan_Type.__name__ = "Integer32"
_FanAndPsPsuFan_Object = MibTableColumn
fanAndPsPsuFan = _FanAndPsPsuFan_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 11, 1, 4),
    _FanAndPsPsuFan_Type()
)
fanAndPsPsuFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsPsuFan.setStatus("mandatory")


class _FanAndPsPsuTemperature_Type(Integer32):
    """Custom type fanAndPsPsuTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("good", 0),
          ("high", 1),
          ("not-present", 2),
          ("not-supported", 3))
    )


_FanAndPsPsuTemperature_Type.__name__ = "Integer32"
_FanAndPsPsuTemperature_Object = MibTableColumn
fanAndPsPsuTemperature = _FanAndPsPsuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 11, 1, 5),
    _FanAndPsPsuTemperature_Type()
)
fanAndPsPsuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsPsuTemperature.setStatus("mandatory")


class _FanAndPsPsuPower_Type(Integer32):
    """Custom type fanAndPsPsuPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bad", 1),
          ("good", 0),
          ("not-present", 2),
          ("not-supported", 3))
    )


_FanAndPsPsuPower_Type.__name__ = "Integer32"
_FanAndPsPsuPower_Object = MibTableColumn
fanAndPsPsuPower = _FanAndPsPsuPower_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 11, 1, 6),
    _FanAndPsPsuPower_Type()
)
fanAndPsPsuPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsPsuPower.setStatus("mandatory")


class _FanAndPsAccelFanStatus_Type(Integer32):
    """Custom type fanAndPsAccelFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-supported", 0),
          ("not-ok", 2),
          ("ok", 1))
    )


_FanAndPsAccelFanStatus_Type.__name__ = "Integer32"
_FanAndPsAccelFanStatus_Object = MibScalar
fanAndPsAccelFanStatus = _FanAndPsAccelFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 12),
    _FanAndPsAccelFanStatus_Type()
)
fanAndPsAccelFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsAccelFanStatus.setStatus("mandatory")


class _Restart_Type(Integer32):
    """Custom type restart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("restart-cold", 2),
          ("restart-none", 0),
          ("restart-warm", 1))
    )


_Restart_Type.__name__ = "Integer32"
_Restart_Object = MibScalar
restart = _Restart_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 2),
    _Restart_Type()
)
restart.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    restart.setStatus("mandatory")
_Cpu_ObjectIdentity = ObjectIdentity
cpu = _Cpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3)
)


class _CpuUtilisationMax_Type(Integer32):
    """Custom type cpuUtilisationMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuUtilisationMax_Type.__name__ = "Integer32"
_CpuUtilisationMax_Object = MibScalar
cpuUtilisationMax = _CpuUtilisationMax_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 1),
    _CpuUtilisationMax_Type()
)
cpuUtilisationMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilisationMax.setStatus("mandatory")


class _CpuUtilisationAvg_Type(Integer32):
    """Custom type cpuUtilisationAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuUtilisationAvg_Type.__name__ = "Integer32"
_CpuUtilisationAvg_Object = MibScalar
cpuUtilisationAvg = _CpuUtilisationAvg_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 2),
    _CpuUtilisationAvg_Type()
)
cpuUtilisationAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilisationAvg.setStatus("mandatory")


class _CpuUtilisationAvgLastMinute_Type(Integer32):
    """Custom type cpuUtilisationAvgLastMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuUtilisationAvgLastMinute_Type.__name__ = "Integer32"
_CpuUtilisationAvgLastMinute_Object = MibScalar
cpuUtilisationAvgLastMinute = _CpuUtilisationAvgLastMinute_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 3),
    _CpuUtilisationAvgLastMinute_Type()
)
cpuUtilisationAvgLastMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilisationAvgLastMinute.setStatus("mandatory")


class _CpuUtilisationAvgLast10Seconds_Type(Integer32):
    """Custom type cpuUtilisationAvgLast10Seconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuUtilisationAvgLast10Seconds_Type.__name__ = "Integer32"
_CpuUtilisationAvgLast10Seconds_Object = MibScalar
cpuUtilisationAvgLast10Seconds = _CpuUtilisationAvgLast10Seconds_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 4),
    _CpuUtilisationAvgLast10Seconds_Type()
)
cpuUtilisationAvgLast10Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilisationAvgLast10Seconds.setStatus("mandatory")


class _CpuUtilisationAvgLastSecond_Type(Integer32):
    """Custom type cpuUtilisationAvgLastSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuUtilisationAvgLastSecond_Type.__name__ = "Integer32"
_CpuUtilisationAvgLastSecond_Object = MibScalar
cpuUtilisationAvgLastSecond = _CpuUtilisationAvgLastSecond_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 5),
    _CpuUtilisationAvgLastSecond_Type()
)
cpuUtilisationAvgLastSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilisationAvgLastSecond.setStatus("mandatory")


class _CpuUtilisationMaxLast5Minutes_Type(Integer32):
    """Custom type cpuUtilisationMaxLast5Minutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuUtilisationMaxLast5Minutes_Type.__name__ = "Integer32"
_CpuUtilisationMaxLast5Minutes_Object = MibScalar
cpuUtilisationMaxLast5Minutes = _CpuUtilisationMaxLast5Minutes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 6),
    _CpuUtilisationMaxLast5Minutes_Type()
)
cpuUtilisationMaxLast5Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilisationMaxLast5Minutes.setStatus("mandatory")


class _CpuUtilisationAvgLast5Minutes_Type(Integer32):
    """Custom type cpuUtilisationAvgLast5Minutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuUtilisationAvgLast5Minutes_Type.__name__ = "Integer32"
_CpuUtilisationAvgLast5Minutes_Object = MibScalar
cpuUtilisationAvgLast5Minutes = _CpuUtilisationAvgLast5Minutes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 7),
    _CpuUtilisationAvgLast5Minutes_Type()
)
cpuUtilisationAvgLast5Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilisationAvgLast5Minutes.setStatus("mandatory")
_SysTemperature_ObjectIdentity = ObjectIdentity
sysTemperature = _SysTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4)
)
_GeneralTemperature_ObjectIdentity = ObjectIdentity
generalTemperature = _GeneralTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 1)
)


class _GeneralTemperatureSupported_Type(Integer32):
    """Custom type generalTemperatureSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-supported", 0),
          ("supported", 1))
    )


_GeneralTemperatureSupported_Type.__name__ = "Integer32"
_GeneralTemperatureSupported_Object = MibScalar
generalTemperatureSupported = _GeneralTemperatureSupported_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 1, 1),
    _GeneralTemperatureSupported_Type()
)
generalTemperatureSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generalTemperatureSupported.setStatus("mandatory")
_GeneralTemperatureActualTemp_Type = Integer32
_GeneralTemperatureActualTemp_Object = MibScalar
generalTemperatureActualTemp = _GeneralTemperatureActualTemp_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 1, 2),
    _GeneralTemperatureActualTemp_Type()
)
generalTemperatureActualTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generalTemperatureActualTemp.setStatus("mandatory")


class _GeneralTemperatureStatus_Type(Integer32):
    """Custom type generalTemperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-ok", 2),
          ("ok", 1))
    )


_GeneralTemperatureStatus_Type.__name__ = "Integer32"
_GeneralTemperatureStatus_Object = MibScalar
generalTemperatureStatus = _GeneralTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 1, 3),
    _GeneralTemperatureStatus_Type()
)
generalTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generalTemperatureStatus.setStatus("mandatory")
_GeneralTemperatureThreshold_Type = Integer32
_GeneralTemperatureThreshold_Object = MibScalar
generalTemperatureThreshold = _GeneralTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 1, 4),
    _GeneralTemperatureThreshold_Type()
)
generalTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generalTemperatureThreshold.setStatus("mandatory")
_SbTemperature_ObjectIdentity = ObjectIdentity
sbTemperature = _SbTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2)
)
_SbTempTable_Object = MibTable
sbTempTable = _SbTempTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    sbTempTable.setStatus("mandatory")
_SbTempEntry_Object = MibTableRow
sbTempEntry = _SbTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 1, 1)
)
sbTempEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "sbTempIndex"),
)
if mibBuilder.loadTexts:
    sbTempEntry.setStatus("mandatory")


class _SbTempIndex_Type(Integer32):
    """Custom type sbTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_SbTempIndex_Type.__name__ = "Integer32"
_SbTempIndex_Object = MibTableColumn
sbTempIndex = _SbTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 1, 1, 1),
    _SbTempIndex_Type()
)
sbTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbTempIndex.setStatus("mandatory")
_SbTempActualTemperature_Type = Integer32
_SbTempActualTemperature_Object = MibTableColumn
sbTempActualTemperature = _SbTempActualTemperature_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 1, 1, 2),
    _SbTempActualTemperature_Type()
)
sbTempActualTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbTempActualTemperature.setStatus("mandatory")


class _SbTempFixedThresholdStatus_Type(Integer32):
    """Custom type sbTempFixedThresholdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crossover", 2),
          ("normal", 1))
    )


_SbTempFixedThresholdStatus_Type.__name__ = "Integer32"
_SbTempFixedThresholdStatus_Object = MibTableColumn
sbTempFixedThresholdStatus = _SbTempFixedThresholdStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 1, 1, 3),
    _SbTempFixedThresholdStatus_Type()
)
sbTempFixedThresholdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbTempFixedThresholdStatus.setStatus("mandatory")


class _SbTempSettableThresholdStatus_Type(Integer32):
    """Custom type sbTempSettableThresholdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crossover", 2),
          ("normal", 1),
          ("undefined", 3))
    )


_SbTempSettableThresholdStatus_Type.__name__ = "Integer32"
_SbTempSettableThresholdStatus_Object = MibTableColumn
sbTempSettableThresholdStatus = _SbTempSettableThresholdStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 1, 1, 4),
    _SbTempSettableThresholdStatus_Type()
)
sbTempSettableThresholdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbTempSettableThresholdStatus.setStatus("mandatory")


class _SbTempSettableThreshold_Type(Integer32):
    """Custom type sbTempSettableThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 100),
    )


_SbTempSettableThreshold_Type.__name__ = "Integer32"
_SbTempSettableThreshold_Object = MibTableColumn
sbTempSettableThreshold = _SbTempSettableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 1, 1, 5),
    _SbTempSettableThreshold_Type()
)
sbTempSettableThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbTempSettableThreshold.setStatus("mandatory")
_SbTempFixedThreshold_Type = Integer32
_SbTempFixedThreshold_Object = MibScalar
sbTempFixedThreshold = _SbTempFixedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 2),
    _SbTempFixedThreshold_Type()
)
sbTempFixedThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbTempFixedThreshold.setStatus("mandatory")
_AcceleratorTemperature_ObjectIdentity = ObjectIdentity
acceleratorTemperature = _AcceleratorTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 3)
)


class _AcceleratorTemperatureSupported_Type(Integer32):
    """Custom type acceleratorTemperatureSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-supported", 0),
          ("supported", 1))
    )


_AcceleratorTemperatureSupported_Type.__name__ = "Integer32"
_AcceleratorTemperatureSupported_Object = MibScalar
acceleratorTemperatureSupported = _AcceleratorTemperatureSupported_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 3, 1),
    _AcceleratorTemperatureSupported_Type()
)
acceleratorTemperatureSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acceleratorTemperatureSupported.setStatus("mandatory")
_AcceleratorTemperatureActualTemp_Type = Integer32
_AcceleratorTemperatureActualTemp_Object = MibScalar
acceleratorTemperatureActualTemp = _AcceleratorTemperatureActualTemp_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 3, 2),
    _AcceleratorTemperatureActualTemp_Type()
)
acceleratorTemperatureActualTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acceleratorTemperatureActualTemp.setStatus("mandatory")


class _AcceleratorTemperatureStatus_Type(Integer32):
    """Custom type acceleratorTemperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-ok", 2),
          ("ok", 1))
    )


_AcceleratorTemperatureStatus_Type.__name__ = "Integer32"
_AcceleratorTemperatureStatus_Object = MibScalar
acceleratorTemperatureStatus = _AcceleratorTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 3, 3),
    _AcceleratorTemperatureStatus_Type()
)
acceleratorTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acceleratorTemperatureStatus.setStatus("mandatory")
_AcceleratorTemperatureThreshold_Type = Integer32
_AcceleratorTemperatureThreshold_Object = MibScalar
acceleratorTemperatureThreshold = _AcceleratorTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 3, 4),
    _AcceleratorTemperatureThreshold_Type()
)
acceleratorTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acceleratorTemperatureThreshold.setStatus("mandatory")


class _AtContactDetails_Type(DisplayString):
    """Custom type atContactDetails based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AtContactDetails_Type.__name__ = "DisplayString"
_AtContactDetails_Object = MibScalar
atContactDetails = _AtContactDetails_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 5),
    _AtContactDetails_Type()
)
atContactDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atContactDetails.setStatus("mandatory")
_BbrNvs_ObjectIdentity = ObjectIdentity
bbrNvs = _BbrNvs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 6)
)
_Memory_ObjectIdentity = ObjectIdentity
memory = _Memory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 7)
)


class _FreeMemory_Type(Integer32):
    """Custom type freeMemory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FreeMemory_Type.__name__ = "Integer32"
_FreeMemory_Object = MibScalar
freeMemory = _FreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 7, 1),
    _FreeMemory_Type()
)
freeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freeMemory.setStatus("mandatory")
_TotalBuffers_Type = Integer32
_TotalBuffers_Object = MibScalar
totalBuffers = _TotalBuffers_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 7, 2),
    _TotalBuffers_Type()
)
totalBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBuffers.setStatus("mandatory")


class _RealTimeClockStatus_Type(Integer32):
    """Custom type realTimeClockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("normal", 1))
    )


_RealTimeClockStatus_Type.__name__ = "Integer32"
_RealTimeClockStatus_Object = MibScalar
realTimeClockStatus = _RealTimeClockStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 8),
    _RealTimeClockStatus_Type()
)
realTimeClockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realTimeClockStatus.setStatus("mandatory")


class _HostId_Type(Integer32):
    """Custom type hostId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_HostId_Type.__name__ = "Integer32"
_HostId_Object = MibScalar
hostId = _HostId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 9),
    _HostId_Type()
)
hostId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostId.setStatus("mandatory")
_Modules_ObjectIdentity = ObjectIdentity
modules = _Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4)
)
_Ethernet_ObjectIdentity = ObjectIdentity
ethernet = _Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 23)
)
_EthIntTable_Object = MibTable
ethIntTable = _EthIntTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 23, 1)
)
if mibBuilder.loadTexts:
    ethIntTable.setStatus("mandatory")
_EthIntEntry_Object = MibTableRow
ethIntEntry = _EthIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 23, 1, 1)
)
ethIntEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "ethIntIndex"),
)
if mibBuilder.loadTexts:
    ethIntEntry.setStatus("mandatory")
_EthIntIndex_Type = Integer32
_EthIntIndex_Object = MibTableColumn
ethIntIndex = _EthIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 23, 1, 1, 1),
    _EthIntIndex_Type()
)
ethIntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntIndex.setStatus("mandatory")
_EthIntBoardIndex_Type = Integer32
_EthIntBoardIndex_Object = MibTableColumn
ethIntBoardIndex = _EthIntBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 23, 1, 1, 2),
    _EthIntBoardIndex_Type()
)
ethIntBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntBoardIndex.setStatus("mandatory")
_EthIntBoardPosition_Type = Integer32
_EthIntBoardPosition_Object = MibTableColumn
ethIntBoardPosition = _EthIntBoardPosition_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 23, 1, 1, 3),
    _EthIntBoardPosition_Type()
)
ethIntBoardPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntBoardPosition.setStatus("mandatory")


class _EthIntDuplexMode_Type(Integer32):
    """Custom type ethIntDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 1),
          ("half-duplex", 2),
          ("unknown", 3))
    )


_EthIntDuplexMode_Type.__name__ = "Integer32"
_EthIntDuplexMode_Object = MibTableColumn
ethIntDuplexMode = _EthIntDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 23, 1, 1, 4),
    _EthIntDuplexMode_Type()
)
ethIntDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntDuplexMode.setStatus("mandatory")
_Flash_ObjectIdentity = ObjectIdentity
flash = _Flash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31)
)
_FlashGetFailure_Type = Integer32
_FlashGetFailure_Object = MibScalar
flashGetFailure = _FlashGetFailure_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 1),
    _FlashGetFailure_Type()
)
flashGetFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashGetFailure.setStatus("mandatory")
_FlashOpenFailure_Type = Integer32
_FlashOpenFailure_Object = MibScalar
flashOpenFailure = _FlashOpenFailure_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 2),
    _FlashOpenFailure_Type()
)
flashOpenFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashOpenFailure.setStatus("mandatory")
_FlashReadFailure_Type = Integer32
_FlashReadFailure_Object = MibScalar
flashReadFailure = _FlashReadFailure_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 3),
    _FlashReadFailure_Type()
)
flashReadFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashReadFailure.setStatus("mandatory")
_FlashCloseFailure_Type = Integer32
_FlashCloseFailure_Object = MibScalar
flashCloseFailure = _FlashCloseFailure_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 4),
    _FlashCloseFailure_Type()
)
flashCloseFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashCloseFailure.setStatus("mandatory")
_FlashCompleteFailure_Type = Integer32
_FlashCompleteFailure_Object = MibScalar
flashCompleteFailure = _FlashCompleteFailure_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 5),
    _FlashCompleteFailure_Type()
)
flashCompleteFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashCompleteFailure.setStatus("mandatory")
_FlashWriteFailure_Type = Integer32
_FlashWriteFailure_Object = MibScalar
flashWriteFailure = _FlashWriteFailure_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 6),
    _FlashWriteFailure_Type()
)
flashWriteFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashWriteFailure.setStatus("mandatory")
_FlashCreateFailure_Type = Integer32
_FlashCreateFailure_Object = MibScalar
flashCreateFailure = _FlashCreateFailure_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 7),
    _FlashCreateFailure_Type()
)
flashCreateFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashCreateFailure.setStatus("mandatory")
_FlashPutFailure_Type = Integer32
_FlashPutFailure_Object = MibScalar
flashPutFailure = _FlashPutFailure_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 8),
    _FlashPutFailure_Type()
)
flashPutFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashPutFailure.setStatus("mandatory")
_FlashDeleteFailure_Type = Integer32
_FlashDeleteFailure_Object = MibScalar
flashDeleteFailure = _FlashDeleteFailure_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 9),
    _FlashDeleteFailure_Type()
)
flashDeleteFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashDeleteFailure.setStatus("mandatory")
_FlashCheckFailure_Type = Integer32
_FlashCheckFailure_Object = MibScalar
flashCheckFailure = _FlashCheckFailure_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 10),
    _FlashCheckFailure_Type()
)
flashCheckFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashCheckFailure.setStatus("mandatory")
_FlashEraseFailure_Type = Integer32
_FlashEraseFailure_Object = MibScalar
flashEraseFailure = _FlashEraseFailure_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 11),
    _FlashEraseFailure_Type()
)
flashEraseFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashEraseFailure.setStatus("mandatory")
_FlashCompactFailure_Type = Integer32
_FlashCompactFailure_Object = MibScalar
flashCompactFailure = _FlashCompactFailure_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 12),
    _FlashCompactFailure_Type()
)
flashCompactFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashCompactFailure.setStatus("mandatory")
_FlashVerifyFailure_Type = Integer32
_FlashVerifyFailure_Object = MibScalar
flashVerifyFailure = _FlashVerifyFailure_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 13),
    _FlashVerifyFailure_Type()
)
flashVerifyFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashVerifyFailure.setStatus("mandatory")
_Cc_ObjectIdentity = ObjectIdentity
cc = _Cc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37)
)
_CcDetailsTable_Object = MibTable
ccDetailsTable = _CcDetailsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1)
)
if mibBuilder.loadTexts:
    ccDetailsTable.setStatus("mandatory")
_CcDetailsEntry_Object = MibTableRow
ccDetailsEntry = _CcDetailsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1)
)
ccDetailsEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "ccDetailsIndex"),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 1),
    _CcDetailsIndex_Type()
)
ccDetailsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDetailsIndex.setStatus("mandatory")


class _CcDetailsName_Type(DisplayString):
    """Custom type ccDetailsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CcDetailsName_Type.__name__ = "DisplayString"
_CcDetailsName_Object = MibTableColumn
ccDetailsName = _CcDetailsName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 2),
    _CcDetailsName_Type()
)
ccDetailsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsName.setStatus("mandatory")


class _CcDetailsRemoteName_Type(DisplayString):
    """Custom type ccDetailsRemoteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CcDetailsRemoteName_Type.__name__ = "DisplayString"
_CcDetailsRemoteName_Object = MibTableColumn
ccDetailsRemoteName = _CcDetailsRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 3),
    _CcDetailsRemoteName_Type()
)
ccDetailsRemoteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsRemoteName.setStatus("mandatory")


class _CcDetailsCalledNumber_Type(DisplayString):
    """Custom type ccDetailsCalledNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CcDetailsCalledNumber_Type.__name__ = "DisplayString"
_CcDetailsCalledNumber_Object = MibTableColumn
ccDetailsCalledNumber = _CcDetailsCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 4),
    _CcDetailsCalledNumber_Type()
)
ccDetailsCalledNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsCalledNumber.setStatus("mandatory")


class _CcDetailsCallingNumber_Type(DisplayString):
    """Custom type ccDetailsCallingNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CcDetailsCallingNumber_Type.__name__ = "DisplayString"
_CcDetailsCallingNumber_Object = MibTableColumn
ccDetailsCallingNumber = _CcDetailsCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 5),
    _CcDetailsCallingNumber_Type()
)
ccDetailsCallingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsCallingNumber.setStatus("mandatory")


class _CcDetailsAlternateNumber_Type(DisplayString):
    """Custom type ccDetailsAlternateNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CcDetailsAlternateNumber_Type.__name__ = "DisplayString"
_CcDetailsAlternateNumber_Object = MibTableColumn
ccDetailsAlternateNumber = _CcDetailsAlternateNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 14),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 15),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 16),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 17),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 18),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 19),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 20),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 21),
    _CcDetailsOutSetupCalledSub_Type()
)
ccDetailsOutSetupCalledSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsOutSetupCalledSub.setStatus("mandatory")


class _CcDetailsOutSubaddress_Type(DisplayString):
    """Custom type ccDetailsOutSubaddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CcDetailsOutSubaddress_Type.__name__ = "DisplayString"
_CcDetailsOutSubaddress_Object = MibTableColumn
ccDetailsOutSubaddress = _CcDetailsOutSubaddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 22),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 23),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 24),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 25),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 26),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 27),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 28),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 29),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 30),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 31),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 32),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 33),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 34),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 35),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 36),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 37),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 38),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 39),
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
        ValueRangeConstraint(1, 33),
    )


_CcDetailsPppTemplate_Type.__name__ = "Integer32"
_CcDetailsPppTemplate_Object = MibTableColumn
ccDetailsPppTemplate = _CcDetailsPppTemplate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 40),
    _CcDetailsPppTemplate_Type()
)
ccDetailsPppTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetailsPppTemplate.setStatus("mandatory")
_CcDetailsUserModule_Type = Integer32
_CcDetailsUserModule_Object = MibTableColumn
ccDetailsUserModule = _CcDetailsUserModule_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 41),
    _CcDetailsUserModule_Type()
)
ccDetailsUserModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDetailsUserModule.setStatus("mandatory")
_CcDetailsNumberAttachments_Type = Integer32
_CcDetailsNumberAttachments_Object = MibTableColumn
ccDetailsNumberAttachments = _CcDetailsNumberAttachments_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 1, 1, 42),
    _CcDetailsNumberAttachments_Type()
)
ccDetailsNumberAttachments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDetailsNumberAttachments.setStatus("mandatory")
_CcCliListTable_Object = MibTable
ccCliListTable = _CcCliListTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 2)
)
if mibBuilder.loadTexts:
    ccCliListTable.setStatus("mandatory")
_CcCliListEntry_Object = MibTableRow
ccCliListEntry = _CcCliListEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 2, 1)
)
ccCliListEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "ccCliListListIndex"),
    (0, "ALLIEDTELESYN-MIB", "ccCliListEntryIndex"),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 2, 1, 1),
    _CcCliListListIndex_Type()
)
ccCliListListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCliListListIndex.setStatus("mandatory")
_CcCliListEntryIndex_Type = Integer32
_CcCliListEntryIndex_Object = MibTableColumn
ccCliListEntryIndex = _CcCliListEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 2, 1, 2),
    _CcCliListEntryIndex_Type()
)
ccCliListEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCliListEntryIndex.setStatus("mandatory")


class _CcCliListNumber_Type(DisplayString):
    """Custom type ccCliListNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CcCliListNumber_Type.__name__ = "DisplayString"
_CcCliListNumber_Object = MibTableColumn
ccCliListNumber = _CcCliListNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 2, 1, 3),
    _CcCliListNumber_Type()
)
ccCliListNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCliListNumber.setStatus("mandatory")
_CcActiveCallTable_Object = MibTable
ccActiveCallTable = _CcActiveCallTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 3)
)
if mibBuilder.loadTexts:
    ccActiveCallTable.setStatus("mandatory")
_CcActiveCallEntry_Object = MibTableRow
ccActiveCallEntry = _CcActiveCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 3, 1)
)
ccActiveCallEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "ccActiveCallIndex"),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 3, 1, 2),
    _CcActiveCallDetailsIndex_Type()
)
ccActiveCallDetailsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccActiveCallDetailsIndex.setStatus("mandatory")
_CcActiveCallIfIndex_Type = InterfaceIndexOrZero
_CcActiveCallIfIndex_Object = MibTableColumn
ccActiveCallIfIndex = _CcActiveCallIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 3, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 3, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 3, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 3, 1, 6),
    _CcActiveCallDirection_Type()
)
ccActiveCallDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccActiveCallDirection.setStatus("mandatory")
_CcActiveCallUserModule_Type = Integer32
_CcActiveCallUserModule_Object = MibTableColumn
ccActiveCallUserModule = _CcActiveCallUserModule_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 3, 1, 7),
    _CcActiveCallUserModule_Type()
)
ccActiveCallUserModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccActiveCallUserModule.setStatus("mandatory")
_CcActiveCallUserInstance_Type = Integer32
_CcActiveCallUserInstance_Object = MibTableColumn
ccActiveCallUserInstance = _CcActiveCallUserInstance_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 3, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 3, 1, 9),
    _CcActiveCallBchannelIndex_Type()
)
ccActiveCallBchannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccActiveCallBchannelIndex.setStatus("mandatory")
_CcCallLogTable_Object = MibTable
ccCallLogTable = _CcCallLogTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 4)
)
if mibBuilder.loadTexts:
    ccCallLogTable.setStatus("mandatory")
_CcCallLogEntry_Object = MibTableRow
ccCallLogEntry = _CcCallLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 4, 1)
)
ccCallLogEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "ccCallLogIndex"),
)
if mibBuilder.loadTexts:
    ccCallLogEntry.setStatus("mandatory")
_CcCallLogIndex_Type = Integer32
_CcCallLogIndex_Object = MibTableColumn
ccCallLogIndex = _CcCallLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 4, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 4, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 4, 1, 5),
    _CcCallLogDirection_Type()
)
ccCallLogDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCallLogDirection.setStatus("mandatory")
_CcCallLogDuration_Type = Integer32
_CcCallLogDuration_Object = MibTableColumn
ccCallLogDuration = _CcCallLogDuration_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 4, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 4, 1, 7),
    _CcCallLogRemoteNumber_Type()
)
ccCallLogRemoteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCallLogRemoteNumber.setStatus("mandatory")
_CcAttachmentTable_Object = MibTable
ccAttachmentTable = _CcAttachmentTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 5)
)
if mibBuilder.loadTexts:
    ccAttachmentTable.setStatus("mandatory")
_CcAttachmentEntry_Object = MibTableRow
ccAttachmentEntry = _CcAttachmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 5, 1)
)
ccAttachmentEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "ccAttachmentDetailsIndex"),
    (0, "ALLIEDTELESYN-MIB", "ccAttachmentEntryIndex"),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 5, 1, 1),
    _CcAttachmentDetailsIndex_Type()
)
ccAttachmentDetailsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccAttachmentDetailsIndex.setStatus("mandatory")
_CcAttachmentEntryIndex_Type = Integer32
_CcAttachmentEntryIndex_Object = MibTableColumn
ccAttachmentEntryIndex = _CcAttachmentEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 5, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 5, 1, 3),
    _CcAttachmentActiveCallIndex_Type()
)
ccAttachmentActiveCallIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccAttachmentActiveCallIndex.setStatus("mandatory")
_CcAttachmentUserInstance_Type = Integer32
_CcAttachmentUserInstance_Object = MibTableColumn
ccAttachmentUserInstance = _CcAttachmentUserInstance_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 5, 1, 4),
    _CcAttachmentUserInstance_Type()
)
ccAttachmentUserInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccAttachmentUserInstance.setStatus("mandatory")
_CcBchannelTable_Object = MibTable
ccBchannelTable = _CcBchannelTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 6)
)
if mibBuilder.loadTexts:
    ccBchannelTable.setStatus("mandatory")
_CcBchannelEntry_Object = MibTableRow
ccBchannelEntry = _CcBchannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 6, 1)
)
ccBchannelEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "ccBchannelIfIndex"),
    (0, "ALLIEDTELESYN-MIB", "ccBchannelChannelIndex"),
)
if mibBuilder.loadTexts:
    ccBchannelEntry.setStatus("mandatory")
_CcBchannelIfIndex_Type = Integer32
_CcBchannelIfIndex_Object = MibTableColumn
ccBchannelIfIndex = _CcBchannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 6, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 6, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 6, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 6, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 6, 1, 5),
    _CcBchannelActiveCallIndex_Type()
)
ccBchannelActiveCallIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccBchannelActiveCallIndex.setStatus("mandatory")
_CcBchannelPriority_Type = Integer32
_CcBchannelPriority_Object = MibTableColumn
ccBchannelPriority = _CcBchannelPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 6, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 37, 6, 1, 7),
    _CcBchannelDirection_Type()
)
ccBchannelDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccBchannelDirection.setStatus("mandatory")
_Bri_ObjectIdentity = ObjectIdentity
bri = _Bri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 41)
)
_BriIntTable_Object = MibTable
briIntTable = _BriIntTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 41, 1)
)
if mibBuilder.loadTexts:
    briIntTable.setStatus("mandatory")
_BriIntEntry_Object = MibTableRow
briIntEntry = _BriIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 41, 1, 1)
)
briIntEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "briIntIndex"),
)
if mibBuilder.loadTexts:
    briIntEntry.setStatus("mandatory")
_BriIntIndex_Type = Integer32
_BriIntIndex_Object = MibTableColumn
briIntIndex = _BriIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 41, 1, 1, 1),
    _BriIntIndex_Type()
)
briIntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briIntIndex.setStatus("mandatory")
_BriIntBoardIndex_Type = Integer32
_BriIntBoardIndex_Object = MibTableColumn
briIntBoardIndex = _BriIntBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 41, 1, 1, 2),
    _BriIntBoardIndex_Type()
)
briIntBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briIntBoardIndex.setStatus("mandatory")
_BriIntBoardPosition_Type = Integer32
_BriIntBoardPosition_Object = MibTableColumn
briIntBoardPosition = _BriIntBoardPosition_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 41, 1, 1, 3),
    _BriIntBoardPosition_Type()
)
briIntBoardPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briIntBoardPosition.setStatus("mandatory")


class _BriIntMode_Type(Integer32):
    """Custom type briIntMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("isdn", 1),
          ("mixed", 3),
          ("tdm", 2))
    )


_BriIntMode_Type.__name__ = "Integer32"
_BriIntMode_Object = MibTableColumn
briIntMode = _BriIntMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 41, 1, 1, 4),
    _BriIntMode_Type()
)
briIntMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briIntMode.setStatus("mandatory")
_BriIntTdmChannelMap_Type = Integer32
_BriIntTdmChannelMap_Object = MibTableColumn
briIntTdmChannelMap = _BriIntTdmChannelMap_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 41, 1, 1, 5),
    _BriIntTdmChannelMap_Type()
)
briIntTdmChannelMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briIntTdmChannelMap.setStatus("mandatory")
_BriIntIsdnChannelMap_Type = Integer32
_BriIntIsdnChannelMap_Object = MibTableColumn
briIntIsdnChannelMap = _BriIntIsdnChannelMap_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 41, 1, 1, 6),
    _BriIntIsdnChannelMap_Type()
)
briIntIsdnChannelMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briIntIsdnChannelMap.setStatus("mandatory")
_BriChanTable_Object = MibTable
briChanTable = _BriChanTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 41, 2)
)
if mibBuilder.loadTexts:
    briChanTable.setStatus("mandatory")
_BriChanEntry_Object = MibTableRow
briChanEntry = _BriChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 41, 2, 1)
)
briChanEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "briChanIntIndex"),
    (0, "ALLIEDTELESYN-MIB", "briChanChannelIndex"),
)
if mibBuilder.loadTexts:
    briChanEntry.setStatus("mandatory")
_BriChanIntIndex_Type = Integer32
_BriChanIntIndex_Object = MibTableColumn
briChanIntIndex = _BriChanIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 41, 2, 1, 1),
    _BriChanIntIndex_Type()
)
briChanIntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briChanIntIndex.setStatus("mandatory")


class _BriChanChannelIndex_Type(Integer32):
    """Custom type briChanChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_BriChanChannelIndex_Type.__name__ = "Integer32"
_BriChanChannelIndex_Object = MibTableColumn
briChanChannelIndex = _BriChanChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 41, 2, 1, 2),
    _BriChanChannelIndex_Type()
)
briChanChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briChanChannelIndex.setStatus("mandatory")


class _BriChanMode_Type(Integer32):
    """Custom type briChanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("isdn", 1),
          ("none", 3),
          ("tdm", 2))
    )


_BriChanMode_Type.__name__ = "Integer32"
_BriChanMode_Object = MibTableColumn
briChanMode = _BriChanMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 41, 2, 1, 3),
    _BriChanMode_Type()
)
briChanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briChanMode.setStatus("mandatory")


class _BriChanState_Type(Integer32):
    """Custom type briChanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_BriChanState_Type.__name__ = "Integer32"
_BriChanState_Object = MibTableColumn
briChanState = _BriChanState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 41, 2, 1, 4),
    _BriChanState_Type()
)
briChanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briChanState.setStatus("mandatory")
_Pri_ObjectIdentity = ObjectIdentity
pri = _Pri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42)
)
_PriIntTable_Object = MibTable
priIntTable = _PriIntTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1)
)
if mibBuilder.loadTexts:
    priIntTable.setStatus("mandatory")
_PriIntEntry_Object = MibTableRow
priIntEntry = _PriIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1)
)
priIntEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "priIntIndex"),
)
if mibBuilder.loadTexts:
    priIntEntry.setStatus("mandatory")
_PriIntIndex_Type = Integer32
_PriIntIndex_Object = MibTableColumn
priIntIndex = _PriIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1, 1),
    _PriIntIndex_Type()
)
priIntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    priIntIndex.setStatus("mandatory")
_PriIntBoardIndex_Type = Integer32
_PriIntBoardIndex_Object = MibTableColumn
priIntBoardIndex = _PriIntBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1, 2),
    _PriIntBoardIndex_Type()
)
priIntBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    priIntBoardIndex.setStatus("mandatory")
_PriIntBoardPosition_Type = Integer32
_PriIntBoardPosition_Object = MibTableColumn
priIntBoardPosition = _PriIntBoardPosition_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1, 3),
    _PriIntBoardPosition_Type()
)
priIntBoardPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    priIntBoardPosition.setStatus("mandatory")


class _PriIntMode_Type(Integer32):
    """Custom type priIntMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("isdn", 1),
          ("mixed", 3),
          ("tdm", 2))
    )


_PriIntMode_Type.__name__ = "Integer32"
_PriIntMode_Object = MibTableColumn
priIntMode = _PriIntMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1, 4),
    _PriIntMode_Type()
)
priIntMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    priIntMode.setStatus("mandatory")
_PriIntTdmChannelMap_Type = Integer32
_PriIntTdmChannelMap_Object = MibTableColumn
priIntTdmChannelMap = _PriIntTdmChannelMap_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1, 5),
    _PriIntTdmChannelMap_Type()
)
priIntTdmChannelMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    priIntTdmChannelMap.setStatus("mandatory")
_PriIntIsdnChannelMap_Type = Integer32
_PriIntIsdnChannelMap_Object = MibTableColumn
priIntIsdnChannelMap = _PriIntIsdnChannelMap_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1, 6),
    _PriIntIsdnChannelMap_Type()
)
priIntIsdnChannelMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    priIntIsdnChannelMap.setStatus("mandatory")


class _PriIntType_Type(Integer32):
    """Custom type priIntType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e1", 1),
          ("t1", 2),
          ("unknown", 3))
    )


_PriIntType_Type.__name__ = "Integer32"
_PriIntType_Object = MibTableColumn
priIntType = _PriIntType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1, 7),
    _PriIntType_Type()
)
priIntType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    priIntType.setStatus("mandatory")
_PriChanTable_Object = MibTable
priChanTable = _PriChanTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 2)
)
if mibBuilder.loadTexts:
    priChanTable.setStatus("mandatory")
_PriChanEntry_Object = MibTableRow
priChanEntry = _PriChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 2, 1)
)
priChanEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "priChanIntIndex"),
    (0, "ALLIEDTELESYN-MIB", "priChanChannelIndex"),
)
if mibBuilder.loadTexts:
    priChanEntry.setStatus("mandatory")
_PriChanIntIndex_Type = Integer32
_PriChanIntIndex_Object = MibTableColumn
priChanIntIndex = _PriChanIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 2, 1, 1),
    _PriChanIntIndex_Type()
)
priChanIntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    priChanIntIndex.setStatus("mandatory")


class _PriChanChannelIndex_Type(Integer32):
    """Custom type priChanChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_PriChanChannelIndex_Type.__name__ = "Integer32"
_PriChanChannelIndex_Object = MibTableColumn
priChanChannelIndex = _PriChanChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 2, 1, 2),
    _PriChanChannelIndex_Type()
)
priChanChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    priChanChannelIndex.setStatus("mandatory")


class _PriChanMode_Type(Integer32):
    """Custom type priChanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("isdn", 1),
          ("neither", 3),
          ("tdm", 2))
    )


_PriChanMode_Type.__name__ = "Integer32"
_PriChanMode_Object = MibTableColumn
priChanMode = _PriChanMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 2, 1, 3),
    _PriChanMode_Type()
)
priChanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    priChanMode.setStatus("mandatory")


class _PriChanState_Type(Integer32):
    """Custom type priChanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_PriChanState_Type.__name__ = "Integer32"
_PriChanState_Object = MibTableColumn
priChanState = _PriChanState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 2, 1, 4),
    _PriChanState_Type()
)
priChanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    priChanState.setStatus("mandatory")
_Loader_ObjectIdentity = ObjectIdentity
loader = _Loader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 48)
)
_LoadTable_Object = MibTable
loadTable = _LoadTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 48, 1)
)
if mibBuilder.loadTexts:
    loadTable.setStatus("mandatory")
_LoadEntry_Object = MibTableRow
loadEntry = _LoadEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 48, 1, 1)
)
loadEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "loadIndex"),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 48, 1, 1, 1),
    _LoadIndex_Type()
)
loadIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadIndex.setStatus("mandatory")
_LoadServer_Type = IpAddress
_LoadServer_Object = MibTableColumn
loadServer = _LoadServer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 48, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 48, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 48, 1, 1, 4),
    _LoadFilename_Type()
)
loadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadFilename.setStatus("mandatory")
_LoadDelay_Type = Integer32
_LoadDelay_Object = MibTableColumn
loadDelay = _LoadDelay_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 48, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 48, 2),
    _LoadStatus_Type()
)
loadStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadStatus.setStatus("mandatory")
_Install_ObjectIdentity = ObjectIdentity
install = _Install_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49)
)
_InstallTable_Object = MibTable
installTable = _InstallTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1)
)
if mibBuilder.loadTexts:
    installTable.setStatus("mandatory")
_InstallEntry_Object = MibTableRow
installEntry = _InstallEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1)
)
installEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "instIndex"),
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
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("current", 4),
          ("default", 3),
          ("preferred", 2),
          ("temporary", 1))
    )


_InstIndex_Type.__name__ = "Integer32"
_InstIndex_Object = MibTableColumn
instIndex = _InstIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1, 2),
    _InstRelDevice_Type()
)
instRelDevice.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1, 3),
    _InstRelName_Type()
)
instRelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instRelName.setStatus("mandatory")
_InstRelMajor_Type = Integer32
_InstRelMajor_Object = MibTableColumn
instRelMajor = _InstRelMajor_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1, 4),
    _InstRelMajor_Type()
)
instRelMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instRelMajor.setStatus("mandatory")
_InstRelMinor_Type = Integer32
_InstRelMinor_Object = MibTableColumn
instRelMinor = _InstRelMinor_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1, 6),
    _InstPatDevice_Type()
)
instPatDevice.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1, 7),
    _InstPatName_Type()
)
instPatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instPatName.setStatus("mandatory")
_InstRelInterim_Type = Integer32
_InstRelInterim_Object = MibTableColumn
instRelInterim = _InstRelInterim_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1, 8),
    _InstRelInterim_Type()
)
instRelInterim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instRelInterim.setStatus("mandatory")


class _InstRelExists_Type(Integer32):
    """Custom type instRelExists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_InstRelExists_Type.__name__ = "Integer32"
_InstRelExists_Object = MibTableColumn
instRelExists = _InstRelExists_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1, 9),
    _InstRelExists_Type()
)
instRelExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instRelExists.setStatus("mandatory")


class _InstPatExists_Type(Integer32):
    """Custom type instPatExists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_InstPatExists_Type.__name__ = "Integer32"
_InstPatExists_Object = MibTableColumn
instPatExists = _InstPatExists_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1, 10),
    _InstPatExists_Type()
)
instPatExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instPatExists.setStatus("mandatory")
_InstallHistoryTable_Object = MibTable
installHistoryTable = _InstallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 2)
)
if mibBuilder.loadTexts:
    installHistoryTable.setStatus("mandatory")
_InstallHistoryEntry_Object = MibTableRow
installHistoryEntry = _InstallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 2, 1)
)
installHistoryEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "instHistIndex"),
)
if mibBuilder.loadTexts:
    installHistoryEntry.setStatus("mandatory")
_InstHistIndex_Type = Integer32
_InstHistIndex_Object = MibTableColumn
instHistIndex = _InstHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 3),
    _ConfigFile_Type()
)
configFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFile.setStatus("mandatory")
_LicenceTable_Object = MibTable
licenceTable = _LicenceTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 4)
)
if mibBuilder.loadTexts:
    licenceTable.setStatus("mandatory")
_LicenceEntry_Object = MibTableRow
licenceEntry = _LicenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 4, 1)
)
licenceEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "licenceIndex"),
)
if mibBuilder.loadTexts:
    licenceEntry.setStatus("mandatory")
_LicenceIndex_Type = Integer32
_LicenceIndex_Object = MibTableColumn
licenceIndex = _LicenceIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 4, 1, 3),
    _LicenceRelease_Type()
)
licenceRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenceRelease.setStatus("mandatory")
_LicenceMajor_Type = Integer32
_LicenceMajor_Object = MibTableColumn
licenceMajor = _LicenceMajor_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 4, 1, 4),
    _LicenceMajor_Type()
)
licenceMajor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenceMajor.setStatus("mandatory")
_LicenceMinor_Type = Integer32
_LicenceMinor_Object = MibTableColumn
licenceMinor = _LicenceMinor_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 4, 1, 5),
    _LicenceMinor_Type()
)
licenceMinor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenceMinor.setStatus("mandatory")


class _LicencePassword_Type(DisplayString):
    """Custom type licencePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_LicencePassword_Type.__name__ = "DisplayString"
_LicencePassword_Object = MibTableColumn
licencePassword = _LicencePassword_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 4, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 4, 1, 7),
    _LicenceExpiry_Type()
)
licenceExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenceExpiry.setStatus("mandatory")
_LicenceInterim_Type = Integer32
_LicenceInterim_Object = MibTableColumn
licenceInterim = _LicenceInterim_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 4, 1, 8),
    _LicenceInterim_Type()
)
licenceInterim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenceInterim.setStatus("mandatory")


class _CreateConfigFile_Type(DisplayString):
    """Custom type createConfigFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CreateConfigFile_Type.__name__ = "DisplayString"
_CreateConfigFile_Object = MibScalar
createConfigFile = _CreateConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 5),
    _CreateConfigFile_Type()
)
createConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    createConfigFile.setStatus("mandatory")


class _ConfigFileExist_Type(Integer32):
    """Custom type configFileExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_ConfigFileExist_Type.__name__ = "Integer32"
_ConfigFileExist_Object = MibScalar
configFileExist = _ConfigFileExist_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 6),
    _ConfigFileExist_Type()
)
configFileExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configFileExist.setStatus("mandatory")


class _CurrentConfigFile_Type(DisplayString):
    """Custom type currentConfigFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CurrentConfigFile_Type.__name__ = "DisplayString"
_CurrentConfigFile_Object = MibScalar
currentConfigFile = _CurrentConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 7),
    _CurrentConfigFile_Type()
)
currentConfigFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentConfigFile.setStatus("mandatory")
_Trigger_ObjectIdentity = ObjectIdentity
trigger = _Trigger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53)
)
_TriggerLastTriggerActivated_Type = Integer32
_TriggerLastTriggerActivated_Object = MibScalar
triggerLastTriggerActivated = _TriggerLastTriggerActivated_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 1),
    _TriggerLastTriggerActivated_Type()
)
triggerLastTriggerActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerLastTriggerActivated.setStatus("mandatory")
_File_ObjectIdentity = ObjectIdentity
file = _File_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 56)
)
_FileTable_Object = MibTable
fileTable = _FileTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 56, 1)
)
if mibBuilder.loadTexts:
    fileTable.setStatus("mandatory")
_FileEntry_Object = MibTableRow
fileEntry = _FileEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 56, 1, 1)
)
fileEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "fileIndex"),
)
if mibBuilder.loadTexts:
    fileEntry.setStatus("mandatory")
_FileIndex_Type = Integer32
_FileIndex_Object = MibTableColumn
fileIndex = _FileIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 56, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 56, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 56, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 56, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 56, 1, 1, 5),
    _FileStatus_Type()
)
fileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileStatus.setStatus("mandatory")
_FileSize_Type = Integer32
_FileSize_Object = MibTableColumn
fileSize = _FileSize_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 56, 1, 1, 6),
    _FileSize_Type()
)
fileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSize.setStatus("mandatory")
_FileNumbers_Type = Integer32
_FileNumbers_Object = MibScalar
fileNumbers = _FileNumbers_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 56, 2),
    _FileNumbers_Type()
)
fileNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileNumbers.setStatus("mandatory")
_Ping_ObjectIdentity = ObjectIdentity
ping = _Ping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58)
)
_PingTable_Object = MibTable
pingTable = _PingTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1)
)
if mibBuilder.loadTexts:
    pingTable.setStatus("mandatory")
_PingEntry_Object = MibTableRow
pingEntry = _PingEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1)
)
pingEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "pingIndex"),
)
if mibBuilder.loadTexts:
    pingEntry.setStatus("mandatory")


class _PingIndex_Type(Integer32):
    """Custom type pingIndex based on Integer32"""
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


_PingIndex_Type.__name__ = "Integer32"
_PingIndex_Object = MibTableColumn
pingIndex = _PingIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1, 1),
    _PingIndex_Type()
)
pingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingIndex.setStatus("mandatory")


class _PingProtocol_Type(Integer32):
    """Custom type pingProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("apple", 1),
          ("ip", 2),
          ("ipx", 3),
          ("osi", 4),
          ("undefined", 0))
    )


_PingProtocol_Type.__name__ = "Integer32"
_PingProtocol_Object = MibTableColumn
pingProtocol = _PingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1, 2),
    _PingProtocol_Type()
)
pingProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingProtocol.setStatus("mandatory")
_PingAddress_Type = OctetString
_PingAddress_Object = MibTableColumn
pingAddress = _PingAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1, 3),
    _PingAddress_Type()
)
pingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingAddress.setStatus("mandatory")
_PingNumberOfPackets_Type = Integer32
_PingNumberOfPackets_Object = MibTableColumn
pingNumberOfPackets = _PingNumberOfPackets_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1, 4),
    _PingNumberOfPackets_Type()
)
pingNumberOfPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingNumberOfPackets.setStatus("mandatory")


class _PingPacketSize_Type(Integer32):
    """Custom type pingPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_PingPacketSize_Type.__name__ = "Integer32"
_PingPacketSize_Object = MibTableColumn
pingPacketSize = _PingPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1, 5),
    _PingPacketSize_Type()
)
pingPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingPacketSize.setStatus("mandatory")
_PingTimeout_Type = Integer32
_PingTimeout_Object = MibTableColumn
pingTimeout = _PingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1, 6),
    _PingTimeout_Type()
)
pingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingTimeout.setStatus("mandatory")
_PingDelay_Type = Integer32
_PingDelay_Object = MibTableColumn
pingDelay = _PingDelay_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1, 7),
    _PingDelay_Type()
)
pingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingDelay.setStatus("mandatory")


class _PingTrapOnCompletion_Type(Integer32):
    """Custom type pingTrapOnCompletion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_PingTrapOnCompletion_Type.__name__ = "Integer32"
_PingTrapOnCompletion_Object = MibTableColumn
pingTrapOnCompletion = _PingTrapOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1, 8),
    _PingTrapOnCompletion_Type()
)
pingTrapOnCompletion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingTrapOnCompletion.setStatus("mandatory")


class _PingTypeOfService_Type(Integer32):
    """Custom type pingTypeOfService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PingTypeOfService_Type.__name__ = "Integer32"
_PingTypeOfService_Object = MibTableColumn
pingTypeOfService = _PingTypeOfService_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1, 9),
    _PingTypeOfService_Type()
)
pingTypeOfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingTypeOfService.setStatus("mandatory")
_PingPattern_Type = Integer32
_PingPattern_Object = MibTableColumn
pingPattern = _PingPattern_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1, 10),
    _PingPattern_Type()
)
pingPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingPattern.setStatus("mandatory")


class _PingStatus_Type(Integer32):
    """Custom type pingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start-running", 1),
          ("stop-stopped", 2))
    )


_PingStatus_Type.__name__ = "Integer32"
_PingStatus_Object = MibScalar
pingStatus = _PingStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 2),
    _PingStatus_Type()
)
pingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingStatus.setStatus("mandatory")
_PingStatistics_ObjectIdentity = ObjectIdentity
pingStatistics = _PingStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 3)
)
_PingSentPackets_Type = Integer32
_PingSentPackets_Object = MibScalar
pingSentPackets = _PingSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 3, 1),
    _PingSentPackets_Type()
)
pingSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingSentPackets.setStatus("mandatory")
_PingReceivedPackets_Type = Integer32
_PingReceivedPackets_Object = MibScalar
pingReceivedPackets = _PingReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 3, 2),
    _PingReceivedPackets_Type()
)
pingReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingReceivedPackets.setStatus("mandatory")
_PingMinimumRoundTripTime_Type = Integer32
_PingMinimumRoundTripTime_Object = MibScalar
pingMinimumRoundTripTime = _PingMinimumRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 3, 3),
    _PingMinimumRoundTripTime_Type()
)
pingMinimumRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingMinimumRoundTripTime.setStatus("mandatory")
_PingAverageRoundTripTime_Type = Integer32
_PingAverageRoundTripTime_Object = MibScalar
pingAverageRoundTripTime = _PingAverageRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 3, 4),
    _PingAverageRoundTripTime_Type()
)
pingAverageRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingAverageRoundTripTime.setStatus("mandatory")
_PingMaximumRoundTripTime_Type = Integer32
_PingMaximumRoundTripTime_Object = MibScalar
pingMaximumRoundTripTime = _PingMaximumRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 3, 5),
    _PingMaximumRoundTripTime_Type()
)
pingMaximumRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingMaximumRoundTripTime.setStatus("mandatory")
_Dhcp_ObjectIdentity = ObjectIdentity
dhcp = _Dhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70)
)
_DhcpRangeTable_Object = MibTable
dhcpRangeTable = _DhcpRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 1)
)
if mibBuilder.loadTexts:
    dhcpRangeTable.setStatus("mandatory")
_DhcpRangeEntry_Object = MibTableRow
dhcpRangeEntry = _DhcpRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 1, 1)
)
dhcpRangeEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "dhcpRangeIndex"),
)
if mibBuilder.loadTexts:
    dhcpRangeEntry.setStatus("mandatory")
_DhcpRangeIndex_Type = Integer32
_DhcpRangeIndex_Object = MibTableColumn
dhcpRangeIndex = _DhcpRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 1, 1, 1),
    _DhcpRangeIndex_Type()
)
dhcpRangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRangeIndex.setStatus("mandatory")


class _DhcpRangeName_Type(DisplayString):
    """Custom type dhcpRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_DhcpRangeName_Type.__name__ = "DisplayString"
_DhcpRangeName_Object = MibTableColumn
dhcpRangeName = _DhcpRangeName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 1, 1, 2),
    _DhcpRangeName_Type()
)
dhcpRangeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRangeName.setStatus("mandatory")
_DhcpRangeBaseAddress_Type = IpAddress
_DhcpRangeBaseAddress_Object = MibTableColumn
dhcpRangeBaseAddress = _DhcpRangeBaseAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 1, 1, 3),
    _DhcpRangeBaseAddress_Type()
)
dhcpRangeBaseAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRangeBaseAddress.setStatus("mandatory")


class _DhcpRangeNumberOfAddresses_Type(Integer32):
    """Custom type dhcpRangeNumberOfAddresses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_DhcpRangeNumberOfAddresses_Type.__name__ = "Integer32"
_DhcpRangeNumberOfAddresses_Object = MibTableColumn
dhcpRangeNumberOfAddresses = _DhcpRangeNumberOfAddresses_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 1, 1, 4),
    _DhcpRangeNumberOfAddresses_Type()
)
dhcpRangeNumberOfAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRangeNumberOfAddresses.setStatus("mandatory")
_DhcpRangeGateway_Type = IpAddress
_DhcpRangeGateway_Object = MibTableColumn
dhcpRangeGateway = _DhcpRangeGateway_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 1, 1, 5),
    _DhcpRangeGateway_Type()
)
dhcpRangeGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRangeGateway.setStatus("mandatory")
_DhcpTrapVariable_ObjectIdentity = ObjectIdentity
dhcpTrapVariable = _DhcpTrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 2)
)
_DhcpRangeExhaustedGateway_Type = IpAddress
_DhcpRangeExhaustedGateway_Object = MibScalar
dhcpRangeExhaustedGateway = _DhcpRangeExhaustedGateway_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 2, 1),
    _DhcpRangeExhaustedGateway_Type()
)
dhcpRangeExhaustedGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRangeExhaustedGateway.setStatus("mandatory")
_DhcpRangeExhaustedInterface_Type = IpAddress
_DhcpRangeExhaustedInterface_Object = MibScalar
dhcpRangeExhaustedInterface = _DhcpRangeExhaustedInterface_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 2, 2),
    _DhcpRangeExhaustedInterface_Type()
)
dhcpRangeExhaustedInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRangeExhaustedInterface.setStatus("mandatory")
_DhcpClientTable_Object = MibTable
dhcpClientTable = _DhcpClientTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 3)
)
if mibBuilder.loadTexts:
    dhcpClientTable.setStatus("mandatory")
_DhcpClientEntry_Object = MibTableRow
dhcpClientEntry = _DhcpClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 3, 1)
)
dhcpClientEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "dhcpRangeIndex"),
    (0, "ALLIEDTELESYN-MIB", "dhcpClientIpAddress"),
)
if mibBuilder.loadTexts:
    dhcpClientEntry.setStatus("mandatory")
_DhcpClientIpAddress_Type = IpAddress
_DhcpClientIpAddress_Object = MibTableColumn
dhcpClientIpAddress = _DhcpClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 3, 1, 1),
    _DhcpClientIpAddress_Type()
)
dhcpClientIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientIpAddress.setStatus("mandatory")
_DhcpClientID_Type = OctetString
_DhcpClientID_Object = MibTableColumn
dhcpClientID = _DhcpClientID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 3, 1, 2),
    _DhcpClientID_Type()
)
dhcpClientID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientID.setStatus("mandatory")


class _DhcpClientState_Type(Integer32):
    """Custom type dhcpClientState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inuse", 2),
          ("offered", 3),
          ("reclaiming", 1),
          ("unused", 0))
    )


_DhcpClientState_Type.__name__ = "Integer32"
_DhcpClientState_Object = MibTableColumn
dhcpClientState = _DhcpClientState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 3, 1, 3),
    _DhcpClientState_Type()
)
dhcpClientState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientState.setStatus("mandatory")


class _DhcpClientType_Type(Integer32):
    """Custom type dhcpClientType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("dyn", 2),
          ("static", 3))
    )


_DhcpClientType_Type.__name__ = "Integer32"
_DhcpClientType_Object = MibTableColumn
dhcpClientType = _DhcpClientType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 3, 1, 4),
    _DhcpClientType_Type()
)
dhcpClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientType.setStatus("mandatory")
_DhcpClientExpiry_Type = OctetString
_DhcpClientExpiry_Object = MibTableColumn
dhcpClientExpiry = _DhcpClientExpiry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 3, 1, 5),
    _DhcpClientExpiry_Type()
)
dhcpClientExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientExpiry.setStatus("mandatory")
_Firewall_ObjectIdentity = ObjectIdentity
firewall = _Firewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 77)
)


class _FirewallTrapMessage_Type(DisplayString):
    """Custom type firewallTrapMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FirewallTrapMessage_Type.__name__ = "DisplayString"
_FirewallTrapMessage_Object = MibScalar
firewallTrapMessage = _FirewallTrapMessage_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 77, 1),
    _FirewallTrapMessage_Type()
)
firewallTrapMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallTrapMessage.setStatus("mandatory")
_Swi_ObjectIdentity = ObjectIdentity
swi = _Swi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87)
)
_SwiPortTable_Object = MibTable
swiPortTable = _SwiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 1)
)
if mibBuilder.loadTexts:
    swiPortTable.setStatus("mandatory")
_SwiPortEntry_Object = MibTableRow
swiPortEntry = _SwiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 1, 1)
)
swiPortEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "swiPortNumber"),
)
if mibBuilder.loadTexts:
    swiPortEntry.setStatus("mandatory")
_SwiPortNumber_Type = Integer32
_SwiPortNumber_Object = MibTableColumn
swiPortNumber = _SwiPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 1, 1, 1),
    _SwiPortNumber_Type()
)
swiPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swiPortNumber.setStatus("mandatory")
_SwiPortIngressLimit_Type = Integer32
_SwiPortIngressLimit_Object = MibTableColumn
swiPortIngressLimit = _SwiPortIngressLimit_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 1, 1, 20),
    _SwiPortIngressLimit_Type()
)
swiPortIngressLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swiPortIngressLimit.setStatus("mandatory")
_SwiPortEgressLimit_Type = Integer32
_SwiPortEgressLimit_Object = MibTableColumn
swiPortEgressLimit = _SwiPortEgressLimit_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 1, 1, 21),
    _SwiPortEgressLimit_Type()
)
swiPortEgressLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swiPortEgressLimit.setStatus("mandatory")
_Swi56xxPortCounterTable_Object = MibTable
swi56xxPortCounterTable = _Swi56xxPortCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2)
)
if mibBuilder.loadTexts:
    swi56xxPortCounterTable.setStatus("mandatory")
_Swi56xxPortCounterEntry_Object = MibTableRow
swi56xxPortCounterEntry = _Swi56xxPortCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1)
)
swi56xxPortCounterEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "swi56xxPortNumber"),
)
if mibBuilder.loadTexts:
    swi56xxPortCounterEntry.setStatus("mandatory")
_Swi56xxPortNumber_Type = Integer32
_Swi56xxPortNumber_Object = MibTableColumn
swi56xxPortNumber = _Swi56xxPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 1),
    _Swi56xxPortNumber_Type()
)
swi56xxPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortNumber.setStatus("mandatory")
_Swi56xxRxTx64kPkts_Type = Counter32
_Swi56xxRxTx64kPkts_Object = MibTableColumn
swi56xxRxTx64kPkts = _Swi56xxRxTx64kPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 2),
    _Swi56xxRxTx64kPkts_Type()
)
swi56xxRxTx64kPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxRxTx64kPkts.setStatus("mandatory")
_Swi56xxRxTx65To127kPkts_Type = Counter32
_Swi56xxRxTx65To127kPkts_Object = MibTableColumn
swi56xxRxTx65To127kPkts = _Swi56xxRxTx65To127kPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 3),
    _Swi56xxRxTx65To127kPkts_Type()
)
swi56xxRxTx65To127kPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxRxTx65To127kPkts.setStatus("mandatory")
_Swi56xxRxTx128To255kPkts_Type = Counter32
_Swi56xxRxTx128To255kPkts_Object = MibTableColumn
swi56xxRxTx128To255kPkts = _Swi56xxRxTx128To255kPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 4),
    _Swi56xxRxTx128To255kPkts_Type()
)
swi56xxRxTx128To255kPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxRxTx128To255kPkts.setStatus("mandatory")
_Swi56xxRxTx256To511kPkts_Type = Counter32
_Swi56xxRxTx256To511kPkts_Object = MibTableColumn
swi56xxRxTx256To511kPkts = _Swi56xxRxTx256To511kPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 5),
    _Swi56xxRxTx256To511kPkts_Type()
)
swi56xxRxTx256To511kPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxRxTx256To511kPkts.setStatus("mandatory")
_Swi56xxRxTx512To1023kPkts_Type = Counter32
_Swi56xxRxTx512To1023kPkts_Object = MibTableColumn
swi56xxRxTx512To1023kPkts = _Swi56xxRxTx512To1023kPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 6),
    _Swi56xxRxTx512To1023kPkts_Type()
)
swi56xxRxTx512To1023kPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxRxTx512To1023kPkts.setStatus("mandatory")
_Swi56xxRxTx1024ToMaxPktSzPkts_Type = Counter32
_Swi56xxRxTx1024ToMaxPktSzPkts_Object = MibTableColumn
swi56xxRxTx1024ToMaxPktSzPkts = _Swi56xxRxTx1024ToMaxPktSzPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 7),
    _Swi56xxRxTx1024ToMaxPktSzPkts_Type()
)
swi56xxRxTx1024ToMaxPktSzPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxRxTx1024ToMaxPktSzPkts.setStatus("mandatory")
_Swi56xxRxTx519To1522kPkts_Type = Counter32
_Swi56xxRxTx519To1522kPkts_Object = MibTableColumn
swi56xxRxTx519To1522kPkts = _Swi56xxRxTx519To1522kPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 8),
    _Swi56xxRxTx519To1522kPkts_Type()
)
swi56xxRxTx519To1522kPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxRxTx519To1522kPkts.setStatus("mandatory")
_Swi56xxPortRxOctets_Type = Counter32
_Swi56xxPortRxOctets_Object = MibTableColumn
swi56xxPortRxOctets = _Swi56xxPortRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 9),
    _Swi56xxPortRxOctets_Type()
)
swi56xxPortRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxOctets.setStatus("mandatory")
_Swi56xxPortRxPkts_Type = Counter32
_Swi56xxPortRxPkts_Object = MibTableColumn
swi56xxPortRxPkts = _Swi56xxPortRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 10),
    _Swi56xxPortRxPkts_Type()
)
swi56xxPortRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxPkts.setStatus("mandatory")
_Swi56xxPortRxFCSErrors_Type = Counter32
_Swi56xxPortRxFCSErrors_Object = MibTableColumn
swi56xxPortRxFCSErrors = _Swi56xxPortRxFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 11),
    _Swi56xxPortRxFCSErrors_Type()
)
swi56xxPortRxFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxFCSErrors.setStatus("mandatory")
_Swi56xxPortRxMulticastPkts_Type = Counter32
_Swi56xxPortRxMulticastPkts_Object = MibTableColumn
swi56xxPortRxMulticastPkts = _Swi56xxPortRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 12),
    _Swi56xxPortRxMulticastPkts_Type()
)
swi56xxPortRxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxMulticastPkts.setStatus("mandatory")
_Swi56xxPortRxBroadcastPkts_Type = Counter32
_Swi56xxPortRxBroadcastPkts_Object = MibTableColumn
swi56xxPortRxBroadcastPkts = _Swi56xxPortRxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 13),
    _Swi56xxPortRxBroadcastPkts_Type()
)
swi56xxPortRxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxBroadcastPkts.setStatus("mandatory")
_Swi56xxPortRxPauseMACCtlFrms_Type = Counter32
_Swi56xxPortRxPauseMACCtlFrms_Object = MibTableColumn
swi56xxPortRxPauseMACCtlFrms = _Swi56xxPortRxPauseMACCtlFrms_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 14),
    _Swi56xxPortRxPauseMACCtlFrms_Type()
)
swi56xxPortRxPauseMACCtlFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxPauseMACCtlFrms.setStatus("mandatory")
_Swi56xxPortRxOversizePkts_Type = Counter32
_Swi56xxPortRxOversizePkts_Object = MibTableColumn
swi56xxPortRxOversizePkts = _Swi56xxPortRxOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 15),
    _Swi56xxPortRxOversizePkts_Type()
)
swi56xxPortRxOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxOversizePkts.setStatus("mandatory")
_Swi56xxPortRxFragments_Type = Counter32
_Swi56xxPortRxFragments_Object = MibTableColumn
swi56xxPortRxFragments = _Swi56xxPortRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 16),
    _Swi56xxPortRxFragments_Type()
)
swi56xxPortRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxFragments.setStatus("mandatory")
_Swi56xxPortRxJabbers_Type = Counter32
_Swi56xxPortRxJabbers_Object = MibTableColumn
swi56xxPortRxJabbers = _Swi56xxPortRxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 17),
    _Swi56xxPortRxJabbers_Type()
)
swi56xxPortRxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxJabbers.setStatus("mandatory")
_Swi56xxPortRxMACControlFrms_Type = Counter32
_Swi56xxPortRxMACControlFrms_Object = MibTableColumn
swi56xxPortRxMACControlFrms = _Swi56xxPortRxMACControlFrms_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 18),
    _Swi56xxPortRxMACControlFrms_Type()
)
swi56xxPortRxMACControlFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxMACControlFrms.setStatus("mandatory")
_Swi56xxPortRxUnsupportOpcode_Type = Counter32
_Swi56xxPortRxUnsupportOpcode_Object = MibTableColumn
swi56xxPortRxUnsupportOpcode = _Swi56xxPortRxUnsupportOpcode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 19),
    _Swi56xxPortRxUnsupportOpcode_Type()
)
swi56xxPortRxUnsupportOpcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxUnsupportOpcode.setStatus("mandatory")
_Swi56xxPortRxAlignmentErrors_Type = Counter32
_Swi56xxPortRxAlignmentErrors_Object = MibTableColumn
swi56xxPortRxAlignmentErrors = _Swi56xxPortRxAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 20),
    _Swi56xxPortRxAlignmentErrors_Type()
)
swi56xxPortRxAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxAlignmentErrors.setStatus("mandatory")
_Swi56xxPortRxOutOfRngeLenFld_Type = Counter32
_Swi56xxPortRxOutOfRngeLenFld_Object = MibTableColumn
swi56xxPortRxOutOfRngeLenFld = _Swi56xxPortRxOutOfRngeLenFld_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 21),
    _Swi56xxPortRxOutOfRngeLenFld_Type()
)
swi56xxPortRxOutOfRngeLenFld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxOutOfRngeLenFld.setStatus("mandatory")
_Swi56xxPortRxSymErDurCarrier_Type = Counter32
_Swi56xxPortRxSymErDurCarrier_Object = MibTableColumn
swi56xxPortRxSymErDurCarrier = _Swi56xxPortRxSymErDurCarrier_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 22),
    _Swi56xxPortRxSymErDurCarrier_Type()
)
swi56xxPortRxSymErDurCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxSymErDurCarrier.setStatus("mandatory")
_Swi56xxPortRxCarrierSenseErr_Type = Counter32
_Swi56xxPortRxCarrierSenseErr_Object = MibTableColumn
swi56xxPortRxCarrierSenseErr = _Swi56xxPortRxCarrierSenseErr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 23),
    _Swi56xxPortRxCarrierSenseErr_Type()
)
swi56xxPortRxCarrierSenseErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxCarrierSenseErr.setStatus("mandatory")
_Swi56xxPortRxUndersizePkts_Type = Counter32
_Swi56xxPortRxUndersizePkts_Object = MibTableColumn
swi56xxPortRxUndersizePkts = _Swi56xxPortRxUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 24),
    _Swi56xxPortRxUndersizePkts_Type()
)
swi56xxPortRxUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxUndersizePkts.setStatus("mandatory")
_Swi56xxPortRxIpInHdrErrors_Type = Counter32
_Swi56xxPortRxIpInHdrErrors_Object = MibTableColumn
swi56xxPortRxIpInHdrErrors = _Swi56xxPortRxIpInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 25),
    _Swi56xxPortRxIpInHdrErrors_Type()
)
swi56xxPortRxIpInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxIpInHdrErrors.setStatus("mandatory")
_Swi56xxPortTxOctets_Type = Counter32
_Swi56xxPortTxOctets_Object = MibTableColumn
swi56xxPortTxOctets = _Swi56xxPortTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 26),
    _Swi56xxPortTxOctets_Type()
)
swi56xxPortTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxOctets.setStatus("mandatory")
_Swi56xxPortTxPkts_Type = Counter32
_Swi56xxPortTxPkts_Object = MibTableColumn
swi56xxPortTxPkts = _Swi56xxPortTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 27),
    _Swi56xxPortTxPkts_Type()
)
swi56xxPortTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxPkts.setStatus("mandatory")
_Swi56xxPortTxFCSErrors_Type = Counter32
_Swi56xxPortTxFCSErrors_Object = MibTableColumn
swi56xxPortTxFCSErrors = _Swi56xxPortTxFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 28),
    _Swi56xxPortTxFCSErrors_Type()
)
swi56xxPortTxFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxFCSErrors.setStatus("mandatory")
_Swi56xxPortTxMulticastPkts_Type = Counter32
_Swi56xxPortTxMulticastPkts_Object = MibTableColumn
swi56xxPortTxMulticastPkts = _Swi56xxPortTxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 29),
    _Swi56xxPortTxMulticastPkts_Type()
)
swi56xxPortTxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxMulticastPkts.setStatus("mandatory")
_Swi56xxPortTxBroadcastPkts_Type = Counter32
_Swi56xxPortTxBroadcastPkts_Object = MibTableColumn
swi56xxPortTxBroadcastPkts = _Swi56xxPortTxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 30),
    _Swi56xxPortTxBroadcastPkts_Type()
)
swi56xxPortTxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxBroadcastPkts.setStatus("mandatory")
_Swi56xxPortTxPauseMACCtlFrms_Type = Counter32
_Swi56xxPortTxPauseMACCtlFrms_Object = MibTableColumn
swi56xxPortTxPauseMACCtlFrms = _Swi56xxPortTxPauseMACCtlFrms_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 31),
    _Swi56xxPortTxPauseMACCtlFrms_Type()
)
swi56xxPortTxPauseMACCtlFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxPauseMACCtlFrms.setStatus("mandatory")
_Swi56xxPortTxOversizePkts_Type = Counter32
_Swi56xxPortTxOversizePkts_Object = MibTableColumn
swi56xxPortTxOversizePkts = _Swi56xxPortTxOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 32),
    _Swi56xxPortTxOversizePkts_Type()
)
swi56xxPortTxOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxOversizePkts.setStatus("mandatory")
_Swi56xxPortTxFragments_Type = Counter32
_Swi56xxPortTxFragments_Object = MibTableColumn
swi56xxPortTxFragments = _Swi56xxPortTxFragments_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 33),
    _Swi56xxPortTxFragments_Type()
)
swi56xxPortTxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxFragments.setStatus("mandatory")
_Swi56xxPortTxJabbers_Type = Counter32
_Swi56xxPortTxJabbers_Object = MibTableColumn
swi56xxPortTxJabbers = _Swi56xxPortTxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 34),
    _Swi56xxPortTxJabbers_Type()
)
swi56xxPortTxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxJabbers.setStatus("mandatory")
_Swi56xxPortTxPauseCtrlFrms_Type = Counter32
_Swi56xxPortTxPauseCtrlFrms_Object = MibTableColumn
swi56xxPortTxPauseCtrlFrms = _Swi56xxPortTxPauseCtrlFrms_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 35),
    _Swi56xxPortTxPauseCtrlFrms_Type()
)
swi56xxPortTxPauseCtrlFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxPauseCtrlFrms.setStatus("mandatory")
_Swi56xxPortTxFrameWDeferrdTx_Type = Counter32
_Swi56xxPortTxFrameWDeferrdTx_Object = MibTableColumn
swi56xxPortTxFrameWDeferrdTx = _Swi56xxPortTxFrameWDeferrdTx_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 36),
    _Swi56xxPortTxFrameWDeferrdTx_Type()
)
swi56xxPortTxFrameWDeferrdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxFrameWDeferrdTx.setStatus("mandatory")
_Swi56xxPortTxFrmWExcesDefer_Type = Counter32
_Swi56xxPortTxFrmWExcesDefer_Object = MibTableColumn
swi56xxPortTxFrmWExcesDefer = _Swi56xxPortTxFrmWExcesDefer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 37),
    _Swi56xxPortTxFrmWExcesDefer_Type()
)
swi56xxPortTxFrmWExcesDefer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxFrmWExcesDefer.setStatus("mandatory")
_Swi56xxPortTxSingleCollsnFrm_Type = Counter32
_Swi56xxPortTxSingleCollsnFrm_Object = MibTableColumn
swi56xxPortTxSingleCollsnFrm = _Swi56xxPortTxSingleCollsnFrm_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 38),
    _Swi56xxPortTxSingleCollsnFrm_Type()
)
swi56xxPortTxSingleCollsnFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxSingleCollsnFrm.setStatus("mandatory")
_Swi56xxPortTxMultCollsnFrm_Type = Counter32
_Swi56xxPortTxMultCollsnFrm_Object = MibTableColumn
swi56xxPortTxMultCollsnFrm = _Swi56xxPortTxMultCollsnFrm_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 39),
    _Swi56xxPortTxMultCollsnFrm_Type()
)
swi56xxPortTxMultCollsnFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxMultCollsnFrm.setStatus("mandatory")
_Swi56xxPortTxLateCollsns_Type = Counter32
_Swi56xxPortTxLateCollsns_Object = MibTableColumn
swi56xxPortTxLateCollsns = _Swi56xxPortTxLateCollsns_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 40),
    _Swi56xxPortTxLateCollsns_Type()
)
swi56xxPortTxLateCollsns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxLateCollsns.setStatus("mandatory")
_Swi56xxPortTxExcessivCollsns_Type = Counter32
_Swi56xxPortTxExcessivCollsns_Object = MibTableColumn
swi56xxPortTxExcessivCollsns = _Swi56xxPortTxExcessivCollsns_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 41),
    _Swi56xxPortTxExcessivCollsns_Type()
)
swi56xxPortTxExcessivCollsns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxExcessivCollsns.setStatus("mandatory")
_Swi56xxPortTxCollisionFrames_Type = Counter32
_Swi56xxPortTxCollisionFrames_Object = MibTableColumn
swi56xxPortTxCollisionFrames = _Swi56xxPortTxCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 42),
    _Swi56xxPortTxCollisionFrames_Type()
)
swi56xxPortTxCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxCollisionFrames.setStatus("mandatory")
_Swi56xxPortMiscDropEvents_Type = Counter32
_Swi56xxPortMiscDropEvents_Object = MibTableColumn
swi56xxPortMiscDropEvents = _Swi56xxPortMiscDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 43),
    _Swi56xxPortMiscDropEvents_Type()
)
swi56xxPortMiscDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortMiscDropEvents.setStatus("mandatory")
_Swi56xxPortMiscTaggedPktTx_Type = Counter32
_Swi56xxPortMiscTaggedPktTx_Object = MibTableColumn
swi56xxPortMiscTaggedPktTx = _Swi56xxPortMiscTaggedPktTx_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 44),
    _Swi56xxPortMiscTaggedPktTx_Type()
)
swi56xxPortMiscTaggedPktTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortMiscTaggedPktTx.setStatus("mandatory")
_Swi56xxPortMiscTotalPktTxAbort_Type = Counter32
_Swi56xxPortMiscTotalPktTxAbort_Object = MibTableColumn
swi56xxPortMiscTotalPktTxAbort = _Swi56xxPortMiscTotalPktTxAbort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 45),
    _Swi56xxPortMiscTotalPktTxAbort_Type()
)
swi56xxPortMiscTotalPktTxAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortMiscTotalPktTxAbort.setStatus("mandatory")
_Swi56xxPortHWMultiTTLexpired_Type = Counter32
_Swi56xxPortHWMultiTTLexpired_Object = MibTableColumn
swi56xxPortHWMultiTTLexpired = _Swi56xxPortHWMultiTTLexpired_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 46),
    _Swi56xxPortHWMultiTTLexpired_Type()
)
swi56xxPortHWMultiTTLexpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortHWMultiTTLexpired.setStatus("mandatory")
_Swi56xxPortHWMultiBridgedFrames_Type = Counter32
_Swi56xxPortHWMultiBridgedFrames_Object = MibTableColumn
swi56xxPortHWMultiBridgedFrames = _Swi56xxPortHWMultiBridgedFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 47),
    _Swi56xxPortHWMultiBridgedFrames_Type()
)
swi56xxPortHWMultiBridgedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortHWMultiBridgedFrames.setStatus("mandatory")
_Swi56xxPortHWMultiRxDrops_Type = Counter32
_Swi56xxPortHWMultiRxDrops_Object = MibTableColumn
swi56xxPortHWMultiRxDrops = _Swi56xxPortHWMultiRxDrops_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 48),
    _Swi56xxPortHWMultiRxDrops_Type()
)
swi56xxPortHWMultiRxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortHWMultiRxDrops.setStatus("mandatory")
_Swi56xxPortHWMultiTxDrops_Type = Counter32
_Swi56xxPortHWMultiTxDrops_Object = MibTableColumn
swi56xxPortHWMultiTxDrops = _Swi56xxPortHWMultiTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 49),
    _Swi56xxPortHWMultiTxDrops_Type()
)
swi56xxPortHWMultiTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortHWMultiTxDrops.setStatus("mandatory")
_SwiDebugVariables_ObjectIdentity = ObjectIdentity
swiDebugVariables = _SwiDebugVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 3)
)
_SwiDebugMemoryParityErrors_Type = Counter32
_SwiDebugMemoryParityErrors_Object = MibScalar
swiDebugMemoryParityErrors = _SwiDebugMemoryParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 3, 1),
    _SwiDebugMemoryParityErrors_Type()
)
swiDebugMemoryParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swiDebugMemoryParityErrors.setStatus("mandatory")
_Lb_ObjectIdentity = ObjectIdentity
lb = _Lb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104)
)
_LbShowGlobalTable_Object = MibTable
lbShowGlobalTable = _LbShowGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 1)
)
if mibBuilder.loadTexts:
    lbShowGlobalTable.setStatus("mandatory")
_LbShowGlobalEntry_Object = MibTableRow
lbShowGlobalEntry = _LbShowGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 1, 1)
)
lbShowGlobalEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "lbGlobalIndex"),
)
if mibBuilder.loadTexts:
    lbShowGlobalEntry.setStatus("mandatory")
_LbGlobalIndex_Type = Integer32
_LbGlobalIndex_Object = MibTableColumn
lbGlobalIndex = _LbGlobalIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 1, 1, 1),
    _LbGlobalIndex_Type()
)
lbGlobalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbGlobalIndex.setStatus("mandatory")
_LbAffinityTimeOut_Type = Integer32
_LbAffinityTimeOut_Object = MibTableColumn
lbAffinityTimeOut = _LbAffinityTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 1, 1, 2),
    _LbAffinityTimeOut_Type()
)
lbAffinityTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbAffinityTimeOut.setStatus("mandatory")
_LbOrphanTimeOut_Type = Integer32
_LbOrphanTimeOut_Object = MibTableColumn
lbOrphanTimeOut = _LbOrphanTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 1, 1, 3),
    _LbOrphanTimeOut_Type()
)
lbOrphanTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbOrphanTimeOut.setStatus("mandatory")
_LbCriticalRst_Type = Integer32
_LbCriticalRst_Object = MibTableColumn
lbCriticalRst = _LbCriticalRst_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 1, 1, 4),
    _LbCriticalRst_Type()
)
lbCriticalRst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbCriticalRst.setStatus("mandatory")
_LbTotalResources_Type = Integer32
_LbTotalResources_Object = MibTableColumn
lbTotalResources = _LbTotalResources_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 1, 1, 5),
    _LbTotalResources_Type()
)
lbTotalResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTotalResources.setStatus("mandatory")
_LbTotalResPools_Type = Integer32
_LbTotalResPools_Object = MibTableColumn
lbTotalResPools = _LbTotalResPools_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 1, 1, 6),
    _LbTotalResPools_Type()
)
lbTotalResPools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTotalResPools.setStatus("mandatory")
_LbTotalVirtBals_Type = Integer32
_LbTotalVirtBals_Object = MibTableColumn
lbTotalVirtBals = _LbTotalVirtBals_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 1, 1, 7),
    _LbTotalVirtBals_Type()
)
lbTotalVirtBals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTotalVirtBals.setStatus("mandatory")
_LbCurrentConnections_Type = Integer32
_LbCurrentConnections_Object = MibTableColumn
lbCurrentConnections = _LbCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 1, 1, 8),
    _LbCurrentConnections_Type()
)
lbCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbCurrentConnections.setStatus("mandatory")
_LbShowResTable_Object = MibTable
lbShowResTable = _LbShowResTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 2)
)
if mibBuilder.loadTexts:
    lbShowResTable.setStatus("mandatory")
_LbShowResEntry_Object = MibTableRow
lbShowResEntry = _LbShowResEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 2, 1)
)
lbShowResEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "lbResIndex"),
)
if mibBuilder.loadTexts:
    lbShowResEntry.setStatus("mandatory")
_LbResIndex_Type = Integer32
_LbResIndex_Object = MibTableColumn
lbResIndex = _LbResIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 2, 1, 1),
    _LbResIndex_Type()
)
lbResIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbResIndex.setStatus("mandatory")


class _LbResource_Type(DisplayString):
    """Custom type lbResource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LbResource_Type.__name__ = "DisplayString"
_LbResource_Object = MibTableColumn
lbResource = _LbResource_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 2, 1, 2),
    _LbResource_Type()
)
lbResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbResource.setStatus("mandatory")
_LbResIp_Type = IpAddress
_LbResIp_Object = MibTableColumn
lbResIp = _LbResIp_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 2, 1, 3),
    _LbResIp_Type()
)
lbResIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbResIp.setStatus("mandatory")
_LbResPort_Type = Integer32
_LbResPort_Object = MibTableColumn
lbResPort = _LbResPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 2, 1, 4),
    _LbResPort_Type()
)
lbResPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbResPort.setStatus("mandatory")


class _LbResState_Type(DisplayString):
    """Custom type lbResState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LbResState_Type.__name__ = "DisplayString"
_LbResState_Object = MibTableColumn
lbResState = _LbResState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 2, 1, 5),
    _LbResState_Type()
)
lbResState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbResState.setStatus("mandatory")
_LbResWeight_Type = Integer32
_LbResWeight_Object = MibTableColumn
lbResWeight = _LbResWeight_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 2, 1, 6),
    _LbResWeight_Type()
)
lbResWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbResWeight.setStatus("mandatory")
_LbResTotalConnections_Type = Integer32
_LbResTotalConnections_Object = MibTableColumn
lbResTotalConnections = _LbResTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 2, 1, 7),
    _LbResTotalConnections_Type()
)
lbResTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbResTotalConnections.setStatus("mandatory")
_LbResCurrentConnections_Type = Integer32
_LbResCurrentConnections_Object = MibTableColumn
lbResCurrentConnections = _LbResCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 2, 1, 8),
    _LbResCurrentConnections_Type()
)
lbResCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbResCurrentConnections.setStatus("mandatory")
_LbShowResPoolTable_Object = MibTable
lbShowResPoolTable = _LbShowResPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 3)
)
if mibBuilder.loadTexts:
    lbShowResPoolTable.setStatus("mandatory")
_LbShowResPoolEntry_Object = MibTableRow
lbShowResPoolEntry = _LbShowResPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 3, 1)
)
lbShowResPoolEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "lbResPoolIndex"),
    (0, "ALLIEDTELESYN-MIB", "lbResPoolResourceIndex"),
)
if mibBuilder.loadTexts:
    lbShowResPoolEntry.setStatus("mandatory")
_LbResPoolIndex_Type = Integer32
_LbResPoolIndex_Object = MibTableColumn
lbResPoolIndex = _LbResPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 3, 1, 1),
    _LbResPoolIndex_Type()
)
lbResPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbResPoolIndex.setStatus("mandatory")
_LbResPoolResourceIndex_Type = Integer32
_LbResPoolResourceIndex_Object = MibTableColumn
lbResPoolResourceIndex = _LbResPoolResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 3, 1, 2),
    _LbResPoolResourceIndex_Type()
)
lbResPoolResourceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbResPoolResourceIndex.setStatus("mandatory")


class _LbResPool_Type(DisplayString):
    """Custom type lbResPool based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LbResPool_Type.__name__ = "DisplayString"
_LbResPool_Object = MibTableColumn
lbResPool = _LbResPool_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 3, 1, 3),
    _LbResPool_Type()
)
lbResPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbResPool.setStatus("mandatory")


class _LbResPoolSelectionAlg_Type(DisplayString):
    """Custom type lbResPoolSelectionAlg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LbResPoolSelectionAlg_Type.__name__ = "DisplayString"
_LbResPoolSelectionAlg_Object = MibTableColumn
lbResPoolSelectionAlg = _LbResPoolSelectionAlg_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 3, 1, 4),
    _LbResPoolSelectionAlg_Type()
)
lbResPoolSelectionAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbResPoolSelectionAlg.setStatus("mandatory")


class _LbResPoolFailOnLast_Type(DisplayString):
    """Custom type lbResPoolFailOnLast based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LbResPoolFailOnLast_Type.__name__ = "DisplayString"
_LbResPoolFailOnLast_Object = MibTableColumn
lbResPoolFailOnLast = _LbResPoolFailOnLast_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 3, 1, 5),
    _LbResPoolFailOnLast_Type()
)
lbResPoolFailOnLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbResPoolFailOnLast.setStatus("mandatory")


class _LbResPoolTotalConnections_Type(DisplayString):
    """Custom type lbResPoolTotalConnections based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LbResPoolTotalConnections_Type.__name__ = "DisplayString"
_LbResPoolTotalConnections_Object = MibTableColumn
lbResPoolTotalConnections = _LbResPoolTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 3, 1, 6),
    _LbResPoolTotalConnections_Type()
)
lbResPoolTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbResPoolTotalConnections.setStatus("mandatory")


class _LbResPoolResources_Type(DisplayString):
    """Custom type lbResPoolResources based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LbResPoolResources_Type.__name__ = "DisplayString"
_LbResPoolResources_Object = MibTableColumn
lbResPoolResources = _LbResPoolResources_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 3, 1, 7),
    _LbResPoolResources_Type()
)
lbResPoolResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbResPoolResources.setStatus("mandatory")
_LbShowVirtBalTable_Object = MibTable
lbShowVirtBalTable = _LbShowVirtBalTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 4)
)
if mibBuilder.loadTexts:
    lbShowVirtBalTable.setStatus("mandatory")
_LbShowVirtBalEntry_Object = MibTableRow
lbShowVirtBalEntry = _LbShowVirtBalEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 4, 1)
)
lbShowVirtBalEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "lbVirtBalIndex"),
)
if mibBuilder.loadTexts:
    lbShowVirtBalEntry.setStatus("mandatory")
_LbVirtBalIndex_Type = Integer32
_LbVirtBalIndex_Object = MibTableColumn
lbVirtBalIndex = _LbVirtBalIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 4, 1, 1),
    _LbVirtBalIndex_Type()
)
lbVirtBalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbVirtBalIndex.setStatus("mandatory")


class _LbVirtBal_Type(DisplayString):
    """Custom type lbVirtBal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LbVirtBal_Type.__name__ = "DisplayString"
_LbVirtBal_Object = MibTableColumn
lbVirtBal = _LbVirtBal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 4, 1, 2),
    _LbVirtBal_Type()
)
lbVirtBal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbVirtBal.setStatus("mandatory")
_LbVirtBalPublicIp_Type = IpAddress
_LbVirtBalPublicIp_Object = MibTableColumn
lbVirtBalPublicIp = _LbVirtBalPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 4, 1, 3),
    _LbVirtBalPublicIp_Type()
)
lbVirtBalPublicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbVirtBalPublicIp.setStatus("mandatory")
_LbVirtBalPublicPort_Type = Integer32
_LbVirtBalPublicPort_Object = MibTableColumn
lbVirtBalPublicPort = _LbVirtBalPublicPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 4, 1, 4),
    _LbVirtBalPublicPort_Type()
)
lbVirtBalPublicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbVirtBalPublicPort.setStatus("mandatory")


class _LbVirtBalState_Type(DisplayString):
    """Custom type lbVirtBalState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LbVirtBalState_Type.__name__ = "DisplayString"
_LbVirtBalState_Object = MibTableColumn
lbVirtBalState = _LbVirtBalState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 4, 1, 5),
    _LbVirtBalState_Type()
)
lbVirtBalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbVirtBalState.setStatus("mandatory")


class _LbVirtBalResPool_Type(DisplayString):
    """Custom type lbVirtBalResPool based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LbVirtBalResPool_Type.__name__ = "DisplayString"
_LbVirtBalResPool_Object = MibTableColumn
lbVirtBalResPool = _LbVirtBalResPool_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 4, 1, 6),
    _LbVirtBalResPool_Type()
)
lbVirtBalResPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbVirtBalResPool.setStatus("mandatory")


class _LbVirtBalType_Type(DisplayString):
    """Custom type lbVirtBalType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LbVirtBalType_Type.__name__ = "DisplayString"
_LbVirtBalType_Object = MibTableColumn
lbVirtBalType = _LbVirtBalType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 4, 1, 7),
    _LbVirtBalType_Type()
)
lbVirtBalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbVirtBalType.setStatus("mandatory")
_LbVirtBalTotalConnections_Type = Integer32
_LbVirtBalTotalConnections_Object = MibTableColumn
lbVirtBalTotalConnections = _LbVirtBalTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 4, 1, 8),
    _LbVirtBalTotalConnections_Type()
)
lbVirtBalTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbVirtBalTotalConnections.setStatus("mandatory")


class _LbVirtBalAffinity_Type(DisplayString):
    """Custom type lbVirtBalAffinity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LbVirtBalAffinity_Type.__name__ = "DisplayString"
_LbVirtBalAffinity_Object = MibTableColumn
lbVirtBalAffinity = _LbVirtBalAffinity_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 4, 1, 9),
    _LbVirtBalAffinity_Type()
)
lbVirtBalAffinity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbVirtBalAffinity.setStatus("mandatory")


class _LbVirtBalHttpErrorCode_Type(DisplayString):
    """Custom type lbVirtBalHttpErrorCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LbVirtBalHttpErrorCode_Type.__name__ = "DisplayString"
_LbVirtBalHttpErrorCode_Object = MibTableColumn
lbVirtBalHttpErrorCode = _LbVirtBalHttpErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 4, 1, 10),
    _LbVirtBalHttpErrorCode_Type()
)
lbVirtBalHttpErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbVirtBalHttpErrorCode.setStatus("mandatory")
_LbShowAffTable_Object = MibTable
lbShowAffTable = _LbShowAffTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 5)
)
if mibBuilder.loadTexts:
    lbShowAffTable.setStatus("mandatory")
_LbShowAffEntry_Object = MibTableRow
lbShowAffEntry = _LbShowAffEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 5, 1)
)
lbShowAffEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "lbAffIndex"),
)
if mibBuilder.loadTexts:
    lbShowAffEntry.setStatus("mandatory")
_LbAffIndex_Type = Integer32
_LbAffIndex_Object = MibTableColumn
lbAffIndex = _LbAffIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 5, 1, 1),
    _LbAffIndex_Type()
)
lbAffIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbAffIndex.setStatus("mandatory")


class _LbAffVirtBal_Type(DisplayString):
    """Custom type lbAffVirtBal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LbAffVirtBal_Type.__name__ = "DisplayString"
_LbAffVirtBal_Object = MibTableColumn
lbAffVirtBal = _LbAffVirtBal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 5, 1, 2),
    _LbAffVirtBal_Type()
)
lbAffVirtBal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbAffVirtBal.setStatus("mandatory")
_LbAffClientIp_Type = IpAddress
_LbAffClientIp_Object = MibTableColumn
lbAffClientIp = _LbAffClientIp_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 5, 1, 3),
    _LbAffClientIp_Type()
)
lbAffClientIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbAffClientIp.setStatus("mandatory")


class _LbAffCookie_Type(DisplayString):
    """Custom type lbAffCookie based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LbAffCookie_Type.__name__ = "DisplayString"
_LbAffCookie_Object = MibTableColumn
lbAffCookie = _LbAffCookie_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 5, 1, 4),
    _LbAffCookie_Type()
)
lbAffCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbAffCookie.setStatus("mandatory")


class _LbAffResource_Type(DisplayString):
    """Custom type lbAffResource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LbAffResource_Type.__name__ = "DisplayString"
_LbAffResource_Object = MibTableColumn
lbAffResource = _LbAffResource_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 5, 1, 5),
    _LbAffResource_Type()
)
lbAffResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbAffResource.setStatus("mandatory")
_LbAffExpiry_Type = Integer32
_LbAffExpiry_Object = MibTableColumn
lbAffExpiry = _LbAffExpiry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 5, 1, 6),
    _LbAffExpiry_Type()
)
lbAffExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbAffExpiry.setStatus("mandatory")
_LbShowConTable_Object = MibTable
lbShowConTable = _LbShowConTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 6)
)
if mibBuilder.loadTexts:
    lbShowConTable.setStatus("mandatory")
_LbShowConEntry_Object = MibTableRow
lbShowConEntry = _LbShowConEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 6, 1)
)
lbShowConEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "lbConIndex"),
)
if mibBuilder.loadTexts:
    lbShowConEntry.setStatus("mandatory")
_LbConIndex_Type = Integer32
_LbConIndex_Object = MibTableColumn
lbConIndex = _LbConIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 6, 1, 1),
    _LbConIndex_Type()
)
lbConIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbConIndex.setStatus("mandatory")


class _LbConVirtBal_Type(DisplayString):
    """Custom type lbConVirtBal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LbConVirtBal_Type.__name__ = "DisplayString"
_LbConVirtBal_Object = MibTableColumn
lbConVirtBal = _LbConVirtBal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 6, 1, 2),
    _LbConVirtBal_Type()
)
lbConVirtBal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbConVirtBal.setStatus("mandatory")
_LbConClientIp_Type = IpAddress
_LbConClientIp_Object = MibTableColumn
lbConClientIp = _LbConClientIp_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 6, 1, 3),
    _LbConClientIp_Type()
)
lbConClientIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbConClientIp.setStatus("mandatory")
_LbConPort_Type = Integer32
_LbConPort_Object = MibTableColumn
lbConPort = _LbConPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 6, 1, 4),
    _LbConPort_Type()
)
lbConPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbConPort.setStatus("mandatory")


class _LbConResource_Type(DisplayString):
    """Custom type lbConResource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LbConResource_Type.__name__ = "DisplayString"
_LbConResource_Object = MibTableColumn
lbConResource = _LbConResource_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 6, 1, 5),
    _LbConResource_Type()
)
lbConResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbConResource.setStatus("mandatory")
_Ds3module_ObjectIdentity = ObjectIdentity
ds3module = _Ds3module_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 109)
)
_Ds3TrapTable_Object = MibTable
ds3TrapTable = _Ds3TrapTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 109, 1)
)
if mibBuilder.loadTexts:
    ds3TrapTable.setStatus("mandatory")
_Ds3TrapEntry_Object = MibTableRow
ds3TrapEntry = _Ds3TrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 109, 1, 1)
)
ds3TrapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ds3TrapEntry.setStatus("mandatory")


class _Ds3TcaTrapEnable_Type(Integer32):
    """Custom type ds3TcaTrapEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ds3TcaTrapEnable_Type.__name__ = "Integer32"
_Ds3TcaTrapEnable_Object = MibTableColumn
ds3TcaTrapEnable = _Ds3TcaTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 109, 1, 1, 1),
    _Ds3TcaTrapEnable_Type()
)
ds3TcaTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3TcaTrapEnable.setStatus("mandatory")


class _Ds3TrapError_Type(Integer32):
    """Custom type ds3TrapError based on Integer32"""
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
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("ds3CCVs", 9),
          ("ds3CESs", 10),
          ("ds3CSESs", 11),
          ("ds3LCVs", 6),
          ("ds3LESs", 8),
          ("ds3NoError", 1),
          ("ds3PCVs", 7),
          ("ds3PES", 2),
          ("ds3PSES", 3),
          ("ds3SEFs", 4),
          ("ds3UAS", 5))
    )


_Ds3TrapError_Type.__name__ = "Integer32"
_Ds3TrapError_Object = MibTableColumn
ds3TrapError = _Ds3TrapError_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 109, 1, 1, 2),
    _Ds3TrapError_Type()
)
ds3TrapError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3TrapError.setStatus("mandatory")


class _Ds3TrapLoc_Type(Integer32):
    """Custom type ds3TrapLoc based on Integer32"""
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
        *(("ds3Far", 3),
          ("ds3Near", 2),
          ("ds3NoLoc", 1))
    )


_Ds3TrapLoc_Type.__name__ = "Integer32"
_Ds3TrapLoc_Object = MibTableColumn
ds3TrapLoc = _Ds3TrapLoc_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 109, 1, 1, 3),
    _Ds3TrapLoc_Type()
)
ds3TrapLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3TrapLoc.setStatus("mandatory")


class _Ds3TrapInterval_Type(Integer32):
    """Custom type ds3TrapInterval based on Integer32"""
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
        *(("ds3Fifteen", 2),
          ("ds3NoInt", 1),
          ("ds3Twentyfour", 3))
    )


_Ds3TrapInterval_Type.__name__ = "Integer32"
_Ds3TrapInterval_Object = MibTableColumn
ds3TrapInterval = _Ds3TrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 109, 1, 1, 4),
    _Ds3TrapInterval_Type()
)
ds3TrapInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3TrapInterval.setStatus("mandatory")
_ArInterfaces_ObjectIdentity = ObjectIdentity
arInterfaces = _ArInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5)
)
_ArBoardMaxIndex_Type = Integer32
_ArBoardMaxIndex_Object = MibScalar
arBoardMaxIndex = _ArBoardMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 1),
    _ArBoardMaxIndex_Type()
)
arBoardMaxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arBoardMaxIndex.setStatus("mandatory")
_ArBoardTable_Object = MibTable
arBoardTable = _ArBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 2)
)
if mibBuilder.loadTexts:
    arBoardTable.setStatus("mandatory")
_ArBoardEntry_Object = MibTableRow
arBoardEntry = _ArBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 2, 1)
)
arBoardEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "arBoardIndex"),
)
if mibBuilder.loadTexts:
    arBoardEntry.setStatus("mandatory")
_ArBoardIndex_Type = Integer32
_ArBoardIndex_Object = MibTableColumn
arBoardIndex = _ArBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 2, 1, 1),
    _ArBoardIndex_Type()
)
arBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arBoardIndex.setStatus("mandatory")
_ArBoardId_Type = ObjectIdentifier
_ArBoardId_Object = MibTableColumn
arBoardId = _ArBoardId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 2, 1, 2),
    _ArBoardId_Type()
)
arBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arBoardId.setStatus("mandatory")


class _ArBoardName_Type(DisplayString):
    """Custom type arBoardName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ArBoardName_Type.__name__ = "DisplayString"
_ArBoardName_Object = MibTableColumn
arBoardName = _ArBoardName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 2, 1, 3),
    _ArBoardName_Type()
)
arBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arBoardName.setStatus("mandatory")


class _ArBoardRevision_Type(DisplayString):
    """Custom type arBoardRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ArBoardRevision_Type.__name__ = "DisplayString"
_ArBoardRevision_Object = MibTableColumn
arBoardRevision = _ArBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 2, 1, 4),
    _ArBoardRevision_Type()
)
arBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arBoardRevision.setStatus("mandatory")


class _ArBoardSerialNumber_Type(DisplayString):
    """Custom type arBoardSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ArBoardSerialNumber_Type.__name__ = "DisplayString"
_ArBoardSerialNumber_Object = MibTableColumn
arBoardSerialNumber = _ArBoardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 2, 1, 5),
    _ArBoardSerialNumber_Type()
)
arBoardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arBoardSerialNumber.setStatus("mandatory")
_ArBoardTotalSlots_Type = Integer32
_ArBoardTotalSlots_Object = MibTableColumn
arBoardTotalSlots = _ArBoardTotalSlots_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 2, 1, 6),
    _ArBoardTotalSlots_Type()
)
arBoardTotalSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arBoardTotalSlots.setStatus("mandatory")
_ArBoardTotalPositions_Type = Integer32
_ArBoardTotalPositions_Object = MibTableColumn
arBoardTotalPositions = _ArBoardTotalPositions_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 2, 1, 7),
    _ArBoardTotalPositions_Type()
)
arBoardTotalPositions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arBoardTotalPositions.setStatus("mandatory")
_ArSlotTable_Object = MibTable
arSlotTable = _ArSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 3)
)
if mibBuilder.loadTexts:
    arSlotTable.setStatus("mandatory")
_ArSlotEntry_Object = MibTableRow
arSlotEntry = _ArSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 3, 1)
)
arSlotEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "arSlotBoardIndex"),
    (0, "ALLIEDTELESYN-MIB", "arSlotSlotIndex"),
)
if mibBuilder.loadTexts:
    arSlotEntry.setStatus("mandatory")
_ArSlotBoardIndex_Type = Integer32
_ArSlotBoardIndex_Object = MibTableColumn
arSlotBoardIndex = _ArSlotBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 3, 1, 1),
    _ArSlotBoardIndex_Type()
)
arSlotBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arSlotBoardIndex.setStatus("mandatory")
_ArSlotSlotIndex_Type = Integer32
_ArSlotSlotIndex_Object = MibTableColumn
arSlotSlotIndex = _ArSlotSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 3, 1, 2),
    _ArSlotSlotIndex_Type()
)
arSlotSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arSlotSlotIndex.setStatus("mandatory")
_ArSlotHeldBoardIndex_Type = Integer32
_ArSlotHeldBoardIndex_Object = MibTableColumn
arSlotHeldBoardIndex = _ArSlotHeldBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 3, 1, 3),
    _ArSlotHeldBoardIndex_Type()
)
arSlotHeldBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arSlotHeldBoardIndex.setStatus("mandatory")


class _ArSlotDescription_Type(DisplayString):
    """Custom type arSlotDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ArSlotDescription_Type.__name__ = "DisplayString"
_ArSlotDescription_Object = MibTableColumn
arSlotDescription = _ArSlotDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 3, 1, 4),
    _ArSlotDescription_Type()
)
arSlotDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arSlotDescription.setStatus("mandatory")
_ArInterfaceTable_Object = MibTable
arInterfaceTable = _ArInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 4)
)
if mibBuilder.loadTexts:
    arInterfaceTable.setStatus("mandatory")
_ArInterfaceEntry_Object = MibTableRow
arInterfaceEntry = _ArInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 4, 1)
)
arInterfaceEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "arInterfaceBoardIndex"),
    (0, "ALLIEDTELESYN-MIB", "arInterfacePosition"),
)
if mibBuilder.loadTexts:
    arInterfaceEntry.setStatus("mandatory")
_ArInterfaceBoardIndex_Type = Integer32
_ArInterfaceBoardIndex_Object = MibTableColumn
arInterfaceBoardIndex = _ArInterfaceBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 4, 1, 1),
    _ArInterfaceBoardIndex_Type()
)
arInterfaceBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arInterfaceBoardIndex.setStatus("mandatory")
_ArInterfacePosition_Type = Integer32
_ArInterfacePosition_Object = MibTableColumn
arInterfacePosition = _ArInterfacePosition_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 4, 1, 2),
    _ArInterfacePosition_Type()
)
arInterfacePosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arInterfacePosition.setStatus("mandatory")
_ArInterfaceIfIndex_Type = InterfaceIndexOrZero
_ArInterfaceIfIndex_Object = MibTableColumn
arInterfaceIfIndex = _ArInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 4, 1, 3),
    _ArInterfaceIfIndex_Type()
)
arInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arInterfaceIfIndex.setStatus("mandatory")


class _ArInterfaceName_Type(DisplayString):
    """Custom type arInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ArInterfaceName_Type.__name__ = "DisplayString"
_ArInterfaceName_Object = MibTableColumn
arInterfaceName = _ArInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 4, 1, 4),
    _ArInterfaceName_Type()
)
arInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arInterfaceName.setStatus("mandatory")


class _ArInterfaceFullName_Type(DisplayString):
    """Custom type arInterfaceFullName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ArInterfaceFullName_Type.__name__ = "DisplayString"
_ArInterfaceFullName_Object = MibTableColumn
arInterfaceFullName = _ArInterfaceFullName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 4, 1, 5),
    _ArInterfaceFullName_Type()
)
arInterfaceFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arInterfaceFullName.setStatus("mandatory")
_ArIfXTable_Object = MibTable
arIfXTable = _ArIfXTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 5)
)
if mibBuilder.loadTexts:
    arIfXTable.setStatus("mandatory")
_ArIfXEntry_Object = MibTableRow
arIfXEntry = _ArIfXEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 5, 1)
)
arIfXEntry.setIndexNames(
    (0, "ALLIEDTELESYN-MIB", "arIfXIndex"),
)
if mibBuilder.loadTexts:
    arIfXEntry.setStatus("mandatory")
_ArIfXIndex_Type = Integer32
_ArIfXIndex_Object = MibTableColumn
arIfXIndex = _ArIfXIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 5, 1, 1),
    _ArIfXIndex_Type()
)
arIfXIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arIfXIndex.setStatus("mandatory")
_ArIfXAverageInputBitsSecond_Type = Integer32
_ArIfXAverageInputBitsSecond_Object = MibTableColumn
arIfXAverageInputBitsSecond = _ArIfXAverageInputBitsSecond_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 5, 1, 2),
    _ArIfXAverageInputBitsSecond_Type()
)
arIfXAverageInputBitsSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arIfXAverageInputBitsSecond.setStatus("mandatory")
_ArIfXAverageInputPacketsSecond_Type = Integer32
_ArIfXAverageInputPacketsSecond_Object = MibTableColumn
arIfXAverageInputPacketsSecond = _ArIfXAverageInputPacketsSecond_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 5, 1, 3),
    _ArIfXAverageInputPacketsSecond_Type()
)
arIfXAverageInputPacketsSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arIfXAverageInputPacketsSecond.setStatus("mandatory")
_ArIfXAverageOutputBitsSecond_Type = Integer32
_ArIfXAverageOutputBitsSecond_Object = MibTableColumn
arIfXAverageOutputBitsSecond = _ArIfXAverageOutputBitsSecond_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 5, 1, 4),
    _ArIfXAverageOutputBitsSecond_Type()
)
arIfXAverageOutputBitsSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arIfXAverageOutputBitsSecond.setStatus("mandatory")
_ArIfXAverageOutputPacketsSecond_Type = Integer32
_ArIfXAverageOutputPacketsSecond_Object = MibTableColumn
arIfXAverageOutputPacketsSecond = _ArIfXAverageOutputPacketsSecond_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 5, 1, 5),
    _ArIfXAverageOutputPacketsSecond_Type()
)
arIfXAverageOutputPacketsSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arIfXAverageOutputPacketsSecond.setStatus("mandatory")
_Protocols_ObjectIdentity = ObjectIdentity
protocols = _Protocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 6)
)

# Managed Objects groups


# Notification objects

fanAndPsRpsConnectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0, 1)
)
fanAndPsRpsConnectionTrap.setObjects(
    ("ALLIEDTELESYN-MIB", "fanAndPsRpsConnectionStatus")
)
if mibBuilder.loadTexts:
    fanAndPsRpsConnectionTrap.setStatus(
        ""
    )

fanAndPsMainPSUStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0, 2)
)
fanAndPsMainPSUStatusTrap.setObjects(
    ("ALLIEDTELESYN-MIB", "fanAndPsMainPSUStatus")
)
if mibBuilder.loadTexts:
    fanAndPsMainPSUStatusTrap.setStatus(
        ""
    )

fanAndPsRedundantPSUStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0, 3)
)
fanAndPsRedundantPSUStatusTrap.setObjects(
    ("ALLIEDTELESYN-MIB", "fanAndPsRedundantPSUStatus")
)
if mibBuilder.loadTexts:
    fanAndPsRedundantPSUStatusTrap.setStatus(
        ""
    )

fanAndPsMainFanStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0, 4)
)
fanAndPsMainFanStatusTrap.setObjects(
    ("ALLIEDTELESYN-MIB", "fanAndPsMainFanStatus")
)
if mibBuilder.loadTexts:
    fanAndPsMainFanStatusTrap.setStatus(
        ""
    )

fanAndPsRedundantFanStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0, 5)
)
fanAndPsRedundantFanStatusTrap.setObjects(
    ("ALLIEDTELESYN-MIB", "fanAndPsRedundantFanStatus")
)
if mibBuilder.loadTexts:
    fanAndPsRedundantFanStatusTrap.setStatus(
        ""
    )

fanAndPsTemperatureStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0, 6)
)
fanAndPsTemperatureStatusTrap.setObjects(
    ("ALLIEDTELESYN-MIB", "fanAndPsTemperatureStatus")
)
if mibBuilder.loadTexts:
    fanAndPsTemperatureStatusTrap.setStatus(
        ""
    )

fanAndPsFanTrayPresentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0, 7)
)
fanAndPsFanTrayPresentTrap.setObjects(
    ("ALLIEDTELESYN-MIB", "fanAndPsFanTrayPresent")
)
if mibBuilder.loadTexts:
    fanAndPsFanTrayPresentTrap.setStatus(
        ""
    )

fanAndPsFanTrayStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0, 8)
)
fanAndPsFanTrayStatusTrap.setObjects(
    ("ALLIEDTELESYN-MIB", "fanAndPsFanTrayStatus")
)
if mibBuilder.loadTexts:
    fanAndPsFanTrayStatusTrap.setStatus(
        ""
    )

fanAndPsMainMonitoringStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0, 9)
)
fanAndPsMainMonitoringStatusTrap.setObjects(
    ("ALLIEDTELESYN-MIB", "fanAndPsMainMonitoringStatus")
)
if mibBuilder.loadTexts:
    fanAndPsMainMonitoringStatusTrap.setStatus(
        ""
    )

fanAndPsAccelFanStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0, 10)
)
fanAndPsAccelFanStatusTrap.setObjects(
    ("ALLIEDTELESYN-MIB", "fanAndPsAccelFanStatus")
)
if mibBuilder.loadTexts:
    fanAndPsAccelFanStatusTrap.setStatus(
        ""
    )

generalTemperatureStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 1, 0, 1)
)
generalTemperatureStatusTrap.setObjects(
      *(("ALLIEDTELESYN-MIB", "generalTemperatureStatus"),
        ("ALLIEDTELESYN-MIB", "generalTemperatureActualTemp"),
        ("ALLIEDTELESYN-MIB", "generalTemperatureThreshold"))
)
if mibBuilder.loadTexts:
    generalTemperatureStatusTrap.setStatus(
        ""
    )

sbTempFixedThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 0, 1)
)
sbTempFixedThresholdTrap.setObjects(
      *(("ALLIEDTELESYN-MIB", "sbTempFixedThresholdStatus"),
        ("ALLIEDTELESYN-MIB", "sbTempActualTemperature"),
        ("ALLIEDTELESYN-MIB", "sbTempFixedThreshold"))
)
if mibBuilder.loadTexts:
    sbTempFixedThresholdTrap.setStatus(
        ""
    )

sbTempSettableThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 0, 2)
)
sbTempSettableThresholdTrap.setObjects(
      *(("ALLIEDTELESYN-MIB", "sbTempSettableThresholdStatus"),
        ("ALLIEDTELESYN-MIB", "sbTempActualTemperature"),
        ("ALLIEDTELESYN-MIB", "sbTempSettableThreshold"))
)
if mibBuilder.loadTexts:
    sbTempSettableThresholdTrap.setStatus(
        ""
    )

acceleratorTemperatureStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 3, 0, 1)
)
acceleratorTemperatureStatusTrap.setObjects(
    ("ALLIEDTELESYN-MIB", "acceleratorTemperatureStatus")
)
if mibBuilder.loadTexts:
    acceleratorTemperatureStatusTrap.setStatus(
        ""
    )

bbrNvsReinitialiseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 6, 0, 1)
)
if mibBuilder.loadTexts:
    bbrNvsReinitialiseTrap.setStatus(
        ""
    )

flashFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 0, 1)
)
flashFailureTrap.setObjects(
      *(("ALLIEDTELESYN-MIB", "flashGetFailure"),
        ("ALLIEDTELESYN-MIB", "flashOpenFailure"),
        ("ALLIEDTELESYN-MIB", "flashReadFailure"),
        ("ALLIEDTELESYN-MIB", "flashCloseFailure"),
        ("ALLIEDTELESYN-MIB", "flashCompleteFailure"),
        ("ALLIEDTELESYN-MIB", "flashWriteFailure"),
        ("ALLIEDTELESYN-MIB", "flashCreateFailure"),
        ("ALLIEDTELESYN-MIB", "flashPutFailure"),
        ("ALLIEDTELESYN-MIB", "flashDeleteFailure"),
        ("ALLIEDTELESYN-MIB", "flashCheckFailure"),
        ("ALLIEDTELESYN-MIB", "flashEraseFailure"),
        ("ALLIEDTELESYN-MIB", "flashCompactFailure"),
        ("ALLIEDTELESYN-MIB", "flashVerifyFailure"))
)
if mibBuilder.loadTexts:
    flashFailureTrap.setStatus(
        ""
    )

configFileExistTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 0, 1)
)
configFileExistTrap.setObjects(
    ("ALLIEDTELESYN-MIB", "configFileExist")
)
if mibBuilder.loadTexts:
    configFileExistTrap.setStatus(
        ""
    )

triggerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 0, 1)
)
triggerTrap.setObjects(
    ("ALLIEDTELESYN-MIB", "triggerLastTriggerActivated")
)
if mibBuilder.loadTexts:
    triggerTrap.setStatus(
        ""
    )

pingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 0, 1)
)
if mibBuilder.loadTexts:
    pingTrap.setStatus(
        ""
    )

dhcpRangeExhaustedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 0, 1)
)
dhcpRangeExhaustedTrap.setObjects(
      *(("ALLIEDTELESYN-MIB", "dhcpRangeExhaustedGateway"),
        ("ALLIEDTELESYN-MIB", "dhcpRangeExhaustedInterface"))
)
if mibBuilder.loadTexts:
    dhcpRangeExhaustedTrap.setStatus(
        ""
    )

firewallTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 77, 0, 1)
)
firewallTrap.setObjects(
    ("ALLIEDTELESYN-MIB", "firewallTrapMessage")
)
if mibBuilder.loadTexts:
    firewallTrap.setStatus(
        ""
    )

swiIntrusionDetectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 0, 6)
)
swiIntrusionDetectionTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    swiIntrusionDetectionTrap.setStatus(
        ""
    )

tcaTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 109, 0, 1)
)
tcaTrap.setObjects(
      *(("ALLIEDTELESYN-MIB", "ds3TrapError"),
        ("ALLIEDTELESYN-MIB", "ds3TrapLoc"),
        ("ALLIEDTELESYN-MIB", "ds3TrapInterval"))
)
if mibBuilder.loadTexts:
    tcaTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALLIEDTELESYN-MIB",
    **{"InterfaceIndexOrZero": InterfaceIndexOrZero,
       "alliedTelesyn": alliedTelesyn,
       "products": products,
       "bridgeRouter": bridgeRouter,
       "centreCOM-AR300Router": centreCOM_AR300Router,
       "centreCOM-AR720Router": centreCOM_AR720Router,
       "centreCOM-AR300LRouter": centreCOM_AR300LRouter,
       "centreCOM-AR310Router": centreCOM_AR310Router,
       "centreCOM-AR300LURouter": centreCOM_AR300LURouter,
       "centreCOM-AR300URouter": centreCOM_AR300URouter,
       "centreCOM-AR310URouter": centreCOM_AR310URouter,
       "centreCOM-AR350Router": centreCOM_AR350Router,
       "centreCOM-AR370Router": centreCOM_AR370Router,
       "centreCOM-AR330Router": centreCOM_AR330Router,
       "centreCOM-AR395Router": centreCOM_AR395Router,
       "centreCOM-AR390Router": centreCOM_AR390Router,
       "centreCOM-AR370URouter": centreCOM_AR370URouter,
       "centreCOM-AR740Router": centreCOM_AR740Router,
       "centreCOM-AR140SRouter": centreCOM_AR140SRouter,
       "centreCOM-AR140URouter": centreCOM_AR140URouter,
       "centreCOM-AR320Router": centreCOM_AR320Router,
       "centreCOM-AR130SRouter": centreCOM_AR130SRouter,
       "centreCOM-AR130URouter": centreCOM_AR130URouter,
       "centreCOM-AR160Router": centreCOM_AR160Router,
       "at-AR740RouterDC": at_AR740RouterDC,
       "centreCOM-AR120Router": centreCOM_AR120Router,
       "at-AR410Router": at_AR410Router,
       "at-AR725Router": at_AR725Router,
       "at-AR745Router": at_AR745Router,
       "at-AR410v2Router": at_AR410v2Router,
       "at-AR410v3Router": at_AR410v3Router,
       "at-AR725RouterDC": at_AR725RouterDC,
       "at-AR745RouterDC": at_AR745RouterDC,
       "at-AR450Router": at_AR450Router,
       "at-AR450DualRouter": at_AR450DualRouter,
       "at-AR440Router": at_AR440Router,
       "at-AR441Router": at_AR441Router,
       "at-AR442Router": at_AR442Router,
       "at-AR443Router": at_AR443Router,
       "at-AR444Router": at_AR444Router,
       "at-AR420Router": at_AR420Router,
       "at-AR550Router": at_AR550Router,
       "at-AR551Router": at_AR551Router,
       "at-AR552Router": at_AR552Router,
       "routerSwitch": routerSwitch,
       "at-Rapier24": at_Rapier24,
       "at-Rapier16fSC": at_Rapier16fSC,
       "at-Rapier16fVF": at_Rapier16fVF,
       "at-Rapier16fMT": at_Rapier16fMT,
       "at-Rapier48": at_Rapier48,
       "at-Rapier8t8fSC": at_Rapier8t8fSC,
       "at-Rapier8t8fSCi": at_Rapier8t8fSCi,
       "at-Rapier8t8fMT": at_Rapier8t8fMT,
       "at-Rapier8t8fMTi": at_Rapier8t8fMTi,
       "at-Rapier8fSC": at_Rapier8fSC,
       "at-Rapier8fSCi": at_Rapier8fSCi,
       "at-Rapier8fMT": at_Rapier8fMT,
       "at-Rapier8fMTi": at_Rapier8fMTi,
       "at-Rapier16fMTi": at_Rapier16fMTi,
       "at-RapierG6": at_RapierG6,
       "at-RapierG6SX": at_RapierG6SX,
       "at-RapierG6LX": at_RapierG6LX,
       "at-RapierG6MT": at_RapierG6MT,
       "at-Rapier16fSCi": at_Rapier16fSCi,
       "at-Rapier24i": at_Rapier24i,
       "at-Rapier48i": at_Rapier48i,
       "at-Switchblade4AC": at_Switchblade4AC,
       "at-Switchblade4DC": at_Switchblade4DC,
       "at-Switchblade8AC": at_Switchblade8AC,
       "at-Switchblade8DC": at_Switchblade8DC,
       "at-9816GF": at_9816GF,
       "at-9812TF": at_9812TF,
       "at-9816GB": at_9816GB,
       "at-9812T": at_9812T,
       "at-8724XL": at_8724XL,
       "at-8748XL": at_8748XL,
       "at-8724XLDC": at_8724XLDC,
       "at-8748XLDC": at_8748XLDC,
       "at-9816GB-DC": at_9816GB_DC,
       "at-9812T-DC": at_9812T_DC,
       "at-8824": at_8824,
       "at-8848": at_8848,
       "at-8824-DC": at_8824_DC,
       "at-8848-DC": at_8848_DC,
       "at-8624XL-80": at_8624XL_80,
       "at-8724XL-80": at_8724XL_80,
       "at-8748XL-80": at_8748XL_80,
       "at-8948EX": at_8948EX,
       "at-8948MX": at_8948MX,
       "at-8624T2M": at_8624T2M,
       "at-Rapier24i-DC-NEBS": at_Rapier24i_DC_NEBS,
       "at-8724XL-DC-NEBS": at_8724XL_DC_NEBS,
       "at-9924T": at_9924T,
       "at-9924SP": at_9924SP,
       "at-9924T-4SP": at_9924T_4SP,
       "at-9924TEMC": at_9924TEMC,
       "at-8724MLB": at_8724MLB,
       "at-8624POE": at_8624POE,
       "at-86482SP": at_86482SP,
       "mibObject": mibObject,
       "brouterMib": brouterMib,
       "atRouter": atRouter,
       "objects": objects,
       "boards": boards,
       "pprIcmAr023": pprIcmAr023,
       "pprIcmAr021s": pprIcmAr021s,
       "pprIcmAr022": pprIcmAr022,
       "pprIcmAr025": pprIcmAr025,
       "pprIcmAr024": pprIcmAr024,
       "pprAr300": pprAr300,
       "pprAr300L": pprAr300L,
       "pprAr310": pprAr310,
       "pprAr120": pprAr120,
       "pprAr300Lu": pprAr300Lu,
       "pprAr300u": pprAr300u,
       "pprAr310u": pprAr310u,
       "pprAr350": pprAr350,
       "pprIcmAr021u": pprIcmAr021u,
       "pprAr720": pprAr720,
       "pprAr010": pprAr010,
       "pprAr012": pprAr012,
       "pprAr011": pprAr011,
       "pprAr370": pprAr370,
       "pprAr330": pprAr330,
       "pprAr395": pprAr395,
       "pprAr390": pprAr390,
       "pprAr370u": pprAr370u,
       "pprIcmAr020": pprIcmAr020,
       "pprAr740": pprAr740,
       "pprAr140s": pprAr140s,
       "pprAr140u": pprAr140u,
       "pprAr160su": pprAr160su,
       "pprAr320": pprAr320,
       "pprAr130s": pprAr130s,
       "pprAr130u": pprAr130u,
       "pprRapier24": pprRapier24,
       "pprNsm0404Pic": pprNsm0404Pic,
       "pprA35SXSC": pprA35SXSC,
       "pprA35LXSC": pprA35LXSC,
       "pprA36MTRJ": pprA36MTRJ,
       "pprA37VF45": pprA37VF45,
       "pprA38LC": pprA38LC,
       "pprA39Tx": pprA39Tx,
       "pprAr740DC": pprAr740DC,
       "pprNsm0418BRI": pprNsm0418BRI,
       "pprRapier16fSC": pprRapier16fSC,
       "ppr8624xl80": ppr8624xl80,
       "pprRapier16fMT": pprRapier16fMT,
       "pprRapier16fMTi": pprRapier16fMTi,
       "pprRapier8t8fSC": pprRapier8t8fSC,
       "pprRapier8t8fSCi": pprRapier8t8fSCi,
       "pprRapier8t8fMT": pprRapier8t8fMT,
       "pprRapier8t8fMTi": pprRapier8t8fMTi,
       "pprRapier8fSC": pprRapier8fSC,
       "pprRapier8fSCi": pprRapier8fSCi,
       "pprRapier8fMT": pprRapier8fMT,
       "pprRapier8fMTi": pprRapier8fMTi,
       "pprRapierG6": pprRapierG6,
       "pprRapierG6SX": pprRapierG6SX,
       "pprRapierG6LX": pprRapierG6LX,
       "pprRapierG6MT": pprRapierG6MT,
       "pprRapier16fSCi": pprRapier16fSCi,
       "pprRapier24i": pprRapier24i,
       "pprAr824": pprAr824,
       "pprAr816fSC": pprAr816fSC,
       "pprAr816fSCi": pprAr816fSCi,
       "pprAr816fMT": pprAr816fMT,
       "pprAr816fMTi": pprAr816fMTi,
       "pprAr88t8fSC": pprAr88t8fSC,
       "pprAr88t8fSCi": pprAr88t8fSCi,
       "pprAr88t8fMT": pprAr88t8fMT,
       "pprAr88t8fMTi": pprAr88t8fMTi,
       "pprAr88fSC": pprAr88fSC,
       "pprAr88fSCi": pprAr88fSCi,
       "pprAr88fMT": pprAr88fMT,
       "pprAr88fMTi": pprAr88fMTi,
       "pprAr824i": pprAr824i,
       "pprAt8724XL": pprAt8724XL,
       "pprAt8748XL": pprAt8748XL,
       "pprAt8724XLDC": pprAt8724XLDC,
       "pprAt8748XLDC": pprAt8748XLDC,
       "pprAt8824": pprAt8824,
       "pprAt8824DC": pprAt8824DC,
       "ppr8724XLDC": ppr8724XLDC,
       "ppr8748XLDC": ppr8748XLDC,
       "pprRapier24iDC-NEBS": pprRapier24iDC_NEBS,
       "pprAt8724XLDC-NEBS": pprAt8724XLDC_NEBS,
       "pprAt8848DC": pprAt8848DC,
       "pprRapier48": pprRapier48,
       "pprAt8848": pprAt8848,
       "pprRapier48i": pprRapier48i,
       "pprNsm0424BRI": pprNsm0424BRI,
       "pprIcmAR026": pprIcmAR026,
       "ppr9816GF": ppr9816GF,
       "ppr9812TF": ppr9812TF,
       "pprSbChassis4AC": pprSbChassis4AC,
       "pprSbChassis4DC": pprSbChassis4DC,
       "pprSbChassis8AC": pprSbChassis8AC,
       "pprSbChassis8DC": pprSbChassis8DC,
       "pprSbChassis16AC": pprSbChassis16AC,
       "pprSbChassis16DC": pprSbChassis16DC,
       "pprSbControl": pprSbControl,
       "pprSbControlDTM": pprSbControlDTM,
       "pprSb48t": pprSb48t,
       "pprSb96t": pprSb96t,
       "pprSb32fSC": pprSb32fSC,
       "pprSb32fMT": pprSb32fMT,
       "pprSb8fRJ": pprSb8fRJ,
       "pprSb8fSXSC": pprSb8fSXSC,
       "pprSb8fSXMT": pprSb8fSXMT,
       "pprSb8fLXSC": pprSb8fLXSC,
       "pprSb8fLXMT": pprSb8fLXMT,
       "pprAr410": pprAr410,
       "pprA40SC": pprA40SC,
       "pprA40MTRJ": pprA40MTRJ,
       "pprA41SC": pprA41SC,
       "pprA41MTRJ": pprA41MTRJ,
       "pprAr725": pprAr725,
       "pprAr745": pprAr745,
       "pprSb8GBIC": pprSb8GBIC,
       "pprA42GBIC": pprA42GBIC,
       "ppr9816GB": ppr9816GB,
       "ppr9812T": ppr9812T,
       "pprNsm048DS3": pprNsm048DS3,
       "pprAr450": pprAr450,
       "pprAr450Dual": pprAr450Dual,
       "pprSbExpander": pprSbExpander,
       "pprAr725DC": pprAr725DC,
       "pprAr745DC": pprAr745DC,
       "pprAr410v2": pprAr410v2,
       "pprAr410v3": pprAr410v3,
       "pprIcmAr027": pprIcmAr027,
       "ppr8948EX": ppr8948EX,
       "ppr8948MX": ppr8948MX,
       "ppr9816GBDC": ppr9816GBDC,
       "ppr9812TDC": ppr9812TDC,
       "pprIcmAr021v2s": pprIcmAr021v2s,
       "pprA50": pprA50,
       "pprA51": pprA51,
       "pprA52": pprA52,
       "pprA53": pprA53,
       "pprFanA01": pprFanA01,
       "pprAtPwr01AC": pprAtPwr01AC,
       "pprAtPwr01DC": pprAtPwr01DC,
       "pprAtFan01": pprAtFan01,
       "pprSb24RJ": pprSb24RJ,
       "pprSb1XFP": pprSb1XFP,
       "ppr9924T": ppr9924T,
       "ppr9924SP": ppr9924SP,
       "ppr9924TEMC": ppr9924TEMC,
       "ppr9924T4SP": ppr9924T4SP,
       "pprAR440": pprAR440,
       "pprAR441": pprAR441,
       "pprAR442": pprAR442,
       "pprAR443": pprAR443,
       "pprAR444": pprAR444,
       "pprAR420": pprAR420,
       "pprAt8624T2M": pprAt8624T2M,
       "pprA46Tx": pprA46Tx,
       "pprAR550": pprAR550,
       "pprAR551": pprAR551,
       "pprAR552": pprAR552,
       "pprC8724MLB": pprC8724MLB,
       "pprAt86482SP": pprAt86482SP,
       "pprAt8624POE": pprAt8624POE,
       "pprAtPwr01RAC": pprAtPwr01RAC,
       "pprAtFan01R": pprAtFan01R,
       "pprAtPwr02AC": pprAtPwr02AC,
       "pprAtPwr02RAC": pprAtPwr02RAC,
       "pprSb24SFP": pprSb24SFP,
       "release": release,
       "iftypes": iftypes,
       "ifaceEth": ifaceEth,
       "ifaceSyn": ifaceSyn,
       "ifaceAsyn": ifaceAsyn,
       "ifaceBri": ifaceBri,
       "ifacePri": ifacePri,
       "ifacePots": ifacePots,
       "ifaceGBIC": ifaceGBIC,
       "chips": chips,
       "chip68020Cpu": chip68020Cpu,
       "chip68340Cpu": chip68340Cpu,
       "chip68302Cpu": chip68302Cpu,
       "chip68360Cpu": chip68360Cpu,
       "chip860TCpu": chip860TCpu,
       "chipRtc1": chipRtc1,
       "chipRtc2": chipRtc2,
       "chipRtc3": chipRtc3,
       "chipRtc4": chipRtc4,
       "chipRam1mb": chipRam1mb,
       "chipRam2mb": chipRam2mb,
       "chipRam3mb": chipRam3mb,
       "chipRam4mb": chipRam4mb,
       "chipRam6mb": chipRam6mb,
       "chipRam8mb": chipRam8mb,
       "chipRam12mb": chipRam12mb,
       "chipRam16mb": chipRam16mb,
       "chipRam20mb": chipRam20mb,
       "chipRam32mb": chipRam32mb,
       "chipFlash1mb": chipFlash1mb,
       "chipFlash2mb": chipFlash2mb,
       "chipFlash3mb": chipFlash3mb,
       "chipFlash4mb": chipFlash4mb,
       "chipFlash6mb": chipFlash6mb,
       "chipFlash8mb": chipFlash8mb,
       "chipPem": chipPem,
       "traps": traps,
       "sysinfo": sysinfo,
       "fanAndPs": fanAndPs,
       "fanAndPsRpsConnectionTrap": fanAndPsRpsConnectionTrap,
       "fanAndPsMainPSUStatusTrap": fanAndPsMainPSUStatusTrap,
       "fanAndPsRedundantPSUStatusTrap": fanAndPsRedundantPSUStatusTrap,
       "fanAndPsMainFanStatusTrap": fanAndPsMainFanStatusTrap,
       "fanAndPsRedundantFanStatusTrap": fanAndPsRedundantFanStatusTrap,
       "fanAndPsTemperatureStatusTrap": fanAndPsTemperatureStatusTrap,
       "fanAndPsFanTrayPresentTrap": fanAndPsFanTrayPresentTrap,
       "fanAndPsFanTrayStatusTrap": fanAndPsFanTrayStatusTrap,
       "fanAndPsMainMonitoringStatusTrap": fanAndPsMainMonitoringStatusTrap,
       "fanAndPsAccelFanStatusTrap": fanAndPsAccelFanStatusTrap,
       "fanAndPsRpsConnectionStatus": fanAndPsRpsConnectionStatus,
       "fanAndPsMainPSUStatus": fanAndPsMainPSUStatus,
       "fanAndPsRedundantPSUStatus": fanAndPsRedundantPSUStatus,
       "fanAndPsRpsMonitoringStatus": fanAndPsRpsMonitoringStatus,
       "fanAndPsMainFanStatus": fanAndPsMainFanStatus,
       "fanAndPsRedundantFanStatus": fanAndPsRedundantFanStatus,
       "fanAndPsTemperatureStatus": fanAndPsTemperatureStatus,
       "fanAndPsFanTrayPresent": fanAndPsFanTrayPresent,
       "fanAndPsFanTrayStatus": fanAndPsFanTrayStatus,
       "fanAndPsMainMonitoringStatus": fanAndPsMainMonitoringStatus,
       "fanAndPsPsuStatusTable": fanAndPsPsuStatusTable,
       "fanAndPsPsuStatusEntry": fanAndPsPsuStatusEntry,
       "fanAndPsPsuNumber": fanAndPsPsuNumber,
       "fanAndPsPsuPresent": fanAndPsPsuPresent,
       "fanAndPsPsuType": fanAndPsPsuType,
       "fanAndPsPsuFan": fanAndPsPsuFan,
       "fanAndPsPsuTemperature": fanAndPsPsuTemperature,
       "fanAndPsPsuPower": fanAndPsPsuPower,
       "fanAndPsAccelFanStatus": fanAndPsAccelFanStatus,
       "restart": restart,
       "cpu": cpu,
       "cpuUtilisationMax": cpuUtilisationMax,
       "cpuUtilisationAvg": cpuUtilisationAvg,
       "cpuUtilisationAvgLastMinute": cpuUtilisationAvgLastMinute,
       "cpuUtilisationAvgLast10Seconds": cpuUtilisationAvgLast10Seconds,
       "cpuUtilisationAvgLastSecond": cpuUtilisationAvgLastSecond,
       "cpuUtilisationMaxLast5Minutes": cpuUtilisationMaxLast5Minutes,
       "cpuUtilisationAvgLast5Minutes": cpuUtilisationAvgLast5Minutes,
       "sysTemperature": sysTemperature,
       "generalTemperature": generalTemperature,
       "generalTemperatureStatusTrap": generalTemperatureStatusTrap,
       "generalTemperatureSupported": generalTemperatureSupported,
       "generalTemperatureActualTemp": generalTemperatureActualTemp,
       "generalTemperatureStatus": generalTemperatureStatus,
       "generalTemperatureThreshold": generalTemperatureThreshold,
       "sbTemperature": sbTemperature,
       "sbTempFixedThresholdTrap": sbTempFixedThresholdTrap,
       "sbTempSettableThresholdTrap": sbTempSettableThresholdTrap,
       "sbTempTable": sbTempTable,
       "sbTempEntry": sbTempEntry,
       "sbTempIndex": sbTempIndex,
       "sbTempActualTemperature": sbTempActualTemperature,
       "sbTempFixedThresholdStatus": sbTempFixedThresholdStatus,
       "sbTempSettableThresholdStatus": sbTempSettableThresholdStatus,
       "sbTempSettableThreshold": sbTempSettableThreshold,
       "sbTempFixedThreshold": sbTempFixedThreshold,
       "acceleratorTemperature": acceleratorTemperature,
       "acceleratorTemperatureStatusTrap": acceleratorTemperatureStatusTrap,
       "acceleratorTemperatureSupported": acceleratorTemperatureSupported,
       "acceleratorTemperatureActualTemp": acceleratorTemperatureActualTemp,
       "acceleratorTemperatureStatus": acceleratorTemperatureStatus,
       "acceleratorTemperatureThreshold": acceleratorTemperatureThreshold,
       "atContactDetails": atContactDetails,
       "bbrNvs": bbrNvs,
       "bbrNvsReinitialiseTrap": bbrNvsReinitialiseTrap,
       "memory": memory,
       "freeMemory": freeMemory,
       "totalBuffers": totalBuffers,
       "realTimeClockStatus": realTimeClockStatus,
       "hostId": hostId,
       "modules": modules,
       "ethernet": ethernet,
       "ethIntTable": ethIntTable,
       "ethIntEntry": ethIntEntry,
       "ethIntIndex": ethIntIndex,
       "ethIntBoardIndex": ethIntBoardIndex,
       "ethIntBoardPosition": ethIntBoardPosition,
       "ethIntDuplexMode": ethIntDuplexMode,
       "flash": flash,
       "flashFailureTrap": flashFailureTrap,
       "flashGetFailure": flashGetFailure,
       "flashOpenFailure": flashOpenFailure,
       "flashReadFailure": flashReadFailure,
       "flashCloseFailure": flashCloseFailure,
       "flashCompleteFailure": flashCompleteFailure,
       "flashWriteFailure": flashWriteFailure,
       "flashCreateFailure": flashCreateFailure,
       "flashPutFailure": flashPutFailure,
       "flashDeleteFailure": flashDeleteFailure,
       "flashCheckFailure": flashCheckFailure,
       "flashEraseFailure": flashEraseFailure,
       "flashCompactFailure": flashCompactFailure,
       "flashVerifyFailure": flashVerifyFailure,
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
       "bri": bri,
       "briIntTable": briIntTable,
       "briIntEntry": briIntEntry,
       "briIntIndex": briIntIndex,
       "briIntBoardIndex": briIntBoardIndex,
       "briIntBoardPosition": briIntBoardPosition,
       "briIntMode": briIntMode,
       "briIntTdmChannelMap": briIntTdmChannelMap,
       "briIntIsdnChannelMap": briIntIsdnChannelMap,
       "briChanTable": briChanTable,
       "briChanEntry": briChanEntry,
       "briChanIntIndex": briChanIntIndex,
       "briChanChannelIndex": briChanChannelIndex,
       "briChanMode": briChanMode,
       "briChanState": briChanState,
       "pri": pri,
       "priIntTable": priIntTable,
       "priIntEntry": priIntEntry,
       "priIntIndex": priIntIndex,
       "priIntBoardIndex": priIntBoardIndex,
       "priIntBoardPosition": priIntBoardPosition,
       "priIntMode": priIntMode,
       "priIntTdmChannelMap": priIntTdmChannelMap,
       "priIntIsdnChannelMap": priIntIsdnChannelMap,
       "priIntType": priIntType,
       "priChanTable": priChanTable,
       "priChanEntry": priChanEntry,
       "priChanIntIndex": priChanIntIndex,
       "priChanChannelIndex": priChanChannelIndex,
       "priChanMode": priChanMode,
       "priChanState": priChanState,
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
       "configFileExistTrap": configFileExistTrap,
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
       "instRelExists": instRelExists,
       "instPatExists": instPatExists,
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
       "createConfigFile": createConfigFile,
       "configFileExist": configFileExist,
       "currentConfigFile": currentConfigFile,
       "trigger": trigger,
       "triggerTrap": triggerTrap,
       "triggerLastTriggerActivated": triggerLastTriggerActivated,
       "file": file,
       "fileTable": fileTable,
       "fileEntry": fileEntry,
       "fileIndex": fileIndex,
       "fileName": fileName,
       "fileDevice": fileDevice,
       "fileCreationTime": fileCreationTime,
       "fileStatus": fileStatus,
       "fileSize": fileSize,
       "fileNumbers": fileNumbers,
       "ping": ping,
       "pingTrap": pingTrap,
       "pingTable": pingTable,
       "pingEntry": pingEntry,
       "pingIndex": pingIndex,
       "pingProtocol": pingProtocol,
       "pingAddress": pingAddress,
       "pingNumberOfPackets": pingNumberOfPackets,
       "pingPacketSize": pingPacketSize,
       "pingTimeout": pingTimeout,
       "pingDelay": pingDelay,
       "pingTrapOnCompletion": pingTrapOnCompletion,
       "pingTypeOfService": pingTypeOfService,
       "pingPattern": pingPattern,
       "pingStatus": pingStatus,
       "pingStatistics": pingStatistics,
       "pingSentPackets": pingSentPackets,
       "pingReceivedPackets": pingReceivedPackets,
       "pingMinimumRoundTripTime": pingMinimumRoundTripTime,
       "pingAverageRoundTripTime": pingAverageRoundTripTime,
       "pingMaximumRoundTripTime": pingMaximumRoundTripTime,
       "dhcp": dhcp,
       "dhcpRangeExhaustedTrap": dhcpRangeExhaustedTrap,
       "dhcpRangeTable": dhcpRangeTable,
       "dhcpRangeEntry": dhcpRangeEntry,
       "dhcpRangeIndex": dhcpRangeIndex,
       "dhcpRangeName": dhcpRangeName,
       "dhcpRangeBaseAddress": dhcpRangeBaseAddress,
       "dhcpRangeNumberOfAddresses": dhcpRangeNumberOfAddresses,
       "dhcpRangeGateway": dhcpRangeGateway,
       "dhcpTrapVariable": dhcpTrapVariable,
       "dhcpRangeExhaustedGateway": dhcpRangeExhaustedGateway,
       "dhcpRangeExhaustedInterface": dhcpRangeExhaustedInterface,
       "dhcpClientTable": dhcpClientTable,
       "dhcpClientEntry": dhcpClientEntry,
       "dhcpClientIpAddress": dhcpClientIpAddress,
       "dhcpClientID": dhcpClientID,
       "dhcpClientState": dhcpClientState,
       "dhcpClientType": dhcpClientType,
       "dhcpClientExpiry": dhcpClientExpiry,
       "firewall": firewall,
       "firewallTrap": firewallTrap,
       "firewallTrapMessage": firewallTrapMessage,
       "swi": swi,
       "swiIntrusionDetectionTrap": swiIntrusionDetectionTrap,
       "swiPortTable": swiPortTable,
       "swiPortEntry": swiPortEntry,
       "swiPortNumber": swiPortNumber,
       "swiPortIngressLimit": swiPortIngressLimit,
       "swiPortEgressLimit": swiPortEgressLimit,
       "swi56xxPortCounterTable": swi56xxPortCounterTable,
       "swi56xxPortCounterEntry": swi56xxPortCounterEntry,
       "swi56xxPortNumber": swi56xxPortNumber,
       "swi56xxRxTx64kPkts": swi56xxRxTx64kPkts,
       "swi56xxRxTx65To127kPkts": swi56xxRxTx65To127kPkts,
       "swi56xxRxTx128To255kPkts": swi56xxRxTx128To255kPkts,
       "swi56xxRxTx256To511kPkts": swi56xxRxTx256To511kPkts,
       "swi56xxRxTx512To1023kPkts": swi56xxRxTx512To1023kPkts,
       "swi56xxRxTx1024ToMaxPktSzPkts": swi56xxRxTx1024ToMaxPktSzPkts,
       "swi56xxRxTx519To1522kPkts": swi56xxRxTx519To1522kPkts,
       "swi56xxPortRxOctets": swi56xxPortRxOctets,
       "swi56xxPortRxPkts": swi56xxPortRxPkts,
       "swi56xxPortRxFCSErrors": swi56xxPortRxFCSErrors,
       "swi56xxPortRxMulticastPkts": swi56xxPortRxMulticastPkts,
       "swi56xxPortRxBroadcastPkts": swi56xxPortRxBroadcastPkts,
       "swi56xxPortRxPauseMACCtlFrms": swi56xxPortRxPauseMACCtlFrms,
       "swi56xxPortRxOversizePkts": swi56xxPortRxOversizePkts,
       "swi56xxPortRxFragments": swi56xxPortRxFragments,
       "swi56xxPortRxJabbers": swi56xxPortRxJabbers,
       "swi56xxPortRxMACControlFrms": swi56xxPortRxMACControlFrms,
       "swi56xxPortRxUnsupportOpcode": swi56xxPortRxUnsupportOpcode,
       "swi56xxPortRxAlignmentErrors": swi56xxPortRxAlignmentErrors,
       "swi56xxPortRxOutOfRngeLenFld": swi56xxPortRxOutOfRngeLenFld,
       "swi56xxPortRxSymErDurCarrier": swi56xxPortRxSymErDurCarrier,
       "swi56xxPortRxCarrierSenseErr": swi56xxPortRxCarrierSenseErr,
       "swi56xxPortRxUndersizePkts": swi56xxPortRxUndersizePkts,
       "swi56xxPortRxIpInHdrErrors": swi56xxPortRxIpInHdrErrors,
       "swi56xxPortTxOctets": swi56xxPortTxOctets,
       "swi56xxPortTxPkts": swi56xxPortTxPkts,
       "swi56xxPortTxFCSErrors": swi56xxPortTxFCSErrors,
       "swi56xxPortTxMulticastPkts": swi56xxPortTxMulticastPkts,
       "swi56xxPortTxBroadcastPkts": swi56xxPortTxBroadcastPkts,
       "swi56xxPortTxPauseMACCtlFrms": swi56xxPortTxPauseMACCtlFrms,
       "swi56xxPortTxOversizePkts": swi56xxPortTxOversizePkts,
       "swi56xxPortTxFragments": swi56xxPortTxFragments,
       "swi56xxPortTxJabbers": swi56xxPortTxJabbers,
       "swi56xxPortTxPauseCtrlFrms": swi56xxPortTxPauseCtrlFrms,
       "swi56xxPortTxFrameWDeferrdTx": swi56xxPortTxFrameWDeferrdTx,
       "swi56xxPortTxFrmWExcesDefer": swi56xxPortTxFrmWExcesDefer,
       "swi56xxPortTxSingleCollsnFrm": swi56xxPortTxSingleCollsnFrm,
       "swi56xxPortTxMultCollsnFrm": swi56xxPortTxMultCollsnFrm,
       "swi56xxPortTxLateCollsns": swi56xxPortTxLateCollsns,
       "swi56xxPortTxExcessivCollsns": swi56xxPortTxExcessivCollsns,
       "swi56xxPortTxCollisionFrames": swi56xxPortTxCollisionFrames,
       "swi56xxPortMiscDropEvents": swi56xxPortMiscDropEvents,
       "swi56xxPortMiscTaggedPktTx": swi56xxPortMiscTaggedPktTx,
       "swi56xxPortMiscTotalPktTxAbort": swi56xxPortMiscTotalPktTxAbort,
       "swi56xxPortHWMultiTTLexpired": swi56xxPortHWMultiTTLexpired,
       "swi56xxPortHWMultiBridgedFrames": swi56xxPortHWMultiBridgedFrames,
       "swi56xxPortHWMultiRxDrops": swi56xxPortHWMultiRxDrops,
       "swi56xxPortHWMultiTxDrops": swi56xxPortHWMultiTxDrops,
       "swiDebugVariables": swiDebugVariables,
       "swiDebugMemoryParityErrors": swiDebugMemoryParityErrors,
       "lb": lb,
       "lbShowGlobalTable": lbShowGlobalTable,
       "lbShowGlobalEntry": lbShowGlobalEntry,
       "lbGlobalIndex": lbGlobalIndex,
       "lbAffinityTimeOut": lbAffinityTimeOut,
       "lbOrphanTimeOut": lbOrphanTimeOut,
       "lbCriticalRst": lbCriticalRst,
       "lbTotalResources": lbTotalResources,
       "lbTotalResPools": lbTotalResPools,
       "lbTotalVirtBals": lbTotalVirtBals,
       "lbCurrentConnections": lbCurrentConnections,
       "lbShowResTable": lbShowResTable,
       "lbShowResEntry": lbShowResEntry,
       "lbResIndex": lbResIndex,
       "lbResource": lbResource,
       "lbResIp": lbResIp,
       "lbResPort": lbResPort,
       "lbResState": lbResState,
       "lbResWeight": lbResWeight,
       "lbResTotalConnections": lbResTotalConnections,
       "lbResCurrentConnections": lbResCurrentConnections,
       "lbShowResPoolTable": lbShowResPoolTable,
       "lbShowResPoolEntry": lbShowResPoolEntry,
       "lbResPoolIndex": lbResPoolIndex,
       "lbResPoolResourceIndex": lbResPoolResourceIndex,
       "lbResPool": lbResPool,
       "lbResPoolSelectionAlg": lbResPoolSelectionAlg,
       "lbResPoolFailOnLast": lbResPoolFailOnLast,
       "lbResPoolTotalConnections": lbResPoolTotalConnections,
       "lbResPoolResources": lbResPoolResources,
       "lbShowVirtBalTable": lbShowVirtBalTable,
       "lbShowVirtBalEntry": lbShowVirtBalEntry,
       "lbVirtBalIndex": lbVirtBalIndex,
       "lbVirtBal": lbVirtBal,
       "lbVirtBalPublicIp": lbVirtBalPublicIp,
       "lbVirtBalPublicPort": lbVirtBalPublicPort,
       "lbVirtBalState": lbVirtBalState,
       "lbVirtBalResPool": lbVirtBalResPool,
       "lbVirtBalType": lbVirtBalType,
       "lbVirtBalTotalConnections": lbVirtBalTotalConnections,
       "lbVirtBalAffinity": lbVirtBalAffinity,
       "lbVirtBalHttpErrorCode": lbVirtBalHttpErrorCode,
       "lbShowAffTable": lbShowAffTable,
       "lbShowAffEntry": lbShowAffEntry,
       "lbAffIndex": lbAffIndex,
       "lbAffVirtBal": lbAffVirtBal,
       "lbAffClientIp": lbAffClientIp,
       "lbAffCookie": lbAffCookie,
       "lbAffResource": lbAffResource,
       "lbAffExpiry": lbAffExpiry,
       "lbShowConTable": lbShowConTable,
       "lbShowConEntry": lbShowConEntry,
       "lbConIndex": lbConIndex,
       "lbConVirtBal": lbConVirtBal,
       "lbConClientIp": lbConClientIp,
       "lbConPort": lbConPort,
       "lbConResource": lbConResource,
       "ds3module": ds3module,
       "tcaTrap": tcaTrap,
       "ds3TrapTable": ds3TrapTable,
       "ds3TrapEntry": ds3TrapEntry,
       "ds3TcaTrapEnable": ds3TcaTrapEnable,
       "ds3TrapError": ds3TrapError,
       "ds3TrapLoc": ds3TrapLoc,
       "ds3TrapInterval": ds3TrapInterval,
       "arInterfaces": arInterfaces,
       "arBoardMaxIndex": arBoardMaxIndex,
       "arBoardTable": arBoardTable,
       "arBoardEntry": arBoardEntry,
       "arBoardIndex": arBoardIndex,
       "arBoardId": arBoardId,
       "arBoardName": arBoardName,
       "arBoardRevision": arBoardRevision,
       "arBoardSerialNumber": arBoardSerialNumber,
       "arBoardTotalSlots": arBoardTotalSlots,
       "arBoardTotalPositions": arBoardTotalPositions,
       "arSlotTable": arSlotTable,
       "arSlotEntry": arSlotEntry,
       "arSlotBoardIndex": arSlotBoardIndex,
       "arSlotSlotIndex": arSlotSlotIndex,
       "arSlotHeldBoardIndex": arSlotHeldBoardIndex,
       "arSlotDescription": arSlotDescription,
       "arInterfaceTable": arInterfaceTable,
       "arInterfaceEntry": arInterfaceEntry,
       "arInterfaceBoardIndex": arInterfaceBoardIndex,
       "arInterfacePosition": arInterfacePosition,
       "arInterfaceIfIndex": arInterfaceIfIndex,
       "arInterfaceName": arInterfaceName,
       "arInterfaceFullName": arInterfaceFullName,
       "arIfXTable": arIfXTable,
       "arIfXEntry": arIfXEntry,
       "arIfXIndex": arIfXIndex,
       "arIfXAverageInputBitsSecond": arIfXAverageInputBitsSecond,
       "arIfXAverageInputPacketsSecond": arIfXAverageInputPacketsSecond,
       "arIfXAverageOutputBitsSecond": arIfXAverageOutputBitsSecond,
       "arIfXAverageOutputPacketsSecond": arIfXAverageOutputPacketsSecond,
       "protocols": protocols}
)
